# Scenario: Mining agreement renewal inside an ancestral domain

Use case D. Model: `qwen2.5:7b`. Run 2026-11-09T16:14:09+00:00. Every entry below is in `audit_log.jsonl` with its hash.

## Pre-agreed rules

- Nothing is rejected or approved automatically; a human reviews every flag.
- Consent is the consensus of all members under customary law (IPRA s3(g)).
- No issuance or renewal without NCIP certification, and none while FPIC is pending (IPRA s59).
- Private (sacred) content is never shared outside the community.

## Day 0 - evt-1

> A mining company asks to renew its 25-year agreement, which covers part of an Indigenous community's ancestral domain, on the original terms.

Released to: denr_mgb_agent

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-1; board posts: 0  
**Retrieved:** Mining Act (RA 7942) s16, IPRA (RA 8371) s59, G-01, K-CD02, PH-L02, PH-J01, K-CD04

**Reasoning:**
1. The mining company seeks renewal, which requires prior consent from the Indigenous Cultural Community (ICC/IP) under RA 7942.
2. IPRA s59 mandates NCIP certification before any issuance or renewal of mining permits, especially in ancestral domains.
3. There is a potential conflict between the Mining Act's requirement for prior consent and IPRA's requirement for consensus among all members.
4. The case law suggests that while the Mining Act requires prior consent, it does not explicitly state that NCIP certification is mandatory.

**Recommendation:** The renewal application should be referred to the NCIP for certification, as required by IPRA s59.

**Policy references:** [PH-L02] Mining Act (RA 7942) s16; [PH-L01] IPRA (RA 8371) s59; [K-CD02] Lone Congressional District of Benguet Province v. Lepanto Consolidated Mining Co.; Republic v. Lepanto Consolidated Mining Co., G.R. Nos. 244063 and 244216  
**Gaps or conflicts:** There is a potential conflict between the Mining Act's requirement for prior consent and IPRA's requirement for consensus among all members.  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 4e0ec07ae55d8f9a…`

**Expected:** Endorse to NCIP for FPIC and the Certification Precondition first.  
**Expected references found:** 2/2 (IPRA s59, Mining Act s16)

## Day 30 - evt-2

> The company argues FPIC cannot apply because the agreement predates IPRA, and files for arbitration.

Released to: denr_mgb_agent, legal_adviser

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-1, evt-2; board posts: 0  
**Retrieved:** Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), IPRA (RA 8371) s59, G-01, K-CD02

**Reasoning:**
1. IPRA s59 mandates NCIP certification
2. FPIC required for renewal
3. Precedent supports IPRA over mining act
4. Arbitration cannot override public policy

**Recommendation:** The company's argument is invalid; the renewal of its mining agreement requires NCIP certification and FPIC from the affected community.

**Policy references:** IPRA s59; Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022)  
**Gaps or conflicts:** -  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** high · **Human review:** pending (routine)  
`entry_hash eb6b93d9c5542b87…`

### legal_adviser (Policy and legal adviser)

**Saw:** evt-2; board posts: 1  
**Retrieved:** Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), IPRA (RA 8371) s3(g), , K-CD02, K-CD01, K-PH05

**Reasoning:**
1. The company's argument is invalid given IPRA s59 and Supreme Court rulings.
2. FPIC is a requirement for renewal regardless of when the agreement was signed.
3. NCIP certification is mandatory before any renewal can proceed.
4. The absence of NCIP AO 3, s.2026 creates uncertainty in FPIC procedures.

**Recommendation:** The company's argument should be rejected; the renewal process must comply with IPRA s59 and Supreme Court rulings.

**Policy references:** IPRA s59; [K-CD02] Republic v. Lepanto Consolidated Mining Co., G.R. Nos. 244063 and 244216 (2022); [K-PH05] NCIP AO 3, s. 2026 — The 2026 Guidelines on FPIC and Related Processes  
**Gaps or conflicts:** The absence of NCIP AO 3, s.2026 creates uncertainty in the FPIC procedures.  
**Notify:** ncip_fpic_team_agent, denr_mgb_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 63e827efca715b22…`

