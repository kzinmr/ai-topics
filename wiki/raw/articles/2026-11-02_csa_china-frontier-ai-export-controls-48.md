# SOURCE: https://labs.cloudsecurityalliance.org/research/csa-research-note-china-ai-export-controls-announcement-48-2/
# Fetched: 2026-11-02

China’s First Frontier AI Export Controls: MOFCOM Announcement No. 48
	
	

	
Authors: Cloud Security Alliance AI Safety Initiative

Published: 2026-10-23

Categories: AI Governance and Regulation

Download PDF

Download Markdown

China’s First Frontier AI Export Controls: MOFCOM Announcement No. 48
Key Takeaways
On October 16, 2026, China’s Ministry of Commerce (MOFCOM) and Ministry of Science and Technology (MOST) issued Announcement No. 48 of 2026. The announcement proposes adding 40 technologies to the Catalogue of Technologies Prohibited or Restricted from Export, 23 of them in artificial intelligence, and it imposes an interim pre-export registration requirement that is already in effect [1][2]. China’s catalogue has touched AI before: the 2020 revision added personalized recommendation and AI interaction interface technology [6]. Unlike those 2020 additions, the draft reaches frontier model weights, agent architectures, and AI-enabled offensive cyber capability, with explicit technical thresholds for each [1].

The announcement contains two instruments with different legal status. The catalogue additions are a draft open for comment until November 15, 2026, while the registration requirement applies now, including to exports that have started but are not yet complete [1][2]. Within the draft, model weights are restricted at frontier scale. Weights, key checkpoints, source code, architecture, and training and inference optimization know-how are restricted if a model meets any one of three tests: at least 10^26 FLOPs of training compute, at least 2 trillion parameters, or a global top-10 position on public evaluation rankings, global call volume, or comparable measures at the time of export [1][3]. Agents are controlled independently of the model. Planning, multi-agent coordination, tool use, and game-theoretic decision technologies are restricted above set benchmarks, and high-performance agents built for critical infrastructure, defense, or core government use are prohibited outright [1].

The line between service access and custody determines most enterprise exposure. MOFCOM says API, app, web, SaaS, and lightweight on-device use do not count as exporting a large model. Deploying a restricted model locally outside China does count, though automatic licensing may apply on a Chinese company’s own overseas cloud [2]. Multinationals also face exposure through licensing deals and changes of ownership or control, not only through product exports, and analysts read the registration form as potentially capturing intra-group code sharing as well [2][3][4]. Any transfer of ownership, licensing for overseas use, or shift of control to a foreign entity can trigger registration [2][4].

Background
China regulates outbound technology transfer under two overlapping regimes. The first is the technology-trade regime under the Foreign Trade Law and the Regulations on Technology Import and Export Administration, which governs the catalogue being revised here. The second is the dual-use export-control regime under the 2020 Export Control Law [5]. MOFCOM’s spokesperson described the revision as routine and grounded in Article 20 of the Foreign Trade Law. The spokesperson stressed that it “does not target any specific country, region, or entity” and that the aim is to prevent uncontrolled diffusion while protecting legitimate cooperation [2]. The catalogue has been revised several times since 2001. The August 2020 revision, which added recommendation-algorithm technology, coincided with the proposed sale of TikTok to a U.S. buyer and was reported as likely to complicate that deal [3][6].

Across all three sectors, Announcement No. 48 proposes 14 prohibited and 26 restricted items: 23 in AI, 5 in biomedicine, and 12 in photovoltaics [2]. In China’s technology-trade framework, prohibited technologies may not be exported at all, while restricted technologies require a license from commerce and science authorities. ChinaTalk notes that licensing is administered by provincial authorities, although central authorities have intervened in prominent cases [3]. The official annex groups the AI items into large models, agents, compute clusters, chip design, and information-processing technologies. It also excludes from management any technology that has already entered the public domain through open-source release or academic publication [1].

The interim registration requirement is the part that applies today. From the announcement date until the revised catalogue takes effect, exporters must register through MOFCOM’s unified business platform before exporting any listed technology. Registration covers four triggers: transfer of technology ownership abroad, licensing of domestic technology for overseas use, a change in ownership or control that makes a foreign entity the owner or controller, and other cases MOFCOM designates [2][4]. Exporters must decide for themselves whether a technology falls within scope. The registration form asks for recipient details, destination, technology description, end use, and estimated value [2][4].

