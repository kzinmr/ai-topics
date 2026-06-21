---
title: "Building Reliable Agentic AI Systems"
source: "https://martinfowler.com/articles/reliable-llm-bayer.html"
author: ", Sarang Sanjay Kulkarni,"
date: "2026-06-19"
date_ingested: "2026-06-21"
type: raw_article
tags: ["ai-agents", "agentic-rag", "reliability", "case-study", "rag", "text-to-sql"]
---

# Building Reliable Agentic AI Systems

**Author**: , Sarang Sanjay Kulkarni,  
**Date**: 2026-06-19  
**Source**: [https://martinfowler.com/articles/reliable-llm-bayer.html](https://martinfowler.com/articles/reliable-llm-bayer.html)

A Case Study in building production-ready agentic AI systems

    This paper presents the Preclinical Information Center (PRINCE), a cloud-hosted platform
    developed by Bayer AG with Thoughtworks to address pharmaceutical industry challenges in drug
    development. PRINCE leverages Agentic Retrieval-Augmented Generation
    and Text-to-SQL to integrate decades of safety study reports. We describe PRINCE's evolution
    from keyword-based search to an intelligent research assistant capable of answering complex
    questions and drafting regulatory documents. We reflect on key engineering decisions through
    the lens of context engineering&#x2014;how information was shaped and routed between specialized
    agents&#x2014;and harness engineering&#x2014;how orchestration, recovery, and observability were built
    around the models to maintain control and reliability. The system prioritizes trust through
    transparency, explainability, and human-in-the-loop integration. PRINCE demonstrates AI's
    transformative potential in pharmaceuticals, significantly improving data accessibility and
    research efficiency while ensuring governance and compliance.
  

16 June 2026

Sarang Sanjay Kulkarni

Sarang Kulkarni is a Principal Consultant at Thoughtworks, working at the intersection of
        software engineering, data platforms, and applied AI. He focuses on building
        production-grade GenAI systems, particularly Retrieval-Augmented Generation (RAG) and
        multi-agent workflows, and helps teams take these systems from early ideas to real-world
        use. Sarang also contributes to Thoughtworks&#x2019; Global AI Service Development team and teaches
        an O&#x2019;Reilly
        course on building production-ready RAG applications.

## Contents

- The Challenge: Navigating the Preclinical Data Maze

- The Solution: PRINCE - An Evolutionary Platform

- System Architecture: Engineering a Reliable Agentic RAG System

- The Agentic RAG System

- Clarify User Intent

- Think &amp; Plan: Process Reflection

- The Researcher Agent

- The Reflection Agent: Data Validation and Sufficiency

- The Writer Agent: Answer Synthesis and Formatting

- Building Trust in a Production LLM System

- Transparency and Explainability

- Evaluation

- Monitoring

- Engineering for Resilience: Error Handling and Recovery

- Enhancing Data Quality: Named Entity Recognition and Annotation

- The Journey Continues: Iterative Development

- Conclusion

Preclinical drug discovery is inherently complex and data-intensive.
      Researchers face the significant challenge of efficiently accessing and
      analyzing vast volumes of information generated during this critical phase.
      Traditional keyword-based search methods, often reliant on rigid Boolean
      logic, frequently fall short when confronted with the nuanced and intricate
      nature of preclinical research questions.

The advent of Large Language Models (LLMs) has presented a transformative opportunity. By
      combining the generative power of LLMs with the precision of information retrieval systems, Retrieval-Augmented Generation (RAG) has emerged as a promising technique.
      This approach holds the potential to revolutionize preclinical data access, enabling
      researchers to pose complex questions in natural language and receive accurate, context-rich
      answers grounded in proprietary data.

Recognizing this potential early, Bayer committed to exploring how these
      technologies could address longstanding challenges in preclinical research.

In this post, we share that journey&#x2014;how Bayer's early investment in generative AI
      has resulted in PRINCE, an agentic AI system built on Agentic RAG. This case study
      explores the technical architecture, engineering decisions, and lessons
      learned in transforming preclinical data retrieval from a challenging maze
      into an intuitive conversational experience.

Many of the engineering decisions behind PRINCE can now be understood through the lens of context
      engineering and harness engineering, although when the system was first designed we did not use these terms. Context engineering shaped what information each model
      received, what it did not receive, and how context moved between specialized steps such as
      research, reflection, and writing. Harness engineering shaped the scaffolding around the
      models: orchestration, tool boundaries, state persistence, retries, fallbacks, validation,
      reflection loops, observability, and human review.

While this post focuses on the technical architecture and engineering challenges, our paper
      published in Frontiers in Artificial Intelligence covers the
      product evolution and business impact in more detail.

## The Challenge: Navigating the Preclinical Data Maze

The preclinical research landscape at Bayer, like many large
        pharmaceutical organizations, is characterized by a diverse and extensive
        array of data. This includes highly structured datasets from various studies, alongside vast
        amounts of unstructured
        information embedded within text documents such as study reports,
        publications, and regulatory submissions. Researchers frequently
        encountered significant hurdles in accessing and analyzing this
        information effectively:

- Data Silos: information was fragmented and scattered across numerous
          disparate systems and repositories, making it exceedingly difficult to gain a
          comprehensive, holistic view of preclinical data related to a specific compound
          or study. 

- Limited Search Capabilities: traditional keyword-based search engines
          struggled with the complexity and variability of preclinical terminology and
          research questions, often yielding irrelevant, incomplete, or overwhelming
          results. 

- Time-Consuming Manual Analysis: extracting specific insights or compiling
          information across multiple documents required considerable manual effort,
          diverting valuable researcher time away from core scientific activities.

These inherent challenges highlighted a clear need for a more
        efficient, intelligent, and integrated approach to preclinical data
        retrieval and analysis.

## The Solution: PRINCE - An Evolutionary Platform

To address these challenges, Bayer developed the Preclinical
        Information Center (PRINCE) platform. PRINCE was conceived as a unified
        gateway to preclinical data, initially focusing on consolidating
        previously siloed structured study metadata and exposing them in a “Searchable” manner.
        This initial phase allowed users to apply advanced filters and retrieve
        information primarily from structured study metadata.

However, a significant portion of Bayer's valuable preclinical
        knowledge resides within unstructured PDF study reports accumulated over
        decades. Due to numerous system migrations over the years, the structured
        metadata associated with these reports could be incomplete, missing, or
        even contain incorrect annotations. Crucially, the authoritative “gold
        standard” information was consistently present within the approved PDF
        study reports.

The emergence of Generative AI, particularly RAG, provided the key to
        unlocking this wealth of unstructured data. By integrating RAG
        capabilities, PRINCE began to shift the paradigm from a filter-based
        'search' tool to a natural language 'ask' system, enabling researchers to
        query the content of these study reports directly.

This evolution reflects PRINCE's progression through three distinct
        phases:

- Search: the initial phase focused on creating a unified gateway to
          thousands of nonclinical study reports, consolidating multiple in-house data silos from
          various preclinical domains into a
          searchable format, primarily leveraging structured metadata.

- Ask: this phase introduced an AI-powered question-answering system utilizing
          Retrieval Augmented Generation (RAG). This enabled researchers to derive insights directly
          from unstructured data, including scanned PDFs from historical reports, by posing
          questions in natural language.

- Do: the current phase positions PRINCE as an active research assistant capable of
          executing complex tasks. This is achieved through the integration of multi-agent systems,
          allowing the platform to handle intricate queries, orchestrate workflows, and support
          activities like drafting regulatory documents.

This deliberate evolution from Search to Ask to Do represents a strategic
        response to the industry's need for greater efficiency and innovation in
        preclinical development. By providing researchers with increasingly powerful
        tools to access, analyze, and act upon preclinical data, PRINCE aims to enable
        faster data-driven decision-making, reduce the need for unnecessary experiments,
        and ultimately accelerate the development of safer, more effective
        therapies.

## System Architecture: Engineering a Reliable Agentic RAG System

The system functions as an interactive conversational UI, powered by a robust backend
        infrastructure. Its architecture, designed for handling complex queries and delivering
        accurate, context-rich answers, is orchestrated using LangGraph and served via a 
        FastAPI application.

Figure 1 provides the system context&#x2014;UI, backend, data
        stores, LLM fallbacks, and observability&#x2014;while Figure 2
        zooms into how the system coordinates its specialized agents.

Figure 1: System context and supporting
        platforms.

- User Request: the process begins when a user submits a request through the
          Conversational UI which is built with React.

- Orchestration: the user's request is routed to a LangGraph-based orchestration layer in
          the backend. This workflow engine coordinates a multi-stage process that progresses
          through
          clarifying user intent, thinking and planning, conducting research (using RAG and
          Text-to-SQL),
          validating data completion, and finally generating a response through the Writer agent.
          The
          workflow includes deliberate pause points and feedback loops to ensure data completeness
          before
          proceeding. (We explore the details of this agentic workflow in a dedicated section
          later.)

- Data Retrieval and State Management: the Researcher agents interact with a comprehensive
          and
          distributed data ecosystem: 

- Vector representations of all study reports are stored in OpenSearch, forming
            the core knowledge base for information retrieval.

- Curated structured data, resulting from various ETL and harmonization
            processes, is accessed via Athena.

- The state of the agent's execution is meticulously tracked. After each logical
            step (a LangGraph node execution), the corresponding state is persisted in 
              PostgreSQL using a LangGraph checkpointer.

- Broader application-level state is managed in 
              DynamoDB.

- The system leverages internal GenAI platforms that host models from OpenAI, Anthropic,
          Google, and open-source providers. These platforms expose all models via a unified
          OpenAI-compatible endpoint, making it easy to swap models and choose the best tool for
          each task. They also manage the control plane, enforcing rate limits and other safeguards
          to prevent abuse.

- Resilience and Error Handling: robustness is a critical design principle, with
          multiple fallback mechanisms in place: 

- If a specific LLM fails, the system automatically retries
            the request several times before falling back to an alternative model or platform to
            ensure service continuity.

- To recover quickly from transient failures, retries are
            implemented at both the individual LLM call level and the logical node level (i.e., an
            entire step in the agent's plan).

- Also, agents are provided the context of the errors so that they can chart a different
            trajectory or alternative plan of action as a response.

- Observability and Evaluation: the entire system is monitored for performance and
          reliability: 

- General system health and metrics are tracked using Cloudwatch.

- Langfuse serves as the primary observability tool, providing detailed traces of
            all production traffic. This allows for in-depth debugging of issues. Furthermore,
            evaluation datasets are stored and managed within Langfuse, making it easier to analyze
            performance scores and diagnose specific failures. The evaluation is done using RAGAS
            evaluation framework. The live traffic evaluation is done on a daily basis while the
            dataset evaluation is done whenever significant changes are made to the core workflow,
            prompts, or underlying models.

- Final Response: once the agents have processed the request and generated a
          satisfactory response, it is sent back to the Conversational UI to be presented to the
          user.

A design principle running through this architecture is context discipline. Larger context
        windows did not remove the need to be selective about what each agent sees. In early
        iterations, putting too much information into the context made the system harder to steer
        and harder to evaluate. PRINCE therefore avoids treating the prompt as one large container
        for all available information. Instead, different stages receive different context: planning
        context for Think &amp; Plan, retrieval context for the Researcher Agent, evidence context
        for the Reflection Agent, and synthesis context for the Writer Agent. This reduces context
        pollution and makes the system easier to debug, evaluate, and improve.

These steps ensure that the system can provide reliable and contextually relevant answers
        to a wide range of complex queries by leveraging a sophisticated, multi-agent architecture
        and a diverse set of powerful tools and data sources.

## The Agentic RAG System

PRINCE incorporates an agentic RAG system (Figure 2) to handle complex user requests that require multiple
        steps, reasoning, and interaction with different tools or data sources. This setup,
        implemented using LangGraph, orchestrates the overall workflow and leverages Researcher
        Agent, Writer Agent, and Reflection Agent for specific tasks. The system
        is designed to be robust and reliable, with multiple fallback mechanisms in place to ensure
        that the system can continue to function even if some of the components fail.

Figure 2: The research workflow.

### Clarify User Intent

The Clarify User Intent step serves as the first line of defense against
          ambiguity. As the system scaled to include diverse domains like toxicology and
          pharmacology, simple user queries often became ambiguous, making it difficult to
          automatically select the right tools. Rather than relying on expensive trial-and-error
          across all data sources, the system proactively asks clarifying questions to pinpoint the
          specific domain or data type.

This ensures the system enhances the query with the necessary constraints to target the
          correct tools. We are also optimizing this by developing domain-level selection in
          the UI, which will allow users to pre-filter valid tools upfront. To further reduce
          friction, the system also provides AI-assisted source recommendations: when a user has not
          selected any data source &#x2014; or has selected several without a clear focus &#x2014; the model
          analyzes the intent behind the user's query and suggests the most relevant sources. The
          user retains full control and can accept, adjust, or override the recommendation, ensuring
          domain expertise always has the final say. This “fail-fast” mechanism prevents wasted
          execution on vague queries, while careful tuning ensures the system remains unobtrusive
          when the intent is already clear.

From a context engineering perspective, this step is the first assembly decision in the
          workflow: it constrains which tools, domains, and data sources will be in scope before any
          retrieval begins, ensuring subsequent agents receive a focused rather than open-ended
          problem.

### Think &amp; Plan: Process Reflection

The Think &amp; Plan step is responsible for devising a strategy to fulfill the
          user's request. This critical component gives the system a dedicated space to reason about
          the next steps before taking action&#x2014;a technique inspired by Anthropic's Think tool.
          Importantly, this step performs process reflection: evaluating whether the agent is
          making the right progress toward its end goal and is on right trajectory, rather than
          evaluating the data itself.

In multi-step agentic workflows, particularly those involving many sequential actions,
          process reflection is essential. Consider a scenario where the system needs to execute 50
          steps to complete a complex task. At each juncture, the system must ask: Am I taking these
          steps in the right manner? Am I making the progress I'm supposed to make? Is the current
          trajectory leading toward the user's goal? The Think &amp; Plan step provides this
          metacognitive capability, allowing the system to reflect on its own workflow and adjust
          its strategy accordingly.

This “thinking space” has proven particularly valuable in scenarios involving multiple
          tool calls.
          When PRINCE was initially developed, it had only a couple of tools: one for RAG-based
          retrieval and
          another for Text-to-SQL queries. However, as we integrated more data sources to expand the
          system's
          capabilities, the number of available tools grew significantly. With this explosion of
          tools came an
          inherent challenge: overlapping concerns and domain boundaries across different tools.

For example, multiple tools might serve similar but subtly different purposes&#x2014;querying
          structured
          metadata versus unstructured reports, or retrieving study summaries versus detailed
          experimental data.
          When presented with tools that belong to similar domains but handle slightly different
          data, the LLM
          would sometimes struggle to select the most appropriate tool for a given query. By
          introducing a
          dedicated thinking step, the system can explicitly reason about which tool best matches
          the user's
          intent, evaluate the characteristics of each available tool, and make a more informed
          decision. This
          approach led to a dramatic improvement in the accuracy of tool selection.

Beyond tool selection, the Think &amp; Plan step is essential for orchestrating
          multi-step processes. Many complex queries in PRINCE require a series of tool calls where
          the output of one tool must be analyzed before determining the next action. For instance,
          the system might first query structured metadata to identify relevant studies, then use
          those study IDs to retrieve detailed information from unstructured reports, and finally
          synthesize the findings. Without a dedicated space for process reflection, the system
          would attempt to execute these steps linearly without evaluating whether each step is
          bringing it closer to the goal. With the thinking step in place, the system can pause,
          assess its progress in the workflow, and intelligently plan the subsequent tool calls
          needed to complete the user's request.

### The Researcher Agent

The Researcher Agent serves as the system's primary information gatherer. As we
          onboard new scientific domains onto PRINCE, we consistently observe that data falls into
          two primary categories: structured and unstructured. While specific
          implementation techniques may vary across domains &#x2014; for instance, leveraging Snowflake
          Cortex Analyst for pharmacology queries for Text-to-SQL versus other more custom methods
          for toxicology&#x2014;the fundamentals behind these retrieval strategies remain consistent.

As PRINCE expands across multiple preclinical domains, a single Researcher agent with a
          flat tool list
          becomes increasingly hard to manage. Many tools operate on similar concepts&#x2014;&#x201C;studies&#x201D;,
          &#x201C;findings&#x201D;, &#x201C;assays&#x201D;&#x2014;but point to different underlying datasets, schemas, and regulatory
          interpretations depending on the domain. For example, when a user refers to &#x201C;the study&#x201D;,
          the relevant context might be a repeat&#x2011;dose toxicology study, a cardiovascular safety
          pharmacology package, or a particular assay in aggregated mass&#x2011;data tables, each with its
          own preferred sources of truth.

To avoid one monolithic agent juggling overlapping tools and subtly different data
          contracts, we are actively evolving the Researcher capability into a hierarchy of
          domain&#x2011;specific
          sub&#x2011;agents. In this proposed architecture, each domain agent will own its own toolset (for
          example, toxicology RAG + tox
          metadata SQL, or pharmacology RAG + assay&#x2011;level SQL) along with tailored prompt
          instructions that encode how that domain&#x2019;s data model works, which tables or indices are
          authoritative, and how to interpret key concepts. We anticipate this will keep
          responsibilities coherent,
          reduce accidental cross&#x2011;domain leakage, and make it easier to reason about and test
          retrieval behaviour per domain.

To effectively harvest insights from this diverse landscape, the Researcher Agent employs
          a hybrid retriever approach focused on two distinct
          patterns:

- Retrieval-Augmented Generation (RAG): for processing unstructured data,
            primarily PDF reports.

- Text-to-SQL: for querying structured data housed in Amazon Athena.

This dual-strategy allows the system to bridge the gap between narrative scientific
          reports and quantitative experimental data.

In this updated vision, the top&#x2011;level Researcher Agent is designed to act as a
          coordinator rather than a
          single all&#x2011;knowing component. Given the clarified user intent and any explicit domain
          selection from the UI, it will route the query to the appropriate domain sub&#x2011;agent, which
          can then
          decide how to combine RAG and Text&#x2011;to&#x2011;SQL within its own boundary. This pattern aims to
          preserve the simplicity of &#x201C;one researcher&#x201D; from the user&#x2019;s perspective, while internally
          allowing each domain to evolve its own tools, schemas, and retrieval recipes without
          destabilizing the rest of the system.

#### Retrieval-Augmented Generation (RAG) for Unstructured Data

Given the vast repository of thousands of preclinical study reports and other
            unstructured documents, RAG is essential for extracting relevant insights by grounding
            LLM responses in this specific knowledge base. The RAG pipeline comprises a
            comprehensive ingestion process and a sophisticated
            query-time architecture.

Ingestion Process: Preclinical study reports, mostly PDFs spanning decades and
            often including scanned documents with complex tables, are first centralized into an S3
            data lake and passed through an extraction pipeline tuned for this corpus. The extracted
            text is normalized into structured JSON and then chunked using a strategy that preserves
            enough scientific context while keeping chunks efficient for retrieval.

Each chunk is enriched with study&#x2011; and section&#x2011;level metadata from Amazon Athena (for
            example study ID, compound, species, route, page, and parent section), which later
            enables precise metadata filtering in the RAG layer. Finally, these annotated chunks are
            embedded and indexed in Amazon OpenSearch Service,
            forming the vector store that backs semantic and metadata&#x2011;aware retrieval over both the
            historical corpus and the daily deltas as new or updated reports arrive.

Query-Time RAG Pipeline: When a user submits a query, the system initiates a
            multi-stage retrieval process. This pipeline is engineered to effectively retrieve the
            most relevant and trustworthy information from the vector database to ground the LLM's
            response.

“Were any of the following clinical findings observed in study T123456-2: piloerection, ataxia, eyes partially closed, and loose faeces?”

keyword extractor

“piloerection”, “ataxia”, “eyes partially closed”, “loose faeces”

filter extractor

eq(study_id, T123456-2)

query expander

1. Can you provide details on the clinical symptomsreported in research T123456-2, including anyoccurrences of goosebumps, lack of coordination,semi-closed eyelids, or diarrhea?2. In the results of experiment T123456-2, were there anyrecorded observations of hair standing on end, unsteadymovement, eyes not fully open, or watery stools?3. What were the clinical observations noted in trialT123456-2, particularly regarding the presence of hairbristling, impaired balance, partially shut eyes, or softbowel movements?4. ... 5. ...

weighted hybrid search

retrieves ~20 chunks

0.3

0.7

re-ranker

reranker selects top 7 chunks

final prompt generator

response to user

Responding to a query issued in natural language

An LLM analyzes the query and extracts keywords

Concurrently, the LLM generates a metadata filter to
                    narrow the search space

The LLM generates a query expander to
                    broaden the search space

The retriever uses a weighted hybrid search to retrieve the most relevant
                    information

The reranker refines the results to ensure the most relevant information is
                    brought to the LLM

The final prompt generator generates the final prompt for the LLM

The responder sends the response to the user

To illustrate this pipeline, consider the example query: “Were any of the
            following clinical findings observed in study T123456-2: piloerection, ataxia,
            eyes partially closed, and loose faeces?”. The system processes this query
            through the following steps:

- Keyword Extraction: the user's natural language query is first analyzed by an
              LLM. Through careful prompt engineering, the model is instructed to extract
              keywords highly relevant for keyword search within our document corpus (e.g.,
              “piloerection”, “ataxia”, “eyes partially closed”, “loose faeces”).

- Metadata Filter Generation: concurrently, the LLM generates a
              metadata filter based on the query. For example, a filter eq(study_id, T123456-2) is
              extracted to narrow the search space. This filter is dynamically generated using
              few-shot prompting with various permutation and combination examples provided to the
              model, ensuring it can handle diverse filtering requests.

- Query Expansion: to ensure comprehensive retrieval and account for variations in
              phrasing and terminology, query expansion (multi
              query or query rewrite) is performed by a smaller, faster model. This generates n=5
              semantically similar queries based on the original question. For the example query,
              this might include variations like:

- “Clinical symptoms reported in research T123456-2, including goosebumps,
                lack of coordination, semi-closed eyelids, or diarrhea.”

- “Recorded observations in experiment T123456-2 regarding hair standing on
                end, unsteady movement, eyes not fully open, or watery stools.”

- “What were the clinical observations noted in trial T123456-2,
                particularly regarding the presence of hair bristling, impaired balance,
                partially shut eyes, or soft bowel movements.”

- Hybrid Retriever: information retrieval from the vector database (Amazon OpenSearch
                Service) utilizes a Hybrid Search approach that combines metadata filtering,
              semantic vector similarity search (kNN), and keyword-based retrieval. This process is
              executed as follows:

- Metadata Filtering: the metadata filter generated in the previous step
                (e.g., eq(study_id, T123456-2)) is applied directly to the vector database query.
                This pre-filters the search space based on the structured metadata attached to the
                chunks during the ingestion process from Amazon Athena, ensuring that only chunks
                associated with the specified study ID (or other relevant metadata) are considered.
                This significantly reduces the search space from millions of vectors to a more
                manageable range of tens to hundreds, improving efficiency and relevance.

- Parallel Hybrid Search Execution: for each of the n=5 expanded queries, a
                single hybrid search query is executed in parallel against the filtered Amazon
                OpenSearch Service vector database. This query combines both semantic vector
                similarity search (kNN) and keyword-based search, leveraging OpenSearch's
                capabilities for efficient multi-vector and text search.

- Weighted Result Scoring: within each individual hybrid search executed in
                parallel, a weighted approach is applied to the results. A weight of 0.7 is given to
                the semantic search results and 0.3 to the keyword search results to balance
                contextual understanding and precise term matching. This weighting was determined
                through experimentation to optimize retrieval effectiveness for our data.

- Result Aggregation and Initial Ranking: the results (sets of relevant
                chunks with their weighted scores) from all 5 parallel hybrid search executions are
                aggregated. Unique chunks from all search results are pulled together, and their
                highest weighted score across the parallel searches is used to determine an initial
                ranking. This step initially retrieves a larger set of potential context chunks
                (k=~20) based on these aggregated and weighted scores.

- Reranking: the initial set of retrieved chunks (k=~20) is then refined using a Rerank step. A cross-encoder model (bge-reranker-large)
              evaluates the relevance of each retrieved chunk against the original question,
              selecting the top k=7 most relevant chunks to be used as context for the LLM. This
              reranking step is crucial for ensuring that the most pertinent information, even if
              not the highest in initial semantic similarity or keyword match, is prioritized for
              the final response generation.

- Final LLM Prompt Generation: the refined context (k=7 chunks) is then
              combined with the original question to form the final LLM prompt. This prompt is
              carefully constructed to guide the LLM in generating a focused and accurate response
              based on the provided context, minimizing the risk of hallucination.

- Response Generation with Citation: a state-of-the-art reasoning model then processes
              the final
              prompt and the provided context to generate response with citation. The LLM
              synthesizes the information from the context to formulate a coherent and accurate
              answer. Crucially, the response automatically includes citations linking back to the
              specific chunks in the original document(s) that support the generated answer.

- Monitoring: the entire Query-Time RAG process, from initial query to final
              response generation, is continuously monitored using Langfuse for
              observability, performance and quality analysis.

#### Text-to-SQL for Structured Data

While RAG excels at unstructured data, queries requiring precise filtering,
            aggregation, or comparison of structured data points are better suited for Text-to-SQL.
            Examples include “Give me 50 example studies done on RAT” or retrieving specific
            numerical assay results including dosage groups. As shown in the 
              Researcher Agent can intelligently decide to hand over such queries to the
            Text-to-SQL tool.

Figure 3: Text-to-SQL tool

The process for converting a natural language question into an executable
            SQL query and retrieving results involves several key steps:

- Query Analysis and Intent Recognition: the user's natural language query is
              analyzed to understand the user's intent and identify the specific data points and
              filters being requested from the structured metadata.

- Schema Understanding and Relevant Schema Selection: to accurately generate a
              SQL query, the LLM requires an understanding of the relevant database schema. For
              large and complex schemas, only the necessary schema components relevant to the user's
              query are dynamically injected into the LLM's context. This reduces the complexity for
              the model and improves the accuracy of the generated SQL.

- Dynamic Few-Shot Prompting for SQL Generation: converting complex natural
              language queries into precise SQL dialect (in our case, Athena) can be challenging for
              LLMs. To address this, we employ dynamic few-shot prompting. A collection of carefully
              hand-picked examples, representing various complex query patterns and their
              corresponding correct SQL translations in the Athena dialect, is stored in a separate
              collection within our vector database. Based on the user's query, relevant examples
              are retrieved from this “semantic layer” using vector similarity search and included
              in the prompt to the LLM. This provides the LLM with in-context learning examples,
              guiding it to generate accurate SQL queries in the correct dialect. Continuous
              addition of new examples based on encountered challenges further improves the system's
              performance over time.

- SQL Query Generation and Validation: a model with strong code generation
              capabilities,
              conditioned on the relevant schema information and dynamic few-shot examples,
              generates the
              corresponding SQL query. To ensure the LLM can accurately process the results and
              identify the correct rows for subsequent synthesis, certain essential columns, such as
              study ID and study title, are always included in the generated SELECT query. The
              generated query is then validated to ensure it adheres to allowed operations (e.g.,
              only SELECT queries are permitted; DELETE, INSERT, or UPDATE queries are explicitly
              blocked for data integrity and security). Notably, an earlier iteration of this
              process included an LLM review step for generated SQL queries; however, this step was
              later removed as it was fou
