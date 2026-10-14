---
title: "Legacy Code Seams"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, software-engineering, testing, architecture, design-patterns, java]
sources:
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch02.html
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch11.html
  - https://learning.oreilly.com/library/view/working-effectively-with/0131177052/ch04.html
  - https://learning.oreilly.com/library/view/monolith-to-microservices/9781492047834/ch03.html
confidence: high
---

# Legacy Code Seams

A seam is a substitution opportunity that changes the behavior reached by a piece of code while leaving that piece's call site unchanged. Michael Feathers develops this model in *Working Effectively with Legacy Code*, Chapter 4, to make existing code testable with limited changes.

Every usable seam needs an **enabling point**: the place that selects the substitute. Identifying an interface or overridable method is insufficient if the caller still fixes the concrete implementation internally.

## Types and enabling points

| Type | Substitution mechanism | Enabling point | Main concern |
|---|---|---|---|
| Object | Supply a different collaborator or override | Object construction, argument or composition setup | Preserve the real call path and contract |
| Link | Resolve a symbol/class to another implementation | Linker inputs, classpath or build setup | Make test/production resolution differences explicit |
| Preprocessing | Replace text before compilation | Build definition or conditional preprocessing | Hidden variants and maintenance complexity |

Feathers generally prefers object seams in object-oriented languages because their selection is more explicit. His Java classpath example illustrates a link seam; it is a historical testing technique, rather than a recommendation for a current Java module configuration.

## Sensing and separation

Substitution can serve two different purposes:

- **Separation:** avoid a database, network call or other dependency that makes a test slow, unsafe or difficult to run.
- **Sensing:** record arguments, calls or effects so the test can assert what happened.

A substitute that does nothing provides separation but may provide no useful observation. A recorder supports sensing, but still does not establish that a real remote system would accept the interaction. Use the seam for [[concepts/characterization-testing]] and retain appropriate real integration checks.

## Example application

Suppose a billing routine constructs its own email sender. Adding an interface alone does not let a test select a recorder. Moving the selection into an explicit composition point lets the same billing routine use the real sender in production and the recorder in a test. This is an original illustration of the enabling-point distinction.

Keep the initial change small: changing the dependency boundary and changing the business calculation together makes a regression harder to localize. A seam creates a place to observe and replace behavior; it does not validate the calculation or authorize its redesign.

## Worked example: select a notification recorder

This original Python illustration has no network side effects:

```python
class FeeBatch:
    def __init__(self, emit_notice):
        self.emit_notice = emit_notice

    def process(self, amount_cents):
        if type(amount_cents) is not int or not 0 <= amount_cents <= 1_000_000:
            raise ValueError("amount must be integer cents in the allowed range")
        fee_cents = amount_cents * 25 // 1000
        self.emit_notice({"fee_cents": fee_cents})
        return fee_cents

notices = []
batch = FeeBatch(notices.append)
assert batch.process(1999) == 49
assert notices == [{"fee_cents": 49}]
```

`process` reaches the collaborator through `self.emit_notice`. The **enabling point** is construction of `FeeBatch`, where the supplied function is selected. A production composition supplies a real sender; the test supplies `notices.append`. The invocation `batch.process(1999)` is unchanged between those compositions.

The recorder performs separation, because no real notification is sent, and sensing, because the exact argument and call count can be checked. Replacing it with a function that discards its argument would keep separation but lose that evidence.

If the original constructor creates its own concrete sender, first introduce the selection boundary with the calculation unchanged. That preparatory refactor has its own risk; check observable behavior before combining it with a rounding change. Dependency injection means supplying a collaborator from outside the object, as illustrated here; it does not require a framework.

**Check your understanding:** Does the assertion establish that the real notification service accepts this message? No. It establishes the batch's request to its collaborator. A real integration check must establish delivery behavior, failures and the receiver's contract.

## From testing to migration

Sam Newman's *Monolith to Microservices*, Chapter 3, uses an internal abstraction when the capability cannot be intercepted at the system perimeter. The old implementation remains active while a replacement is built, tested and selected later. See [[concepts/incremental-legacy-migration]].

A test enabling point and a production migration switch have different operating obligations. A production switch also needs ownership, observability, compatible state and eventual removal of obsolete paths.

## Related

- [[concepts/characterization-testing]] — capture behavior after dependencies are isolated
- [[concepts/incremental-legacy-migration]] — use boundaries for gradual replacement
- [[concepts/architectural-fitness-functions]] — protect dependency constraints
- [[queries/modernization-inner-loop-study-notes]] — inspected sections