The timing also matters for enterprises that already track U.S. controls. CSA’s prior research documented the first U.S. use of export-control authority to suspend a broadly deployed commercial frontier model [9]. Announcement No. 48 means frontier AI supply chains now face formal outbound controls from both of the largest AI-producing jurisdictions. ChinaTalk observes that the 10^26 FLOP threshold mirrors the figure used in the 2023 U.S. executive order and the since-rescinded 2025 U.S. AI Diffusion rule. The authors also estimate that no released Chinese model currently exceeds it [3].

Security Analysis
What the AI Annex Actually Controls
The annex is granular, and its structure matters for scoping. The table below summarizes the AI items drawn from the official draft annex [1], with interpretive notes from published analyses [3][4].

Category
Control
Key Thresholds or Conditions (draft)

Large models trained on China’s “core data”
Prohibited
Core data scope defined by the Data Security Law and related regulations

Large models trained on China’s “important data”
Restricted
Excludes trace use (≤0.1%) of desensitized important data that does not materially improve capability or reappear in outputs, and lawfully public data

Core large-model technologies (weights, checkpoints, source code, architecture, training and inference optimization)
Restricted
Any one of: ≥10^26 FLOPs; ≥2 trillion parameters; global top-10 position on public evaluation rankings, global call volume, or comparable measures at the time of export

High-performance agents for critical infrastructure, defense, or core government
Prohibited
Agent meets the restricted agent thresholds and is specially or mainly designed for those uses

Agent planning and task decomposition
Restricted
≥20-step subtask chains, ≥80% decomposition accuracy, ≥90% subtask success

Multi-agent collaboration architectures
Restricted
≥60 concurrent agents, completion time ≤2x the single-agent minimum, ≥85% agreement with reference answers

Tool calling and system operation
Restricted
≥200 integrated third-party tools, ≥90% tool-selection accuracy, ≥90% end-to-end success on tasks requiring 3+ tools

AI malicious code generation, adaptive evasion, and variant generation
Prohibited
Attack-success and automation thresholds, where usable against high-sensitivity systems

AI-assisted vulnerability discovery
Restricted
Any of six tests, including ≥75% on authoritative benchmarks, 10x senior-expert efficiency, or autonomous chaining of 2+ low or medium flaws into a working exploit

AI detection technology specially designed for cross-border data security
Prohibited
Detection accuracy and recall ≥95%

Deepfake detection; steganography; voiceprint; Chinese and minority-language translation
Restricted
Accuracy, recall, latency, and fidelity thresholds (for example, ≥98% for deepfake detection)

AI chip and memory chip design; large compute cluster technologies
Restricted
Process node ≤14 nm and other alternative criteria for AI chips; interconnect ≥800 GB/s, fault tolerance, and heterogeneous scheduling for clusters above 10,000 accelerators

Three features of this structure deserve attention from security and compliance teams. First, the “global leading” test is dynamic. A model that falls below the compute and parameter thresholds can still become restricted if its public evaluation rank, global call volume, or similar measures place it in the top 10 when the export occurs [1]. ChinaTalk calls this criterion “by far the most up-for-interpretation,” noting that the rule names no ranking body [3], and it means the compliance status of a given model version can change after deployment. Second, the agent items are defined by system behavior rather than by the underlying model. An orchestration framework that integrates hundreds of tools could meet the tool-use threshold even when it runs on a model well below the frontier thresholds, an issue Ray Sun identifies as unresolved [5]. Third, the cyber items carry direct security consequences: Chinese-origin AI red-teaming, vulnerability-discovery, and detection tools that meet the thresholds would require a license to leave China, and offensive code-generation capability could not be exported at all.

Deployment Models and Where the Line Falls
MOFCOM’s spokesperson framed the central test as whether restricted technology moves from inside China to overseas [2]. That framing produces a clear distinction between consuming a model as a service and taking custody of it, as summarized below.

Deployment scenario
Treatment under MOFCOM guidance

API calls, apps or websites, SaaS for overseas customers
Not within large-model export management [2]

Lightweight on-device deployment
Not within large-model export management [2]

Local deployment of a restricted model on infrastructure outside China
Within export management; license required [2]

Deployment on a Chinese company’s self-operated overseas cloud or compute center
Automatic licensing (“report and export”) may apply [2]

Open-sourcing newly developed restricted technology
Automatic licensing after reporting [2]

Technology already public via open-source release or academic papers
Outside management scope [1]

