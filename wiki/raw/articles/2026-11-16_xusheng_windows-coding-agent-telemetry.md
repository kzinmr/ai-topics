---
source_url: https://xusheng.dev/posts/windows-coding-agent-telemetry/
ingested: 2026-11-17
sha256: ebda293b993f4d88
hn_note: HN 619p https://news.ycombinator.com/item?id=50524736
---

Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use :: Xusheng Li 

>

Xusheng

Blog

Contact

CV

 7 minutes

Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use

Reverse engineering Windows 11's MissionControlAggregator reveals coding-agent and developer-tool usage bits in a diagnostic ETW report.

I recently asked AI to help me look through the latest Windows binaries for undocumented features and functionality. Among the leads it turned up, one list immediately caught my attention: coding agents such as 
codex.exe
, 
claude.exe
, 
copilot.exe
, and 
cursor.exe
, alongside familiar developer tools such as 
python.exe
, 
dotnet.exe
, 
gcc.exe
, and 
code.exe
.

Why would a Windows system DLL need a list of coding agents and developer tools?

The names were in 
MissionControlAggregator.dll
. I asked the agent to follow the references and dig into what the DLL actually does. That led from a handful of string comparisons to a running Windows component that records which coding agents and developer tools have been used, saves that information locally, and reports it to Windows Diagnostics. And unless you have opted out of the “optional” diagnostic data (which is enabled by default), the data is uploaded to Microsoft.

I 
shared the initial finding on X
. This post includes more details about the investigation behind it.

Following the names

Opening the DLL in 
Binary Ninja
 made the first lead easy to see. These were explicit executable names embedded in a Windows component:

Following the references showed that the names were used in comparisons. There are four CLI-agent slots checking 
copilot.exe
, 
claude.exe
, 
codex.exe
, and 
agy.exe
, with extensionless equivalents on the WSL route. Five desktop-agent slots check 
github.exe
, 
claude.exe
, 
codex.exe
, 
cursor.exe
, and 
antigravity.exe
.

Here is one of the comparisons against 
codex.exe
:

The compiler-generated C++ names are unwieldy, so I will call these functions 
executable-name matchers
. For reference, one related matcher is 
std::_Func_impl_no_alloc<<lambda_340dfe7e962ab225b6ac33bc664bd54f>, bool, std::basic_string_view<wchar_t, std::char_traits<wchar_t>> const&, Microsoft::Diagnostics::MissionControlAggregator::Utils::AppType>::_Do_call
. The screenshot shows another lambda instantiation performing the same kind of name comparison.

The feature guarding the new agent checks has a particularly direct name: 
CLICodingAgentUsage
, feature ID 
62580080
.

And the list extends beyond AI agents. The same component checks for 
node.exe
, 
python.exe
, 
dotnet.exe
, 
gcc.exe
, 
clang.exe
, 
gdb.exe
, 
javac.exe
, 
devenv.exe
, and 
code.exe
, among others. Those checks feed broader developer-tool categories. Some of these checks also verify the publisher: the Node.js slot expects 
Node.js Foundation
, Python expects 
Python Software Foundation
, and the .NET and Visual Studio slots expect 
Microsoft Corporation
. The compiler/debugger group containing GCC and Clang has no additional publisher check in this path.

Where does the DLL get this information?

The next question was whether the component scans running processes itself. Following 
Aggregator::OnLoad
 revealed that it subscribes to existing Windows events instead.

For Windows programs, it consumes 
KernelProcess.AppStateChangeSummary
 and 
Win32kTraceLogging.AppInteractivitySummary
. These provide application identities that its handlers parse and pass to the matchers. For WSL, it consumes 
Microsoft.Windows.Lxss.Manager.Exec
 and 
ExecCritical
, using the 
imageName
 field. A regular Windows 
codex.exe
 can therefore reach the CLI-agent checks through the app-state summary route; this is not limited to Linux programs running inside WSL.

The relevant flow looks like this:

Aggregator::OnLoad

├─ WSL Exec / ExecCritical

│ └─ ProcessWslExecEvent → CLI agent matchers

