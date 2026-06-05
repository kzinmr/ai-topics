---
name: english-e2e-harness
kind: system
---

# English E2E Harness

### Description

Runs English-described end-to-end web tests that may start servers, drive real
browsers, close and reopen tabs on a schedule, kill or restart allowed
processes, collect evidence, and assert observable behavior.

### Services

- `scenario-planner`
- `preflight-checker`
- `server-manager`
- `browser-launcher`
- `timeline-coordinator`
- `browser-event-driver`
- `process-event-driver`
- `telemetry-collector`
- `assertion-judge`
- `cleanup-manager`
- `reporter`

### Requires

- `test_brief`: English E2E scenario, including user-visible steps, timing-sensitive events, process disruptions, and expected behavior
- `project_root`: local repository or app directory where server commands run
- `server_commands`: one or more commands used to start required local servers
- `base_url`: URL the browser should test after servers are ready
- `browser_matrix`: browsers, devices, viewports, and tab/session requirements
- `process_policy`: allowlist of process names, ports, tmux sessions, or PIDs that this run may start, kill, or restart
- `credential_policy`: names of environment variables the test may require; never raw secret values
- `artifact_policy`: where screenshots, traces, videos, logs, snapshots, and reports should be written
- `timeout_policy`: startup, navigation, action, assertion, and global timeout budgets

### Ensures

- `e2e_report`: final pass, fail, blocked, or error report with reproduction steps and concise evidence
- `assertion_report`: every assertion from the English brief mapped to pass, fail, blocked, or skipped with observed evidence
- `event_timeline`: ordered timeline of browser actions, process events, waits, restarts, tab closes, tab reopens, and assertions with observed timestamps
- `evidence_bundle`: artifact index containing paths to screenshots, traces, videos, console logs, network logs, server logs, and tmux captures
- `cleanup_report`: processes and browser sessions cleaned up, intentionally preserved, or requiring manual attention
- if preflight blocks execution: `e2e_report` explains the missing tool, unsafe process policy, unavailable credential variable, port conflict, or bad command without starting browsers or servers
- if assertions fail: `e2e_report` still includes artifacts and exact failing observations rather than treating test failure as harness failure

### Errors

- `unsafe-process-request`: the English brief asks to kill or restart something outside `process_policy`
- `harness-tool-unavailable`: a required CLI tool is missing
- `artifact-write-failed`: required evidence cannot be written to the declared artifact location

### Invariants

- Never kill, restart, or signal a process unless it was started by this run or explicitly allowlisted by `process_policy`.
- Never log, echo, serialize, or publish raw credential values.
- Use real browser actions for user behavior; do not replace user-visible checks with DOM mutation shortcuts.
- Every timing-sensitive assertion records planned time, observed time, tolerance, and evidence.
- Cleanup is attempted after every started run, including failed and interrupted runs.
- Published outputs contain artifact paths and summaries, not private scratch files.

### Tools

- `cli:tmux`: start and inspect long-running server processes
- `cli:playwright-cli`: open browsers, manage tabs, drive interactions, capture snapshots, traces, screenshots, console, and network events
- `cli:node`: run project scripts or local test helpers when declared by the scenario
- `cli:ps`: inspect local process state
- `cli:pkill`: stop allowlisted processes when policy permits it

### Runtime

- `persist`: true

### Execution

