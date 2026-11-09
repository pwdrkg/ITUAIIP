# Scenario: Mining agreement renewal inside an ancestral domain

Use case D. Model: `qwen2.5:7b`. Run 2026-11-09T17:03:40+00:00. Every entry below is in `audit_log.jsonl` with its hash.

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
1. The mining company seeks renewal, which requires prior consent from the indigenous community.
2. IPRA s59 mandates NCIP certification before issuing or renewing any concession without FPIC consensus.
3. Renewal must respect customary law and ensure free and informed consent of all members (IPRA s3(g)).
4. The Mining Act allows for renewal under similar terms, but does not override IPRA's requirement for community consent.

**Recommendation:** The renewal request cannot be processed without NCIP certification and FPIC from the indigenous community.

**Policy references:** [PH-L02] Mining Act (RA 7942) s16; [PH-L02] Mining Act (RA 7942) s32; [PH-J01] Cruz v. Secretary of Environment and Natural Resources, G.R. No. 135385; [PH-L01] IPRA (RA 8371) s59  
**Gaps or conflicts:** There is a potential conflict between the Mining Act's requirement for prior consent and IPRA's definition of free and informed consent as consensus among all community members.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash a22e997d3371d9d3…`

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
3. Precedent in Republic v. Lepanto Consolidated Mining Co.
4. Mining agreement predates IPRA but must comply with current law

**Recommendation:** The company cannot renew its mining agreement without obtaining NCIP certification and FPIC from the affected community.

**Policy references:** IPRA s59; Republic v. Lepanto Consolidated Mining Co., G.R. Nos. 244063 and 244216 (2022)  
**Gaps or conflicts:** -  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** high · **Human review:** pending (routine)  
`entry_hash b72351ac304ff58a…`

### legal_adviser (Policy and legal adviser)

**Saw:** evt-2; board posts: 1  
**Retrieved:** Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), IPRA (RA 8371) s3(g), , K-CD02, K-CD01, K-PH05

**Reasoning:**
1. The company's argument is based on pre-IPRA agreements.
2. IPRA s59 mandates NCIP certification and FPIC for renewals.
3. FPIC cannot be waived or bypassed due to the agreement’s age.
4. Arbitration does not override legal requirements.

**Recommendation:** The company must obtain the necessary FPIC from the affected community and NCIP certification before renewing its mining agreement.

**Policy references:** IPRA s3(g); IPRA s59; [K-CD02] Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022); [K-PH05] NCIP AO 3, s. 2026  
**Gaps or conflicts:** The absence of the full text and transition rules for NCIP AO 3, s.2026 creates uncertainty.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, denr_mgb_agent · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash 1d5a2d650a424f64…`

**Expected:** Renewal depends on the law in force, and s59 covers renewals; DENR-MGB alerts NCIP, which is not a party.  
**Expected references found:** 2/2 (IPRA s3(g), IPRA s59)

## Day 45 - evt-3

> NCIP's FPIC team opens FPIC; household representatives and elders are recorded separately, and most place the mine inside the domain.

Released to: ncip_fpic_team_agent, story_agent

### ncip_fpic_team_agent (NCIP regional FPIC team)

**Saw:** evt-3; board posts: 3  
**Retrieved:** , Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012, and its implementing memorandum circular, PH-C01, PH-N02, K-PH05

**Reasoning:**
1. NCIP's FPIC team has opened the process with representatives and elders recorded separately.
2. Most household representatives placed the mine inside their domain.
3. The company cannot renew its mining agreement without NCIP certification and FPIC from the community (denr_mgb_agent).
4. The 2012 guidelines on FPIC procedures are not assumed to still control due to policy gaps.
5. The 2026 Guidelines on FPIC and Related Processes need to be applied, as they provide detailed steps for conducting FPIC.

**Recommendation:** Proceed with the FPIC process according to the 2026 guidelines, ensuring meaningful participation of community members.