├─ KernelProcess.AppStateChangeSummary

│ └─ ProcessAppStateChangeSummaryEvent → CLI agent matchers

└─ Win32kTraceLogging.AppInteractivitySummary

 └─ ProcessAppInteractivitySummaryEvent → desktop agent matchers

Aggregator::OnRelativeTimerExpire

└─ MissionControlAggregatorLogging::ReportCohorts<12,4,5>

 └─ Segments.SubCohorts ETW report

Aggregator::OnUnload / intermediate timer

└─ PersistentState::SaveToDisk

A successful match sets a slot in the aggregator’s state. Later, 
ReportCohorts<12,4,5>
 turns those slots into bitsets and emits a report named 
Segments.SubCohorts
. The numbers correspond to twelve broader tool categories, four CLI agents, and five desktop agents.

ETW (Event Tracing for Windows)
 is the mechanism carrying that report. In this case, it is a self-describing TraceLogging event. Rather than writing the executable names into every report, the component assigns each category a bit. A set Codex bit means the matching tool was observed during the reporting window.

The source events also include runtime, time in focus, interaction counters, and resource usage. This component appears to discard those details and record only a bitmap of which agents were observed. The report’s timestamps describe the collection window, not how long each agent was used.

Although I found no prompt text or source code in this report, collecting which agents and developer tools someone uses already has significant privacy implications.

Is it actually running on a normal machine?

Strings and code are a useful lead, but I wanted to see the component running. I checked my Parallels Windows 11 ARM64 VM, build 
26200.9974
. Its 
MissionControlAggregator.dll
 was version 
10.0.26100.9818
, and 
CLICodingAgentUsage
 was already enabled as a service experiment. I had not manually enabled the feature.

DiagTrack, the 
Connected User Experiences and Telemetry
 service, was also already running with its startup type set to 
Automatic
. It starts a separate 
AggregatorHost.exe
 process, and that process loads the DLL. The following administrative PowerShell commands show the service, its child process, and the loaded module:

PS> Get-Service DiagTrack | Format-Table Name,Status,StartType -AutoSize

Name Status StartType

---- ------ ---------

DiagTrack Running Automatic

PS> Get-Process AggregatorHost | Format-Table ProcessName,Id -AutoSize

ProcessName Id

----------- --

AggregatorHost 
1500

PS> Get-CimInstance Win32_Service -Filter 
"Name='DiagTrack'"
 |

 Format-List Name,State,StartMode,ProcessId

Name 
:
 DiagTrack

State 
:
 Running

StartMode 
:
 Auto

ProcessId 
:

10148

PS> Get-CimInstance Win32_Process -Filter 
"Name='AggregatorHost.exe'"
 |

 Format-List ProcessId,ParentProcessId

ProcessId 
:

1500

ParentProcessId 
:

10148

PS> tasklist /m MissionControlAggregator.dll

Image Name PID Modules

========================= ======== ============================================

AggregatorHost.exe 
1500
 MissionControlAggregator.dll

The process IDs connect the pieces: DiagTrack runs in process 
10148
, which is the parent of 
AggregatorHost.exe
, process 
1500
; the module listing places 
MissionControlAggregator.dll
 inside that child.

The public ISO’s baseline VM had the coding-agent feature disabled by image default, so the evidence does not support saying that it is active on every Windows installation. On my ARM64 VM, however, the relevant feature and service were active before the test.

Testing it in practice

To test the finding in practice, I copied 
cmd.exe
 to a file named 
codex.exe
 and ran it in the interactive Windows session. The name alone was enough for the component to recognize it as Codex.

I captured an 
AppStateChangeSummary
 for the running process from the 
KernelProcess
 provider (
{2839ff94-8f12-4e1b-82e3-af7af77a450f}
), with 
LaunchCount=1
 and 
TerminateCount=0
. The aggregator’s saved state contained the value 
2
 in CLI slot 2, the Codex slot. A separate run without an additional ETW trace also set that slot, confirming that detection worked through Windows’ existing diagnostic collection.

That state is persisted in:

