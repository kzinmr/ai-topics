---
title: Google SRE - Configuration Management Strategies for Teams
source_url: https://sre.google/workbook/configuration-specifics/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/configuration-specifics.html
original_sha256: cfb60da1dbdc990ca66f3c05fbd1c1cf830510e3027c679f34f1b589e818f29e
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/configuration-specifics/
ingested: '2026-10-14'
sha256: 8472408fe5864a4df5f2a91d1736bb50040f90d2a006d63a7c48e6a4fef17b57
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Configuration Specifics
By Dave Cunningham and Misha Brukman
with Christophe Kalt and Betsy Beyer
Managing production systems is one of the many ways SREs provide value to an organization. The task of configuring and running applications in production requires insight into how those systems are put together and how they work. When things go wrong, the on-call engineer needs to know exactly where the configurations are and how to change them. This responsibility can become a burden if a team or organization hasn’t invested in addressing configuration-related toil.
This book covers the subject of toil at length (see
Eliminating Toil
). If your SRE team is burdened with a lot of configuration-related toil, we hope that implementing some of the ideas presented in this chapter will help you reclaim some of the time you spend making configuration changes.
Configuration-Induced Toil
At the start of a project’s lifecycle, configuration is usually relatively lightweight and straightforward. You might have a few files in a
data-only
format like
INI
,
JSON
,
YAML
, or XML. Managing these files requires little toil. As the number of applications, servers, and variations increases over time, configuration can become very complex and verbose. For example, you might have originally “changed a setting” by editing one configuration file, but now you have to update configuration files in multiple locations. Reading such configuration is also hard, as important differences are hidden in a sea of irrelevant duplicated details. We can characterize this configuration-related toil as
replication toil
: the mundane task of
managing configuration
replicated across a system. This kind of toil isn’t limited to large organizations and huge systems—it’s especially common to microservice architectures with many independently configured components.
Engineers often respond to replication toil by building automation or a configuration framework. They aim to remove duplication in the config system, and to make configuration easier to understand and maintain. Reusing techniques from software engineering, this approach often makes use of a “configuration language.” Google SRE has created a number of configuration languages with the aim of
reducing toil
for our largest and most complex production systems.
Unfortunately, this tactic doesn’t necessarily eliminate configuration toil. Freed from an overwhelming number of individual configs, the project (and its config corpus) grows with renewed energy. Inevitably, you run up against
complexity toil
: the challenging and frustrating task of dealing with the emergent and sometimes undesirable behaviors of complex automation. This kind of toil typically materializes in larger organizations (10+ engineers) and compounds with growth. The earlier you can tackle complexity toil, the better; the size and complexity of configuration will only grow over time.
Reducing Configuration-Induced Toil
If your project is riddled with configuration-related toil, you have a few basic strategies for improving the situation.
In rare cases, and if your application is custom-built, you might opt to remove the configuration altogether. The application may be naturally better than a configuration language at handling certain aspects of configuration: it might make sense for the application to assign defaults because it has access to information about the machine, or to vary some values dynamically because it can scale according to load.
If removing configuration is not an option, and
replication toil
is becoming a problem, consider automation to reduce the duplication in your configuration corpus. You might integrate a new configuration language, or you might need to improve or replace your existing configuration setup.
1
The next section,
Critical Properties and Pitfalls of Configuration Systems
, provides some guidance on choosing or designing that system.
If you go the route of setting up a new configuration framework, you’ll need to integrate the configuration language with the application that needs to be configured.
Integrating an Existing Application: Kubernetes
uses Kubernetes as an example of an existing application to be integrated, and
Integrating Custom Applications (In-House Software)
gives some more general advice. These sections walk through some examples using Jsonnet (which we chose as a representative configuration language for illustration purposes).
Once you have a configuration system in place to help with replication toil—whether you’re already committed to your existing solution, or you choose to implement a new configuration language—the best practices in
Effectively Operating a Configuration System
,
When to Evaluate Configuration
, and
Guarding Against Abusive Configuration
should be helpful in optimizing your setup, no matter which language you’re using. Adopting those processes and tools can help
minimize complexity toil
.
Critical Properties and Pitfalls of Configuration Systems
Configuration Design and Best Practices
outlined some critical properties of any configuration system. In addition to generic ideal requirements like lightweightness, ease of learning, simplicity, and expressive power, an efficient configuration system must:
Support configuration health, engineer confidence, and productivity via
tooling
for managing the config files (linters, debuggers, formatters, IDE integration, etc.).
Provide
hermetic
evaluation of configuration for rollbacks and general replayability.
Separate config and data
to allow for easy analysis of the config and a range of configuration interfaces.
It is not widely understood that these properties are critical, and arriving at our current understanding was indeed a journey. During this journey, Google invented several configuration systems that lacked these critical properties. We were not alone, either. Despite the great variety of popular configuration systems, it is difficult to find one that does not fall foul of at least one of the following pitfalls.
Pitfall 1: Failing to Recognize Configuration as a Programming Language Problem
If you’re not intentionally designing a language, then it’s highly unlikely the “language” you’ll end up with is a good one.
While configuration languages describe data rather than behavior, they still have the other characteristics of programming languages. If our configuration strategy starts with the objective of using a data-only format, programming language features tend to creep through the back door. Rather than remaining a
data-only
language, the format becomes an esoteric and complex
programming
language.
For example, some systems add a
count
attribute to the schema of a virtual machine (VM) being provisioned. This attribute is not a property of the VM itself, but instead indicates that you want more than one of them. While useful, this is a feature of a programming language, not a data format, because it requires an external evaluator or interpreter. A classical programming language approach would use logic outside the artifact, such as a
for
loop or list comprehension, to generate more VMs as required.
Another example is a configuration language that accrues
string interpolation rules
instead of supporting general expressions. The strings appear to be “just data,” although they can actually contain complex code, including data structure operations, checksums, base64 encoding, and so on.
The popular YAML + Jinja solution also has drawbacks. Simple pure-data formats such as XML, JSON, YAML, and text-formatted protocol buffers are excellent choices for pure-data use cases. Likewise, textual templating engines such as Jinja2 or Go templates are excellent for HTML templating. But when combined in a configuration language, they become difficult for both humans and tools to maintain and analyze. In all of these cases, this pitfall leaves us with a complex esoteric “language” that isn’t suited to tooling.
Pitfall 2: Designing Accidental or Ad Hoc Language Features
SREs typically feel configuration usability problems when operating systems at scale. A new language won’t have good tooling support (IDE support, good linters), and developing custom tooling is painful if the language has undocumented or esoteric semantics.
Adding ad hoc programming language features to a simple config format over time might create a feature-complete solution, but ad hoc languages are more complex and usually have less expressive power than their formally designed equivalents. They also risk developing gotchas and idiosyncrasies because their authors couldn’t consider the interaction between features ahead of time.
Instead of hoping your configuration system won’t grow complex enough to need simple programming constructs, it’s better to consider these requirements at the initial design phase.
Pitfall 3: Building Too Much Domain-Specific Optimization
The smaller the user base is for a new domain-specific solution, the longer you have to wait to accumulate enough users to justify building tooling. Engineers are unwilling to spend time understanding the language properly because it has little applicability outside this domain. Learning resources like
Stack Overflow
are less likely to be available.
Pitfall 4: Interleaving “Configuration Evaluation” with “Side Effects”
Side effects include either making changes to external systems, or consulting out-of-band data sources (DNS, VM IDs, latest build versions) during configuration runs.
Systems that allow these side effects
violate hermeticity
, and also prevent the
separation of config from data
. In an extreme case, it is impossible to debug your config without spending money by reserving cloud resources. In order to allow separation of config and data, first evaluate the config, then make the resulting data available to the user to analyze, and only then allow for side effects.
Pitfall 5: Using an Existing General-Purpose Scripting Language Like Python, Ruby, or Lua
This seems like a trivial way to avoid the first four pitfalls, but implementations that use a general-purpose scripting language are heavyweight and/or need intrusive sandboxing to ensure hermeticity. Since general-purpose languages can access the local system, security considerations may also call for sandboxing.
Additionally, we can’t assume that the people maintaining configuration will be familiar with all of these languages.
The desire to avoid these pitfalls led to the development of reusable domain-specific languages (DSLs) for configuration, such as
HOCON
,
Flabbergast
,
Dhall
, and
Jsonnet
. We recommend using an existing DSL for configuration. Even if a DSL seems too powerful for your needs, you may need the additional functionality at some point, and you can always restrict the functionality of the language using an in-house style guide.
A Very Quick Introduction to Jsonnet
Jsonnet is a hermetic open source DSL that can be used as a library or command-line tool to provide configuration for any application. It is used widely both inside and outside Google.
2
The language is designed to be familiar to programmers: it uses Python-like syntax, object orientation, and functional constructs. It is an extension of JSON, meaning that a JSON file is simply a Jsonnet program that outputs itself. Jsonnet is more permissive with quotes and commas than JSON, and supports comments. More importantly, it adds computational constructs.
While you don’t need to be particularly familiar with Jsonnet syntax to follow the rest of this chapter, spending just a few moments reading the
online tutorial
can help orient you.
Note
There is no dominant configuration language at Google or among our reader base, but we needed to choose
some
language that allows us to provide examples. This chapter uses Jsonnet to show practical examples of the recommendations we provide in
Configuration Design and Best Practices
.
If you aren’t already committed to a particular configuration language and want to use Jsonnet, you can directly apply the examples in this chapter. In all cases, we’ve done our best to make it as easy as possible for you to abstract the underlying lesson from the code examples.
Additionally, some of the examples explore concepts (like Turing completeness) that you might expect to find in a programming book. We have taken great care to dive only as deep as required to explain a subtlety that has actually bitten us in production. In most complex systems—and certainly with respect to configurations—the failures are at the edges.
Integrating a Configuration Language
This section uses Jsonnet to discuss how to integrate a configuration language with the application you need to configure, but the same techniques also transfer to other configuration languages.
Generating Config in Specific Formats
A configuration language might natively output in the correct format. For example, Jsonnet outputs JSON, which is compatible with many applications. JSON is also sufficient for consumers of languages that extend JSON, such as JavaScript, YAML, or
HashiCorp’s Configuration Language
. If this is your situation, you don’t need to perform any further integration work.
For other configuration formats that are not natively supported:
You need to find a way to represent configuration data within the configuration language. Usually, this is not hard because configuration values like maps, lists, strings, and other primitive values are generic and available in all languages.
Once this data is represented in the config language, you can use the constructs of that language to reduce duplication (and thus, toil).
You need to write (or reuse) a serialization function for the necessary output format. For example, the Jsonnet standard library has functions for outputting INI and XML from its internal JSON-like representation.  If configuration data resists representation within the configuration language (for example, a Bash script), you can use basic string templating techniques as a last resort. You can find practical examples at
https://bit.ly/2La0zDe
.
Driving Multiple Applications
Once you can drive arbitrary existing applications from the config language, you might be able to target several applications from the same config. If your applications use different config formats, you’ll need to perform some conversion work. Once you’re able to generate configuration in the necessary formats, you can easily unify, synchronize, and eliminate repetition across your entire config corpus. Given the prevalence of JSON and JSON-based formats, you may not even have to generate different formats—for example, this is true if you use a deployment architecture that uses
GCP Deployment Manager
,
AWS Cloud Formation
, or
Terraform
for base infrastructure, plus Kubernetes for containers.
At this point, you can:
Output an Nginx web server configuration and a Terraform firewall configuration from a single Jsonnet evaluation that defines the port only once.
Configure your monitoring dashboards, retention policies, and alert notification pipelines from the same files.
Manage the performance tradeoff between VM startup scripts and disk image-building scripts by moving initialization commands from one list to another.
After you unite disparate configs in one place, you have many opportunities to refine and abstract the config. Configs can even be nested—for example, a
Cassandra config
may be embedded inside the Deployment Manager config of its base infrastructure or inside a Kubernetes ConfigMap. A good configuration language can handle any awkward string quoting and generally make this operation natural and simple.
To make it easy to write many different files for various applications, Jsonnet has a mode that expects config execution to yield a single JSON object that maps filenames to file content (formatted as needed). You can simulate this facility in other configuration languages by emitting a map from string to string and using a postprocessing step or wrapper script to write the files.
Integrating an Existing Application: Kubernetes
Kubernetes makes for an interesting case study for a couple of reasons:
Jobs running on Kubernetes need to be configured, and their configuration can become complex.
Kubernetes does not come with a bundled configuration language (not even an ad hoc one, thankfully).
Kubernetes users with minimally complex objects simply use YAML. Users with larger infrastructure extend their Kubernetes workflow with languages like Jsonnet to provide the abstraction facilities needed at that scale.
What Kubernetes Provides
Kubernetes is an open source system for orchestrating containerized workloads on a cluster of machines. Its API allows you to manage the containers themselves and many important details, such as communication between containers, communication in/out of the cluster, load balancing, storage, progressive rollout, and autoscaling. Each item of configuration is represented with a JSON object that can be managed via an API endpoint. The command-line tool kubectl lets you read these objects from disk and send them to the API.
On disk, the JSON objects are actually encoded as YAML streams.
3
YAML is easily readable and converts easily to JSON via commonly available libraries. The out-of-the-box user experience involves writing YAML files that represent Kubernetes objects and running kubectl to deploy them to a cluster.
To learn about best practices for configuring Kubernetes, see the
Kubernetes documentation on that topic
.
Example Kubernetes Config
YAML, the user interface to Kubernetes configuration, provides some simple features like comments, and has a concise syntax that most people prefer to raw JSON. However, YAML falls short when it comes to abstraction: it only provides anchors,
4
which are rarely useful in practice and are not supported by Kubernetes.
Suppose you want to replicate a Kubernetes object four times with different namespaces, labels, and other minor variations. Following the best practices of immutable infrastructure, you store the config of all four variants, duplicating the other identical aspects of the configuration. The following code snippet presents one variant (for the sake of brevity, we omit the other three files):
# example1.yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: guestbook
    tier: frontend
  name: frontend
  namespace: prod