**Policy references:** IPRA s59; [K-PH05] NCIP AO 3, s. 2026 — The 2026 Guidelines on FPIC and Related Processes  
**Gaps or conflicts:** Unclear responsibilities in FPIC procedures during transition.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 00db818391c17342…`

### story_agent (Application)

**Saw:** evt-3; board posts: 0  
**Pipeline tools:** [household_register_and_bias_check] Household register: 12 accounts recorded separately (2 elder, 10 household_representative). 10 of 12 place the mine inside the ancestral domain. Claims on consent: 'no consent given': 12. No claim rests only on representatives.  
**Retrieved:** G-09, K-IN17, , PH-N02, K-PH05

**Reasoning:**
1. NCIP's FPIC team has recorded household representatives and elders separately.
2. Most place the mine inside the domain, indicating consent.
3. No shared register of pending claims exists, creating a policy gap.
4. The 2012 guidelines on FPIC are referenced but not the 2026 ones, which may have updated procedures.

**Recommendation:** Establish a shared register of pending claims to ensure transparency and compliance with IPRA s59.

**Policy references:** IPRA s59; NCIP AO No. 3, s. 2012; NCIP AO 3, s. 2026  
**Gaps or conflicts:** No shared, live register of pending claims exists.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash dae84a0792e902ea…`

**Expected:** Household register and overlap map from matched accounts; customary decision process.  
**Expected references found:** 0/3 (none)

## Day 75 - evt-4

> The arbitrators rule that FPIC and certification cannot be imposed and treat the agreement as renewed.

Released to: denr_mgb_agent

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-1, evt-2, evt-4; board posts: 1  
**Retrieved:** Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), IPRA (RA 8371) s59, G-09, K-CD02, PH-N02

**Reasoning:**
1. The agreement predates IPRA but must still comply with current laws.
2. FPIC and NCIP certification are mandatory for renewals under IPRA s59.
3. Arbitrators' decision cannot override legal requirements.
4. Recommendation should align with legal obligations.

**Recommendation:** The mining agreement cannot be renewed without obtaining the necessary FPIC from the affected community and NCIP certification.

**Policy references:** IPRA s59; [K-CD02] Lone Congressional District of Benguet Province v. Lepanto Consolidated Mining Co.; Republic v. Lepanto Consolidated Mining Co., G.R. Nos. 244063 and 244216  
**Gaps or conflicts:** The decision to treat the agreement as renewed without FPIC and NCIP certification conflicts with legal requirements.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash c756c2fd6163497c…`

**Expected:** Share the ruling with NCIP and the legal adviser, hold the renewal while FPIC is pending, and ask a court to set it aside on public-policy grounds.  
**Expected references found:** 1/2 (IPRA s59)

## Day 105 - evt-5

> Two appointed representatives now say the community consented years ago.

Released to: story_agent

### story_agent (Application)

**Saw:** evt-3, evt-5; board posts: 1  
**Pipeline tools:** [household_register_and_bias_check] Household register: 14 accounts recorded separately (2 appointed_representative, 2 elder, 10 household_representative). 10 of 14 place the mine inside the ancestral domain. Claims on consent: 'no consent given': 12; 'the community consented years ago': 2. BIAS FLAG: the claim 'the community consented years ago' is supported only by appointed representatives (R01, R02) and contradicts 12 household and elder accounts. Send to human review with the community; do not change the record.  
**Retrieved:** Kenya Community Land Act 2016, s15, IPRA (RA 8371) s16, NPC Circular No. 2023-04 (Guidelines on Consent, 7 November 2023), PH-N02, K-PH05

**Reasoning:**
1. The community's consent is a requirement.
2. Evidence shows only two representatives claim past consent, contradicting most accounts.
3. NCIP guidelines require meaningful participation; appointed reps alone cannot override majority.
4. Gaps exist in the process regarding validation and documentation.

**Recommendation:** Conduct a community assembly to validate the consent of all members according to IPRA and NCIP guidelines.

**Policy references:** IPRA s16; [PH-N02] NCIP AO No. 3, s. 2012; [K-PH05] NCIP AO 3, s. 2026  
**Gaps or conflicts:** The claim 'the community consented years ago' is supported only by appointed representatives and contradicts most household accounts.; There are no recent records of a community assembly to validate the current state of consent.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash dce12590a7b1cc14…`

**Expected:** Bias check flags a change made only by representatives; human review checks it against the recorded consent of all households; nothing changes automatically.  
**Expected references found:** 0/3 (none)

## Day 120 - evt-6

> The company offers benefits through those representatives in exchange for consent, and local officials ask to join the dispute.

Released to: story_agent, ncip_fpic_team_agent, ncip_en_banc_agent, denr_mgb_agent, npc_agent, lgu_agent, legal_adviser

### story_agent (Application)

