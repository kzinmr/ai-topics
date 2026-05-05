---
title: "Development Practices"
url: "https://boyter.org/posts/development-practices/"
fetched_at: 2026-05-05T07:01:57.122255+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Development Practices

Source: https://boyter.org/posts/development-practices/

Development Practices
2021/11/24
(666 words)
Development Practices
Follow a development practice of developer empowerment. Encourage change and experimentation with zero or low penalty for defects allowing them to be found early and resolved with additional tests or automation.
I embrace the fact that bugs and problems will be found, but by making the penalty for them exceedingly low we can ensure that they are identified and resolved quickly with little to no production impact. All processes from CI/CD and development are built around this idea and ensure that rapid changes can be made, allowing for extensible solutions, with as low a cost of development as possible while keeping quality high. This also has the added benefit of being a developer friendly approach that ensures teams remain engaged with as little buck passing as possible.
The following development practices are also supported and where appropriate are implemented to ensure the quality of any solution delivered is high and that development remains as easy as possible with minimal blockers.
Use of source control. Appropriate branches, with progress branches checked in allowing for rapid feedback and quick checks to ensure the wrong direction is not taken.
Frequent incremental commits using source control.
Use of static analysis and linting tools prior to committing to ensure that code is consistent and remains of high quality.
Ability to spin up the environment locally. While difficult with serverless infrastructure with up front effort it is possible to run integrations locally to allow for faster development. This can be achieved by using shims in the code allowing for the use of the local filesystem for S3 components and things such as DynamoDB Local for local development. Docker can be used to make this easier.
Give developers a sandbox AWS account for validation of code. This is to allow them to set up integrations such as SQS and develop against it locally to ensure code works, saving them having to deploy to validate, which saves on development and debugging costs.
Build unit and integration tests as appropriate, with the emphasis being on delivering quality code.
Use security scanners to ensure that secrets and keys are never committed to source control, and in the case they are, remove them. If using git this can be achieved using git-filter-branch or tools such as BFG.
Where possible apply S.O.L.I.D development principles.
Either commit vendor dependencies or have a managed place to store them in order to allow control of the version and ensure that development can continue in the case that 3rd party providers are down. This also allows for security management scanning and auditing.
Everyone is responsible for the quality of the solution. This means that developers own the quality of code they write equally with everyone else on the project, ensuring the highest quality of development.
Defence in depth solution design. This ensures that system failures should not degrade the performance of the application as a whole. An example would be that queues and other techniques are implemented such that when the target system recovers the system processes as normal.
Event driven architecture. This applies to defence in depth systems but also ensures minimal cost, as the system scales and grows to meet the needs as required.
Serverless as a preference. This lowers costs, ensures that the system is generally recoverable and self healing.
Managed services as a preference. This lowers maintenance costs and ensures backups are performed on an automated basis as well as scaling.
Encryption by default. Everything is encrypted at rest and in transport. No clear text communication across the stack ever. Where required encrypted memory though the use of secure string implementations can be used.
Stick to AWS best practices with extensions as required.
Continually improve processes to resolve issues. If something causes a problem now, fixing it with a test or other tool solves it for everyone.
Traceable logging. All logs are written to be traceable by transaction, caller and to a specific location within the codebase allowing for prompt investigation where a problem is found.