spec:
  externalTrafficPolicy: Cluster
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: guestbook
    tier: frontend
  sessionAffinity: None
  type: NodePort
The variants are hard to read and maintain because the important differences are obscured.
Integrating the Configuration Language
As discussed in
Configuration-Induced Toil
, managing a large number of YAML files can take a significant amount of time. A configuration language can help simplify this task. The most straightforward approach is to emit a single Kubernetes object from each execution of Jsonnet, then pipe the resulting JSON directly into kubectl, which processes the JSON as if it’s YAML. Alternatively, you could emit a YAML stream(a sequence of such objects
5
) or a single kubectl list object, or have Jsonnet emit multiple files from the same config. For further discussion, see the
Jsonnet website
.
Developers should be aware that in general, YAML allows you to write configs that are not expressible in JSON (and therefore, can’t be generated by Jsonnet). YAML configs can contain exceptional IEEE floating-point values like NaN, or objects with nonstring fields like arrays, other objects, or null. In practice, these features are very rarely used, and Kubernetes doesn’t allow them because the config must be JSON-encoded when sent to the API.
The following snippet shows what our example Kubernetes configuration would look like in Jsonnet:
// templates.libsonnet
{
  MyTemplate:: {
    local service = self,
    tier:: error 'Needs tier',
    apiVersion: 'v1',
    kind: 'Service',

    local selector_labels = { app: 'guestbook', tier: service.tier },

    metadata: {
      labels: selector_labels,
      name: 'guestbook-' + service.tier,
      namespace: 'default',
    },

    spec: {
      externalTrafficPolicy: 'Cluster',
      ports: [{
        port: 80,
        protocol: 'TCP',
        targetPort: 80,
      }],
      selector: selector_labels,
      sessionAffinity: 'None',
      type: 'NodePort',
    },
  },
}
// example1.jsonnet
local templates = import 'templates.libsonnet';

