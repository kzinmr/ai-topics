---
title: "Why didn't we use the COM static store to clean up the unmarshalable delegate?"
url: "https://devblogs.microsoft.com/oldnewthing/20261023-00/?p=112793/"
fetched_at: 2026-10-24T10:00:50.252319+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why didn't we use the COM static store to clean up the unmarshalable delegate?

Source: https://devblogs.microsoft.com/oldnewthing/20261023-00/?p=112793/

A third suggestion from Luca Bacci on
creating a fake agile wrapper that is technically agile but is not useful outside its home apartment
was to
use the COM static store
.
The COM static store doesn’t help us, because the COM static store runs down when the last thread shuts down COM, whereas we want something that runs down when a single apartment shuts down COM.
There is a per-apartment version of the COM static store, but it is part of the
Core­Application­View
, which is (1) something that only UWP programs have, and (2) exists only for apartments that have a core application view, and those are restricted to single-threaded apartments.
Even if there were a per-apartment static store, putting something into it would require generating a unique name and remembering it for later removal. You could probably use the stringified address of the object, with a fixed GUID prefix as a pseudo-namespace. Since we’re dealing with a dictionary, the insertion and removal operations are going to be
O
(log
n
) or
O
(1), depending on the implementation, but even the constant-time version will have a higher constant than a single index lookup in the Global Interface Table.