```prose
let cleanup_report = null
let execution_result = null
let server_state = null
let browser_state = null

let plan = call scenario-planner
  test_brief: test_brief
  browser_matrix: browser_matrix
  process_policy: process_policy
  timeout_policy: timeout_policy
  artifact_policy: artifact_policy

let preflight = call preflight-checker
  project_root: project_root
  server_commands: server_commands
  base_url: base_url
  credential_policy: credential_policy
  process_policy: process_policy
  artifact_policy: artifact_policy
  timeout_policy: timeout_policy
  e2e_plan: plan.e2e_plan

if preflight has blocking findings:
  execution_result = {
    status: "blocked",
    e2e_plan: plan.e2e_plan,
    preflight_report: preflight.preflight_report
  }
else:
  try:
    server_state = call server-manager
      project_root: project_root
      server_commands: server_commands
      base_url: base_url
      process_policy: process_policy
      timeout_policy: timeout_policy
      artifact_policy: artifact_policy
      e2e_plan: plan.e2e_plan

    browser_state = call browser-launcher
      base_url: base_url
      browser_matrix: browser_matrix
      artifact_policy: artifact_policy
      timeout_policy: timeout_policy
      e2e_plan: plan.e2e_plan

    let timeline = call timeline-coordinator
      e2e_plan: plan.e2e_plan
      server_state: server_state
      browser_state: browser_state
      timeout_policy: timeout_policy

    parallel (on-fail: "continue"):
      let browser_events = call browser-event-driver
        e2e_plan: plan.e2e_plan
        browser_state: browser_state
        timeline: timeline
        artifact_policy: artifact_policy
        timeout_policy: timeout_policy

      let process_events = call process-event-driver
        e2e_plan: plan.e2e_plan
        server_state: server_state
        timeline: timeline
        process_policy: process_policy
        artifact_policy: artifact_policy
        timeout_policy: timeout_policy

      let telemetry = call telemetry-collector
        e2e_plan: plan.e2e_plan
        server_state: server_state
        browser_state: browser_state
        timeline: timeline
        artifact_policy: artifact_policy

    let assertions = call assertion-judge
      e2e_plan: plan.e2e_plan
      browser_events: browser_events
      process_events: process_events
      telemetry: telemetry
      timeout_policy: timeout_policy

    execution_result = {
      status: "complete",
      e2e_plan: plan.e2e_plan,
      server_state: server_state,
      browser_state: browser_state,
      browser_events: browser_events,
      process_events: process_events,
      telemetry: telemetry,
      assertion_report: assertions.assertion_report
    }
  catch as err:
    execution_result = {
      status: "error",
      error: err,
      e2e_plan: plan.e2e_plan,
      server_state: server_state,
      browser_state: browser_state
    }
  finally:
    cleanup_report = call cleanup-manager
      server_state: server_state
      browser_state: browser_state
      process_policy: process_policy
      artifact_policy: artifact_policy

return call reporter
  execution_result: execution_result
  cleanup_report: cleanup_report
  artifact_policy: artifact_policy
```

## scenario-planner

### Requires

- `test_brief`: English E2E scenario
- `browser_matrix`: browser, device, viewport, and tab/session requirements
- `process_policy`: process action allowlist
- `timeout_policy`: timing and timeout budgets
- `artifact_policy`: evidence retention rules

### Ensures

- `e2e_plan`: normalized plan with setup, browser steps, process events, timed actions, assertions, tolerances, and artifact requests
- `plan_warnings`: ambiguities or assumptions preserved for the final report

### Shape

- `self`: translate English into an executable test plan and reject unsafe ambiguity
- `prohibited`: running commands, opening browsers, killing processes, or reading secrets

## preflight-checker

### Requires

- `project_root`: app directory
- `server_commands`: commands to start servers
- `base_url`: target URL
- `credential_policy`: required environment variable names
- `process_policy`: process allowlist
- `artifact_policy`: artifact paths
- `timeout_policy`: timeout budgets
- `e2e_plan`: normalized plan

### Ensures

- `preflight_report`: blocking and non-blocking readiness findings
- `run_contract`: exact tools, commands, environment variable names, artifact paths, and allowed process targets for this run

### Shape

- `self`: inspect readiness and safety boundaries
- `prohibited`: starting servers, opening browsers, killing processes, or revealing credential values

## server-manager

### Requires

- `project_root`: app directory
- `server_commands`: commands to start servers
- `base_url`: health target
- `process_policy`: process allowlist
- `timeout_policy`: timeout budgets
- `artifact_policy`: log locations
- `e2e_plan`: normalized plan

### Ensures

- `server_state`: tmux sessions, commands, ports, PIDs when observable, health status, and log paths
- `server_readiness`: evidence that the app is reachable or a blocked startup diagnosis

