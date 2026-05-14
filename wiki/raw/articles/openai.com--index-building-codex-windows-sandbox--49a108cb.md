---
title: "Building a safe, effective sandbox to enable Codex on Windows"
url: "https://openai.com/index/building-codex-windows-sandbox"
fetched_at: 2026-05-14T07:00:38.178310+00:00
source: "OpenAI News"
tags: [blog, raw]
---

# Building a safe, effective sandbox to enable Codex on Windows

Source: https://openai.com/index/building-codex-windows-sandbox

When I joined the Codex engineering team in September 2025, Codex for Windows didn’t have a sandbox implementation meaning that Windows users were forced to choose between two subpar options when using OpenAI's coding agents:
Approving nearly every command (even reads) that a coding agent wanted to run, which is inefficient and pesky.
A major benefit of using Codex is that you don’t have to do all the
tedious work yourself.
Enabling Full Access mode: letting Codex run all commands without approval or restrictions, which removes friction at the expense of oversight.
Codex
⁠
, our coding agent, runs on developer laptops—whether that's through the CLI, the IDE extension, or the desktop app. It manages a conversation between a human at a keyboard and a model running in the cloud to handle inference.
Codex runs with the permissions of a real user by default, meaning it can do everything the user can do. This is powerful and potentially dangerous. The coding model may tell the harness to run commands locally, from running tests to reading or editing a file to creating a Git branch, so Codex's default mode attempts to find the right balance between effectiveness and safety. This default mode allows Codex to read files almost anywhere and write files within your workspace (i.e., the directory where you're running Codex), with no internet access unless you specify you want it. To achieve this automatic constraint of writing files and accessing the network within safe bounds, Codex needs a sandbox environment that actually enforces these constraints.
A
sandbox
is a constrained execution environment. When a developer uses Codex, their computer's operating system launches a command with reduced permissions, and those constraints propagate down the process tree. Every Codex command is sandboxed from the start, and every descendant process stays inside the same boundary.
Codex needs isolation features enforced by the computer's operating system to implement an effective sandbox. Some operating systems provide utilities that do this well (e.g., Seatbelt on MacOs, seccomp or bubblewrap on Linux); however, Windows doesn't currently provide this type of capability out of the box.
To make Codex just as safe and delightful to use on Windows as it already is everywhere else, we needed to implement our own sandbox.
Windows offers some tools and primitives for isolation. While none of them quite met our requirements, we looked at a number of potential solutions—namely, AppContainer, Windows Sandbox, and Mandatory Integrity Control labeling.
What:
AppContainer is the native Windows sandbox, a capability-based isolation model built for apps that know, up front, exactly what they need to access.
Why
: Appealing because it offers a real OS boundary instead of best-effort restrictions.
Why not
: Codex is not one tightly scoped app. It drives open-ended developer workflows: shells, Git, Python, package managers, build tools, and whatever other binaries the agent decides it needs. In practice, that made AppContainer the wrong shape for the problem. It was strong isolation, but for a much narrower class of workloads than “let an agent operate like a developer.”
What:
Windows Sandbox is Microsoft’s disposable lightweight VM. You get a fresh Windows desktop with a strong isolation boundary, and whatever you do inside it disappears when the session ends.
Why
: Interesting for obvious reasons—far more compatible with arbitrary software than AppContainer, and from a security perspective it's a much stronger box.
Why not
: Codex needs to act directly on the user’s actual checkout, tools, and environment, not inside a separate throwaway desktop that would need setup and host/guest bridging. It also had a fundamental product problem: Windows Sandbox isn't even available on Windows Home SKUs.
Mandatory Integrity Control (MIC) integrity labeling
What
: Windows has a concept called “integrity levels,” such as low, medium, and high, that determine how much the system trusts objects and processes. The basic rule is that a lower-integrity process cannot write to an object with a higher integrity level, even if the normal ACL would otherwise allow it. For example, a low-integrity process is treated as less trusted, so Windows blocks it from writing to normal medium-integrity objects, unless those objects are explicitly relabeled to allow it.
Why
: MIC looked elegant on paper—run Codex at low integrity, relabel the writable roots as low integrity, and let Windows enforce no-writes everywhere else. That would've given us a non-admin path with a real OS mechanism behind it.
Why not
: Like ACLs, integrity labels modify the real host filesystem, and in this case the semantic change is especially broad. Marking a workspace as low integrity does not just mean “Codex can write here.” It means low-integrity processes
in general
can write there. On a real developer machine, that turns the user’s actual checkout into a low-integrity sink for the host, which is much riskier than granting carefully targeted ACLs to one sandbox design. Even if medium-integrity developer tools continue to work, the underlying trust model of the workspace has changed in a way that's hard to contain and harder to justify.
Having evaluated all of the options as non-starters, we started designing our own solution to bring a good Codex experience to Windows users.
The first prototype: the "unelevated sandbox"
Our first working prototype used a combination of Windows concepts and tools to implement the isolation we needed. From the beginning, one goal was to make this work without requiring
elevation
, meaning that Codex would not need to prompt the user for administrator privileges just to set up or run the sandbox. That meant figuring out how to put reasonable limits on two things: file writes and network access.
If we didn't limit file writes at all, we'd have a safety issue. If we limited file writes too much, the sandbox would hurt user productivity, needing to ask for constant approval. To solve this problem, we relied on two important Windows building blocks: SIDs and write-restricted tokens.
A SID, or security identifier, is the identity Windows ties
to permissions
. Each user has a SID, groups have SIDs, and even a single login session gets its own SID. For example, a current logged-in session might have a SID like
S-1-5-5-X-Y
. The SID assigned to the local administrators group might be
S-1-5-32-544
.
Windows also lets you create synthetic SIDs that don't correspond to a real user but can still appear in ACLs (access control lists), which define who can read/write/execute specific files or directories. That makes SIDs a useful primitive for our sandbox: we can create SIDs exclusively for the Codex sandbox to use, without interfering with anything else on the machine.
Process tokens are security objects in Windows that define identity and privileges for a running process. They determine what actions a process can perform. A
write-restricted token
is a particular type of process token that makes Windows perform an additional access check on write operations.
In order for a write to succeed, two checks must pass:
The normal user identity (the token “owner”) must be allowed to do it
At least one SID in the token’s restricted SID list must also be granted access
In practice, these checks let us use ACLs to define exactly where the sandbox could modify the filesystem, which offered the granularity we needed around write operations.
With SIDs and write-restricted tokens, our unelevated sandbox worked like this:
The sandbox setup created a synthetic SID called
sandbox-write
.
The
sandbox-write
SID was granted write, execute, and delete access to
The current working directory
Any additional
writable_roots
configured in
config.toml
.
The sandbox setup explicitly denied that same SID write access to “read-only within writable” locations such as:
<cwd>/.git
<cwd>/.codex
<cwd>/.agents
Codex launched commands under a write-restricted token whose restricted SID list includes
Everyone
, the current logged in session SID, and the
sandbox-write
synthetic SID.
This flow effectively solved limiting file writes and seemed promising. Now we needed a solution for limiting the sandbox's network access.
Limiting network access is an important part of the sandbox; without it, malicious code could exfiltrate data from the machine up to the internet. Because we wanted to avoid an elevation requirement, we had limited options to strongly block network traffic. The tools we wanted to use, like Windows Firewall, generally could not be installed without admin permissions.
Without Windows Firewall as an option, we limited what we could control. We tried to make the child environment fail-closed for the kinds of networked tools developers actually use, so that Git commands, package installers, etc., would fail in the sandbox and the user would have to approve any internet-facing operations. The idea was to poison the obvious escape hatches: send proxy-aware traffic to a dead endpoint, make Git’s HTTP(S) transport do the same, and make Git over SSH fail immediately. On top of that, we prepended a small
denybin
directory to PATH and reordered
PATHEXT
so stub SSH and SCP scripts would resolve before the real binaries.
For example, here are some of the specific environment overrides we used to limit network access:
HTTPS_PROXY=http://127.0.0.1:9
ALL_PROXY=http://127.0.0.1:9
GIT_HTTPS_PROXY=http://127.0.0.1:9
NO_PROXY=localhost,127.0.0.1,::1
GIT_SSH_COMMAND=cmd /c exit 1
That caught a lot of normal tool-driven traffic, but it was still only advisory. A process could ignore the environment, bypass PATH, or just open sockets directly—too risky.
As with any interesting software implementation, the first prototype had some pros and cons. While it got the job done with only a few standard Windows capabilities, allowed for very explicit and granular filesystem writes, and ran unelevated—cutting the need for users to accept excessive elevation prompts or be admins on their local machine—it had some real drawbacks, some of which disqualified it from becoming our final design:
Speed of setup: Applying workspace ACLs can be expensive depending on the topology of the workspace directory.
Footprint: We applied real ACLs to the developer’s system, although the footprint is not particularly invasive because all the applied ACLs pertain to a custom-created synthetic SID that is used only by the sandbox.
Difficult-to-change semantics: The reliance on ACLs for file-based restrictions means it's expensive and complex to change sandbox semantics. Whereas on macOS, we can dynamically change how we generate the
.sbpl
file used to configure Seatbelt, the Windows sandbox could require a slow and intense operation to adjust ACLs.
Network protection is weak. As mentioned before, it was “advisory,” would definitely be circumvented by some programs that implemented their own networking stack, and wasn't designed to hold up to adversarial code.
The first three issues are inherent to a custom sandbox implementation that's flexible enough for agentic flows. The network suppression story was different, though.
In addition to a malicious agent being able to easily circumvent the environment-based network suppression, plenty of good-intentioned code/binaries would also circumvent it simply if they didn’t honor the environment proxy variables, or if they implemented their own socket-based network code. We felt that this aspect was enough to consider investing in a better sandbox mode.
To gain better network suppression, we wanted to use Windows Firewall, which allows us to block outbound network traffic for users or programs. Unfortunately, we couldn't effectively create a functional firewall rule that applied only to the commands spawned by the Codex harness for a few reasons:
Windows doesn't allow matching a firewall rule to the non-principal identity of a restricted token. This means we couldn't apply a firewall rule to “any token that includes our synthetic SID in its restricted SID list."
While we could create a firewall rule that matches a specific binary, that only allows us to limit networking for
codex.exe
itself. It wouldn't apply to the processes that the agent spawns on behalf of the user, like Git or Python processes.
Other firewall match dimensions were the wrong shape, too. User-scoped rules still matched the real Windows user in the unelevated design, not just the restricted child. Program-path rules were too coarse: they could block
codex.exe
or
python.exe
generally, but not this one sandboxed invocation of
python.exe
. Port- or address-based rules were also the wrong policy entirely. For instance, we didn't want to block port 443; we wanted to block arbitrary outbound access for this specific restricted process tree.
To apply a firewall rule specifically to our sandboxed commands, we needed to run them as a separate principal, not as the “real” user. This approach led us down a new path, one in which we relaxed our “no elevation” constraint.
The redesign: the "elevated sandbox"
The next iteration of the sandbox, which is our current implementation, requires elevated admin permissions at setup time. I therefore refer to it as “the elevated sandbox.” At the boundary where Codex spawns a command on the system, the elevated sandbox looks like the unelevated one. It still runs child processes under a restricted token—similarly a
write_restricted
token with the same restricted SID list of
[Everyone, Logon,
Synthetic
]
—however, the principal of this token is no longer the actual Windows user but one of two local users created by Codex itself:
CodexSandboxOffline
(the one targeted by firewall rules)
CodexSandboxOnline
(the one not targeted by firewall rules)
This seemingly small detail actually has big implications for the sandbox, who can use it, and the complexity of its setup and runtime execution.
It’s visually similar to the unelevated prototype, with the introduction of firewall rules and a dedicated Windows user, which actually runs the commands. (However, the introduction of these new concepts, means that there is more setup work to do before the sandbox can start running and protecting commands.)
The unelevated sandbox design had a simple setup step, but it was relatively small:
Create a synthetic SID if needed
Apply ACLs for the sandbox-write synthetic SID
The elevated sandbox, however, has more to do.
Create a synthetic SID, if not already created
Create the online and offline sandbox users, if not already created
Store the newly-created users’ credentials locally and encrypt using the Windows Data Protection API (DPAPI) in a place where the sandbox users cannot actually read
Create firewall rules that block all outbound network access for the
CodexSandboxOffline
user or, if they already exist, validate they're correct
There's an additional wrinkle in the setup stage. Codex’s sandbox is expected to have read access equivalent to the actual Windows user. In the unelevated sandbox, where the restricted token’s principal SID was the Windows user, this was achieved. However, that doesn't come for free when the principal becomes a new
CodexSandbox
user. Many relevant directories on Windows will grant read/execute permissions to “Authenticated Users”. One notable example is the user’s profile directory. By default, Windows users cannot read the profile directories of other Windows users, so even simple file reads in many scenarios would fail.
To address this, we added another layer to the sandbox setup process—one for granting
read
ACLs to the sandbox users where such ACLs might not already exist. For example, to some commonly used Windows directories:
C:\Users\<real-user>
C:\Windows\
C:\Program Files\
C:\Program Files (x86)\
C:\ProgramData\
Because this list of directories is best-effort and installing ACLs on each one can be quite expensive, we run this logic asynchronously so the sandbox setup step, which is blocking to users, doesn't have to wait for them to complete.
We encapsulated the setup logic in its own binary partly to cross the UAC boundary only when needed. But the deeper reason was architectural: sandbox setup has a fundamentally different job from
codex.exe
. Keeping the sandbox setup logic in a dedicated binary let
codex.exe
stay a normal, unelevated harness; kept the Windows-only setup machinery from bloating
codex.exe
on other platforms; decoupled longer-running setup work from the lifetime of the main process; and gave us one place to handle the different setup paths the sandbox needed.
Because of how Windows user and token login boundaries work, we couldn't continue to create a restricted token and spawn a process under it the way we could with the unelevated sandbox. To actually spawn commands as a different Windows user, our first idea was the following flow:
codex.exe
runs as the real Windows user. Then, in a sequence, Codex:
Calls
LogonUserW(...)
for the sandbox user.
Calls
CreateRestrictedToken(...)
on that sandbox-user token.
Using that restricted sandbox-user token, calls
CreateProcessAsUserW(...)
to launch the final child.
In practice, that desired flow didn't work because of a privilege wall at
CreateProcessAsUserW(...)
. This means
codex.exe
could create a restricted token for the sandbox user, but it couldn't reliably launch a child with that token from the real-user side of the boundary. We needed a process that was already running as the sandbox user—this would let the restriction step and final spawn happen on the sandbox-user side of the boundary instead of the real-user side.
That requirement led to
codex-command-runner.exe
, a new binary whose only job is to mint a restricted token and spawn the requested command. Instead of asking
codex.exe
to do the entire flow itself (real user → sandbox user → restricted token → child process), we split the flow in two:
codex.exe
calls
CreateProcessWithLogonW(...)
to launch
codex-command-runner.exe
as the sandbox user, without using a restricted token yet.
Inside the runner,
OpenProcessToken(GetCurrentProcess(), ...)
opens the runner’s own token, which already belongs to the sandbox user.
The runner calls
GetTokenInformation(...)
to extract the sandbox logon SID, then
CreateRestrictedToken(...)
to build the final restricted token.
Still inside the runner, it calls
CreateProcessAsUserW(...)
with that restricted token to launch the real child.
Albert Einstein said, “Everything should be made as simple as possible, but no simpler.” In that spirit, our design adequately solved each problem. The final architecture has the four layers we have previously covered:
codex.exe
itself
codex-windows-sandbox-setup.exe
for handling all elevated setup related work
codex-command-runner.exe
for running restricted token commands
The child process
When I first approached this project, I did not have a strong sense of where it would wind up. My approach was to start by instrumenting the sandboxing capability in the boundary between Codex and the operating system. This approach closely matches how Codex’s sandbox is implemented on MacOs and Linux.
As I learned more about the specific tools that Windows provides, and through dozens of decisions balancing security and ease of use, the system grew to its current form—multiple binaries, custom users, firewall rules, an elevated setup step, asynchronous processes, and more.
It’s not a particularly simple system, but each piece of complexity was added out of necessity, to build a sandbox that is both safe and, as much as possible, not in the user's way.
Balancing safety with actual usefulness
Working to deliver a good user experience for Codex users on Windows, our goal was to make something safe that didn't compromise on usefulness—the whole point of using Codex is to have agents be able to do work without your constant attention.
One of the biggest lessons from this project was that Windows did not hand us one primitive that cleanly maps to “safe autonomous coding agent.” We composed several tools and concepts to build something coherent. Some early ideas were dead ends. The final design was a hybrid of earlier prototypes that each solved part of the problem.
The other lesson was that security for a coding agent is a different beast than more classic application security. Codex has to work for real developer workflows. The engineering work was about balancing compatibility with agentic workloads against real enforcement. That tension shaped tradeoffs in the final design.
Curious to see the Codex sandbox in action?
Try it out
⁠
.
