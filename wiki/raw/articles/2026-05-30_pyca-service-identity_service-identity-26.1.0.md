---
source_url: https://github.com/pyca/service-identity/releases/tag/26.1.0
title: "service-identity 26.1.0 Release"
date: 2026-05-30
source_slug: pyca-service-identity
author: Hynek Schlawack
x_referrer: hynek
tag_name: "26.1.0"
github_release_id: 331927868
---

# service-identity 26.1.0

**Release date:** 2026-05-30
**Author:** Hynek Schlawack (@hynek)
**Repository:** [pyca/service-identity](https://github.com/pyca/service-identity)

## Highlights

The true highlight is that thanks to cryptography 47, we can drop two dependencies (that have served us very well for more than a decade; thank you so much *pyasn1* maintainers!).

## Full Changelog

### Added

- Python 3.14 and 3.15 are now officially supported. [#85](https://github.com/pyca/service-identity/pull/85) [#93](https://github.com/pyca/service-identity/pull/93)

### Changed

- *service-identity* now uses *cryptography*'s Rust-based ASN.1 decoder and doesn't depend on *pyasn1* and *pyasn1-modules* anymore. As a result, the oldest supported pyOpenSSL backend combination is now *pyOpenSSL* 26.1.0 with *cryptography* 47.0.0. [#95](https://github.com/pyca/service-identity/pull/95)

### Fixed

- Verifying a single-label hostname (e.g. `localhost`) against a wildcard certificate pattern now raises `VerificationError` cleanly instead of crashing with an opaque `ValueError`. [#92](https://github.com/pyca/service-identity/pull/92)
