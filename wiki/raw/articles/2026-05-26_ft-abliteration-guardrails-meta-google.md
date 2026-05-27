# FT: AI Safety Guardrails Stripped from Meta and Google Models in Minutes

**Source:** Financial Times / Resultsense summary  
**Date:** May 26, 2026  
**Authors:** Financial Times journalists + AI safety group Alice

## Summary

The Financial Times and AI safety group Alice demonstrated that freely available tools can strip safety guardrails from open-source models including Meta's Llama 3.3 and Google's Gemma 3, taking minutes and four lines of code. Modified models produced responses on chlorine-gas dispersion, ricin lethality, credit-card-theft code, and child sexual abuse material — outputs the original systems refused.

## Key Facts

- **Heretic**: GitHub-hosted tool used in the FT's test. Creator Philipp Emanuel Weidmann reported it has been used to create 3,500+ "decensored" models with 13 million downloads.
- **Llama 3.3**: FT removed guardrails in under 10 minutes, with 4 lines of code, no specialist hardware. Altered model provided ricin lethality dose information.
- **Gemma 3**: After guardrail removal, responded to chlorine gas dispersion through crowded indoor spaces, credit card theft code generation, and child sexual abuse story writing.
- **Gemma 4**: Weidmann stripped safeguards within 90 minutes of its release.

## Technique

"Abliteration" uses a mathematical operation to neutralize the internal model states that produce refusals. It cannot easily be applied to fully proprietary frontier systems (Claude, ChatGPT) where the underlying model code is not accessible. However, open-source models have historically narrowed the capability gap with proprietary leaders within 6-12 months.

## Industry Responses

- **Google**: Abliteration is "a known technical challenge facing all open models." Pointed to pre-launch safety evaluations.
- **GitHub**: Bans content directly supporting active attacks or malware campaigns but allows source code that could be used to develop malware on educational and net-security-benefit grounds.
- **Meta**: Declined formal comment. Source cited Advanced AI Scaling Framework restricting release of models deemed "catastrophic" risk.
- **Alice CEO Noam Schwartz**: "The genie is out of the bottle. Things that look like sci-fi are no longer sci-fi and we need as a society to prepare accordingly."
