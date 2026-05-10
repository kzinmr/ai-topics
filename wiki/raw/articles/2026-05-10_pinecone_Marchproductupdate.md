---
title: "March Monthly Product Update"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/Marchproductupdate/"
scraped: "2026-05-10T01:27:42.809421+00:00"
lastmod: "2024-04-01T15:21:42Z"
type: "sitemap"
---

# March Monthly Product Update

**Source**: [https://www.pinecone.io/blog/Marchproductupdate/](https://www.pinecone.io/blog/Marchproductupdate/)

←
Blog
March Monthly Product Update
Xian Huang
Apr 1, 2024
Product
Share:
Jump to section:
Broader availability with a new serverless region
Build better RAG applications with updated Node.js and Canopy SDK
Better access control with self-serve SSO and Python proxy support
Easier navigation with a refreshed console
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
We had a productive March, including updated SDKs, new features, and improvements to our console. Check out some of the highlights below.
Broader availability with a new serverless region
We welcomed 2024 with
Pinecone serverless
, introducing a breakthrough
architecture
allowing you to build better AI applications while saving up to 50x
.
You can now deploy Pinecone serverless in the
us-east-1 region
in addition to the us-west-2 region of AWS. Support for serverless in GCP and Azure is coming soon.
Build better RAG applications with updated Node.js and Canopy SDK
The Pinecone Node.js client
v2.1.0
adds functionality to
list record IDs
or just those with a common ID prefix. ID prefixes enable you to query segments of content, which is especially useful for
managing RAG applications
where you often need to chunk large documents into smaller segments. This feature is also
supported
in the Python client (v3.1.0 and later).
import { Pinecone } from '@pinecone-database/pinecone';
const pc = new Pinecone();

const index = pc.index('my-index').namespace('my-namespace');

const results = await index.listPaginated({ prefix: 'doc1#' });
console.log(results);
// {
//   vectors: [
//     { id: 'doc1#01' }, { id: 'doc1#02' }, { id: 'doc1#03' },
//     { id: 'doc1#04' }, { id: 'doc1#05' },  { id: 'doc1#06' },
//     { id: 'doc1#07' }, { id: 'doc1#08' }, { id: 'doc1#09' },
//     ...
//   ],
//   pagination: {
//     next: 'eyJza2lwX3Bhc3QiOiJwcmVUZXN0LS04MCIsInByZWZpeCI6InByZVRlc3QifQ=='
//   },
//   namespace: 'my-namespace',
//   usage: { readUnits: 1 }
// }
Canopy
is an open-source RAG framework and context engine that enables you to quickly and easily experiment with and build applications using RAG. The latest version of
Canopy (v0.8.1)
includes better guidance for you to create a knowledge base when using the core library, bug fixes, and more.
Better access control with self-serve SSO and Python proxy support
Enterprise customers can now
configure single single-on
to manage their teams' access to Pinecone through any identity management solution with SAML 2.0 support, such as Okta.
The
latest version
of our Python SDK adds four optional configuration properties that enable the use of Pinecone
via proxy
. This allows users working in environments with proxy servers, network restrictions, or specific security requirements to configure the Python SDK to work seamlessly within those constraints. We’re
committed
to helping you build secure applications and stay tuned for more security features.
Easier navigation with a refreshed console
You can now find what you need more efficiently. Pick up where you left off with a new index shortcut, and locate indexes faster with the index browser that allows you to search indexes by name. You can also sort indexes alphabetically, by how recently they were viewed or created, or by status, and filter indexes by index type (serverless, pod-based, or starter).
Refreshed console
Last but not least, we’ve added a
Troubleshooting
section in the docs where you can find best practices, and how to address common errors.
Check the
release notes
for a running list of all product and feature releases. If you’re new to Pinecone,
try it out
today.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
