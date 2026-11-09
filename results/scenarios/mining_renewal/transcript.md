# Scenario: Mining agreement renewal inside an ancestral domain

Use case D. Model: `qwen2.5:7b`. Run 2026-11-09T16:31:43+00:00. Every entry below is in `audit_log.jsonl` with its hash.

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
2. IPRA s59 mandates NCIP certification before issuing or renewing any concession without FPIC consensus.
3. Renewal must respect customary law and ICC/IP's free, prior, and informed consent as per IPRA s59.
4. The Mining Act allows for renewal under the same terms but does not override IPRA's requirement.

**Recommendation:** The renewal request cannot be processed without NCIP certification and FPIC from the ICC/IP.

**Policy references:** IPRA s59; Mining Act (RA 7942) s16; G-01: Policy gap (conflict_between_objectives)  
**Gaps or conflicts:** There is a potential conflict between the Mining Act's requirement for prior consent and IPRA's definition of consent as the consensus of all members under customary law.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash 805754855b7a0d1d…`

**Expected:** Endorse to NCIP for FPIC and the Certification Precondition first.  
**Expected references found:** 2/2 (IPRA s59, Mining Act s16)

## Day 30 - evt-2

> The company argues FPIC cannot apply because the agreement predates IPRA, and files for arbitration.

Released to: denr_mgb_agent, legal_adviser

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-1, evt-2; board posts: 0  
**Retrieved:** Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), IPRA (RA 8371) s59, G-01, K-CD02

**Reasoning:**
1. IPRA s59 requires NCIP certification
2. FPIC is a condition for renewal
3. MPSA predates IPRA but still subject to its provisions
4. Arbitration cannot override public policy

**Recommendation:** Deny the company's request for renewal without obtaining NCIP certification and FPIC.

**Policy references:** IPRA s59; Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022)  
**Gaps or conflicts:** -  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** high · **Human review:** pending (routine)  
`entry_hash 81f961f58b133ae2…`

### legal_adviser (Policy and legal adviser)

**Saw:** evt-2; board posts: 0  
**Retrieved:** Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), IPRA (RA 8371) s3(g), , K-CD02, K-CD01, K-PH05

**Reasoning:**
1. The agreement predates IPRA but must comply with current law.
2. FPIC and NCIP certification are mandatory for renewal under IPRA s59.
3. Arbitration cannot override public policy protecting IPs.
4. Need to ensure FPIC process is properly initiated.

**Recommendation:** The company must comply with current IPRA requirements for FPIC and NCIP certification before any renewal can proceed.

**Policy references:** IPRA s3(g); IPRA s59; [K-CD02] Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022); [K-PH05] NCIP AO 3, s. 2026  
**Gaps or conflicts:** NCIP AO 3, s.2026 is not yet available for reference.  
**Policy gate:** held for human review - no-renewal-without-fpic-and-certification. The recommendation aligns with Rule 3, which states that no issuance or renewal can occur without NCIP certification and while FPIC is pending. The recommendation ensures compliance with these requirements.  
**Notify:** ncip_fpic_team_agent, denr_mgb_agent · **Confidence:** high · **Human review:** pending (held by policy gate)  
`entry_hash 0bf3e50199ab7d6a…`

**Expected:** Renewal depends on the law in force, and s59 covers renewals; DENR-MGB alerts NCIP, which is not a party.  
**Expected references found:** 2/2 (IPRA s3(g), IPRA s59)

## Day 45 - evt-3

> NCIP's FPIC team opens FPIC; household representatives and elders are recorded separately, and most place the mine inside the domain.

Released to: ncip_fpic_team_agent, story_agent

### ncip_fpic_team_agent (NCIP regional FPIC team)

**Saw:** evt-3; board posts: 0  
**Retrieved:** , Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012, and its implementing memorandum circular, PH-C01, PH-N02, K-PH05

**Reasoning:**
1. NCIP's FPIC team has opened the process with representatives and elders recorded separately.
2. The evidence does not specify if this is for a single domain or multiple domains.
3. There are no clear guidelines on how to proceed given the transition from 2012 to 2026 procedures.

**Recommendation:** NCIP should clarify if this is for a single or multiple domains and proceed accordingly.

**Policy references:** IPRA s59; [PH-N07]; [K-PH05]  
**Gaps or conflicts:** Unclear transition from 2012 to 2026 FPIC procedures.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 5e93afcbe610e58f…`

### story_agent (Application)

**Saw:** evt-3; board posts: 0  
**Retrieved:** G-09, K-IN17, , PH-N02, K-PH05

**Reasoning:**
1. FPIC process initiated
2. Most community members agree on mine placement
3. NCIP's role critical for certification
4. Need for clear documentation and transparency

**Recommendation:** Proceed with documenting the FPIC process and ensure transparency.

