# Scenario: Flood stories versus the official hazard map

Use case C. Model: `qwen2.5:7b`. Run 2026-11-09T16:21:37+00:00. Every entry below is in `audit_log.jsonl` with its hash.

## Pre-agreed rules

- A record leaves the private store only for a use listed in its permitted-use field.
- Community FPIC is the consensus of all members under customary law (IPRA s3(g)).
- Controlled (tapu) parts of a story are never shared.
- Shared records keep their context and original language.
- Neither the official map nor community accounts are accepted or discarded automatically; discrepancies go to joint validation.
- Every request, discrepancy and decision is written to the audit log.

## Day 0 - evt-1

> The municipal disaster risk reduction office asks to use recorded flood stories to update its hazard map.

Released to: lgu_agent

### lgu_agent (Local government unit)

**Saw:** evt-1; board posts: 0  
**Retrieved:** K-CC06, K-CC11, G-19, K-CC08, PH-S03, PH-L10

**Reasoning:**
1. The LGU must validate community flood stories against official maps.
2. There is no established process for using IKSP in local disaster plans.
3. Community FPIC and consent are required before sharing controlled information.
4. Discrepancies between official and community accounts need joint validation.

**Recommendation:** The LGU should convene a meeting with the NCIP FPIC team to validate flood stories against official maps and ensure community consent before updating the hazard map.

**Policy references:** IPRA s3(g); RA 10121 s2(j); G-19; PH-L10  
**Gaps or conflicts:** No established process for using IKSP in local disaster plans.  
**Notify:** ncip_fpic_team_agent, lgu_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 10e98e8f097da866…`

**Expected:** LGU agent files a request naming the purpose (hazard map update), area and records sought; it does not access records directly.  
**Expected references found:** 1/1 (RA 10121 s2(j))

## Day 2 - evt-2

> Some matching records allow policy use; others allow only the community archive.

Released to: story_agent

### story_agent (Application)

**Saw:** evt-2; board posts: 0  
**Retrieved:** G-09, K-IN17, G-02, PH-L04, PH-D04

**Reasoning:**
1. Records have different permitted uses.
2. Community control vs public research data conflict exists.
3. Need for a shared live register of pending claims is implied.
4. Data consent and collective authorization do not clearly connect.

**Recommendation:** Establish a shared live register of pending claims and develop guidelines for combining individual data consent with collective community authorization in digital records.

**Policy references:** IPRA s59; K-IN17: Policy gap (standards); [PH-L04] Main Philippine Laws on Intellectual Property (incl. IP Code, RA 8293, as amended): person may obtain copies thereof at his own expense.; [G-09] G-09: Policy gap (unclear_responsibility)  
**Gaps or conflicts:** Unclear responsibility for maintaining a shared live register of pending claims.; Lack of clear guidelines on how individual data consent and collective community authorization combine in digital records.  
**Notify:** ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 29cb2a269b49b9cd…`

**Expected:** Story agent checks each record's permitted-use field; only records approved for policy use are eligible; controlled (tapu) parts excluded; context and original language kept.  
**Expected references found:** 0/2 (none)

## Day 5 - evt-3

> The approved stories disagree with the official flood-susceptibility map in both directions - some flooded places are missing from the map; elsewhere residents describe a smaller flood-prone area.

Released to: story_agent, denr_mgb_agent, lgu_agent

### story_agent (Application)

**Saw:** evt-2, evt-3; board posts: 0  
**Retrieved:** K-CC11, K-CC06, G-19, K-PU14

**Reasoning:**
1. Discrepancies between community stories and official maps indicate potential inaccuracies or outdated information.
2. Community knowledge is crucial for disaster risk reduction but needs validation through scientific means.
3. There's a policy gap in integrating indigenous knowledge systems (IKS) into official planning processes.
4. Recommendation should involve validating the community flood accounts against scientific data.

**Recommendation:** Conduct a joint validation of the community flood accounts with scientific data to reconcile discrepancies.