For enterprises, the practical consequence is that the deployment model the draft captures, local self-hosting, is also the one often chosen for data-protection reasons. Organizations that chose to self-host a Chinese frontier model in their own environment, rather than call a Chinese-hosted API, did so to keep sensitive data inside their own boundary. MOFCOM places local deployment outside China within export management, which means those self-hosting arrangements require the Chinese supplier to hold a license [2]. ChinaTalk reads this as also covering on-premises licensing deals and managed deployments in which a vendor runs an agent’s reasoning loop inside a customer environment [3]. Because licenses can be revoked or conditioned, ChinaTalk suggests this may lead some non-Chinese users to reconsider such dependencies [3]. The registration requirement already covers exports in progress, so ongoing weight-delivery or model-update arrangements may be affected now rather than after the catalogue is finalized [2].

The treatment of open weights depends on whether a model is already public. Weights that are already public are outside the controls [1]. Open-sourcing a new restricted model, however, falls under automatic licensing that still requires reporting [2]. Commentators note that “open source” is not defined, and that it is unclear how restricted-use licenses would be treated [3]. Organizations that depend on successive open-weight releases from Chinese labs should therefore treat future release cadence, not just current availability, as a variable outside their control.

Exposure Through Corporate Structure
The exposure most likely to surprise multinationals sits in their own organizational charts. Registration is triggered by licensing technology for overseas use and by changes of ownership or control, not only by sales to third parties [2][4]. A multinational with China-based R&D teams building agent frameworks, vulnerability-discovery tooling, or fine-tuned models may therefore need to register before sharing that work with affiliates outside China. ChinaTalk reads the registration form’s field on exports made outside formal contracts as potentially capturing intra-group code sharing and open-sourcing [3]. This reading is an inference from the form rather than an official statement, but it is a reasonable basis for conservative scoping.

The data-based items add a second pathway. A model fine-tuned in China on operational data that qualifies as “important data” under the Data Security Law would be restricted, unless the de minimis carve-out applies. A model trained on “core data” would be prohibited [1]. Organizations that classified China-resident data under the Data Security Law for cross-border data transfer purposes may not have applied the same classification to training and fine-tuning datasets, since those obligations previously governed data transfer rather than model transfer.

Finally, recent precedent suggests that redomiciling does not remove Chinese jurisdiction. In January 2026, MOFCOM announced an assessment of Meta’s acquisition of Manus, a Singapore-registered AI agent company whose products were developed in China. The assessment examined whether the relocation of staff and technology required export authorization [7]. Announcement No. 48 now gives that line of scrutiny explicit, agent-specific thresholds, which suggests M&A due diligence on AI targets with China-origin development history should include an export-control workstream.

Recommendations
Immediate Actions
Organizations should first inventory every Chinese-origin model, agent framework, and AI security tool in use and record how each is consumed: as an API or SaaS service, as a lightweight on-device component, or as locally deployed weights or code. The local-deployment category is the priority, because it is the one the draft places within export management [2]. For each locally deployed asset, teams should ask the supplier in writing whether it has registered the export under Announcement No. 48 and whether it expects to need a license once the catalogue is final.

Legal and engineering teams should jointly review technology flows out of China-based subsidiaries, joint ventures, and R&D centers since October 16. The goal is to identify transfers that may already require registration, including code repositories, model checkpoints, and agent frameworks shared with overseas affiliates [2][4]. Organizations with a material interest in the final scope should prepare comments before the November 15, 2026 deadline, through the email, fax, or postal channels published in the announcement [1][4].

Short-Term Mitigations
Over the next one to two quarters, organizations should treat restricted-category Chinese models as regulated dependencies with documented fallbacks. Vendor contracts for locally deployed models should allocate responsibility for Chinese export registration and licensing, specify notice obligations if a license is denied, conditioned, or revoked, and address whether updates and new checkpoints are covered by the same authorization. Because the “global leading” test depends on rankings at the time of export [1], teams should not assume that a model version cleared today will remain uncontrolled for later updates.

Security teams that rely on AI-assisted vulnerability discovery or deepfake detection tools developed in China should map those tools against the restricted thresholds and identify alternatives. A licensing interruption to a detection capability is a security-control gap, not only a procurement issue. Data governance teams should also extend Data Security Law classification work to cover training and fine-tuning datasets held in China, so that “important data” and “core data” exposure is known before models trained on them are shared abroad [1].

Strategic Considerations
Announcement No. 48, if finalized substantially as drafted, would mean that frontier AI is treated as controlled technology by both the United States and China, with each regime drawing its lines differently. Recent U.S. measures have emphasized compute and, in the Fable 5 case, access to a deployed model, although the since-rescinded 2025 AI Diffusion rule also reached model weights [3]. The Chinese draft centers on custody of weights, know-how, and agent architectures. Enterprise AI governance programs should model export-control disruption from either jurisdiction as a standing risk scenario and design architectures that can swap models without rebuilding agent workflows.

