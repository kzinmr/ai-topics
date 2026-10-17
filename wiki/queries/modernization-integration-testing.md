---
title: "Integration Testing for Modernization in Restricted Intranet Environments"
created: 2026-10-16
updated: 2026-10-16
type: query
tags: [query, software-engineering, testing, architecture, reliability, networking, data-integration]
sources:
  - https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch08.xhtml
  - https://learning.oreilly.com/library/view/service-virtualization-reality/9781430246718/Chapter04.html
  - https://learning.oreilly.com/library/view/service-virtualization-reality/9781430246718/Chapter05.html
  - https://learning.oreilly.com/library/view/testing-java-microservices/9781617292897/kindle_split_018.html
  - https://martinfowler.com/bliki/ContractTest.html
  - https://docs.pact.io/getting_started/what_is_pact_good_for
  - https://docs.pact.io/getting_started/sharing_pacts
  - https://wiremock.org/docs/standalone/
  - https://wiremock.org/docs/record-playback/
  - https://wiremock.org/docs/stateful-behaviour/
  - https://wiremock.org/docs/simulating-faults/
  - https://java.testcontainers.org/supported_docker_environment/image_registry_rate_limiting/
  - https://www.enterpriseintegrationpatterns.com/patterns/messaging/TestMessage.html
  - https://www.enterpriseintegrationpatterns.com/patterns/messaging/WireTap.html
  - https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html
---

# Integration Testing for Modernization in Restricted Intranet Environments

Enterprise modernization often has to proceed while access to an ERP, mainframe, partner API, message broker or shared database is scarce. Separate repeatable testing of the application from validation of the real boundary. Keep a small, explicit set of checks for the actual network, identity, middleware and business outcomes.

