# From monolith to resilient microservices

**Source:** https://rehanvdm.com/blog/from-monolith-to-resilient-microservices/
**Author:** Rehan van der Merwe
**Date:** 2021-11-17

## Core Message

This presentation combines insights from two related blog posts:
- Should you use microservices?
- Refactoring a distributed monolith to microservices

## Architecture Decision Tree

The author provides a decision tree for choosing between:
1. **Traditional Monolith** — Single application, tightly coupled
2. **Distributed Monolith** — Multiple services, shared business logic (anti-pattern)
3. **Modular Monolith** — Single deployment, strict logical boundaries
4. **Microservice** — Independent services, fully isolated business logic

## Key Insights

- Multiple teams naturally gravitate toward microservices
- Large single teams tend toward monolithic architectures
- Use Amazon EventBridge and Event Carried State Transfer for loose coupling
- "Shoot for Microservice and fall on a Modular monolith if you have to"

## Three Types of Monoliths

1. Traditional Monolith
2. Distributed Monolith
3. Modular Monolith