**Policy references:** IPRA s3(g): Community FPIC is the consensus of all members under customary law; RA 10121 s2(j): Requires disaster risk reduction and climate measures to be sensitive to indigenous knowledge systems, but names no process for documenting, validating or authorising IKSP for use in local disaster plans  
**Gaps or conflicts:** No clear process for using IKSP in disaster and climate planning as mandated by RA 10121 s2(j).  
**Notify:** ncip_fpic_team_agent, denr_mgb_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 47906451ae97ad84…`

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-3; board posts: 1  
**Retrieved:** K-CC11, K-CC06, G-09, PH-N07, PH-N09

**Reasoning:**
1. Discrepancies between community flood accounts and official maps exist.
2. Community flood accounts are valid but need validation with scientific data.
3. No shared, live register of pending claims is available for NCIP certification.
4. NCIP must validate survey plans to ensure no overlap with existing rights.

**Recommendation:** Conduct a joint validation of the community flood accounts with scientific data. Ensure NCIP validates survey plans for potential overlaps and update official maps accordingly.

**Policy references:** [K-CC11]; [K-CC06]; [PH-N07]  
**Gaps or conflicts:** No shared, live register of pending claims for NCIP certification.; Discrepancies between community flood accounts and official maps need resolution.  
**Notify:** story_agent, ncip_fpic_team_agent, legal_adviser · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 0d5fe902b5b01c52…`

### lgu_agent (Local government unit)

**Saw:** evt-1, evt-3; board posts: 2  
**Retrieved:** K-CC11, K-CC06, G-19, K-CC08, PH-S03, K-CC09

**Reasoning:**
1. Discrepancies between community stories and official map need validation
2. Joint validation process recommended by other agents
3. Need for updated flood susceptibility map based on validated data
4. Lack of standardized tools for local flood early warning systems

**Recommendation:** Conduct a joint validation of the community flood accounts with scientific data, as recommended by other agents. Update the official flood susceptibility map based on validated data.

**Policy references:** IPRA s59 (Community FPIC is the consensus of all members under customary law); RA 10121 s2(j) (Disaster risk reduction and climate measures to be sensitive to indigenous knowledge systems); G-19 (Coordination process for using IKSP in disaster and climate planning)  
**Gaps or conflicts:** Lack of standardized tools for local flood early warning systems; No clear process for using IKSP in disaster and climate planning as mandated by RA 10121 s2(j)  
**Notify:** story_agent, denr_mgb_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 32e6ce6dbc4e7f3f…`

**Expected:** Keep both sources; flag each discrepancy with the tellers and map layer behind it; do not discard the stories or redraw boundaries from them; refer to DENR-MGB and the knowledge holders for joint validation.  
**Expected references found:** 3/3 (K-CC06, K-CC11, RA 10121 s2(j))

## Day 10 - evt-4

> Joint validation confirms some discrepancies; the office asks for the full georeferenced archive to finish the map.

Released to: story_agent, ncip_fpic_team_agent, npc_agent, lgu_agent, denr_mgb_agent, legal_adviser

### story_agent (Application)

**Saw:** evt-2, evt-3, evt-4; board posts: 2  
**Retrieved:** PH-C07, G-09, PH-N09, PH-N03

**Reasoning:**
1. Discrepancies exist between community flood accounts and official maps.
2. Joint validation is required for accurate mapping.
3. NCIP's role in validating survey plans must be clarified.
4. There are gaps in the registration of approved titles.

**Recommendation:** The NCIP should lead the joint validation process with scientific data to reconcile discrepancies between community flood accounts and official maps. The DENR should update its official map based on validated data.

**Policy references:** IPRA s59; [PH-N09] NCIP AO 1, s. 2020 — Rules on delineation and titling of ancestral domains and lands: Section 11, 12, 38-40; [G-09]  
**Gaps or conflicts:** Unclear responsibility for registering approved titles.; Lack of a shared, live register of pending claims.  
**Notify:** ncip_fpic_team_agent, denr_mgb_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash f21fb781761f8f25…`

### ncip_fpic_team_agent (NCIP regional FPIC team)

**Saw:** evt-4; board posts: 1  
**Retrieved:** , Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012, and its implementing memorandum circular, PH-C01, K-PH05, PH-N02, K-CD03, K-CD01

**Reasoning:**
1. NCIP mandate for FPIC
2. Joint validation process required
3. Discrepancies need resolution
4. NCIP's role in map coordination

**Recommendation:** The NCIP FPIC team should lead the joint validation process to reconcile discrepancies between community flood accounts and official maps.