**Saw:** evt-3, evt-5, evt-6; board posts: 1  
**Retrieved:** G-01, IPRA (RA 8371) s16, G-13, PH-L07, PH-D04, K-PH05, PH-L01

**Reasoning:**
1. Company offers benefits in exchange for consent; this violates IPRA s16.
2. Local officials joining dispute raises concerns about impartiality and conflict of interest, per NCIP AO 3, s2026.
3. Need to ensure community consensus through FPIC process as mandated by IPRA s59.
4. Benefits offered by company should be negotiated within the framework of customary law and IPRA guidelines.

**Recommendation:** Reject the company's offer to provide benefits in exchange for consent. Initiate a separate mediation process with local officials to ensure their impartiality and avoid conflict of interest.

**Policy references:** IPRA s16; NCIP AO 3, s2026; IPRA s59  
**Gaps or conflicts:** Conflict between the Mining Act's requirement for prior consent and IPRA's definition of consensus as required by customary law.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 062867503eae3c4c…`

### ncip_fpic_team_agent (NCIP regional FPIC team)

**Saw:** evt-3, evt-6; board posts: 7  
**Retrieved:** IPRA (RA 8371) s66, Republic v. Lepanto Consolidated Mining, G.R. Nos. 244063 and 244216 (2022), , PH-N02, K-PH05

**Reasoning:**
1. Company offers benefits
2. Local officials join dispute
3. NCIP mandate
4. Conflict of interest

**Recommendation:** Reject the company's offer to provide benefits in exchange for consent. Initiate a separate mediation process with local officials to ensure their impartiality and avoid conflict of interest.

**Policy references:** IPRA s66; [PH-L01] IPRA (RA 8371) s66; [K-PH05] NCIP AO 3, s. 2026 — The 2026 Guidelines on FPIC and Related Processes  
**Gaps or conflicts:** Unclear FPIC procedures in transition  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, story_agent · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash bce8967b40ec1743…`

### ncip_en_banc_agent (NCIP Commission en banc)

**Saw:** evt-6; board posts: 2  
**Retrieved:** IPRA (RA 8371) s66, IPRA (RA 8371) s62, Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012, and its implementing memorandum circular, K-PH05, K-PH27, PH-J01, PH-J02, PH-N01

**Reasoning:**
1. The company's offer of benefits in exchange for consent is a form of undue influence, which violates IPRA s59.
2. Local officials asking to join the dispute suggests an overlap with their jurisdiction, but NCIP has primary jurisdiction over ICC/IP disputes under IPRA s62 and s66.
3. The FPIC process must be completed according to 2026 guidelines, ensuring meaningful participation of community members (NCIP AO 3, s. 2026).
4. Disputes involving non-IPs should be resolved through NCIP administrative procedures as per NCIP AO 3, s. 2026.

**Recommendation:** Reject the company's offer of benefits and advise local officials to respect NCIP jurisdiction.

**Policy references:** IPRA s59; IPRA s62; IPRA s66; NCIP AO 3, s. 2026  
**Gaps or conflicts:** The company's offer of benefits may constitute undue influence, which is not addressed in the current guidelines.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash c211dd2a731c225e…`

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-1, evt-2, evt-4, evt-6; board posts: 1  
**Retrieved:** G-01, UNDRIP Art. 32(2), IPRA (RA 8371) s62, K-CD05, PH-L02, K-CD02

**Reasoning:**
1. The company is offering benefits to representatives in exchange for consent.
2. Local officials are asking to join the dispute, indicating potential boundary or interest conflicts.
3. FPIC and NCIP certification are required before any mining agreement can be renewed (IPRA s59).
4. Offering benefits in exchange for consent may violate the principle of free and informed consent under IPRA and UNDRIP.
5. Local officials joining the dispute suggests a boundary or interest conflict that needs resolution.

**Recommendation:** Do not approve the renewal or consent to any benefits in exchange for consent.

