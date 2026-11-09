# Use case: IKSP Record Pipeline (Philippines)

Domain: public services (indigenous knowledge, culture and public programmes). Country: Philippines.
Standard: ITU-T Y.3172 machine-learning pipeline (SRC, C, PP, M, P, D, SINK) with an ML function orchestrator (MLFO), ML sandbox and audit log. Framework: ITU AI Readiness Framework 2.0.

## Problem

Indigenous knowledge systems and practices (IKSP) sustain how Indigenous communities in the Philippines farm, govern themselves and respond to hazards, and they can improve public programmes. Accounts recorded from a few voices, cut from their context or changed in translation can misrepresent communities in decisions that last. Communities have the right to control their knowledge (Indigenous Peoples' Rights Act, RA 8371, s32-s35).

Gaps in current practice: dispossession, environmental degradation and language loss weaken transmission; weak implementation of free, prior and informed consent (FPIC) leaves IKSP open to appropriation; external control over Indigenous data weakens data sovereignty; structural discrimination and the digital divide limit participation, including of women and youth; under-investment in Indigenous-led information systems and ethnicity-disaggregated data weakens the evidence for policy.

Research problem: under what conditions can AI support community-directed documentation of IKSP that sustains knowledge transmission and gives a sound basis for authorised educational or policy use?

## Solution

An AI pipeline for community-directed IKSP records:

1. Select and record. The community chooses its knowledge holders; many voices are added, including women, youth and members from each settlement. Each person speaks in a separate session, in their own language, after individual consent and community authorisation are recorded. Each teller self-identifies their group.
2. Read and translate. A voice reader (speech-to-text) handles recordings; a text reader (OCR) handles written accounts, maps and genealogies. Originals are kept; untranslatable terms stay in the original language with a gloss; community translators check both.
3. Cross-check. Places, practices, events and family lines are extracted and linked across tellers and documents, with an agreement score for each account.
4. Check for bias. Accounts given by only one teller, or only by representatives, are flagged for human review. Nothing is rejected automatically.
5. Read back and review. Knowledge holders hear the summary and its translation and confirm or correct it; every correction goes into a meaning-change log.
6. Release by permitted use. The community sets each record's permitted use; records leave the private store only for approved uses.

Use cases: A. community archive and transmission (RA 11961 cultural mapping); B. education (DepEd Indigenous Peoples Education orders); C. disaster and climate planning (RA 10121 s2(j)); D. ancestral domain recognition (IPRA s52(d)); E. protection against appropriation (IPOPHL-NCIP Joint Administrative Order 1, s.2016).

## Y.3172 pipeline requirements

- SRC (sources): knowledge holders chosen by the community plus at least 20 tellers per topic, including women, youth and members from each settlement; self-identification; documents linked where they exist; policy corpus of Philippine law and global examples.
- C (collector): offline-first phone and web recorder (about 37% of Indigenous people live in geographically isolated and disadvantaged areas); consent explained in the teller's language, given per purpose and withdrawable (NPC Circular 2023-04).
- PP (preprocessor): speech-to-text and OCR checked by community translators; translation into Filipino and English keeping the original; policy knowledge base built with the ITU reference code.
- M (models): cross-checker, bias check, policy adviser and institutional agents; every match and flag points to the tellers and documents behind it; agents cite the clause they rely on.
- P (policy): teller consent and community FPIC, defined in IPRA s3(g) as the consensus of all members; tellers mark parts as controlled (tapu) or open (noa), following Te Mana Raraunga; a human can override any AI output (EU AI Act Article 14 model).
- D (distributor): outputs go only to roles the community has approved (NPC Advisory 2024-04); private community data never enters the open knowledge base.
- SINK (outputs): read-back for confirmation; release by permitted use only; every step written to a hash-chained audit log with sources and reasoning.
- MLFO (orchestrator): coordinates the agents (story agent, NCIP FPIC team, NCIP Commission en banc, DENR-MGB, National Privacy Commission, local government, legal adviser), releases scenario events step by step to only the agents that would receive them, and sends disputes to people: boundary disputes to customary process (IPRA s62), fraud review on the community's written request (IPRA s54).

## Agents

- Story agent: household register, matching, bias check, read-back, dossier.
- NCIP FPIC team agent: runs FPIC under the customary decision process; keeps the household register and consent count.
- NCIP en banc agent: Certification Precondition (IPRA s59), appeals, review of consent records.
- DENR-MGB agent: mining agreements and renewals; must have NCIP certification first; geohazard and flood maps.
- NPC agent: consent, data privacy, breach response.
- LGU agent: local records, zoning, local cybersecurity plan, local disaster risk reduction office.
- Legal adviser: law, case law, gaps and global examples; labels non-binding guidance as a benchmark.

## Error scenarios

Scenario 1 (use case D): a mining agreement renewal inside an ancestral domain, over simulated days. A company asks to renew a 25-year agreement on its original terms; argues FPIC cannot apply to a pre-IPRA agreement and files for arbitration; NCIP opens FPIC and households are recorded; the arbitrators treat the agreement as renewed; two appointed representatives claim past consent; the company offers benefits through them. The central issue is whether the agreement can be renewed without FPIC and the NCIP Certification Precondition (IPRA s59).

Scenario 2 (use case C): flood stories versus the official hazard map. The municipal disaster risk reduction office asks to use recorded flood stories to update its hazard map. The stories disagree with the official flood-susceptibility map in both directions. Only records approved for policy use are shared; discrepancies go to joint validation with DENR-MGB and the knowledge holders; only an authorised extract for the requested purpose and area is released.

## Readiness perspectives

Open data and open source (open policy knowledge base, private community data); generative AI content (read-back summaries confirmed by holders); contextualization (222 Indigenous groups and 110 languages in NCIP's database); cross-domain analysis (land, data protection, environment and mining, local government, disaster planning); human supervision (review and override at the policy gate); policy opportunities (gap table); social inclusion (women, youth, remote members; self-identification); digital infrastructure and energy (offline recording, sync later).