**Policy references:** IPRA s59; NCIP AO 3, s.2026 Section 28; [PH-N07] Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012; [PH-C01] PH-C01  
**Gaps or conflicts:** Unclear responsibility for map coordination in transition period; Need for coordinated funding and efforts  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent, denr_mgb_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash 2bc2170700af057f…`

### npc_agent (Data protection (National Privacy Commission))

**Saw:** evt-4; board posts: 2  
**Retrieved:** NPC Advisory No. 2024-04 (19 December 2024), K-IN17, IPRA (RA 8371) s52(h), PH-D04, PH-D02

**Reasoning:**
1. Joint validation process
2. NCIP leadership
3. Data subject rights
4. Discrepancies reconciliation

**Recommendation:** The NCIP should lead the joint validation process with scientific data to reconcile discrepancies between community flood accounts and official maps, ensuring that data subjects' rights are respected.

**Policy references:** [PH-D03]; [K-IN17]; [PH-L01]  
**Gaps or conflicts:** No clear guidance on combining individual consent with collective authorisation in digital contexts.  
**Notify:** ncip_fpic_team_agent, story_agent · **Confidence:** medium · **Human review:** pending (flagged by agent)  
`entry_hash c741461fc29ad88a…`

### lgu_agent (Local government unit)

**Saw:** evt-1, evt-3, evt-4; board posts: 5  
**Retrieved:** Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012, and its implementing memorandum circular, PH-C07, Local Government Code (RA 7160) s41(c), PH-L07, PH-L01

**Reasoning:**
1. The discrepancies between community flood accounts and official maps require joint validation.
2. NCIP should lead the process due to indigenous cultural communities' representation and data subject rights.
3. Validation must include scientific data for accuracy.
4. Full georeferenced archive is needed for comprehensive validation.

**Recommendation:** The NCIP should lead the joint validation process with scientific data to reconcile discrepancies between community flood accounts and official maps. The LGU should provide the full georeferenced archive for this purpose.

**Policy references:** PH-N07: Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012; PH-C07: A 2017 policy review by Dave de Vera of PAFID for ANGOC; PH-L07: Local Government Code (RA 7160) s41(c); [PH-L07] Indigenous Peoples' Rights Act of 1997 (RA 8371)  
**Gaps or conflicts:** -  
**Notify:** ncip_fpic_team_agent, denr_mgb_agent · **Confidence:** high · **Human review:** pending (routine)  
`entry_hash a4d190f0016becdc…`

### denr_mgb_agent (DENR Mines and Geosciences Bureau, regional office)

**Saw:** evt-3, evt-4; board posts: 6  
**Retrieved:** Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012, and its implementing memorandum circular, G-09, IPRA (RA 8371) s59, PH-N09, PH-N03

**Reasoning:**
1. Discrepancies need validation
2. NCIP leads joint validation
3. DENR requires NCIP certification
4. Full georeferenced archive needed for map update

**Recommendation:** The NCIP should lead the joint validation process to reconcile discrepancies between community flood accounts and official maps. The DENR should request the full georeferenced archive from LGU for updating its official map based on validated data.

**Policy references:** [PH-L01] IPRA (RA 8371) s59; [PH-N07] Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012; [G-09] G-09: Policy gap  
**Gaps or conflicts:** No shared live register of pending claims  
**Notify:** ncip_fpic_team_agent, lgu_agent · **Confidence:** high · **Human review:** pending (routine)  
`entry_hash 4db2451bb215a4a6…`

### legal_adviser (Policy and legal adviser)

**Saw:** evt-4; board posts: 5  
**Retrieved:** PH-C07, G-09, Joint DAR-DENR-LRA-NCIP Administrative Order No. 1, s. 2012, and its implementing memorandum circular, PH-N03, PH-N09

**Reasoning:**
1. NCIP leads validation
2. joint process required
3. data protection needed
4. FPIC crucial

**Recommendation:** The NCIP should lead the joint validation process with scientific data to reconcile discrepancies between community flood accounts and official maps. The LGU must provide the full georeferenced archive for this purpose.

**Policy references:** PH-N03; PH-N09; PH-C07; [PH-N07]  
**Gaps or conflicts:** -  
**Notify:** ncip_fpic_team_agent, ncip_en_banc_agent, denr_mgb_agent · **Confidence:** high · **Human review:** pending (routine)  
`entry_hash 09e4bf2e850aabe4…`

**Expected:** Share only an authorised extract for the requested purpose and area; no full archive without a new community decision; legal adviser maps the gap (no process under RA 10121 s2(j) to document, validate or authorise IKSP) to global examples; incorporation into the plan is recorded.  
**Expected references found:** 0/7 (none)

## Controversy

Community stories that contradict an official hazard map may look like a challenge to DENR-MGB's technical authority, or the official map may be used to dismiss residents' experience. Neither source overrides the other: discrepancies go to joint validation, DENR-MGB keeps authority over the technical map, and knowledge holders decide how their accounts are used.

## Summary

- Agent steps logged: 11
- Expected policy references cited: 4/13
- Final hash: `09e4bf2e850aabe4bd9a18fcc9ed3ff7974b74f6198d4feb2bb6037710327b05`