C:\ProgramData\Microsoft\Diagnosis\AggregatorStorage\MissionControlAggregator$

The report normally follows a roughly daily boundary. To capture it immediately, I temporarily moved the saved reporting-window start 25 hours into the past and restarted DiagTrack with a trace listening for the aggregator. The resulting 
Segments.SubCohorts
 event contained:

Provider: Microsoft.Windows.MissionControlAggregator

Time: 2026-11-16T12:34:29.125116Z

Version: 0.1.5

CliAgentSubCohorts: 4

DesktopAgentSubCohorts: 0

FlushedFromSave: true

The value 
4
 is 
1 << 2
: the Codex CLI bit. The name had made it through the input summary, the matcher, the persisted state, and the emitted report.

I also tested the developer-tool path separately, using a copy of 
cmd.exe
 named 
gcc.exe
. It set developer-tool slot 3. With optional diagnostic data allowed, I found the resulting 
Segments.SubCohorts
 event in DiagTrack’s upload queue with 
SubCohorts: [8]
 (
1 << 3
). This is the compiler/debugger category shared by GCC, Clang, and related tools, rather than a separate bit for each executable.

Following the report toward Microsoft

An ETW event by itself would not establish that anything leaves the machine. ETW is used for plenty of local diagnostics. The more revealing question was who was listening to this particular report.

The VM already had a 
Diagtrack-Listener
 session subscribed to both ends of the path. These PowerShell queries showed its subscriptions:

Get-EtwTraceProvider -SessionName Diagtrack-Listener `

 -Guid 
'{2839ff94-8f12-4e1b-82e3-af7af77a450f}'

Get-EtwTraceProvider -SessionName Diagtrack-Listener `

 -Guid 
'{00de11a2-ec06-58e5-1a2b-21bb21dbee4b}'

The first subscription, for 
KernelProcess
, had 
MatchAnyKeyword=0x400000000002
, which includes the summary’s 
0x400000000000
 keyword. The second, for 
Microsoft.Windows.MissionControlAggregator
, had 
MatchAnyKeyword=0xe00000000000
, which includes the report’s 
0x800000000000
 keyword. Both had level 
255
.

The subscription showed where the report could go. To check whether Windows actually queued it for transmission, I inspected DiagTrack’s 
EventStore.db
 and decompressed the JSON batches in its 
AsimovEvents
 table. This revealed an important condition: the agent-usage report is treated as 
optional diagnostic data
.

When optional diagnostic data is allowed (enabled by default in the US setup I tested), Windows queues the coding-agent usage report for upload to Microsoft.
 I verified this by finding the agent event itself in DiagTrack’s upload queue:

{

"name"
: 
"Microsoft.Windows.MissionControlAggregator.Segments.SubCohorts"
,

"ext"
: {

"privacy"
: { 
"isRequired"
: 
false
 }

 },

"data"
: {

"Version"
: 
"0.1.5"
,

"CliAgentSubCohorts"
: [
4
],

"DesktopAgentSubCohorts"
: [
0
],

"FlushedFromSave"
: 
true

 }

}

I checked this with a clean installation of Windows 11 Home ARM64 using the latest official ISO, with the region set to the United States. Before changing any privacy settings, the 
Diagnostic data
 toggle was already enabled and labeled 
Include Optional
. After completing setup with those defaults, 
AllowTelemetry
 was 
3
, confirming that optional diagnostic data was enabled.

Optional diagnostic data is therefore enabled by default, at least in the US setup I tested. If you did not opt out of it during installation or disable optional diagnostic data later, it is still enabled and your coding agent usage data is being uploaded. You can decline optional diagnostics during setup or turn off 
Send optional diagnostic data
 later under 
Settings → Privacy & security → Diagnostics & feedback
. Microsoft’s 
diagnostics and privacy guide
 explains how to change it.

Windows

privacy

telemetry

reverse engineering

Reverse Engineering

 1480 Words

 2026-11-16 00:00

LG Updated Its “Adware”

→

© 2026

CC BY-NC 4.0

Powered by 
Hugo

Made with ❤ by 
Djordje Atlialp