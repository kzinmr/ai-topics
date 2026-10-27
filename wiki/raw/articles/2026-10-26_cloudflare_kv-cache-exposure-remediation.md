---
title: "Cross-request KV cache exposure in GLM-5.3 Workers AI (remediation)"
url: "https://blog.cloudflare.com/kv-cache-exposure-remediation/"
fetched_at: 2026-10-27T11:00:00+00:00
source: "blog.cloudflare.com"
date: 2026-10-26
tags: [blog, raw]
---

Cross-request KV cache exposure in GLM-5.3 Workers AI (remediation)

astro-island,astro-slot,astro-static-slot{display:contents}(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event("astro:only"));})();(()=>{var g=Object.defineProperty;var w=(a,s,c)=>s in a?g(a,s,{enumerable:!0,configurable:!0,writable:!0,value:c}):a[s]=c;var l=(a,s,c)=>w(a,typeof s!="symbol"?s+"":s,c);var E=new Set(["__proto__","constructor","prototype"]);{let a={0:t=>y(t),1:t=>c(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(c(t)),5:t=>new Set(c(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>Number.POSITIVE_INFINITY*t},s=t=>{let[p,e]=t;return p in a?a[p](e):void 0},c=t=>t.map(s),y=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([p,e])=>[p,s(e)]));class f extends HTMLElement{constructor(){super(...arguments);l(this,"Component");l(this,"hydrator");l(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let r=this.querySelectorAll("astro-slot"),n={},d=this.querySelectorAll("template[data-astro-template]");for(let o of d){let i=o.closest(this.tagName);i!=null&&i.isSameNode(this)&&(n[o.getAttribute("data-astro-template")||"default"]=o.innerHTML,o.remove())}for(let o of r){let i=o.closest(this.tagName);i!=null&&i.isSameNode(this)&&(n[o.getAttribute("name")||"default"]=o.innerHTML)}let u;try{u=this.hasAttribute("props")?y(JSON.parse(this.getAttribute("props"))):{}}catch(o){let i=this.getAttribute("component-url")||"",v=this.getAttribute("component-export");throw v&&(i+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${i}`,this.getAttribute("props"),o),o}let h;await this.hydrator(this)(this.Component,u,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});l(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),r.disconnect(),this.childrenConnectedCallback()},r=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});r.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}getRetryImportUrl(e){let r=new URL(e,document.baseURI);return r.searchParams.set("astro-retry",Date.now().toString()),r.toString()}async importWithRetry(e){try{return await import(e)}catch(r){return await new Promise(n=>setTimeout(n,1e3)),import(this.getRetryImportUrl(e))}}handleHydrationError(e){let r=this.getAttribute("component-url"),n=new CustomEvent("astro:hydration-error",{cancelable:!0,bubbles:!0,composed:!0,detail:{error:e,componentUrl:r}});this.dispatchEvent(n)&&console.error(`[astro-island] Error hydrating ${r}`,e)}async start(){let e=JSON.parse(this.getAttribute("opts")),r=this.getAttribute("client");if(Astro[r]===void 0){window.addEventListener(`astro:${r}`,()=>this.start(),{once:!0});return}try{await Astro[r](async()=>{let n=this.getAttribute("renderer-url");try{let[d,{default:u}]=await Promise.all([this.importWithRetry(this.getAttribute("component-url")),n?this.importWithRetry(n):Promise.resolve({default:()=>()=>{}})]),h=this.getAttribute("component-export")||"default";if(h.includes(".")){this.Component=d;for(let m of h.split(".")){if(E.has(m)||!this.Component||typeof this.Component!="object"&&typeof this.Component!="function"||!Object.hasOwn(this.Component,m))throw new Error(`Invalid component export path: ${h}`);this.Component=this.Component[m]}}else{if(E.has(h))throw new Error(`Invalid component export path: ${h}`);this.Component=d[h]}return this.hydrator=u,this.hydrate}catch(d){return this.handleHydrationError(d),()=>{}}},e,this)}catch(n){this.handleHydrationError(n)}}attributeChangedCallback(){this.hydrate()}}l(f,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",f)}})();All CategoriesAIDevelopersRadarProduct NewsSecurityPolicy & LegalZero TrustSpeed & ReliabilityLife at CloudflarePartnersglobalThis.process??={},globalThis.process.env??={};var e=document.querySelector(`[data-dropdown]`);e&&(document.addEventListener(`click`,t=>{let n=t.target;n instanceof Node&&e.open&&!e.contains(n)&&(e.open=!1)}),document.addEventListener(`keydown`,t=>{t.key===`Escape`&&e.open&&(e.open=!1)}));Switch Site LanguageEnglishDeutschEspañolEspañol (Latinoamérica)FrançaisItaliano日本語한국어繁體中文简体中文PortuguêsРусскийBahasa IndonesiaภาษาไทยTiếng ViệtPolskiالعربيةעבריתSvenskaNederlandsTürkçeglobalThis.process??={},globalThis.process.env??={};var e=document.querySelectorAll(`[data-language-dropdown]`);e.length&&(document.addEventListener(`click`,t=>{let n=t.target;n instanceof Node&&e.forEach(e=>{e.open&&!e.contains(n)&&(e.open=!1)})}),document.addEventListener(`keydown`,t=>{t.key===`Escape`&&e.forEach(e=>{e.open&&=!1})}));globalThis.process??={},globalThis.process.env??={};var e=document.documentElement;function t(){let t=e.classList.contains(`dark`);document.querySelectorAll(`[data-theme-toggle]`).forEach(e=>{e.setAttribute(`aria-pressed`,String(t))})}t(),new MutationObserver(t).observe(e,{attributes:!0,attributeFilter:[`class`]});LoginDashboardContact SalesglobalThis.process??={},globalThis.process.env??={};var e=document.querySelector(`[data-search-toggle]`),t=document.querySelector(`[data-ai-search-dialog]`),n=t?.querySelector(`search-modal-snippet`),r=document.querySelector(`#ai-search-widget-script`),i=new Set,a=null,o=`a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), summary, [tabindex]:not([tabindex="-1"])`;function s(){let e=document.activeElement;for(;e instanceof HTMLElement&&e.shadowRoot?.activeElement;)e=e.shadowRoot.activeElement;return e}function c(){return!t||!n?[]:[...t.querySelectorAll(o),...n.shadowRoot?.querySelectorAll(o)??[]].filter(e=>e.getClientRects().length>0&&getComputedStyle(e).visibility!==`hidden`)}function l(){let e=n?.shadowRoot?.querySelector(`[role="dialog"]`);e&&(e.removeAttribute(`aria-labelledby`),e.setAttribute(`aria-label`,t?.dataset.dialogLabel??``))}function u(e){t&&(e?Array.from(document.body.children).forEach(e=>{!(e instanceof HTMLElement)||e===t||e.contains(t)||e.inert||(e.inert=!0,i.add(e))}):(i.forEach(e=>{e.inert=!1}),i.clear()))}function d(){t&&(t.setAttribute(`aria-hidden`,`false`),t.inert=!1,e?.setAttribute(`aria-expanded`,`true`),u(!0),requestAnimationFrame(()=>{let e=s(),n=c();e instanceof HTMLElement&&n.includes(e)||(n[0]??t).focus()}))}function f(){t&&(t.inert=!0,t.setAttribute(`aria-hidden`,`true`),e?.setAttribute(`aria-expanded`,`false`),u(!1),(e&&e.getClientRects().length>0?e:a)?.focus({preventScroll:!0}),a=null)}function p(e){let n=c();if(!t||n.length===0){e.preventDefault(),t?.focus();return}let r=n[0],i=n[n.length-1],a=s(),o=a instanceof HTMLElement&&n.includes(a);e.shiftKey&&(a===r||!o)?(e.preventDefault(),i.focus()):!e.shiftKey&&(a===i||!o)&&(e.preventDefault(),r.focus())}function m(){n&&(a=document.activeElement instanceof HTMLElement?document.activeElement:null,typeof n.open==`function`?n.open():customElements.whenDefined(`search-modal-snippet`).then(()=>n.open?.()))}e?.addEventListener(`click`,m),n?.addEventListener(`open`,d),n?.addEventListener(`close`,f),customElements.whenDefined(`search-modal-snippet`).then(()=>{l(),n?.shadowRoot&&new MutationObserver(l).observe(n.shadowRoot,{childList:!0,subtree:!0})}),t?.addEventListener(`keydown`,e=>{e.key===`Tab`&&p(e)}),document.addEventListener(`keydown`,e=>{(e.metaKey||e.ctrlKey)&&e.key.toLowerCase()===`k`&&(a=document.activeElement instanceof HTMLElement?document.activeElement:null)},!0);var h=8e3;function g(){e&&!e.disabled&&(e.disabled=!0,e.removeAttribute(`aria-expanded`),e.setAttribute(`aria-label`,e.dataset.unavailableLabel??``))}if(e){r?.addEventListener(`error`,g);let e=customElements.whenDefined(`search-modal-snippet`),t=new Promise(e=>setTimeout(e,h));Promise.race([e,t]).then(()=>{customElements.get(`search-modal-snippet`)||g()})}BlogSecurityWorkers AI2 TagsShow 2 tagsPost TagsSecurityWorkers AIAll tagsMatching tagsNo tags found1.1.1.12FAAbuseAccessAccess Control Lists (ACLs)AccessibilityAccount TakeoverAcquisitionsAddressingAdvanced Certificate ManagerAdvanced DDoSAdvertisingAegisAEOAfricaAfroflareAgent CloudAgent Development LifecycleAgent ReadinessAgentsAgents WeekAgents Week 2026AIAI BotsAI GatewayAI SearchAI WAFAI WeekAI-SPMAlertmanagerAlways OnlineAMDAMPAnalyticsAnonymousAnti MalwareAnycastAPIAPI GatewayAPI SecurityAPI ShieldAPJCAppleApplication SecurityApplication ServicesArea 1 SecurityArgo Smart RoutingASCIIAsiaAthenian ProjectAtlassianAttacksAudit LogsAustinAustraliaAuthenticationAuthyAuto RagAutomatic HTTPSAutomatic Platform OptimizationAutomationAutoMinifyAwardsAWSBaiduBandwidth AllianceBandwidth CostsBest PracticesBetaBetter InternetBGPBillingBirthday WeekBlack FridayBlackbirdBot Fight ModeBot ManagementBotnetBotsBPFBrandBrand ProtectionBrazilBrowser InsightsBrowser RenderingBrowser RunBug BountyBugsBYOIPCacheCache PurgeCache ReserveCache RulesCaliforniaCanadaCap'n ProtoCAPTCHACareersCASBCategoriesCDNCDNJSCertificate AuthorityCertificate PinningCertificate TransparencyCertificationCFSSLChallenge PageChatGPTChinaChina NetworkChristmasChromeCIO WeekCISAClaireCLIClickHouseClientlessClientless Web IsolationCloud ConnectorCloud Email SecurityCloudflare AccessCloudflare AppsCloudflare Area 1Cloudflare CallsCloudflare Email ServiceCloudflare for CampaignsCloudflare for SaaSCloudflare for StartupsCloudflare GatewayCloudflare HistoryCloudflare ImagesCloudflare Media PlatformCloudflare MeetupsCloudflare NetworkCloudflare OneCloudflare One ClientCloudflare One User Risk ScoreCloudflare One WeekCloudflare OSCloudflare PagesCloudflare PolishCloudflare QueuesCloudflare RealtimeCloudflare StreamCloudflare TunnelCloudflare TVCloudflare WorkersCloudflare Workers (PT)Cloudflare Workers KVCloudflare Workers KV (ES)Cloudflare Zero TrustCloudforce OneCloudyCode OrangeCoinbaseColombiaCommunityComplianceCompressionConfig RulesConfiguration ManagementCongestion ControlConnectivityConnectivity CloudConsumer ServicesContainersContent Independence DayContent ScanningContextCoreCOVID-19Crawler HintsCrowdStrikeCrypto WeekCryptographyCSAM ReportingCustomer SuccessCustomer ZeroCustomersCVECVE-2023-50387Cyber ReadinessCybersecurityD1DashboardDataData CatalogData CenterData LocalizationData Localization SuiteData LossData Loss PreventionData PlatformData Privacy DayData ProtectionData SovereigntyData Transfer BucketDatabaseDDoSDDoS AlertsDDoS ReportsDebuggingDeep DiveDescalerDesignDeskopeDeveloper DocumentationDeveloper PlatformDeveloper SpotlightDeveloper WeekDevelopersDevelopers StorageDevice SecurityDevOpsDEXDigital Experience MonitoringDigital ForensicsDisruptDistributedDistributed SystemsDistributed WebDiversityDLPDMARCDNSDNS FilteringDNS FloodDNS SecurityDNSSECDogfoodingDoHDomain RankingsDomain Scoped RolesdosdDrupalDue ProcessDurable ExecutionDurable ObjectsEarly HintsEarth DayeBPFEC2eCommerceEdgeEdge ComputingEdge DatabaseEdge RulesEducationEgressElasticElection SecurityElectionsElliptic CurvesEmailEmail RoutingEmail SecurityEmail WorkersEmDashEmissionsEmployee Resource GroupsEncrypted SNIEncryptionEngineeringEnterpriseEntropyEPYCEthereumEuropeEuropean UnionEventsExploitFacebookFancy BearFast FontsFCCFeature FlagsFedRAMPFedRAMP HighFedRAMP ModerateFirefoxFirewallFirmwareFloridaFootballFormal MethodsForresterFortranFoundation DNSFounders' LetterFranceFraudFreeFreedom of SpeechFront EndFull StackFull Stack WeekFunGA WeekGartnerGatebotGDPRGen XGeneral AvailabilityGenerative AIGeo Key ManagerGermanyGitHubGoGoogleGoogle AnalyticsGoogle CloudGoogle WorkspaceGovernment InnovationGrace HopperGrafanaGraphQLGreenGrinchGrowthgRPCGuest PostHackathonHalloweenHardwareHashiCorpHertzbleedHeuristicsHistoryHolidaysHolocaustHong KongHosting ConHostnamesHTTP2HTTP3HTTPSHuman RightsHurricaneHybrid CloudHyperdriveI'm Under Attack ModeIBMICANNiCloud Private RelayIdentityIETFIETF StandardsIL4Image OptimizationImage RecognitionImage ResizingImage StorageImpactImpact WeekIncident ReportIncident ResponseIndiaIndicators of CompromiseIndonesianInferenceInfrastructureInfrastructure as CodeInsightsIntelInterconnectionInternal DNSInternet PerformanceInternet QualityInternet RegulationInternet ShutdownInternet SummitInternet TrafficInternet TrendsInternship ExperienceIntrusion DetectionInvestorsIoCsiOSIoTIPFSIPsecIPv4IPv6IRAPIsraelItalyIWDJAMstackJapanJavaScriptJengoJengo PolicyJoomlaJudeoflareKafkaKernelKey ValueKeyless SSLKeyTrapKillnetKoreaKubernetesLangChainLatencyLatin AmericaLatinflareLavaRandLazarus groupLeaked Credential ChecksLegalLegal Patents SableLGBTQIA+Life at CloudflareLinuxLisbonLive StreamingLlamaLLMLoad BalancingLocalizationLog PushLog4JLog4ShellLoggingLogsLUAMachine LearningMagecartMagic FirewallMagic Network MonitoringMagic TransitMagic WANMagic WAN ConnectorMalicious JavaScriptMalwareManaged ComponentsManaged RulesMarch of CloudflareMASQUEMCPMeerkatMeetUpMerisMessage ProtocolMexicoMicro-frontendsMicrosoftMicrosoft 365Microsoft AzureMiddle EastMigration HubMilestonesMiniflareMirageMiraiMitelMitigationMixed Content ErrorsMLopsMobileMobile SDKModel Context ProtocolMoldovaMonitoringMulti-CloudMulti-UserMySQLNaaSNet NeutralityNetworkNetwork InterconnectNetwork Performance UpdateNetwork ProtectionNetwork ServicesNetworkingNew YearNGINXNinjasNISTNode.jsNorth AmericaNotebooksNotificationsNSEC3OAuthObservabilityOceaniaOCSPOfficesOktaOlympicsOnboardingOpen APIOpen SourceOpenAIOpenBMCOpenDNSOpenSSLOpenTelemetry OptimizationOrigin RulesOutageOxyPacific NorthwestPage RulesPage ShieldParallelsPartnersPartnershipPassword-reusePasswordsPasswords (PT)PatentsPay Per CrawlPAYGOPaymentsPCI CertifiedPeeringPerformancePerformance OptimizationPhishingphpPhythonPingoraPipelinesPlanetScalePlansPlatform EngineeringPlatform WeekPleskPolicy & LegalPoliticsPortugalPost MortemPost-QuantumPostgresPrecursorPrepared StatementsPrismaPrivacyPrivacy PassPrivacy WeekPrivate IPPrivate NetworkProduct DesignProduct NewsProgrammingProgramming (PT)Project Fair ShotProject GalileoProject Honey PotProject PangeaProject SafekeepingProject TurpentinePrometheusProtocolsProudflareProxyingPublic SectorPythonPython WorkersQuantizationQueuesQUICQUICHEQuicksilverR2R2 Super SlurperRadarRadar AlertsRadar APIRadar MapsRailgunRandomnessRansom AttacksRapid ResetRaspberry PiRate LimitingRC4RDDoSReactReading ListReal-timeRecruitingRegional ServicesRegistrarReliabilityRemote Browser IsolationRemote Desktop Protocol Remote WorkReplicationResearchResolverRestreamingRetreatReverse EngineeringREvilRisk ManagementRoad to Zero TrustRocket LoaderRocksDBRoutingRouting SecurityRPCRPKIRRDNSRSARussiaRustRust WorkersSaaSSAAS SecuritySableSaltSamplingSandboxSASESave The WebSDKSearch EngineSecrets StoreSecure Web GatewaySecuritySecurity AnalyticsSecurity CenterSecurity PostureSecurity Posture ManagementSecurity Service EdgeSecurity Weeksecurity.txtSEOServer PushServerlessServerless (PT)Serverless AIServerless WeekServersSIEMSigned Exchanges (SXG)SIMSingaporeSingle Sign On (SSO)Smart PlacementSmart ShieldSnippetsSOC as a ServiceSouth AfricaSouth AmericaSpainspdySpectrumSpeedSpeed & ReliabilitySpeed BrainSpeed WeekSpoofingSportsSQLSRESSESSHSSLStandardsStartup Enterprise PlanStatisticsStopTheHackerStorageSumo LogicSuper BowlSupercloudSupply Chain AttacksSupportSustainabilitySWAGSWGSwiftSwitzerlandSXSWSYNSYN FloodSyriaTCPTeamTeams DashboardTech TalksTechCrunchTechnical WritingTerraformTestimonialsTestingTexasThanksgivingThe Serverlist NewsletterThreat DataThreat FeedsThreat IntelligenceThreat OperationsThreat ReportThreatsTiered CacheTikTokTLSTLS 1.3ToolsTorTracingTrafficTransform RulesTransparencyTrendsTrust & SafetyTTFBTTLTURNTURN ServerTurnstileTypeScriptUDPUkraineUnited KingdomUniversal SSLURL ScannerUSAUser ResearchVDIVectorizeVetflareVideoVisibilityViteVoIPVPCVPNVulnerabilitiesWAFWAF Attack ScoreWAF RulesWaiting RoomWARPWARP ConnectorWASMWeb Application FirewallWeb Asset DiscoveryWeb3WebAssemblyWebinarsWebMCPWebPWebRTCWebSocketsWildebeestWomenflareWordPressWorkers AIWorkers LaunchpadWorkers LogsWorkers ObservabilityWorkers SitesWorkers UnboundWorkers VPCWorkflowsWorld IPv6 DayWranglerx402Year in ReviewZ3ZarazZero Day ThreatsZero TrustZero Trust WeekZone VersioningArtificial IntelligenceWorkersClient-Side SecurityArchitectureMulti-tenant SecuityMulti-tenant SecuritycfBEACONCrawlersSecurityWorkers AIglobalThis.process??={},globalThis.process.env??={},document.querySelectorAll(`[data-breadcrumb-toggle]`).forEach(e=>{let t=e.getAttribute(`aria-controls`),n=t?document.getElementById(t):null,r=e.querySelector(`[data-breadcrumb-toggle-icon]`);n&&e.addEventListener(`click`,()=>{let t=e.getAttribute(`aria-expanded`)!==`true`;e.setAttribute(`aria-expanded`,String(t)),n.style.gridTemplateRows=t?`1fr`:`0fr`,n.inert=!t,r?.classList.toggle(`rotate-180`,t)})});var e=document.querySelectorAll(`[data-tags-dropdown]`);e.length&&(document.addEventListener(`click`,t=>{let n=t.target;n instanceof Node&&e.forEach(e=>{e.open&&!e.contains(n)&&(e.open=!1)})}),document.addEventListener(`keydown`,t=>{t.key===`Escape`&&e.forEach(e=>{e.open&&=!1})})),e.forEach(e=>{let t=e.querySelector(`[data-tag-search-input]`),n=e.querySelector(`[data-tag-search-clear]`),r=e.querySelector(`[data-selected-tags-heading]`),i=e.querySelector(`[data-selected-tags-list]`),a=e.querySelector(`[data-all-tags-heading]`),o=e.querySelector(`[data-matching-tags-heading]`),s=e.querySelector(`[data-no-matching-tags]`),c=e.querySelectorAll(`[data-tag-item]`);if(!t)return;let l=()=>{let e=t.value.trim().toLowerCase(),l=e.length>0;r?.classList.toggle(`hidden`,l),i?.classList.toggle(`hidden`,l),a?.classList.toggle(`hidden`,l),o?.classList.toggle(`hidden`,!l),n?.classList.toggle(`hidden`,!l);let u=0;c.forEach(t=>{let n=t.getAttribute(`data-tag-label`)??``,r=!l||n.includes(e);t.classList.toggle(`hidden`,!r),r&&(u+=1)}),s?.classList.toggle(`hidden`,!(l&&u===0))};t.addEventListener(`input`,l),n?.addEventListener(`click`,()=>{t.value=``,l(),t.focus()}),e.addEventListener(`toggle`,()=>{e.open?t.focus():(t.value=``,l())})});October 26, 2026Cross-request KV cache exposure in the GLM-5.3 Workers AI model, and our remediation with SGLangglobalThis.process??={},globalThis.process.env??={};function e(e){let t=e.closest(`[data-avatar]`);t&&!t.classList.contains(`avatar--fallback`)&&t.classList.add(`avatar--fallback`)}document.addEventListener(`error`,t=>{let n=t.target;n instanceof HTMLImageElement&&e(n)},!0),document.querySelectorAll(`[data-avatar] img`).forEach(t=>{t.complete&&t.naturalWidth===0&&e(t)});Kevin Flansburg and Michelle Chen

On September 8, 2026, we were alerted by a security researcher, Gadi Evron from Knostic, to a tenant isolation issue affecting the GLM-5.3 Workers AI model (@cf/zai-org/glm-5.3) starting on August 27, 2026. We have remediated the issue, and we restored the model on September 9. We have confirmed that no other model hosted on Workers AI was affected.

Between August 27 and September 9, a small number of customers using the GLM 5.3 Workers AI model received responses that contained data from other customers' requests made to the same model shortly before theirs. In total, 155 responses were affected, all to prompts longer than 681,280 tokens.

After excluding our own testing and the researcher's, the requests we identified are consistent in timing and volume with ordinary long-context use, not with someone repeatedly exploiting the bug. We found no evidence of deliberate exploitation.

Today we are publishing this report alongside a post from SGLang, the open-source inference engine that we use, as a coordinated disclosure. This post describes the bug that caused this issue, our response timeline, and the subsequent hardening we have conducted on our production SGLang deployments. We also detail our continued efforts with the upstream maintainers of SGLang to address this and similar bugs.

GLM is a text generation model from Z.ai that is built for agentic coding workflows; it is one of the many models available through Workers AI. Gadi Evron submitted a report on September 8 through our HackerOne program stating that very long prompts sent to @cf/zai-org/glm-5.3 on Workers AI sometimes returned text that belonged to other users' sessions. Cloudflare reproduced the issue the next morning and took the model offline within 40 minutes of declaring an incident. We then deployed a corrected configuration and a patched inference engine, and restored service the same day.

This specific report of cross-request KV cache exposure was the result of two overlapping issues. The first was a misconfiguration of the open-source inference engine, SGLang, used by Cloudflare. We deployed GLM 5.3 with a 1,048,576-token context window, but the KV cache pool on our prefill GPUs only had room for 681,280 tokens. We were aware of this mismatch before launch. We expected the engine to return an error for any prompt it could not process, and our long-context tests returned successful responses, so we did not believe this to be an issue.

The second was a bug in how SGLang handled the resulting over-length requests in disaggregated prefill/decode mode. A prompt that did not fit the pool was internally marked as rejected and replaced with a one-token placeholder, but instead of aborting the request and returning a client error, prefill generated the KV cache for the placeholder prompt and transferred it to the decode node. The decode node received a "transfer complete" message and assumed that prefill overwrote the KV cache from previous requests with the full prompt for this request, when in fact it left the majority of the previous state intact. The decode node subsequently generated a response while attending over stale cache pages that still held data from earlier requests. As a result, responses to prompts longer than 681,280 tokens could contain data from other users' GLM 5.3 sessions.

After disabling the model, we took the following actions to correct this vulnerability before restoring public access to it:

To fix our configuration, we made the pool hold the full context. We adjusted our GLM 5.3 configuration to match our GLM 5.2 configuration, which freed enough GPU memory that the prefill KV pool now holds about 2.04 million tokens, roughly twice the 1,048,576-token context length. A prompt that fits the context window now always fits the pool, so the rejection path is never reached for a valid request. This alone prevents the bug from being exercised.

To fix the engine, we also made the rejection path safe. Relying on pool size alone is fragile: any change to quantization, tensor parallelism, CUDA graph sizes, or a future model version changes the pool size in a way that's easy to miss. Furthermore, there may be other situations in which the prefill scheduler can reject a request and trigger the same bug. To prevent this, we also patched the engine so that a request carrying a pending rejection is retired at the disaggregation admission queue, with its original error, before any bootstrap, allocation, or KV transfer happens. We proposed this upstream as #38704, which also had the decode node verify that the number of tokens transferred matches the number it reserved. The fix was already on SGLang main in #36988, merged September 6 for a related failure path but not yet released. The maintainers also merged #38935, which rejects these requests earlier, following our approach.

We validated both changes against the researcher's reproduction script and our own canary-marker tests before restoring the model.

Workers AI runs GLM 5.3 with SGLang in a disaggregated configuration: a pool of prefill GPUs processes the prompt and produces the model's KV cache for it, then hands that cache over remote direct memory access (RDMA), via Mooncake, to a pool of decode GPUs that generate the response. We have written about this architecture before in our posts on high-performance LLMs and smaller, faster, safer models.

The KV cache in GPU memory is a shared pool of fixed-size pages. Each request is assigned pages when it is admitted and releases them when it finishes. Pages are not currently zeroed between requests; the next request that gets a page simply overwrites it. This approach is common among inference engines and is necessary to achieve the best performance, but it means that the inference engine is responsible for tracking ownership of these memory pages. KV cache page ownership and lifetime tracking has to deal with not just shared ownership within a node (KV cache offload and token generation both access the memory with different lifetimes), but also ownership that is technically shared with the remote prefill node (which holds a simultaneous mutable reference to the page).

Furthermore, the size of this pool is not a configuration value. SGLang sizes it at startup from whatever GPU memory remains after loading the model weights. The model's advertised context length is a separate configuration value. Nothing forces the two to agree, and it is our job to check that they do.

On our GLM 5.3 prefill nodes with our configuration, the pool came to 681,280 tokens while the model's context length is 1,048,576 tokens. The selected KV pool size is printed by SGLang in logs during startup and exposed as a metric. We were aware of this size mismatch; however, during pre-launch testing we observed successful HTTP status codes and a streaming body with no error frames during benchmarking. We assumed that the engine was capable of gracefully handling the difference between the KV cache pool and requested context window via streaming or some other mechanism.

This was one critical gap in our testing: we only validated HTTP response codes and engine performance at long contexts, without validating model output and coherence. We now check KV pool size against context length directly, from the running engine, before any disaggregated deployment change ships, rather than inferring it from response codes.

In v0.5.21, the SGLang team has now addressed this bug in how it was handling prompts longer than the KV pool size. Here’s what was happening before.

When a prompt arrived that was longer than the KV pool could hold, SGLang's scheduler rejected it. The rejection path (Req.set_finish_with_abort) recorded the error to be returned to the client and swapped the prompt for a one-token placeholder so that the request could drain through the normal batch machinery without allocating real memory. On a single-node deployment this worked: the placeholder ran, the batch finished, and the client received an error.

In disaggregated mode such as we operate, the admission queues on both prefill and decode checked whether a request was finished, not whether it was rejected. A rejected request reported itself as live. So:

Every request over the threshold behaved this way. This bug had been reported to SGLang by another user as issue #30233 on July 6, 2026, which Cloudflare noticed while investigating this incident. We had been flagging these types of issues with SGLang since v0.5.10 and this security incident sped up work that Cloudflare had already started in collaboration with the SGLang team. The patch for this issue was released in SGLang v0.5.20, with follow-ups in v0.5.21 and v0.5.22, and is available for all other operators dependent on SGLang to use. We highly recommend all operators update SGLang dependencies to v0.5.22 or later. For more details on specific PRs, read on below.

GLM 5.3 was the only model affected by this bug. Every other disaggregated deployment on Workers AI has KV pools larger than its context length on both prefill and decode, so no request could reach the rejection path. We have applied the engine fix and the hardening described below to every model we serve with SGLang, and our deployment checks require them for every new deployment.

GLM 5.3 launched on Workers AI with a prefill KV pool smaller than its context window. The exposure was present from launch.

Cloudflare begins verifying the HackerOne report.

Security incident declared. Product Security reproduced the leak using two independent accounts within 25 minutes.

After confirming the scope of the issue, GLM 5.3 was set to private. Requests return HTTP 400. Status page updated.

Root cause identified as the prefill pool being smaller than the context length. Canary prefill node with a larger pool confirmed not susceptible.

All prefill nodes rolled to the corrected configuration.

Full deployment rebuilt with the corrected configuration plus a Cloudflare-authored engine patch that correctly returns errors for requests rejected by the prefill scheduler. Validated against the researcher's reproduction script.

Meeting with the SGLang maintainers (RadixArk CTO and core engineers) to agree on upstream fixes.

Additional hardening rolled to all production SGLang deployments (details below).

Upstream SGLang merges the admission fix, per-transfer checksums, abort-ACK preservation, and turns deferred KV release on by default.

Coordinated publication with the researcher and RadixArk.

This bug belongs to a class of KV cache memory-safety bugs that Cloudflare has been working to address for several months. In each case, a page is freed, reused, or read while something else still has a claim on it. We see two common causes.

The first is page lifetime within a single node. Several tasks on a decode node can hold the same page at once: token generation, offload to host memory, the KV transfer receiver, and the abort and error paths. If one of them frees the page while another is still using it, a new request can be given that page while it is still being read or written. Our earlier fixes for decode offload (#24226, #30899) and double release on grammar errors (#30937) were of this kind.

The second is a race across nodes. When a request is aborted while prefill is still writing its KV cache to decode over RDMA, the writes already sent cannot be recalled. If decode frees those pages right away, those pages can be given to another request, and the late writes land in that request's KV cache. Cloudflare has contributed to the effort to fix this race through proposed fixes (#31357, #38961) and a reproduction script (#32564). In both cases the result is corrupted output, or one user's data in another user's response, with no error raised. The bug in this incident was different: a rejected request went through the handoff every time, rather than by a timing accident. But it had the same result: decode reading pages this request never wrote. None of these covered the failure in this incident in which prefill rejected the request, and decode never learned of it.

All of these changes were released to our disaggregated production deployments.

We met with the SGLang maintainers at RadixArk on September 10, the day after the incident. We agreed that RadixArk would investigate the race conditions we had reported, upstream the integrity-checking idea, and build reproduction tests for this class of bug.

The following have landed on SGLang main to address this incident and related KV cache race conditions, and all but one are included in v0.5.22. Operators running disaggregated SGLang should update to v0.5.22 or backport these patches as needed.

Retires aborted prefill requests before their result reaches decode. This stops the exposure in this incident.

Rejects these requests at admission, before any bootstrap, allocation, or KV transfer. Follows the approach in Cloudflare's draft patch, #38704.

sgl-router cancels both halves of a request on client disconnect or prefill failure.

Enables deferred KV release only on backends that support it, then turns it on by default.

Fixes cases where the drain confirmation was lost, so releases happen on confirmation instead of waiting out the timeout.

Holds pages on every transfer failure, not only decode-initiated aborts.

Fixes a regression in the abort notification path.

A failed Mooncake send no longer reports its writes as drained.

Tags abort messages per request so a reused ID cannot consume a stale confirmation. Adds MORI support.

Shares the prefill-to-decode failure notification across Mooncake, NIXL, and MORI.

Optional cap on Mooncake transfer batch size, so one timed-out call cannot leave an unbounded number of writes in flight.

Decode waits for an in-progress offload to host memory before retracting a request and freeing its pages. Authored by Cloudflare.

Keeps tensor-parallel ranks in agreement when a host-memory cache restore fails.

Adds --disaggregation-enable-kv-checksum: decode verifies a checksum of the transferred KV before generating. Cleanup in #39729, merged and awaiting release.

Fixes for SGLang's KV canary, which detects and logs potential corruption.

Metrics for deferred release: count, duration, and whether each hold ended on drain confirmation or timeout.

These follow-ups are still works in progress:

If you run SGLang in disaggregated prefill/decode mode, we recommend the following:

Configuration checks and lifecycle fixes reduce the number of ways a page can be misused. They do not make misuse impossible, and this incident is a reminder that the next bug will have a shape we have not seen. The durable answer is for the engine to detect, at read time, that a request is about to attend over a page it does not own, and fail that one request rather than return someone else's data.

We built a prototype of this over the summer and described it in August. Every physical KV page carries a tag that changes when the page is reallocated, each request records the tags it expects, and the mapping is checked before decode reads the cache. In our tests it cost under 1% in throughput and tail latency. We tested it on GLM 5.2 in mid-August, but disabled it shortly afterwards due to reliability issues.

The prototype was also tied to specific attention backends and model architectures, so it could not be a general fix. We are working with the SGLang team to build a production version into the engine that works across every model, rather than maintaining Cloudflare-specific patches. The per-transfer checksum in #39500 is a first step: it validates the handoff from prefill to decode. Page-level tags go further, because they check every read, including reads long after the transfer.

RDMA copies data directly from one node’s memory to another’s. It’s vital for the two machines to agree on where the data goes, how large it is, and when it’s finished; any mismatch can cause the receiver to read the wrong data. This bug is an example of a consistency failure in a distributed system, in which the two machines had inconsistent views of the state of that system.

Elsewhere in Cloudflare, we have put effort into proving the safety of distributed systems using formal verification methods. Topaz enables conflict-free IP selection for our authoritative DNS servers. Models of Meerkat’s QuePaxa implementation have demonstrated consistency bugs that were subsequently fixed.

We are now directing our experience in formal methods to KV cache transfer engines. This will start with modeling and proving the safety of an RDMA-based KV cache transfer protocol. The goal is to model our production SGLang’s distributed KV cache system using Mooncake, then track and fix any divergence from the safety properties we want to guarantee. The aim is to prove — as far as possible — that a bug like this cannot occur again. Realistically, we expect gaps in what the provers can tell us, but proving the rest of the system allows us to more closely review and monitor those gaps.

We are publishing this report as part of a coordinated disclosure. We want to thank the researcher, Gadi Evron, who reported this through our HackerOne program with a clear, reproducible script and gave us time to fix it and to coordinate with the SGLang maintainers before publishing. We also want to thank the SGLang team at RadixArk, who treated this as their problem as well as ours and landed the upstream fixes with urgency.

Read more at the post from the SGLang team.

If you find a security issue in Workers AI, please report it at hackerone.com/cloudflare.

globalThis.process??={},globalThis.process.env??={};var e=document.querySelector(`[data-back-to-top]`),t=document.querySelector(`[data-back-to-top-progress]`);if(e&&t){let n=e,r=t,i=r.getTotalLength();r.style.strokeDasharray=`${i}`;function a(){let e=window.scrollY;e>400?n.setAttribute(`data-visible`,``):n.removeAttribute(`data-visible`);let t=document.documentElement.scrollHeight-window.innerHeight,a=t>0?Math.min(1,Math.max(0,e/t)):0;r.style.strokeDashoffset=`${i*(1-a)}`}window.addEventListener(`scroll`,a,{passive:!0}),window.addEventListener(`resize`,a,{passive:!0}),a(),n.addEventListener(`click`,()=>{let e=window.matchMedia(`(prefers-reduced-motion: reduce)`).matches;window.scrollTo({top:0,behavior:e?`auto`:`smooth`})})}On this page

Related tagsSecurityWorkers AIFollow on Social Media

CloudflareMichelle ChenSubscribe to receive notifications of new postsEmail address

Thanks for subscribing! Check your inbox to confirm# Cross-request KV cache exposure in the GLM-5.3 Workers AI model, and our remediation with SGLang

Source: https://blog.cloudflare.com/kv-cache-exposure-remediation/

Kevin Flansburg and Michelle Chen, October 26, 2026

On September 8, 2026, we were alerted by a security researcher, Gadi Evron from Knostic, to a tenant isolation issue affecting the GLM-5.3 Workers AI model (@cf/zai-org/glm-5.3) starting on August 27, 2026. We have remediated the issue, and we restored the model on September 9. We have confirmed that no other model hosted on Workers AI was affected.

Between August 27 and September 9, a small number of customers using the GLM 5.3 Workers AI model received responses that contained data from other customers' requests made to the same model shortly before theirs. In total, 155 responses were affected, all to prompts longer than 681,280 tokens.

After excluding our own testing and the researcher's, the requests we identified are consistent in timing and volume with ordinary long-context use, not with someone repeatedly exploiting the bug. We found no evidence of deliberate exploitation.

Today we are publishing this report alongside a post from SGLang, the open-source inference engine that we use, as a coordinated disclosure. This post describes the bug that caused this issue, our response timeline, and the subsequent hardening we have conducted on our production SGLang deployments. We also detail our continued efforts with the upstream maintainers of SGLang to address this and similar bugs.

GLM is a text generation model from Z.ai that is built for agentic coding workflows; it is one of the many models available through Workers AI. Gadi Evron submitted a report on September 8 through our HackerOne program stating that very long prompts sent to @cf/zai-org/glm-5.3 on Workers AI sometimes returned text that belonged to other users' sessions. Cloudflare reproduced the issue the next morning and took the model offline within 40 minutes of declaring an incident. We then deployed a corrected configuration and a patched inference engine, and restored service the same day.

This specific report of cross-request KV cache exposure was the result of two overlapping issues. The first was a misconfiguration of the open-source inference engine, SGLang, used by Cloudflare. We deployed GLM 5.3 with a 1,048,576-token context window, but the KV cache pool on our prefill GPUs only had room for 681,280 tokens. We were aware of this mismatch before launch. We expected the engine to return an error for any prompt it could not process, and our long-context tests returned successful responses, so we did not believe this to be an issue.

The second was a bug in how SGLang handled the resulting over-length requests in disaggregated prefill/decode mode. A prompt that did not fit the pool was internally marked as rejected and replaced with a one-token placeholder, but instead of aborting the request and returning a client error, prefill generated the KV cache for the placeholder prompt and transferred it to the decode node. The decode node received a "transfer complete" message and assumed that prefill overwrote the KV cache from previous requests with the full prompt for this request, when in fact it left the majority of the previous state intact. The decode node subsequently generated a response while attending over stale cache pages that still held data from earlier requests. As a result, responses to prompts longer than 681,280 tokens could contain data from other users' GLM 5.3 sessions.

After disabling the model, we took the following actions to correct this vulnerability before restoring public access to it:

To fix our configuration, we made the pool hold the full context. We adjusted our GLM 5.3 configuration to match our GLM 5.2 configuration, which freed enough GPU memory that the prefill KV pool now holds about 2.04 million tokens, roughly twice the 1,048,576-token context length. A prompt that fits the context window now always fits the pool, so the rejection path is never reached for a valid request. This alone prevents the bug from being exercised.

To fix the engine, we also made the rejection path safe. Relying on pool size alone is fragile: any change to quantization, tensor parallelism, CUDA graph sizes, or a future model version changes the pool size in a way that's easy to miss. Furthermore, there may be other situations in which the prefill scheduler can reject a request and trigger the same bug. To prevent this, we also patched the engine so that a request carrying a pending rejection is retired at the disaggregation admission queue, with its original error, before any bootstrap, allocation, or KV transfer happens. We proposed this upstream as #38704, which also had the decode node verify that the number of tokens transferred matches the number it reserved. The fix was already on SGLang main in #36988, merged September 6 for a related failure path but not yet released. The maintainers also merged #38935, which rejects these requests earlier, following our approach.

We validated both changes against the researcher's reproduction script and our own canary-marker tests before restoring the model.

Workers AI runs GLM 5.3 with SGLang in a disaggregated configuration: a pool of prefill GPUs processes the prompt and produces the model's KV cache for it, then hands that cache over remote direct memory access (RDMA), via Mooncake, to a pool of decode GPUs that generate the response. We have written about this architecture before in our posts on high-performance LLMs and smaller, faster, safer models.

The KV cache in GPU memory is a shared pool of fixed-size pages. Each request is assigned pages when it is admitted and releases them when it finishes. Pages are not currently zeroed between requests; the next request that gets a page simply overwrites it. This approach is common among inference engines and is necessary to achieve the best performance, but it means that the inference engine is responsible for tracking ownership of these memory pages. KV cache page ownership and lifetime tracking has to deal with not just shared ownership within a node (KV cache offload and token generation both access the memory with different lifetimes), but also ownership that is technically shared with the remote prefill node (which holds a simultaneous mutable reference to the page).

Furthermore, the size of this pool is not a configuration value. SGLang sizes it at startup from whatever GPU memory remains after loading the model weights. The model's advertised context length is a separate configuration value. Nothing forces the two to agree, and it is our job to check that they do.

On our GLM 5.3 prefill nodes with our configuration, the pool came to 681,280 tokens while the model's context length is 1,048,576 tokens. The selected KV pool size is printed by SGLang in logs during startup and exposed as a metric. We were aware of this size mismatch; however, during pre-launch testing we observed successful HTTP status codes and a streaming body with no error frames during benchmarking. We assumed that the engine was capable of gracefully handling the difference between the KV cache pool and requested context window via streaming or some other mechanism.

This was one critical gap in our testing: we only validated HTTP response codes and engine performance at long contexts, without validating model output and coherence. We now check KV pool size against context length directly, from the running engine, before any disaggregated deployment change ships, rather than inferring it from response codes.

In v0.5.21, the SGLang team has now addressed this bug in how it was handling prompts longer than the KV pool size. Here’s what was happening before.

When a prompt arrived that was longer than the KV pool could hold, SGLang's scheduler rejected it. The rejection path (Req.set_finish_with_abort) recorded the error to be returned to the client and swapped the prompt for a one-token placeholder so that the request could drain through the normal batch machinery without allocating real memory. On a single-node deployment this worked: the placeholder ran, the batch finished, and the client received an error.

In disaggregated mode such as we operate, the admission queues on both prefill and decode checked whether a request was finished, not whether it was rejected. A rejected request reported itself as live. So:

Every request over the threshold behaved this way. This bug had been reported to SGLang by another user as issue #30233 on July 6, 2026, which Cloudflare noticed while investigating this incident. We had been flagging these types of issues with SGLang since v0.5.10 and this security incident sped up work that Cloudflare had already started in collaboration with the SGLang team. The patch for this issue was released in SGLang v0.5.20, with follow-ups in v0.5.21 and v0.5.22, and is available for all other operators dependent on SGLang to use. We highly recommend all operators update SGLang dependencies to v0.5.22 or later. For more details on specific PRs, read on below.

GLM 5.3 was the only model affected by this bug. Every other disaggregated deployment on Workers AI has KV pools larger than its context length on both prefill and decode, so no request could reach the rejection path. We have applied the engine fix and the hardening described below to every model we serve with SGLang, and our deployment checks require them for every new deployment.

GLM 5.3 launched on Workers AI with a prefill KV pool smaller than its context window. The exposure was present from launch.

Cloudflare begins verifying the HackerOne report.

Security incident declared. Product Security reproduced the leak using two independent accounts within 25 minutes.

After confirming the scope of the issue, GLM 5.3 was set to private. Requests return HTTP 400. Status page updated.

Root cause identified as the prefill pool being smaller than the context length. Canary prefill node with a larger pool confirmed not susceptible.

All prefill nodes rolled to the corrected configuration.

Full deployment rebuilt with the corrected configuration plus a Cloudflare-authored engine patch that correctly returns errors for requests rejected by the prefill scheduler. Validated against the researcher's reproduction script.

Meeting with the SGLang maintainers (RadixArk CTO and core engineers) to agree on upstream fixes.

Additional hardening rolled to all production SGLang deployments (details below).

Upstream SGLang merges the admission fix, per-transfer checksums, abort-ACK preservation, and turns deferred KV release on by default.

Coordinated publication with the researcher and RadixArk.

This bug belongs to a class of KV cache memory-safety bugs that Cloudflare has been working to address for several months. In each case, a page is freed, reused, or read while something else still has a claim on it. We see two common causes.

The first is page lifetime within a single node. Several tasks on a decode node can hold the same page at once: token generation, offload to host memory, the KV transfer receiver, and the abort and error paths. If one of them frees the page while another is still using it, a new request can be given that page while it is still being read or written. Our earlier fixes for decode offload (#24226, #30899) and double release on grammar errors (#30937) were of this kind.

The second is a race across nodes. When a request is aborted while prefill is still writing its KV cache to decode over RDMA, the writes already sent cannot be recalled. If decode frees those pages right away, those pages can be given to another request, and the late writes land in that request's KV cache. Cloudflare has contributed to the effort to fix this race through proposed fixes (#31357, #38961) and a reproduction script (#32564). In both cases the result is corrupted output, or one user's data in another user's response, with no error raised. The bug in this incident was different: a rejected request went through the handoff every time, rather than by a timing accident. But it had the same result: decode reading pages this request never wrote. None of these covered the failure in this incident in which prefill rejected the request, and decode never learned of it.

All of these changes were released to our disaggregated production deployments.

We met with the SGLang maintainers at RadixArk on September 10, the day after the incident. We agreed that RadixArk would investigate the race conditions we had reported, upstream the integrity-checking idea, and build reproduction tests for this class of bug.

The following have landed on SGLang main to address this incident and related KV cache race conditions, and all but one are included in v0.5.22. Operators running disaggregated SGLang should update to v0.5.22 or backport these patches as needed.

Retires aborted prefill requests before their result reaches decode. This stops the exposure in this incident.

Rejects these requests at admission, before any bootstrap, allocation, or KV transfer. Follows the approach in Cloudflare's draft patch, #38704.

sgl-router cancels both halves of a request on client disconnect or prefill failure.

Enables deferred KV release only on backends that support it, then turns it on by default.

Fixes cases where the drain confirmation was lost, so releases happen on confirmation instead of waiting out the timeout.

Holds pages on every transfer failure, not only decode-initiated aborts.

Fixes a regression in the abort notification path.

A failed Mooncake send no longer reports its writes as drained.

Tags abort messages per request so a reused ID cannot consume a stale confirmation. Adds MORI support.

Shares the prefill-to-decode failure notification across Mooncake, NIXL, and MORI.

Optional cap on Mooncake transfer batch size, so one timed-out call cannot leave an unbounded number of writes in flight.

Decode waits for an in-progress offload to host memory before retracting a request and freeing its pages. Authored by Cloudflare.

Keeps tensor-parallel ranks in agreement when a host-memory cache restore fails.

Adds --disaggregation-enable-kv-checksum: decode verifies a checksum of the transferred KV before generating. Cleanup in #39729, merged and awaiting release.

Fixes for SGLang's KV canary, which detects and logs potential corruption.

Metrics for deferred release: count, duration, and whether each hold ended on drain confirmation or timeout.

These follow-ups are still works in progress:

If you run SGLang in disaggregated prefill/decode mode, we recommend the following:

Configuration checks and lifecycle fixes reduce the number of ways a page can be misused. They do not make misuse impossible, and this incident is a reminder that the next bug will have a shape we have not seen. The durable answer is for the engine to detect, at read time, that a request is about to attend over a page it does not own, and fail that one request rather than return someone else's data.

We built a prototype of this over the summer and described it in August. Every physical KV page carries a tag that changes when the page is reallocated, each request records the tags it expects, and the mapping is checked before decode reads the cache. In our tests it cost under 1% in throughput and tail latency. We tested it on GLM 5.2 in mid-August, but disabled it shortly afterwards due to reliability issues.

The prototype was also tied to specific attention backends and model architectures, so it could not be a general fix. We are working with the SGLang team to build a production version into the engine that works across every model, rather than maintaining Cloudflare-specific patches. The per-transfer checksum in #39500 is a first step: it validates the handoff from prefill to decode. Page-level tags go further, because they check every read, including reads long after the transfer.

RDMA copies data directly from one node’s memory to another’s. It’s vital for the two machines to agree on where the data goes, how large it is, and when it’s finished; any mismatch can cause the receiver to read the wrong data. This bug is an example of a consistency failure in a distributed system, in which the two machines had inconsistent views of the state of that system.

Elsewhere in Cloudflare, we have put effort into proving the safety of distributed systems using formal verification methods. Topaz enables conflict-free IP selection for our authoritative DNS servers. Models of Meerkat’s QuePaxa implementation have demonstrated consistency bugs that were subsequently fixed.

We are now directing our experience in formal methods to KV cache transfer engines. This will start with modeling and proving the safety of an RDMA-based KV cache transfer protocol. The goal is to model our production SGLang’s distributed KV cache system using Mooncake, then track and fix any divergence from the safety properties we want to guarantee. The aim is to prove — as far as possible — that a bug like this cannot occur again. Realistically, we expect gaps in what the provers can tell us, but proving the rest of the system allows us to more closely review and monitor those gaps.

We are publishing this report as part of a coordinated disclosure. We want to thank the researcher, Gadi Evron, who reported this through our HackerOne program with a clear, reproducible script and gave us time to fix it and to coordinate with the SGLang maintainers before publishing. We also want to thank the SGLang team at RadixArk, who treated this as their problem as well as ours and landed the upstream fixes with urgency.

Read more at the post from the SGLang team.

If you find a security issue in Workers AI, please report it at hackerone.com/cloudflare.

globalThis.process??={},globalThis.process.env??={};var e=document.querySelector(`[data-back-to-top]`),t=document.querySelector(`[data-back-to-top-progress]`);if(e&&t){let n=e,r=t,i=r.getTotalLength();r.style.strokeDasharray=`${i}`;function a(){let e=window.scrollY;e>400?n.setAttribute(`data-visible`,``):n.removeAttribute(`data-visible`);let t=document.documentElement.scrollHeight-window.innerHeight,a=t>0?Math.min(1,Math.max(0,e/t)):0;r.style.strokeDashoffset=`${i*(1-a)}`}window.addEventListener(`scroll`,a,{passive:!0}),window.addEventListener(`resize`,a,{passive:!0}),a(),n.addEventListener(`click`,()=>{let e=window.matchMedia(`(prefers-reduced-motion: reduce)`).matches;window.scrollTo({top:0,behavior:e?`auto`:`smooth`})})}On this page

Related tagsSecurityWorkers AIFollow on Social Media

CloudflareMichelle ChenSubscribe to receive notifications of new postsEmail address

Thanks for subscribing! Check your inbox to confirm.