**Policy references:** IPRA s59; NCIP AO 3, s.2012 (Revised Guidelines on FPIC); NCIP AO 3, s.2026 (2026 Guidelines on FPIC)  
**Gaps or conflicts:** Unclear responsibility for maintaining a live register of pending claims (G-09)  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash b47a6453523eadfa…`

**Expected:** Household register and overlap map from matched accounts; customary decision process.  
**Expected references found:** 1/3 (NCIP AO 3 s.2012)

## Day 75 - evt-4

> The arbitrators rule that FPIC and certification cannot be imposed and treat the agreement as renewed.

Released to: denr_mgb_agent

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-1, evt-2, evt-4; board posts: 1  
**Retrieved:** Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), IPRA (RA 8371) s59, G-09, K-CD02, PH-N02

**Reasoning:**
1. FPIC and NCIP certification are mandatory
2. Arbitrators' decision conflicts with public policy
3. Recommendation must comply with legal requirements

**Recommendation:** The mining agreement cannot be renewed without obtaining the necessary NCIP certification and FPIC from the affected community.

**Policy references:** IPRA s59; [PH-L01] Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022)  
**Gaps or conflicts:** Conflict between arbitration decision and public policy protecting ICCs/IPs.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser, denr_mgb_agent · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash 5a702337668655b2…`

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
2. Check community consent validity
3. Evaluate evidence for past consent
4. Consider legal requirements

**Recommendation:** Request clarification on past consent and proceed with additional community assembly if necessary.

**Policy references:** IPRA s16; [PH-N02] NCIP AO No. 3, s. 2012; [K-PH05] NCIP AO 3, s. 2026  
**Gaps or conflicts:** Unclear validity of past consent without further evidence.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 8258cbfb94d58bea…`

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
3. IPRA defines consent as consensus, not individual representatives.
4. NCIP's FPIC process is ongoing; need to respect its findings.
5. Benefits and local official involvement may violate IPRA and RA 8371.

**Recommendation:** The company should not offer benefits in exchange for consent and local officials should be advised against joining the dispute.

**Policy references:** IPRA s16; IPRA s59; IPRA s65; NCIP AO 3, s. 2026  
**Gaps or conflicts:** Conflict between company's offer of benefits and IPRA's requirement for genuine consent.; Unclear if local officials' involvement is in line with customary law.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash cab38b0d016d7fba…`

### ncip_fpic_team_agent (NCIP regional FPIC team)

**Saw:** evt-3, evt-6; board posts: 1  
**Retrieved:** IPRA (RA 8371) s66, Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), , PH-N02, K-PH05

**Reasoning:**
1. Company offers benefits to representatives for consent.
2. Local officials ask to join dispute resolution.
3. FPIC is ongoing but guidelines are unclear due to transition period.
4. NCIP's jurisdiction applies over ICCs/IPs disputes, including FPIC.

**Recommendation:** Do not accept benefits from the company or allow local officials to join dispute resolution.

**Policy references:** IPRA s66; [PH-L01] IPRA (RA 8371) s66; [K-PH05] NCIP AO 3, s. 2026 — The 2026 Guidelines on FPIC and Related Processes  
**Gaps or conflicts:** Unclear FPIC procedures due to transition period.; Potential conflict of interest if local officials join dispute resolution.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 52c8a698185f7b52…`

### ncip_en_banc_agent (NCIP Commission en banc)

**Saw:** evt-6; board posts: 0  
**Retrieved:** IPRA (RA 8371) s66, IPRA (RA 8371) s62, Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012, and its implementing memorandum circular, K-PH05, K-PH27, PH-J01, PH-J02, PH-N01

**Reasoning:**
1. The company's offer of benefits to representatives in exchange for consent is a form of undue influence, which violates IPRA s62.
2. Local officials asking to join the dispute suggests an overlap with their jurisdiction, but NCIP has primary jurisdiction over ICC/IP disputes per IPRA s66 and s62.
3. The situation requires resolution through customary law or NCIP administrative procedures as per NCIP AO 3, s. 2026 and NCIP AO 2, s. 2012.

**Recommendation:** The NCIP should intervene to ensure that the consent process is free from undue influence and that customary laws are respected. Local officials should not be involved in the dispute resolution as it pertains to ICC/IP rights.

**Policy references:** IPRA (RA 8371) s66; IPRA (RA 8371) s62; NCIP AO 3, s. 2026; NCIP AO 2, s. 2012  
**Gaps or conflicts:** There is a potential conflict between the company's offer of benefits and the requirement for free, prior, and informed consent under IPRA s59.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash 26ab9be7a4027f7d…`

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-1, evt-2, evt-4, evt-6; board posts: 1  
**Retrieved:** G-01, UNDRIP Art. 32(2), IPRA (RA 8371) s62, K-CD05, PH-L02, K-CD02