**Policy references:** IPRA s59; UNDRIP Art. 32(2); [PH-L01] G-01: Policy gap (conflict_between_objectives): Mining Act prior consent versus IPRA consensus of all members.; [K-CD05] Didipio Earth-Savers' Multi-Purpose Association, Inc. v. Gozun; Philippine Mining Act of 1995 (RA 7942) SEC. 78 and SEC. 79  
**Gaps or conflicts:** The conflict between the Mining Act's requirement for prior consent and IPRA's definition of free and informed consent.; Potential boundary disputes that need resolution through customary processes.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser, denr_mgb_agent · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash bcadcd2ed5e06b82…`

### npc_agent (Data protection (National Privacy Commission))

**Saw:** evt-6; board posts: 0  
**Retrieved:** K-IN17, NPC Advisory No. 2024-04 (19 December 2024), G-01, PH-D02, PH-D01, PH-D04

**Reasoning:**
1. Company offers benefits in exchange for consent, raising concerns about undue influence.
2. Local officials ask to join dispute, potentially affecting community consensus.
3. Need to ensure individual and collective consent aligns with IPRA and Data Privacy Act.

**Recommendation:** The company should not offer benefits in exchange for consent. Local officials should be informed that their participation may affect the community's consensus and should seek a formal FPIC process.

**Policy references:** IPRA s3(g); IPRA s59; Data Privacy Act of 2012 (RA 10173) §3(g); Data Privacy Act of 2012 (RA 10173) §18(a)  
**Gaps or conflicts:** Standards for combining individual consent and collective community authorisation in digital contexts are unclear.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 34771d02c74924bc…`

### lgu_agent (Local government unit)

**Saw:** evt-6; board posts: 0  
**Retrieved:** Local Government Code (RA 7160) s41(c), G-13, G-01, PH-L07

**Reasoning:**
1. Local officials are asked to join a dispute with the company.
2. The company offers benefits in exchange for consent, which may influence local officials' decisions.
3. Indigenous representation is not guaranteed under RA 7160 s41(c).
4. There's a conflict between the Mining Act and IPRA regarding prior consent versus consensus of all members.
5. Local government units have powers to negotiate financial grants or donations, but national security implications require approval.

**Recommendation:** Local officials should not accept benefits from the company in exchange for consent. The offer may compromise their impartiality and violate RA 7160 s41(c) regarding sectoral representation, especially if indigenous communities are involved.

**Policy references:** [PH-L07] Local Government Code (RA 7160) s41(c); [G-13] G-13: Policy gap (conflict_between_objectives); [PH-L07] Local Government Code of 1991 (RA 7160): Section 23; [PH-L07] Local Government Code of 1991 (RA 7160): Sections 35 and 36  
**Gaps or conflicts:** Indigenous representation is not guaranteed under RA 7160 s41(c).; There's a conflict between the Mining Act and IPRA regarding prior consent versus consensus of all members.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash a020beb5c35ff530…`

### legal_adviser (Policy and legal adviser)

**Saw:** evt-2, evt-6; board posts: 9  
**Retrieved:** G-01, G-13, IPRA (RA 8371) s16, PH-L07, PH-D04, K-PH05

**Reasoning:**
1. Company's offer of benefits violates IPRA s59 and RA 7160 s41(c).
2. Local officials' participation may compromise impartiality.
3. FPIC process must be initiated according to NCIP AO 3, s.2026.
4. Conflict between Mining Act and IPRA requires resolution.

**Recommendation:** Reject the company's offer of benefits and initiate a separate mediation process with local officials to ensure their impartiality.

**Policy references:** IPRA s59; RA 7160 s41(c); NCIP AO 3, s.2026; G-01: Policy gap (conflict_between_objectives)  
**Gaps or conflicts:** Conflict between Mining Act and IPRA regarding prior consent vs. consensus of all members.  
**Policy gate:** passed  
**Notify:** ncip_fpic_team_agent, story_agent, denr_mgb_agent · **Confidence:** high · **Human review:** pending (flagged by agent)  
`entry_hash 4b25efec16bdbfd1…`

**Expected:** No private ruling can waive FPIC or certification, which protect public policy; consent of all members free of manipulation; no renewal until both are complete.  
**Expected references found:** 3/4 (IPRA s3(g), IPRA s59, UNDRIP Art. 32(2))

## Controversy

Flagging the representatives' changed accounts may look like distrust of traditional leaders. Flags go only to the community council and NCIP, are never published, and never reject testimony on their own. Elders can explain the change, and the explanation is recorded.

## Summary

- Agent steps logged: 14
- Held by the policy gate: 0
- Expected policy references cited: 8/16
- Final hash: `4b25efec16bdbfd1ff66e9bb9a2ea94a9e53d8bea98c05339bf4306a87b0a344`