*Continuous Delivery*, Chapter 8, directly develops this arrangement: controllable doubles for routine acceptance tests, plus focused suites against real external integration points. Service virtualization makes a dependency available for repeated scenarios; contract checks establish whether the substitute still reflects the relevant real behavior. Neither establishes connectivity through the deployment environment. [Continuous Delivery](https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/ch08.xhtml), [Contract Test](https://martinfowler.com/bliki/ContractTest.html).

## Reading priorities

These are books available through O'Reilly Learning, including titles published by other publishers. Read the selected sections for the problem at hand.

| Priority and resource | Relevant sections | Practical value and limitation |
|---|---|---|
| 1. [Continuous Delivery](https://learning.oreilly.com/library/view/continuous-delivery-reliable/9780321670250/) — Jez Humble and David Farley, 2010 | Chapter 8, especially test doubles and external integration points; Chapters 11 and 12 for environments and data | Establish the overall strategy and separate test schedules. Apply the principles to the available infrastructure. |
| 2. [Service Virtualization: Reality Is Overrated](https://learning.oreilly.com/library/view/service-virtualization-reality/9781430246718/) — John Michelsen and Jason English, 2012 | Chapters 4 and 5 | Directly addresses limited mainframe access, shared capacity, conflicting schedules and data that is consumed by a test. Describes models built from traffic, documents, logs or manual scenarios. Its product advocacy and historical examples are not current comparative product evidence. |
| 3. [Testing Java Microservices](https://learning.oreilly.com/library/view/testing-java-microservices/9781617292897/) — Alex Soto Bueno, Andy Gumbrecht and Jason Porter, 2018 | Chapters 5 and 6 for integration and contracts; Chapter 9 for service virtualization | Connect test categories to implementation. Chapter 9 illustrates Hoverfly capture and simulation; WireMock appears in component testing. Old Java EE, JUnit and dependency examples need current documentation. Microservice decomposition is not a prerequisite for applying the boundary techniques. |
| 4. [Release It!, 2nd Edition](https://learning.oreilly.com/library/view/release-it-2nd/9781680504552/) — Michael T. Nygard | Chapter 5 sections on timeouts, circuit breakers and bulkheads | Turn dependency failure into explicit acceptance criteria. Start with [[concepts/resilience-acceptance-testing]] for explanations and example checks. |
| 5. [Enterprise Integration Patterns](https://learning.oreilly.com/library/view/enterprise-integration-patterns/0321200683/) — Gregor Hohpe and Bobby Woolf | Correlation Identifier, Idempotent Receiver, Wire Tap and Test Message | Particularly useful for MQ and asynchronous integration. The authors' public pattern pages provide a starting point; they do not reproduce every detail of the book. |

For code that cannot select a substitute, read *Working Effectively with Legacy Code*, Chapters 4 and 13, through [[concepts/legacy-code-seams]] and [[concepts/characterization-testing]]. For old/new comparison and approved exceptions, use [[concepts/legacy-behavioral-parity]].

## Separate the evidence produced by each test

The following is an application of the sources to a constrained enterprise environment. Agree the labels with the delivery and receiving teams; the term integration test alone does not identify what was real.

| Check | Real components | Evidence and remaining gap |
|---|---|---|
| Business regression | Application logic; controlled collaborators | Rules, branching and intended calls. Does not verify serialization or remote acceptance if the client is replaced. |
| Adapter and protocol exercise | Production adapter, serializer and client; local virtual peer | Actual request bytes, headers, parsing, error mapping and configured retry behavior. Does not prove the real peer or production trust path. |
| Contract validation | Consumer expectations checked against the provider implementation or controlled real endpoint | Compatibility for the exercised interactions and identified provider version. Does not establish all side effects, performance or deployment connectivity. |
| Environment connectivity check | Deployment artifact, actual runtime, identity, route and real endpoint | DNS, proxy, TLS, authentication, authorization and middleware access. One successful request is not business reconciliation. |
| Business flow and recovery | Required real systems and representative data | Receiver state, totals, ordering and recovery for selected flows. Scope and environment differences remain explicit. |

Keep the real client and encoding path in adapter tests. Replacing a Java gateway method with a function returning success bypasses the very HTTP, SOAP, JMS or file behavior that may change during modernization. A seam is useful, but its location determines the claim the test can support. See [[concepts/legacy-code-seams]].

## Choose an approach that fits cooperation and access

If the provider team can execute verification tests and prepare known provider states, consumer-driven contracts can provide feedback without both services running together. Pact exchanges consumer expectations and provider verification results; its open-source Broker can run inside the organization. This still requires team ownership and compatible test setup. [Pact applicability](https://docs.pact.io/getting_started/what_is_pact_good_for), [sharing pacts](https://docs.pact.io/getting_started/sharing_pacts).

If the provider team cannot participate, use reviewed interface specifications, sanitized observed examples and scheduled direct checks against the permitted real endpoint. Record the observed version/date and unresolved assumptions. Consumer tests against a locally generated mock alone are not provider verification. Pact's documentation specifically identifies uncooperative providers, uncontrolled provider data and performance testing as poor fits. [Pact applicability](https://docs.pact.io/getting_started/what_is_pact_good_for).

If no live access or traffic recording is permitted, build initial fixtures from approved WSDL, schemas, layouts and examples, then mark the behavior as specified rather than observed. *Service Virtualization*, Chapter 5, describes document- and manually constructed models as alternatives to traffic capture. Resolve high-risk assumptions during the next authorized real test; retain blocked checks until then. [Model creation options](https://learning.oreilly.com/library/view/service-virtualization-reality/9781430246718/Chapter05.html).

## Resolve common intranet constraints

| Constraint | Practical response | Check that remains necessary |
|---|---|---|
| Shared endpoint available only in a short window | Run repeatable scenarios locally; reserve the window for contract differences, actual identity and high-risk flows | Provider version, relevant responses and receiver-side results |
| No outbound internet from the test network | Deliver approved, pinned dependencies and fixtures through the existing internal artifact process | Start and run from a clean machine without public downloads |
| Containers or daemon access unavailable | Use an approved standalone process or existing managed test host; WireMock has a JAR distribution | Runtime compatibility, port permissions and process cleanup |
| Docker available but public registries blocked | Mirror the test images and required Testcontainers helper images internally | A cold start can require more than the database/broker image |
| TLS inspection, certificate pinning or proxy restrictions prevent recording | Prefer approved application-level records or supplied examples; use an explicit test endpoint where configurable | Actual TLS chain, hostname checks, client certificate and proxy route |
| Shared test data cannot be reset | Allocate run-specific business identities; prepare linked records across systems and clean up only owned records | Repeated execution, referential consistency and residual side effects |
| Developers cannot reach the integration subnet | Have the authorized operator run the same versioned test bundle from the permitted host and return the agreed evidence | Artifact identity, runtime/configuration identity, exit status and actual results |

[WireMock standalone](https://wiremock.org/docs/standalone/) documents JAR and container options. [Testcontainers image requirements](https://java.testcontainers.org/supported_docker_environment/image_registry_rate_limiting/) enumerate supporting images. Internal distribution, operator execution and selective cleanup above are proposed operating arrangements, subject to the site's existing rules.

After a JDK, framework, client or driver upgrade, check changed runtime defaults: truststore and TLS negotiation, DNS/proxy bypass, credential propagation, timeout/cancellation, retries, connection pools, transaction handling and character conversion. Exercise these with the delivered artifact and intended service identity; a developer account may have different access.

## Maintain useful simulations

[WireMock recording](https://wiremock.org/docs/record-playback/) creates mappings from observed interactions. [Stateful behavior](https://wiremock.org/docs/stateful-behaviour/) and [fault simulation](https://wiremock.org/docs/simulating-faults/) support scenarios beyond a fixed success response. A response recording does not reproduce the provider database or prove that a payment was committed.

For each maintained scenario, retain the interface version, source/date of the expectation, required initial state, material request fields, response/error, expected final state, reset procedure and owner. Revalidate after relevant provider/client changes and before relying on an old fixture for release. Match required fields strictly enough that malformed requests fail; avoid an unrestricted success stub.

Sanitize records inside the permitted boundary. Preserve formats, field lengths and relationships across records while removing secrets and personal data. Add boundary and failure cases absent from captured traffic. Keep simulation mode unable to fall through to the real endpoint when a request is unmatched; an automatic recording fallback can otherwise cause an unintended real transaction.

## Cover asynchronous and batch interfaces

For MQ/JMS, check destination and permissions, serialization, correlation, acknowledgement/commit boundaries, duplicate delivery, ordering where required, redelivery and dead-letter handling. A successful enqueue is not evidence of downstream business completion. [Idempotent Receiver](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) explains why one send can still produce repeated delivery.

For files/SFTP, compare bytes as well as parsed values: encoding, fixed-width padding, line endings, numeric scale, filenames, arrival cutoff, completion marker or atomic rename, partial files and duplicate ingestion. Use actual middleware for the risks that a file fixture cannot reproduce. For batch orchestration, test exit codes, step dependencies, restart checkpoints and business-date handling.

[Wire Tap](https://www.enterpriseintegrationpatterns.com/patterns/messaging/WireTap.html) provides an observation branch; an ordinary competing consumer can instead take messages away from the intended receiver. [Test Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/TestMessage.html) separates tagged test traffic and verifies results. Any use on a shared flow needs agreed routing, data ownership and side-effect isolation; a special ID alone does not make a transaction harmless.

## Work through an ambiguous payment outcome

This fictional example illustrates a recovery obligation that must be agreed with the receiver. A request carries stable operation identity `PAY-123`; the receiver commits it, but the reply is lost. The caller cannot infer failure from its timeout.

| Scenario | Repeatable exercise | Evidence needed from real integration |
|---|---|---|
| Valid payment | Check exact request and accepted response | Correct account, amount, currency and committed receiver record |
| Invalid request | Reject the malformed request at the virtual boundary | Actual error mapping and absence of business update |
| Receiver commits, reply is lost | Model committed state plus a lost/late reply; retry or reconcile under the agreed contract | Stable operation identity and one business effect, or the specified manual reconciliation procedure |
| Process restarts while outcome is unknown | Resume from durable state and query/reconcile the operation | Pending work remains discoverable; no silent loss or blind resubmission |
| Dependency returns after outage | Drain pending work within the agreed limits | Completed and rejected work reconcile to the accepted input set |

Use a stateful receiver harness or explicit provider fixture for the committed-but-no-reply case. Merely returning HTTP 500 or delaying a response does not establish that commit occurred. Without receiver deduplication or a reliable status lookup, bounded retries alone cannot guarantee a single business effect. See [[concepts/resilience-acceptance-testing]] and [[concepts/modernization-workflow-recovery]].

## Plan the next restricted integration window

1. Inventory each boundary, owner, protocol, access window, state setup, side effects and modernization changes. Rank by business impact and likelihood of changed behavior.
2. Capture the old artifact/runtime/configuration, permitted representative inputs and original results. Define approved target rules separately from observed legacy behavior.
3. Prepare repeatable adapter scenarios and validate the comparator with intentional mismatches. Fix local defects before spending the shared window.
4. Package the candidate artifact, harness, contracts, sanitized fixtures, dependency versions, setup/cleanup instructions and result format. Keep credentials outside the bundle.
5. In the permitted environment, first check route/identity/middleware, then relevant contract cases and critical business/recovery flows. Use the same artifact identity throughout.
6. Reconcile receiver state and business totals; record unexplained differences, blocked scenarios, accountable owners and the next verification trigger. Repeat affected checks after changes to code, dependencies, contracts or environment.

Record evidence separately as simulated, provider-validated, environment-validated and business-reconciled. A skipped or unreachable check remains blocked or unverified. Release criteria must say which real evidence is mandatory and who can accept the remaining risk. [[concepts/modernization-traceability]] connects these decisions to requirements; [[queries/modernization-java-logging]] explains the observations needed to diagnose the run.

## Source coverage

On 2026-10-16, focused reading in the authenticated O'Reilly reader covered *Continuous Delivery* Chapter 8 sections on doubles and external integration points; *Service Virtualization* Chapters 4 and 5; and *Testing Java Microservices* Chapter 9 through the virtualization rationale, modes and configuration discussion. Other chapter recommendations use verified contents and the existing Wiki reading notes. Public tool and pattern documentation was checked separately. These are selected-section findings and an applied test design, not a report of executing an enterprise integration test.

Return to [[queries/modernization-reading-guide]] or [[concepts/legacy-modernization-moc]] for the broader modernization route.
