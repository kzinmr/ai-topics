---
title: Microservices vs Monolith
created: 2026-04-16
updated: 2026-04-16
tags:
  - architecture
  - microservices
  - monolith
  - distributed-systems
aliases:
  - monolith-vs-microservices
  - monolith
  - microservices
  - distributed monolith
  - modular monolith
sources:
  - https://rehanvdm.com/blog/should-you-use-microservices/
  - https://rehanvdm.com/blog/from-monolith-to-resilient-microservices/
  - wiki/raw/articles/should-you-use-microservices.md
---

# Microservices vs Monolith Architecture

## Decision Framework

Rehan van der Merwe's architecture decision tree provides a pragmatic approach:

```
Team Size & Complexity Assessment
├── Small team (< 10 people) + Simple domain
│   └── → Traditional Monolith
├── Small team + Complex domain
│   └── → Modular Monolith (shoot for this minimum)
├── Multiple teams + Simple domain
│   └── → Modular Monolith
└── Multiple teams + Complex domain
    └── → Microservices
```

## Architecture Types

### 1. Traditional Monolith
- **Definition**: Single application with all functionality in one codebase
- **Pros**: Simple deployment, easy debugging, shared state
- **Cons**: Tight coupling, single point of failure, hard to scale independently
- **Team Fit**: Small teams, simple domains

### 2. Distributed Monolith
- **Definition**: Multiple services but tightly coupled through shared business logic or synchronous calls
- **Anti-Pattern**: Services depend on each other's internal state or APIs
- **Pros**: Appears to be microservices but with shared complexity
- **Cons**: Cascading failures, complex deployment, difficult debugging
- **Team Fit**: Multiple teams transitioning from monolith

### 3. Modular Monolith
- **Definition**: Single application with clear module boundaries, independent deployment possible
- **Pros**: Clear separation of concerns, easier scaling than traditional monolith
- **Cons**: Still shared deployment, some coupling remains
- **Team Fit**: Growing teams, medium complexity

### 4. Microservices
- **Definition**: Independent services with their own data stores, deployed separately
- **Pros**: Independent scaling, fault isolation, team autonomy
- **Cons**: Complex deployment, distributed debugging, eventual consistency
- **Team Fit**: Large teams, complex domains, mature DevOps

## Conway's Law Application

> "Multiple teams will gravitate towards microservices and a large singular team will tend to build monolithic software."

- Team structure should drive architecture choice, not vice versa
- Align service boundaries with team boundaries
- Use organizational structure as a constraint when designing systems

## Migration Path

1. **Traditional Monolith** → **Modular Monolith**
   - Extract clear module boundaries
   - Implement internal APIs between modules
   - Add comprehensive tests

2. **Modular Monolith** → **Distributed Monolith**
   - Deploy modules as separate services
   - Maintain shared state/data stores
   - Add service discovery

3. **Distributed Monolith** → **Microservices**
   - Give each service its own data store
   - Implement event-driven communication
   - Add proper failure handling and retries

## Key Principles

- **Start Simple**: Begin with monolith unless you have a clear need for microservices
- **Extract When Necessary**: Only split services when team size or complexity demands it
- **Use Event-Driven Patterns**: Amazon EventBridge + Event Carried State Transfer for loose coupling
- **Design for Failure**: Implement retries, DLQs, and circuit breakers
- **Monitor Everything**: Observability is critical for distributed systems

## Related Concepts
- [[lambda-monolith-lambdalith]]
- [[event-driven-architecture]]
- [[conways-law]]
- [[blast-radius]]