**Reasoning:**
1. The company is offering benefits to representatives in exchange for consent.
2. Local officials are asking to join the dispute, which complicates the situation.
3. FPIC and NCIP certification are required before granting or renewing mining agreements (IPRA s59).
4. The Mining Act requires prior consent, while IPRA defines this as consensus under customary law (G-01).

**Recommendation:** The company should not offer benefits in exchange for consent, as this could be seen as a form of undue influence. The local officials' involvement complicates the dispute and may require mediation or arbitration.

**Policy references:** IPRA s59; UNDRIP Art. 32(2); G-01: Policy gap (conflict_between_objectives): Mining Act prior consent versus IPRA consensus of all members.  
**Gaps or conflicts:** The conflict between the Mining Act's requirement for prior consent and IPRA's definition of consensus under customary law.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 5c5afe8a9d46c70e…`

### npc_agent (Data protection (National Privacy Commission))

**Saw:** evt-6; board posts: 0  
**Retrieved:** K-IN17, NPC Advisory No. 2024-04 (19 December 2024), G-01, PH-D02, PH-D01, PH-D04

**Reasoning:**
1. Company offers benefits in exchange for consent, raising concerns about undue influence.
2. Local officials asking to join dispute may complicate community consent process.
3. Need to ensure individual and collective consent aligns with IPRA and Data Privacy Act.

**Recommendation:** Review the consent process to ensure it aligns with IPRA and Data Privacy Act requirements. Ensure that benefits offered do not unduly influence individual or collective consent.

**Policy references:** IPRA s3(g); IPRA s59; Data Privacy Act of 2012 (RA 10173) §3(g); Data Privacy Act of 2012 (RA 10173) §18(a)  
**Gaps or conflicts:** Standards for combining individual and collective consent in digital contexts are not clearly defined.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 3bcd211b4ecfc48d…`

### lgu_agent (Local government unit)

**Saw:** evt-6; board posts: 0  
**Retrieved:** Local Government Code (RA 7160) s41(c), G-13, G-01, PH-L07

**Reasoning:**
1. Local officials are asked to join a dispute with the company.
2. The company offers benefits in exchange for consent, which may influence local officials' decisions.
3. Indigenous representation is not guaranteed under RA 7160 s41(c).
4. There's a conflict between the Mining Act and IPRA regarding prior consent versus consensus of all members.
5. Local government units have powers to negotiate financial grants but must consider national security implications.

**Recommendation:** Local officials should not accept benefits from the company in exchange for consent. They must ensure that all community members, including indigenous groups, are adequately represented and consulted according to IPRA s59.

**Policy references:** [PH-L07] Local Government Code (RA 7160) s41(c); [G-13] G-13: Policy gap (conflict_between_objectives); [PH-L07] Local Government Code of 1991 (RA 7160): Section 23; [PH-L07] Local Government Code of 1991 (RA 7160): Sections 35 and 36  
**Gaps or conflicts:** Indigenous representation is not guaranteed under RA 7160 s41(c).; There's a conflict between the Mining Act and IPRA regarding prior consent versus consensus of all members.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 32c94a3319076001…`

### legal_adviser (Policy and legal adviser)

**Saw:** evt-2, evt-6; board posts: 1  
**Retrieved:** G-01, G-13, IPRA (RA 8371) s16, PH-L07, PH-D04, K-PH05

**Reasoning:**
1. Company's actions violate IPRA s59, requiring NCIP certification for any issuance or renewal.
2. Local officials' involvement may complicate the dispute resolution process.
3. FPIC steps are pending and must be completed before any benefits can be offered.
4. The company's offer of benefits to representatives is a form of inducement, which could undermine consent processes.

**Recommendation:** Deny the company's offer of benefits and instruct local officials to respect customary processes.

**Policy references:** IPRA s59; NCIP AO 3, s.2026; UNDRIP Art. 32(2); G-01: Policy gap (conflict_between_objectives)  
**Gaps or conflicts:** Conflict between the Mining Act's prior consent and IPRA's consensus of all members.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, denr_mgb_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash ef9b6c79f95c90a4…`

**Expected:** No private ruling can waive FPIC or certification, which protect public policy; consent of all members free of manipulation; no renewal until both are complete.  
**Expected references found:** 3/4 (IPRA s3(g), IPRA s59, UNDRIP Art. 32(2))

## Controversy

Flagging the representatives' changed accounts may look like distrust of traditional leaders. Flags go only to the community council and NCIP, are never published, and never reject testimony on their own. Elders can explain the change, and the explanation is recorded.

## Summary

- Agent steps logged: 14
- Held by the policy gate: 1
- Expected policy references cited: 9/16
- Final hash: `ef9b6c79f95c90a478db06c10fde84ba46d43b24023020c671af80ff0e051aaa`
