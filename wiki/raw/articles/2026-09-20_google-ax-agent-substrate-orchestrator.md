---
source_url: https://ax-ai.io/
ingested: 2026-09-28
sha256: acf49c1abe2c46c34ae36bcfb96c6418faa6ee0a846d0f934e0ce6f1488f6a86
---

Declare an agentic task. AX runs it at scale. 
 AX sandboxes your task, wires up its workspace, fences its network, and helps you run a large number of
 them per cluster. Either use a single task per agent, or compose as many as your agent needs. 

 Get started 
 View on GitHub 

 Pause 

 $ cat task.yaml 
 apiVersion: ax.io/v1alpha1 
 kind: Workspace 
 metadata: 
 name: golang 
 spec: 
 git: 
 - repo: https://github.com/golang/go.git 
 branch: "my-fix" 
 --- 
 apiVersion: ax.io/v1alpha1 
 kind: Task 
 metadata: 
 name: test 
 spec: 
 workspaces: 
 - name: golang 
 goal: "Ensure that Go tool chain is available and is built from source" 
 debug: true 
 $ ax apply -f task.yaml 
 workspace.ax.io/golang created 
 task.ax.io/test created 
 $ ax watch task test 
 Watching task default/test... 
 [10:42:01] Phase: Pending Actor: test WorkerIP: 
 [10:42:05] Phase: Running Actor: test WorkerIP: 10.20.3.67 
 Task reached terminal phase "Running". 
 $ ax get tasks 
 NAME ATESPACE PHASE ACTOR WORKER-IP AGE 
 test default Running test 10.20.3.67 5s 
 $ ax ssh test -- ls /workspace 
 go 
 $ ax ssh test -- cd /workspace/go && go build ./... 
 $ ax ssh test -- ps -o pid,cmd 
 PID CMD 
 1 /usr/local/bin/ax-task-runner 
 12 go build ./... 
 $ ax ssh test -- touch notes.txt 
 $ ax suspend task test 
 task.ax.io/test suspended 
 $ ax resume task test 
 task.ax.io/test resumed 
 $ ax ssh test -- ls notes.txt 
 notes.txt 
 $ ax suspend task test 
 task.ax.io/test suspended 
 $ ax delete task test 
 task.ax.io/test deleted 

 Why AX 
 Agents are a new kind of workload. 
 They are neither microservices nor batch jobs. They accumulate
 state, need strict isolation, call out to model APIs and tool servers, and can waste resources if nobody is
 watching. AX gives you four small primitives that handle all of that declaratively. 

 Task 
 Isolated execution 
 Run untrusted agent code in a sandbox with CPU and memory limits. Cheap to create, suspend, and throw away.

 Workspace 
 Easy workspace setup 
 List the Git repos, MCP servers, and skills an agent needs, or just describe the goal. AX sets it all up in
 every sandbox before the task starts. 

 Gateway 
 Network policies 
 Define and quickly manage network policies. Lock traffic down to an explicit allowlist of hosts and
 ports, inject credentials to the incoming requests. 

 Model 
 One place for config 
 Configure models, model parameters, and secrets in one place. Rotate a key or pin a new model version with
 one apply. 

 How it works 
 Scales up to billions of tasks. 
 AX runs on top of Agent Substrate ,
 a compute runtime designed from the ground up for massive density and fast stateful actor lifecycles. 

 Billions of tasks 
 Every task runs as a lightweight actor, allowing you to scale to
 billions of concurrent agent sessions per cluster without orchestrator limits. 

 Sub-second resumption 
 Idle agents waiting on model responses, external tool calls, or human responses are checkpointed, suspended,
 and brought back
 in under a second with zero cold-start delay. 

 Dense multiplexing 
 Dozens of tasks share worker resources, turning idle waiting time into spare compute capacity so you only pay
 when agents are actively thinking and running code. 

 Generative platform 
 Generative features built into the platform. 
 AX integrates generative AI directly into the platform. For example, if you want to set up a workspace just by explaining it in plain English, the environment is prepared automatically before your task starts. 

 task.yaml 
 apiVersion : ax.io/v1alpha1 
 kind : Task 
 metadata : 
 name : data-analysis 
 spec : 
 workspaces : 
 - name : python-env 
 goal : "Set up a Python 3 development environment" 

 Generative workspaces 
 Describe what a ready environment looks like in plain English. AX hands that goal to an agent on first boot
 to install toolchains and verify dependencies. 

 Run anything and everything 
 Interactive coding agents, long-running agent servers, Jupyter notebooks, headless browser testing, and custom tool runtimes—you name it. 

 Perfect match for researchers 
 Spin up massive number of reproducible sandboxes to collect trajectories, run reinforcement
 learning loops, and evaluate agents at scale. 

 For builders & researchers 
 Built to be the most friendly runtime for developers and researchers. 
 We want to make dealing with agentic infrastructure easier so you can focus on your work. AX
 is
 designed with an uncompromising focus on ergonomics, rapid iteration, and joyful workflows for both application
 developers and AI researchers. 
 We aim to keep the runtime minimal and lightweight, while tastefully adding the essential
 features everyone needs to build, evaluate, and scale agents. 

 About 
 Born from research, built for production. 
 AX was born at Google when agentic runtime systems research met frontier compute. Over years
 of building and operating agentic execution engines, teams across Google recognized that agentic workloads
 represent an entirely new computing paradigm: stateful, bursty, long-running actors that compute intensely for a
 minute and then wait for model responses, tool responses, or human approval. Traditional orchestrators built for
 stateless
 microservices or predictable batch jobs become cost-prohibitive when keeping idle sandboxes running, yet lack
 native support for sub-second suspend and resume. 
 Drawing on agentic runtime research from Google DeepMind alongside deep experience in
 large-scale isolation, resumption, and scheduling, AX is being built as an open, declarative control plane
 purpose-built for agent execution. It abstracts tasks, workspaces, network policies, and models into core
 primitives so developers and researchers can run massive fleets of agents without reinventing the underlying
 infrastructure. This project heavily relies on Agent
 Substrate but provides agentic abstractions and generative runtime components.