### Shape

- `self`: start and monitor only declared servers
- `prohibited`: touching unrelated processes or editing app source

## browser-launcher

### Requires

- `base_url`: target URL
- `browser_matrix`: browsers and viewports
- `artifact_policy`: browser artifact locations
- `timeout_policy`: timeout budgets
- `e2e_plan`: normalized plan

### Ensures

- `browser_state`: browser sessions, tabs, viewports, trace/video handles, and initial snapshots
- `launch_report`: launch success, failures, and browser capability notes

### Shape

- `self`: create browser contexts and initial tabs with Playwright
- `prohibited`: bypassing user-visible behavior with DOM mutation shortcuts

## timeline-coordinator

### Requires

- `e2e_plan`: normalized plan
- `server_state`: active server state
- `browser_state`: active browser state
- `timeout_policy`: timeout budgets

### Ensures

- `timeline`: monotonic test start, scheduled browser events, scheduled process events, assertion windows, tolerances, and global deadline

## browser-event-driver

### Requires

- `e2e_plan`: normalized plan
- `browser_state`: active browser sessions
- `timeline`: scheduled event plan
- `artifact_policy`: browser artifact locations
- `timeout_policy`: timeout budgets

### Ensures

- `browser_events`: ordered browser actions and observations, including tab close/reopen events with planned and observed timings
- `browser_artifacts`: screenshots, traces, videos, snapshots, console logs, and network logs

### Strategies

- Use Playwright actions such as click, fill, press, hover, tab-close, tab-new, reload, and snapshot for signoff behavior.
- For requests like "close tab in 2 seconds and reopen", record both scheduled and observed times.

## process-event-driver

### Requires

- `e2e_plan`: normalized plan
- `server_state`: active server state
- `timeline`: scheduled event plan
- `process_policy`: process allowlist
- `artifact_policy`: process artifact locations
- `timeout_policy`: timeout budgets

### Ensures

- `process_events`: ordered process kills, restarts, waits, health probes, and observed recovery behavior
- `process_artifacts`: tmux captures, server logs, process snapshots, and restart evidence

### Errors

- `unsafe-process-request`: a requested signal, kill, or restart is outside policy

## telemetry-collector

### Requires

- `e2e_plan`: normalized plan
- `server_state`: active server state
- `browser_state`: active browser state
- `timeline`: scheduled event plan
- `artifact_policy`: artifact locations

### Ensures

- `telemetry`: console errors, network failures, page errors, server logs, health probes, and timestamped observations
- `telemetry_artifacts`: artifact paths for raw telemetry captured during the run

## assertion-judge

### Requires

- `e2e_plan`: normalized plan
- `browser_events`: browser actions and observations
- `process_events`: process actions and observations
- `telemetry`: collected runtime evidence
- `timeout_policy`: timing tolerances

### Ensures

- `assertion_report`: each English assertion mapped to pass, fail, blocked, or skipped with evidence and timing details
- `failure_diagnosis`: likely cause, reproduction notes, and missing evidence for every failed or blocked assertion

## cleanup-manager

### Requires

- `server_state`: server state or `null`
- `browser_state`: browser state or `null`
- `process_policy`: process allowlist
- `artifact_policy`: artifact locations

### Ensures

- `cleanup_report`: browser sessions closed, servers stopped or intentionally preserved, remaining PIDs, and manual follow-up if cleanup could not finish

### Invariants

- Cleanup acts only on browser sessions and processes created by this run or explicitly allowed by `process_policy`.

## reporter

### Requires

- `execution_result`: blocked, complete, failed, or error execution payload
- `cleanup_report`: cleanup outcome or `null`
- `artifact_policy`: artifact locations

### Ensures

- `e2e_report`: concise final report with status, reproduction command, failures, risks, and artifact index
- `assertion_report`: assertion results or blocked-run explanation
- `event_timeline`: merged timeline of browser, process, telemetry, and assertion events
- `evidence_bundle`: complete artifact index
- `cleanup_report`: cleanup outcome, including no-op cleanup when preflight blocked execution
