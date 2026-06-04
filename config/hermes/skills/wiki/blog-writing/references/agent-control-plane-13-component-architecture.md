# Agent Control Plane: 3-Layer / 13-Component Architecture

Reference for mapping Agent Control Plane components to existing wiki technical primitives.

## 3-Layer Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Agent Control Plane                   │
├─────────────────────────────────────────────────────────┤
│  統治層    │ Identity  │ Permission │ Security  │ Audit │
│ (Who/Can)  │ Registry  │ Management │ Policy    │ Export│
├────────────┼───────────┼────────────┼───────────┼───────┤
│  実行層    │ Execution │ Tool Call  │ Human     │ Roll- │
│ (What/How) │ Logs      │ History    │ Approval  │ back  │
├────────────┼───────────┼────────────┼───────────┼───────┤
│  観測層    │ Evaluation│ Failure    │ Cost      │       │
│ (How well) │ Results   │ Classifi-  │ Management│       │
│            │           │ cation     │           │       │
└────────────┴───────────┴────────────┴───────────┴───────┘
```

## 13-Component × Wiki Primitive Mapping

### Governance Layer (Who / Can)

| # | Component | Wiki Primitives | Maturity |
|---|-----------|-----------------|----------|
| 1 | Agent Registry | `agent-communication-standards` (A2A Agent Cards), `agent-ontology` (Palantir Ontology) | ◎ |
| 2 | Agent Identity | `agent-identity-verification` (Sigstore Signed Agent Cards), `agentic-identity` (Ramp OBOU) | ○ |
| 3 | Permission Mgmt | `agent-governance` (granular boundaries), `agentic-ai-governance` (Yale CELI 3-tier) | ○ |
| 4 | Security Policy | `agent-governance` (Runtime Guardrails), `agent-sandbox-patterns` (Zero Secrets), `mcp-protocol` | ○ |
| 5 | Audit Export | `agent-ontology` (Decision Lineage), `agent-observability` (framework-agnostic traces) | ○ |

### Execution Layer (What / How)

| # | Component | Wiki Primitives | Maturity |
|---|-----------|-----------------|----------|
| 6 | Execution Logs | `agent-observability` (trace collection), `agent-runtime` (execution state) | ◎ |
| 7 | Tool Call History | `agent-observability` (tool traces), `mcp-protocol` (standardized metadata) | ◎ |
| 8 | Human Approval | `human-in-the-loop` (risk-based escalation), `enterprise-agents` (Staged Actions: Propose→Review→Commit) | ○ |
| 9 | Rollback | `enterprise-agents` (Scenario-Based Simulation), `durable-execution` (checkpoint-restart) | ○ |

### Observation Layer (How Well)

| # | Component | Wiki Primitives | Maturity |
|---|-----------|-----------------|----------|
| 10 | Evaluation Results | `agent-observability` (Feedback-Powered Learning Loop), `agent-development-lifecycle` (Test phase) | ◎ |
| 11 | Failure Classification | `agent-observability` (failure identification), `agent-development-lifecycle` (Monitor→Iterate) | △ |
| 12 | Cost Management | `cognitive-cost-of-agents`, `reasoning-model-cost-transparency`, `ai-coding-cost-optimization` | △ |
| 13 | Tenant Memory | Tenant Agent Pack L1 + L7, `agent-sandbox-patterns` (Isolate the Agent) | ◎ |

## Platform Implementation Comparison

| Domain | Google (Gemini EAP) | ServiceNow | Workday | Palantir (AIP) |
|--------|---------------------|------------|---------|----------------|
| Registry | Agent Gateway + Card | Agent Orchestrator | Agent System of Record | Ontology (semantic) |
| Identity | Cloud Identity | ITSM Identity | Employee-parity | Ontology ACL |
| Permission | IAM | Workflow-based | RBAC extension | Granular ACL + Writeback |
| Execution Logs | Cloud Logging | Now Platform Audit | Activity Log | Decision Lineage |
| Human Approval | TBD | Approval Flow extension | Managerial hierarchy | Staged Actions |
| Evaluation | Simulation + Obs. | Built-in dashboards | Performance Metrics | Ontology-based |
| Strength | Infra integration | Existing ITSM base | HR metaphor consistency | Ontology depth |

## Identified Gaps
1. **Agent Policy as Code**: Declarative policy language (like Kubernetes NetworkPolicy / OPA) for Agents
2. **Real-time Registry State**: Beyond static Agent Cards — live "where is this Agent running right now"
3. **Unified Failure Classification**: Systematic taxonomy (currently artisan-level per implementation)
4. **Tenant-Level Cost Visualization**: Real-time per-tenant cost dashboards
5. **HITL UX at Scale**: How to prevent human approval from becoming the bottleneck

## Source Articles
- `blog/2026-05-25_hermes_agent-control-plane-technical-architecture.md`
- `concepts/agent-control-plane.md`
- `raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md`