**Expected:** Renewal depends on the law in force, and s59 covers renewals; DENR-MGB alerts NCIP, which is not a party.  
**Expected references found:** 1/2 (IPRA s59)

## Day 45 - evt-3

> NCIP's FPIC team opens FPIC; household representatives and elders are recorded separately, and most place the mine inside the domain.

Released to: ncip_fpic_team_agent, story_agent

### ncip_fpic_team_agent (NCIP regional FPIC team)

**Saw:** evt-3; board posts: 0  
**Retrieved:** , Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012, and its implementing memorandum circular, PH-C01, PH-N02, K-PH05

**Reasoning:**
1. NCIP's FPIC team has opened the process with household representatives and elders recorded separately.
2. The mine is placed inside the domain by most participants.
3. There are no clear guidelines on how to proceed given the transition from 2012 to 2026 procedures.
4. The community assembly indicates a consensus, but the exact roles of NCIP and other agencies are unclear.

**Recommendation:** Continue with the FPIC process as initiated but ensure that all roles and responsibilities of NCIP are clearly defined.

**Policy references:** NCIP AO 3, s. 2026; [PH-N07]; [PH-C01]  
**Gaps or conflicts:** Unclear transition from 2012 to 2026 procedures.; Lack of clear roles and responsibilities for NCIP in the current context.  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 7cc455c7461f3887…`

### story_agent (Application)

**Saw:** evt-3; board posts: 1  
**Retrieved:** G-09, K-IN17, , PH-N02, K-PH05

**Reasoning:**
1. FPIC process initiated with clear roles
2. Most community members agree on mine placement
3. NCIP's FPIC team should proceed per guidelines
4. Need for a shared register of pending claims

**Recommendation:** NCIP should proceed with the FPIC process as initiated but ensure a shared register of pending claims is established.

**Policy references:** IPRA s59; [PH-N02] NCIP AO No. 3, s. 2012; [K-PH05] NCIP AO 3, s. 2026 — The 2026 Guidelines on FPIC and Related Processes  
**Gaps or conflicts:** No shared, live register of pending claims as per [G-09]  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 47547a8be87f9026…`

**Expected:** Household register and overlap map from matched accounts; customary decision process.  
**Expected references found:** 0/3 (none)

## Day 75 - evt-4

> The arbitrators rule that FPIC and certification cannot be imposed and treat the agreement as renewed.

Released to: denr_mgb_agent

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-1, evt-2, evt-4; board posts: 1  
**Retrieved:** Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), IPRA (RA 8371) s59, G-09, K-CD02, PH-N02

**Reasoning:**
1. FPIC and NCIP certification are mandatory
2. Arbitrators' decision conflicts with legal requirements
3. Recommendation must comply with IPRA s59

**Recommendation:** The mining agreement should be treated as renewed but with the condition that the company must obtain NCIP certification and ensure FPIC from the affected community.

**Policy references:** IPRA s59; [K-CD02] Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022)  
**Gaps or conflicts:** Conflict between arbitration ruling and legal requirements on FPIC and NCIP certification  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 9883a1cab3185491…`

**Expected:** Share the ruling with NCIP and the legal adviser, hold the renewal while FPIC is pending, and ask a court to set it aside on public-policy grounds.  
**Expected references found:** 1/2 (IPRA s59)

## Day 105 - evt-5

> Two appointed representatives now say the community consented years ago.

Released to: story_agent

### story_agent (Application)

**Saw:** evt-3, evt-5; board posts: 1  
**Retrieved:** Kenya Community Land Act 2016, s15, IPRA (RA 8371) s16, NPC Circular No. 2023-04 (Guidelines on Consent, 7 November 2023), PH-N02, K-PH05

**Reasoning:**
1. Review of FPIC process
2. Consent validation required
3. Community assembly rules
4. Need for additional evidence

**Recommendation:** Further evidence needed to validate community consent

**Policy references:** IPRA s16; [PH-N02] Revised Guidelines on the Exercise of Free and Prior Informed Consent (FPIC) and Related Processes (NCIP AO No. 3, s. 2012); [K-PH05] NCIP AO 3, s. 2026 — The 2026 Guidelines on FPIC and Related Processes  
**Gaps or conflicts:** The new claim of past consent contradicts previous records and requires validation.  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 2f9698e1f0004713…`

