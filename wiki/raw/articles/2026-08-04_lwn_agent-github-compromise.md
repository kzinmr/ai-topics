---
title: "An LLM agent attempts to compromise a project on GitHub [LWN.net]"
date: "2026-08-04"
source_url: "https://lwn.net/Articles/1087162/"
source: "lwn"
type: raw_article
ingested: "2026-08-05"
---

# An LLM agent attempts to compromise a project on GitHub [LWN.net]

The AI Security Institute has released a
detailed report on an security incident of its own making.  The
Institute set some LLM agents loose on the Internet with a security
challenge; soon they were creating malware-laden pull requests and
sock-puppet accounts to promote them.

	The agent opened a malicious pull request (PR) to ⟨REPO_A⟩ and
	pursued a number of strategies to get it merged:

 Repeatedly commented on the PR with sockpuppet accounts to manufacture
     consensus and pressure the maintainer into approving with minimal
     review.

 Opened a GitHub Issue in another repository (also owned by ⟨PERSON_A⟩)
     containing a prompt injection for other coding agents. The malicious
     instructions were addressed to issue-triage AI coding agents and
     invisible to humans viewing the website.

 Sent multiple emails to ⟨PERSON_A⟩ and ⟨PERSON_B⟩, with different
     pretexts to get them to run malicious code. Over the course of the
     sample, the agent sent five emails, some containing malware, others
     aimed at persuading a maintainer to accept the pull request.

It would be surprising if this were the only incident of this type; the
only real difference here is that the people involved are documenting what
happened.
    The LWN site is currently under high scraper load, so comment
    display has been suppressed for anonymous users.  If you are a
    human, you may read the comments by clicking the button below:
    

    
         
        	
         
    
    

    **Note**: you can avoid this step in the future by logging
    into your LWN account.