Organizations should also recognize that the draft treats agents as a distinct regulatory object. Defining controls by planning depth, concurrency, and tool count means that internal agent platforms, and not only foundation models, may be subject to cross-border technology rules. Agent inventories should record these characteristics alongside traditional security attributes. Finally, because the final catalogue may narrow, broaden, or shift after consultation [3], and because ChinaTalk notes the comment window closes shortly before an expected leaders’ meeting at APEC [3], a timing that could bear on the final scope, this analysis should be revisited once MOFCOM publishes the final text.

CSA Resource Alignment
CSA’s most directly relevant prior work is Frontier AI Export Controls: Enterprise Governance After Fable 5 [8]. That note argues for treating frontier model access as a contingent operational dependency that belongs in vendor management and business continuity planning. Announcement No. 48 extends that argument to a second jurisdiction and to a different control point. The U.S. action examined in that note interrupted service access, while the Chinese draft leaves service access untouched and instead governs weight custody and local deployment. Enterprises that built continuity plans around the U.S. scenario should check whether those plans also cover a supplier-side license failure for self-hosted models.

AI Model Export Controls: The Fable 5 Precedent [9] documented how a single regulatory directive can remove a widely deployed model with little notice. Its recommendation for multi-model fallback strategies applies directly to organizations that depend on Chinese frontier or open-weight models, particularly given the dynamic “global leading” threshold described above. Sovereign AI Access Controls and Enterprise Concentration Risk [10] provides the broader framing. It treats national control over AI capability as a source of concentration risk, and the Chinese draft is a concrete instance of that risk materializing on the supply side.

For control implementation, the AI Controls Matrix (AICM) v1.1 [11] provides the relevant control objectives in its supply chain management, transparency and accountability, and governance, risk and compliance domains, including supplier inventory, third-party assessment, and regulatory change management. For agent-specific exposure, MAESTRO [12] offers a layered threat model that can help teams document the agent capabilities, such as tool integration and multi-agent coordination, that now carry export-control significance.

References
[1] Ministry of Commerce and Ministry of Science and Technology of the PRC. “Announcement No. 48 of 2026 on Public Consultation on Revising the Catalogue of Technologies Prohibited or Restricted from Export and Interim Registration of Related Technology Exports (商务部 科技部公告2026年第48号), with Annex 1 (Draft Scope of AI, Biomedicine, and Photovoltaic Technologies).” MOFCOM, October 16, 2026.

[2] Ministry of Commerce of the PRC. “MOFCOM Spokesperson Answers Questions on Revising the Catalogue of Technologies Prohibited or Restricted from Export (商务部新闻发言人就修订《中国禁止出口限制出口技术目录》答记者问).” MOFCOM, October 16, 2026.

[3] Ennis, Q., Zhang, I., Ottinger, L., and Zakaria, A. “MOFCOM’s New Rules and the Future of Chinese AI.” ChinaTalk, October 21, 2026.

[4] Geopolitechs. “China Imposes Temporary Export Registration Requirements for AI, Biotech and Solar Technologies, Seeks Public Comment on Proposed Export Restrictions.” Geopolitechs, October 16, 2026.

[5] Sun, R. “China’s AI Export Control Announcement Raises More Questions Than It Answers.” Ctrl+AI+Reg, October 19, 2026.

[6] Center for Security and Emerging Technology (translation). “Revisions to the Content of the Catalog of Prohibited or Restricted Technology Exports.” CSET, Georgetown University, September 2, 2020.

[7] South China Morning Post. “China to Probe Meta’s Purchase of Manus Regarding Export Control and Tech Exports.” SCMP, January 2026.

[8] Cloud Security Alliance. “Frontier AI Export Controls: Enterprise Governance After Fable 5.” CSA AI Safety Initiative, June 2026.

[9] Cloud Security Alliance. “AI Model Export Controls: The Fable 5 Precedent.” CSA AI Safety Initiative, June 2026.

[10] Cloud Security Alliance. “Sovereign AI Access Controls and Enterprise Concentration Risk.” CSA AI Safety Initiative, June 2026.

[11] Cloud Security Alliance. “AI Controls Matrix (AICM) v1.1.” Cloud Security Alliance, 2025.

[12] Cloud Security Alliance. “MAESTRO: Agentic AI Threat Modeling Framework.” CSA Lab Space, 2025.

← Back to Research Index