**Expected:** Bias check flags a change made only by representatives; human review checks it against the recorded consent of all households; nothing changes automatically.  
**Expected references found:** 0/3 (none)

## Day 120 - evt-6

> The company offers benefits through those representatives in exchange for consent, and local officials ask to join the dispute.

Released to: story_agent, ncip_fpic_team_agent, ncip_en_banc_agent, denr_mgb_agent, npc_agent, lgu_agent, legal_adviser

### story_agent (Application)

**Saw:** evt-3, evt-5, evt-6; board posts: 1  
**Retrieved:** G-01, IPRA (RA 8371) s16, G-13, PH-L07, PH-D04, K-PH05, PH-L01

**Reasoning:**
1. Company benefits in exchange for consent raises ethical concerns.
2. Local officials joining dispute complicates community dynamics.
3. FPIC process initiated but needs clear NCIP oversight.
4. Consent defined by IPRA requires consensus, not just representatives.

**Recommendation:** The NCIP should oversee the FPIC process to ensure that all community members, including elders and representatives, are involved in the decision-making. Local officials should not be part of the dispute resolution unless they have been properly authorized by the community.

**Policy references:** IPRA s16; IPRA s59; NCIP AO 3, s. 2026; UNDRIP Art. 32(2); Local Government Code of 1991 (RA 7160) s22  
**Gaps or conflicts:** Conflict between company benefits and ethical consent process.  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 2123bd6244dd1100…`

### ncip_fpic_team_agent (NCIP regional FPIC team)

**Saw:** evt-3, evt-6; board posts: 2  
**Retrieved:** IPRA (RA 8371) s66, Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), , PH-N02, K-PH05

**Reasoning:**
1. Company offers benefits
2. Local officials join dispute
3. NCIP jurisdiction
4. FPIC process ongoing
5. Community consent required

**Recommendation:** The NCIP should intervene to ensure the FPIC process is not influenced by external benefits or local officials' interference.

**Policy references:** IPRA s66; K-PH05 NCIP AO 3, s.2026  
**Gaps or conflicts:** Unclear responsibilities for FPIC procedures in transition.  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent, legal_adviser · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash b90a4b91584e538a…`

### ncip_en_banc_agent (NCIP Commission en banc)

**Saw:** evt-6; board posts: 2  
**Retrieved:** IPRA (RA 8371) s66, IPRA (RA 8371) s62, Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012, and its implementing memorandum circular, K-PH05, K-PH27, PH-J01, PH-J02, PH-N01

**Reasoning:**
1. Local officials' interference is not allowed in FPIC processes.
2. The NCIP should oversee FPIC to ensure community consent is genuine.
3. Benefits offered by the company could influence consent, violating IPRA s59.
4. Disputes involving non-IPs or customary law should be resolved through NCIP procedures.

**Recommendation:** The NCIP should intervene to ensure the FPIC process is not influenced by external benefits or local officials' interference.