templates.MyTemplate {
  tier: 'frontend',
}
// example2.jsonnet
local templates = import 'templates.libsonnet';

templates.MyTemplate {
  tier: 'backend',
  metadata+: {
    namespace: 'prod',
  },
}
// example3.jsonnet
local templates = import 'templates.libsonnet';

templates.MyTemplate {
  tier: 'frontend',
  metadata+: {
    namespace: 'prod',
    labels+: { foo: 'bar' },
  },
}
// example4.jsonnet
local templates = import 'templates.libsonnet';

templates.MyTemplate {
  tier: 'backend',
}
Note the following:
We express all four variants by instantiating an abstract template four times, but you could also use functional abstractions.
While we use a separate Jsonnet file for each instance, you might also consolidate them in a single file.
In the abstract template, the namespace defaults to
default
and the tier must be overridden.
At first glance, the Jsonnet is slightly more verbose, but reduces toil as the number of template instantiations grows.
Within
MyTemplate
, the
local
keyword defines a variable
service
, which is initialized to
self
(a reference to the closest enclosing object). This allows you to refer to the object from within nested objects, where
self
is redefined.
The
tier
field has two colons (rather than the regular JSON single colon) and is hidden (not output) in the generated JSON. Otherwise, Kubernetes will reject
tier
as an unrecognized field. Hidden fields can still be overridden and referenced—in this case, as
service.tier
.
The template cannot be used by itself because referencing
service.tier
triggers the
error
construct, which raises a runtime error with the given text. To avoid the error, each instance of the template overrides the
tier
field with some other expression. In other words, this pattern expresses something similar to a pure virtual/abstract method.
Using functions for abstraction means that config can only be parameterized. In contrast, templates allow you to override any field from the parent. As described in
Configuration Design and Best Practices
, while simplicity should be fundamental to your design, the ability to escape simplicity is important. Template overrides provide a useful escape hatch to change specific details that might normally be considered too low-level. For example:
templates.MyTemplate {
  tier: 'frontend',
  spec+: {
    sessionAffinity: 'ClientIP',
  },
}
Here’s a typical workflow to convert an existing template to Jsonnet:
Convert one of the YAML variants to JSON.
Run the resulting JSON through the Jsonnet formatter.
Manually add Jsonnet constructs to abstract and instantiate the code (as shown in the example).
The example showed how to remove duplication while retaining certain fields that were different. Using a configuration language becomes more compelling as differences become more subtle (e.g., strings are slightly different) or challenging to express (e.g., configuration has structural differences like additional elements in arrays, or the same difference applied across all elements of an array).
In general, abstracting commonalities across different configurations promotes separation of concerns and has the same benefits as modularity in programming languages. You can take advantage of abstraction capabilities for a number of different use cases:
A single team might need to create multiple versions of their configuration that are
almost
(but not quite) the same—for example, when managing deployments across varied environments (prod/stage/dev/test), tuning deployments on different architectures, or adjusting capacity in different geographies.
An organization might have an infrastructure team that maintains reusable components—API serving frameworks, cache servers, or MapReduces—that are used by the application teams. For each component, the infrastructure team can maintain a template that defines the Kubernetes objects needed to run that component at scale. Each application team can instantiate that template to add the particulars of their application.
Integrating Custom Applications (In-House Software)
If your infrastructure utilizes any custom applications (i.e., software developed in-house, as opposed to off-the-shelf solutions), then you can design those applications to coexist with a reusable configuration language. The suggestions in this section should improve the overall user configuration experience when you are writing config files or interacting with the generated config data (e.g., for debugging purposes, or when integrating with other tools). They should also simplify the application’s design and separate configuration from data.
Your broad strategy for approaching custom applications should be to:
Let the config language handle what it’s designed for: the language aspect of the problem.
Let your application handle all other functionality.
The following best practices include examples that use Jsonnet, but the same recommendations apply to other languages:
Consume a single pure data file, and let the config language split the config into files using imports. This means the config language implementation only has to emit (and the application only has to consume) a single file. Also, since applications can combine files in different ways, this strategy explicitly and clearly delineates how the files are combined to form the application configuration.
Represent collections of named entities using objects, where the field contains the object name and the value contains the rest of the entity. Avoid using an array of objects where each element  has a name field.
Bad JSON:
[
   { "name": "cat", ... },
   { "name": "dog", ... }
]
Good JSON:
{
   "cat": { ... },
   "dog": { ... }
}
This strategy makes the collection (and individual animals) easier to extend, and you can reference entities by name (e.g.,
animals.cat
) instead of referencing brittle indexes (e.g.,
animals[0]
).
Avoid grouping entities by type at the top level. Structure the JSON so that logically related configuration is grouped in the same subtree. This allows abstraction (at the config language level) to follow functional boundaries.
Bad JSON:
{
   "pots": { "pot1": { ... }, "pot2": { ... } },
   "lids": { "lid1": { ... }, "lid2": { ... } }
}
Good JSON:
{
   "pot_assembly1": { "pot": { ... }, "lid": { ... } },
   "pot_assembly2": { "pot": { ... }, "lid": { ... } }
}
At the config language level, this strategy enables abstractions like the following:
local kitchen = import 'kitchen.libsonnet';
{
   pot_assembly1: kitchen.CrockPot,
   pot_assembly2: kitchen.SaucePan { pot+: { color: 'red' } },
}
Generally keep the data representation design simple:
Avoid embedding language features in the data representation (as mentioned in
Pitfall 1: Failing to Recognize Configuration as a Programming Language Problem
. These types of abstractions will be underpowered and only create confusion, since they force users to decide whether to use the abstraction features in the data representation or in the configuration language.
Don’t worry about overly verbose data representation. Solutions to reduce verbosity introduce complexity, and the problem can be managed in the configuration language.
Avoid interpreting custom string interpolation syntax, such as conditionals or placeholder references in strings, in your application. Sometimes interpretation is unavoidable—for example, when you need to describe actions that are performed after the pure data version of the config is generated (alerts, handlers, etc.). But otherwise, let the config language do as much of the language-level work as possible.
As mentioned earlier, if you
can
remove configuration altogether, doing so is always your best option. Although the configuration language can hide the complexity of the underlying model by using templates with default values, the generated config data is not completely hidden—it may be processed by tools, inspected by humans, or loaded into config databases. For the same reason, don’t rely on the configuration language to fix inconsistent naming, plurals, or mistakes in the underlying model—fix them in the model itself. If you can’t fix inconsistencies in the model, it is better to live with them at the language level to avoid even more inconsistency.
In our experience, configuration changes tend to dominate outage root causes over time in a system (see our list of top causes of outages in
Results of Postmortem Analysis
). Validating your config changes is a key step to maintaining reliability. We recommend validating the generated config data immediately after configuration execution. Syntactic validation alone (i.e., checking whether JSON is parsable) won’t find many bugs. After generic schema validation, check properties that are specific to your application’s domain—for example, whether required fields are present, referenced filenames exist, and provided values are within allowed ranges.
You can validate Jsonnet’s JSON with
JSONschema
. For applications using
protocol buffers
, you can easily generate the canonical JSON form of these buffers from Jsonnet, and the protocol buffer implementation will validate during deserialization.
No matter how you decide to validate, do not ignore unrecognized field names, as they may indicate a typo at the configuration language level. Jsonnet can mask fields that should not be output using the
::
syntax. It’s also a good idea to perform the same validation in a precommit hook.
Effectively Operating a Configuration System
When implementing “configuration as code” in any language, we recommend following the discipline and processes that aid software engineering generally.
Versioning
Configuration languages usually trigger engineers to write libraries of templates and utility functions. Often, one team maintains these libraries, but many other teams may consume them. When you need to make a breaking change to the library, you have two choices:
Commit a global update of all client code, refactoring the code so that it still works (this may not be organizationally possible).
Version the library so that different consumers can use different versions and migrate independently. Consumers who opt to use deprecated versions won’t get the benefits of the new versions and will incur technical debt—someday, they will have to refactor their code to use the new library.
Most languages, including Jsonnet, do not provide any specific support for versioning; instead, you can easily use directories. For a practical example in Jsonnet, see the
ksonnet-lib repository
, where the version is the first component of the imported path:
local k = import 'ksonnet.beta.2/k.libsonnet';
Source Control
Configuration Design and Best Practices
advocates keeping a historical record of config changes (including who made them) and ensuring that rollbacks are easy and reliable. Checking configuration into source control brings all these capabilities, plus the ability to code review config changes.
Tooling
Consider how you will enforce style and lint your configurations, and investigate if there’s an editor plug-in that integrates these tools into your workflow. Your goals here are to maintain a consistent style across all authors, to improve readability, and to detect errors. Some editors support post-write hooks that can run formatters and other external tools for you. You can also use precommit hooks to run the same tools to ensure checked-in config is high quality.
Testing
We recommend implementing unit tests for upstream template libraries. Make sure the libraries generate the expected concrete configuration when instantiated in various ways. Similarly, libraries of functions should include unit tests so they can be maintained with confidence.
In Jsonnet, you can write tests as Jsonnet files that:
Import the library to be tested.
Exercise the library.
Use either the
assert
statement or the standard library
assertEqual
function to validate its output. The latter presents any mismatching values in its error messages.
The following example tests the
joinName
function and
MyTemplate
:
// utils_test.jsonnet
local utils = import 'utils.libsonnet';
std.assertEqual(utils.joinName(['foo', 'bar']), 'foo-bar') &&
std.assertEqual(utils.MyTemplate { tier: 'frontend' }, { ... })
For larger test suites, you can take advantage of a
more comprehensive unit test framework developed by Jsonnet community members
. You can use this framework to define and run suites of tests in a structured manner—for example, to report the set of all failing tests instead of aborting execution at the first failing assertion.
When to Evaluate Configuration
Our critical properties include
hermeticity
; that is, configuration languages must generate the same config data regardless of where or when they execute. As described in
Configuration Design and Best Practices
a system can be hard or impossible to roll back if it depends on resources that can change outside of its hermetic environment. Generally, hermeticism means that Jsonnet code is always interchangeable with the expanded JSON it represents. Accordingly, you can generate JSON from Jsonnet at any time between when the Jsonnet is updated and when you need the JSON—even each time you need the JSON.
We recommend storing configuration in version control. Then your earliest opportunity to validate the config is before check-in. At the other extreme, an application can evaluate the config when it needs the JSON data. As a middle-of-the-road option, you can evaluate at build time. Each of these options has various tradeoffs, and you should optimize according to the specifics of your use case.
Very Early: Checking in the JSON
You can generate JSON from the Jsonnet code before checking both in to version control. The typical workflow is as follows:
Modify the Jsonnet files.
Run the Jsonnet command-line tool (perhaps wrapped in a script) to regenerate JSON files.
Use a precommit hook to ensure that the Jsonnet code and JSON output are always consistent.
Package everything into a pull request for a code review.
Pros
The reviewer can sanity-check the concrete changes—for example, a refactoring should not affect the generated JSON at all.
You can inspect line annotations by multiple authors across different versions at both the generated and abstracted level. This is useful for auditing changes.
You don’t need to run Jsonnet at runtime, which can help to limit complexity, binary size, and/or risk exposure.
Cons
The generated JSON is not necessarily readable—for example, if it embeds long strings.
The JSON may not be suitable for checking into version control for other reasons—for example, if it’s too large or contains secrets.
Merge conflicts may arise if many concurrent edits to separate Jsonnet files converge to a single JSON file.
Middle of the Road: Evaluate at Build Time
You can avoid checking JSON into source control by running the Jsonnet command-line utility at build time and embedding the generated JSON into the release artifact (e.g., as a tarball).  The application code simply reads the JSON file from disk at initialization time. If you’re using Bazel, you can easily achieve this using the
Jsonnet Bazel rules
. At Google, we commonly favor this approach because of the pros listed next.
Pros
You have the ability to control runtime complexity, binary size, and risk exposure without having to rebuild the JSON files in each pull request.
There’s no risk of desynchronization between originating Jsonnet code and resulting JSON.
Cons
The build is more complex.
It’s harder to evaluate the concrete change during code review.
Late: Evaluate at Runtime
Linking the Jsonnet library allows the application itself to interpret the config at any time, yielding an in-memory representation of the generated JSON config.
Pros
It’s simpler, as you don’t need a prior evaluation.
You gain the ability to evaluate Jsonnet code provided by the user during execution.
Cons
Any linked library increases the footprint and risk exposure.
Configuration bugs may be discovered at runtime, which is too late.
If the Jsonnet code is untrusted, you must take special care. (We discuss why in
Guarding Against Abusive Configuration
.)
To follow our running example, when should you run Jsonnet if you’re generating Kubernetes objects?
The answer depends on your implementation. If you’re building something like ksonnet (a client-side command-line tool that runs Jsonnet code from the local filesystem), the easiest solution is to link the Jsonnet library into the tool and evaluate the Jsonnet in process. Doing so is safe because code runs on the author’s own machine.
Box.com
's infrastructure uses Git hooks to push configuration changes to production. To avoid executing Jsonnet on the server, the Git hooks act on generated JSON that’s kept in the repository. For a deployment management daemon like Helm or Spinnaker, your only choice is to evaluate the Jsonnet on the server at runtime (with the caveats described in the next section).
Guarding Against Abusive Configuration
Unlike long-running services, configuration execution should quickly terminate with the resulting config. Unfortunately, due to bugs or deliberate attacks, configuration may take an arbitrary amount of CPU time or memory. To illustrate why, consider the following nonterminating Jsonnet program:
local f(x) = f(x + 1); f(0)
A program that uses unbounded memory is similar:
local f(x) = f(x + [1]); f([])
You can write equivalent examples using objects instead of functions, or in other configuration languages.
You might try to avoid overconsuming resources by restricting the language so that it is no longer
Turing complete
. However, enforcing that all configurations terminate doesn’t necessarily prevent overconsuming resources. It’s easy to write a program that consumes enough time or memory to be practically nonterminating. For example:
local f(x) = if x == 0 then [] else [f(x - 1), f(x - 1)]; f(100)
In fact,
such programs exist
even with simple config formats like XML and YAML.
In practice, the risk of these scenarios depends on the situation. On the less problematic side, suppose a command-line tool uses Jsonnet to build Kubernetes objects and then deploys those objects.  In this case, the Jsonnet code is trusted: accidents that produce nontermination are rare, and you can use Ctrl-C to mitigate them. Accidental memory exhaustion is extremely unlikely. At the other extreme, with a service like Helm or Spinnaker, which accepts arbitrary config code from an end user and evaluates it in a request handler, you must be very careful to avoid DOS attacks that might tie up request handlers or exhaust memory.
If you evaluate untrusted Jsonnet code in a request handler, you can avoid such attacks by sandboxing the Jsonnet execution. One easy strategy is to use a separate process and
ulimit
(or its non-UNIX equivalent).  Typically, you need to fork to the command-line executable instead of linking the Jsonnet library. As a result, programs that do not complete within given resources fail safely and inform the end user. For additional defense against C++ memory exploits, you can use the native Go implementation of Jsonnet.
Conclusion
Whether you use Jsonnet, adopt another configuration language, or develop your own, we hope that you can apply these best practices to manage the complexity and operational load required to configure your production system with confidence.
At a minimum, the critical properties of a configuration language are good
tooling
,
hermetic
configurations, and
separation of configuration and data
.
Your system may not be complex enough to need a configuration language. Transitioning to a domain-specific language like Jsonnet is a strategy to consider when your complexity increases. Doing so will allow you to provide a consistent and well-structured interface, and will free up your SRE team’s time to work on other important projects.
1
Note that you may be able to write software to convert your old configuration language to the new language; however, if your original source language is nonstandard or broken, this isn’t a viable option.
2
While fields from computational biology to video games use Jsonnet, the most enthusiastic adopters are from the Kubernetes community. Box.com uses Jsonnet to describe the workloads that run on their Kubernetes-based internal infrastructure platform. Databricks and Bitnami also use the language extensively.
3
A YAML stream is a file that contains many YAML documents separated by
"---"
.
4
YAML Specification §6.9.2.
5
In the YAML specification,
objects
are known as
documents
.