**Policy references:** IPRA s62; IPRA s66; [PH-L01] Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012 and its implementing memorandum circular; [K-PH05] NCIP AO 3, s. 2026 — The 2026 Guidelines on FPIC and Related Processes  
**Gaps or conflicts:** The role of the NCIP in resolving disputes between non-IPs and IPs is not clearly defined.  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash 580b2fe9350bb25f…`

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-1, evt-2, evt-4, evt-6; board posts: 4  
**Retrieved:** G-01, UNDRIP Art. 32(2), IPRA (RA 8371) s62, K-CD05, PH-L02, K-CD02

**Reasoning:**
1. Company offers benefits
2. Local officials interfere
3. FPIC process compromised
4. IPRA s59 compliance needed
5. NCIP intervention required

**Recommendation:** NCIP should intervene to ensure the FPIC process is not influenced by external benefits or local officials' interference.

**Policy references:** IPRA s59; UNDRIP Art. 32(2); [PH-L01] IPRA (RA 8371) s62; [K-CD05] Didipio Earth-Savers' Multi-Purpose Association, Inc. v. Gozun  
**Gaps or conflicts:** Conflict between Mining Act and IPRA on prior consent vs. consensus of all members.  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent · **Confidence:** high · **Human review:** pending (routine)  
`entry_hash ef384b3af25139aa…`

### npc_agent (Data protection (National Privacy Commission))

**Saw:** evt-6; board posts: 4  
**Retrieved:** K-IN17, NPC Advisory No. 2024-04 (19 December 2024), G-01, PH-D02, PH-D01, PH-D04

**Reasoning:**
1. Local officials' involvement in dispute resolution is inappropriate.
2. Community consent must be free and informed, not influenced by benefits.
3. NCIP should intervene to ensure FPIC process integrity.
4. Data privacy laws require transparency on AI processing.

**Recommendation:** NCIP should intervene to ensure that the FPIC process is not influenced by external benefits or local officials' interference. The company must provide clear information about AI processing and obtain free, informed consent from all community members.

**Policy references:** IPRA s59; PH-D01 (RA 10173) §3(g); PH-D04 (NPC Circular No. 2023-04, Guidelines on Consent); PH-D02 (Implementing Rules and Regulations of the Data Privacy Act)  
**Gaps or conflicts:** Standards for combining individual and collective consent in digital contexts are unclear.; Conflict between Mining Act's prior consent requirement and IPRA's consensus definition.  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 5b8f7155b399d7e6…`

### lgu_agent (Local government unit)

**Saw:** evt-6; board posts: 5  
**Retrieved:** Local Government Code (RA 7160) s41(c), G-13, G-01, PH-L07

**Reasoning:**
1. Local officials should not be part of the dispute resolution process.
2. NCIP intervention is necessary to ensure FPIC process integrity.
3. Community consent must be free and informed, without external benefits influencing decisions.

**Recommendation:** NCIP should intervene to ensure the FPIC process is not influenced by external benefits or local officials' interference. Local officials must be excluded from dispute resolution unless authorized by the community.

**Policy references:** IPRA s59; [PH-L07] Local Government Code (RA 7160) s41(c); [G-13] G-13: Policy gap (conflict_between_objectives)  
**Gaps or conflicts:** Indigenous representation in local councils not guaranteed. IPRA requires mandatory representation, while the Local Government Code lists indigenous communities as only one option for a sectoral seat.  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash 896a25d6246935ad…`

### legal_adviser (Policy and legal adviser)

**Saw:** evt-2, evt-6; board posts: 7  
**Retrieved:** G-01, G-13, IPRA (RA 8371) s16, PH-L07, PH-D04, K-PH05

**Reasoning:**
1. Company's benefits offer may influence FPIC process
2. Local officials' involvement could compromise community consent
3. NCIP should intervene per team assessments and legal references
4. FPIC steps need confirmation under NCIP AO 3, s.2026

**Recommendation:** NCIP should intervene to ensure the FPIC process is not influenced by external benefits or local officials' interference.

**Policy references:** IPRA s59; IPRA s16; G-01: Policy gap (conflict_between_objectives); [PH-D04] The 2023 Compendium of NPC Issuances (incl. NPC Circular No. 2023-04, Guidelines on Consent)  
**Gaps or conflicts:** Conflict between Mining Act and IPRA on prior consent vs. consensus of all members; Indigenous representation in local councils not guaranteed by law  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent, denr_mgb_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 3e5f6961129d96dc…`

**Expected:** No private ruling can waive FPIC or certification, which protect public policy; consent of all members free of manipulation; no renewal until both are complete.  
**Expected references found:** 2/4 (IPRA s59, UNDRIP Art. 32(2))

## Controversy

Flagging the representatives' changed accounts may look like distrust of traditional leaders. Flags go only to the community council and NCIP, are never published, and never reject testimony on their own. Elders can explain the change, and the explanation is recorded.

## Summary

- Agent steps logged: 14
- Expected policy references cited: 6/16
- Final hash: `3e5f6961129d96dc7d3cdc91eb7368a9b7686d85219381e89fea2301b6ecfb7a`
