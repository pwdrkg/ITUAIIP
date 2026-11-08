// Builds docs/technical-report.docx (max 5 pages, A4, template structure).
// Text follows the team's PDF "IKSP Record Pipeline - tech 5 pages" word for word.
// Run from repo root: node docs/build/technical_report.js
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, ImageRun, AlignmentType, LevelFormat, BorderStyle,
  ExternalHyperlink, Footer, PageNumber,
} = require("docx");

const FONT = "Calibri";
const BODY = 20;   // 10 pt
const SMALL = 16;  // 8 pt (tables)
const PAGE_W = 11906 - 2 * 907; // A4 minus 1.8 cm margins

// Inline markup: **bold**, _italic_
function runs(text, size = BODY, extra = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|_[^_]+_)/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), size, font: FONT, ...extra }));
    const t = m[0];
    if (t.startsWith("**")) out.push(new TextRun({ text: t.slice(2, -2), bold: true, size, font: FONT, ...extra }));
    else out.push(new TextRun({ text: t.slice(1, -1), italics: true, size, font: FONT, ...extra }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), size, font: FONT, ...extra }));
  return out;
}
const p = (text, opts = {}) => new Paragraph({ children: runs(text, opts.size || BODY), spacing: { after: opts.after ?? 60, line: 240 }, alignment: opts.align, keepNext: opts.keepNext });
const h1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: t, font: FONT })] });
const h2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: t, font: FONT })] });
const bullet = (t) => new Paragraph({ numbering: { reference: "bul", level: 0 }, children: runs(t), spacing: { after: 20, line: 240 } });
const num = (t, ref) => new Paragraph({ numbering: { reference: ref, level: 0 }, children: runs(t), spacing: { after: 20, line: 240 } });

const border = { style: BorderStyle.SINGLE, size: 4, color: "A6A6A6" };
const borders = { top: border, bottom: border, left: border, right: border };
function table(widthsPct, header, rows) {
  const widths = widthsPct.map((w) => Math.round((PAGE_W * w) / 100));
  widths[widths.length - 1] = PAGE_W - widths.slice(0, -1).reduce((a, b) => a + b, 0);
  const cell = (text, i, isHead) => new TableCell({
    borders, width: { size: widths[i], type: WidthType.DXA },
    shading: isHead ? { fill: "D9E2F3", type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: 10, bottom: 10, left: 60, right: 60 },
    children: [new Paragraph({ children: runs(text, SMALL, isHead ? { bold: true } : {}), spacing: { before: 0, after: 0, line: 228 } })],
  });
  return new Table({
    width: { size: PAGE_W, type: WidthType.DXA }, columnWidths: widths,
    rows: [
      new TableRow({ tableHeader: true, children: header.map((t, i) => cell(t, i, true)) }),
      ...rows.map((r) => new TableRow({ cantSplit: true, children: r.map((t, i) => cell(t, i, false)) })),
    ],
  });
}

const children = [];

// Title block
children.push(new Paragraph({ children: [new TextRun({ text: "AI for Good Sandbox Hackathon – IKSP Record Pipeline", bold: true, size: 30, font: FONT })], spacing: { after: 80 } }));
children.push(p("**Team leader:** Paul Alvarez", { after: 0 }));
children.push(p("**Team members:** Paul Alvarez", { after: 0 }));
children.push(p("**Contact details:** pevalvarez@gmail.com", { after: 0 }));
children.push(new Paragraph({ spacing: { after: 80 }, children: [
  new TextRun({ text: "Github link: ", bold: true, size: BODY, font: FONT }),
  new ExternalHyperlink({ link: "https://github.com/pwdrkg/ITUAIIP", children: [new TextRun({ text: "https://github.com/pwdrkg/ITUAIIP", style: "Hyperlink", size: BODY, font: FONT })] }),
] }));

// 1. Introduction
children.push(h1("1. Introduction"));
children.push(p("Indigenous knowledge systems and practices (IKSP) sustain how Indigenous communities in the Philippines farm, govern themselves and respond to hazards, and they can make public programmes better. But accounts recorded from a few voices, cut from their context or changed in translation can misrepresent communities in decisions that last. Communities have the right to control their knowledge (IPRA s32–s35)."));
children.push(p("We propose an AI pipeline for community-directed IKSP records. It records accounts from many knowledge holders in their own languages, reads written documents, cross-checks the accounts, flags one-sided ones for human review, and reads the result back so holders can correct it, with every correction logged. Records are released only for uses the community permits: a community archive, school materials, disaster and climate planning, ancestral domain recognition, or protection against appropriation. AI agents playing the government institutions involved test the pipeline against step-by-step error scenarios, and every decision is logged with its reasoning and the clause it relies on."));
children.push(p("The solution follows the ITU-T Y.3172 pipeline, reflects the ITU AI Readiness Framework 2.0, adheres to Philippine law, and maps each domain gap to a global policy example."));

// 2. Description of the use case
children.push(h1("2. Description of the use case"));
children.push(h2("2.1 Problem statement"));
children.push(p("Indigenous knowledge systems and practices (IKSP) inform how Indigenous Cultural Communities/Indigenous Peoples (ICCs/IPs) in the Philippines sustain their livelihoods and govern community relations. The Indigenous Peoples' Rights Act of 1997 recognises communities' rights over their knowledge and cultural heritage, including their authority to control its development and protection (RA 8371, s32–s35). These rights are the foundation for asking how documentation can support the continued use of IKSP and its contribution to public policy."));
children.push(p("Philippine research shows the range of these uses. In Tinoc, Ifugao, research on Kalanguya farming systems drew on community-selected knowledge holders and community validation to document practices in their ecological and cultural setting (Daguitan et al., 2016). Research on the Kalinga _bodong_ (peace pact) system shows Indigenous knowledge informing customary governance: Göransson (2022) examined how _bodong_ supported cooperation during the Chico River Dam struggle, when the proposed dams threatened settlements and livelihoods. IKSP is relevant to decisions about economic security."));
children.push(p("Appropriately documented IKSP can also benefit wider society through better-informed public programmes. The IPCC (2022) links inclusive planning informed by Indigenous knowledge to avoiding maladaptation, where climate responses unintentionally increase vulnerability. The Philippine Disaster Risk Reduction and Management Act requires disaster and climate measures to be \"sensitive to indigenous knowledge systems\" (RA 10121, s2(j)). Community-authorised documentation can support this by making relevant knowledge available for examination in its context; its public value depends on how that knowledge is interpreted and applied, with the participation of its holders."));
children.push(p("The continuity of this knowledge depends on conditions documentation alone cannot secure. In 2024 UNESCO's Intergovernmental Committee noted with concern the declining frequency of practice of Buklog, the Subanen thanksgiving ritual system, the reduced space associated with it, and growing difficulty gathering its materials (Decision 19.COM 6.A.4). Knowledge transmission depends on continued access to the places where practices happen."));
children.push(p("The World Bank (2024) identifies persistent information gaps that constrain poverty reduction and the targeting of services for Indigenous Peoples in the Philippines. For IKSP documentation, the stakes include how community knowledge is represented in decisions affecting land and livelihoods. Accounts detached from their context, or altered in translation, can become the basis for decisions that misrepresent communities' circumstances and priorities. Knowledge holders must therefore be able to examine how their accounts are represented and decide their permitted use."));
children.push(p("**Research problem.** Under what conditions can AI support community-directed documentation of IKSP that sustains knowledge transmission and gives a sound basis for authorised educational or policy use?"));
children.push(p("**Gaps in current practice:**", { after: 40, keepNext: true }));
[
  "Dispossession and environmental degradation threaten the conditions sustaining IKSP, while Indigenous language loss further weakens its continued practice and intergenerational transmission (WHO, 2026).",
  "Inadequate implementation of FPIC leaves IKSP vulnerable to appropriation and unauthorised reuse, undermining Indigenous Peoples' self-determination and cultural and intellectual rights (EMRIP, 2025; Ibrahim, 2026).",
  "External control over Indigenous data constrains communities' authority to determine how their knowledge is documented, interpreted and used, weakening Indigenous data sovereignty (EMRIP, 2025; Ibrahim, 2026).",
  "Structural discrimination and the digital divide restrict full and effective Indigenous participation, including that of women and youth. Systems that privilege dominant languages and knowledge frameworks further marginalise Indigenous perspectives and distort the representation of IKSP (EMRIP, 2025; Ibrahim, 2026).",
  "Insufficient investment in Indigenous-led information systems limits sustained documentation and community control. Incomplete ethnicity-disaggregated data and inconsistent collection methods compound these limitations, weakening the evidence available for equitable policy and programme design (World Bank, 2024; Ibrahim, 2026).",
].forEach((t) => children.push(bullet(t)));
children.push(p("**How our solution closes them:**", { after: 40, keepNext: true }));
[
  "**Select and record.** The community chooses its knowledge holders through its own process; we add many voices, including women, youth and members from each settlement. Each person speaks in a separate session, in their own language, after individual consent and the community's authorisation are recorded. Each teller names their own group (self-identification).",
  "**Read and translate.** A voice reader (speech-to-text) handles recordings; a text reader (OCR) handles written accounts, maps and genealogies. Originals are kept; terms that do not translate stay in the original language with a gloss; community translators check both.",
  "**Cross-check.** Extract places, practices, events and family lines, then link them across tellers and documents, with an agreement score for each account.",
  "**Check for bias.** Flag accounts given by only one teller, or only by representatives, for human review. Nothing is rejected automatically.",
  "**Read back and review.** Knowledge holders hear the summary and its translation, then confirm or correct it; every correction goes into a meaning-change log.",
  "**Release by permitted use.** The community sets each record's permitted use. Records leave the private store only for approved uses, such as a community archive, school materials, a local disaster plan, or an ancestral domain recognition dossier (demo output; a real filing needs sworn, signed statements).",
].forEach((t) => children.push(num(t, "steps")));
children.push(p("**Use cases.** A. Community archive and transmission (RA 11961 cultural mapping). B. Education (DepEd IPEd orders). C. Disaster and climate planning (RA 10121 s2(j)). D. Ancestral domain recognition (IPRA s52(d); only 22% of approved CADTs fully registered by early 2023). E. Protection against appropriation (IPOPHL–NCIP AO 1, s.2016). Scenarios test D and C."));
const img = fs.readFileSync(path.join(__dirname, "..", "architecture.png"));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 20 }, children: [new ImageRun({ type: "png", data: img, transformation: { width: 300, height: 249 }, altText: { title: "Figure 1", description: "Y.3172 pipeline with orchestrator, sandbox and audit log", name: "architecture" } })] }));
children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [new TextRun({ text: "Figure 1. Y.3172 pipeline with orchestrator, sandbox and audit log", italics: true, size: SMALL, font: FONT })] }));
children.push(p("The pipeline follows Y.3172 from source (SRC) to output (SINK). A voice reader and a text reader feed the same cross-checker, so written documents are checked against spoken accounts. The orchestrator (MLFO) runs the agents and scenarios, and every step writes to the audit log."));

// 3. Use case requirement
children.push(h1("3. Use case requirement"));
children.push(p("Each node of the pipeline is associated with requirements. Targets below are our design choices for the demo."));
[
  "**SRC (sources).** Knowledge holders chosen by the community, plus at least 20 tellers per topic, including women, youth and members from each settlement. Each teller self-identifies their group. Documents are linked where they exist (domain recognition needs at least one, s52(d)).",
  "**C (collector).** Recording works offline on a phone and uploads when there is signal, since about 37% of indigenous people live in geographically isolated and disadvantaged areas (GIDAs). Consent is explained in the teller's language before recording, given separately for each purpose, and can be withdrawn as easily as it was given (NPC Circular 2023-04).",
  "**PP (preprocessor).** Speech-to-text and OCR output is checked by community translators. Text is translated into Filipino and English, keeping the original.",
  "**M (models).** Every match and flag points to the exact tellers and documents behind it. Agents cite the clause they rely on.",
  "**P (policy).** Each teller marks parts of their story as controlled (tapu, restricted) or open (noa, shareable), following Te Mana Raraunga. Every use follows the record's permitted use and community consent, defined in IPRA s3(g) as the consensus of all members. A human can override any AI output.",
  "**D (distributor).** Private community data never enters the open knowledge base. Outputs go only to roles the community has approved.",
  "**SINK (outputs).** Every step is written to a tamper-evident audit log with sources and reasoning.",
].forEach((t) => children.push(bullet(t)));

// 4. Mapping
children.push(h1("4. Mapping with ITU-T Y.3172, Readiness 2.0 Report, and domain-specific policies"));
children.push(table([7, 28, 24, 41], ["", "Use case (public services: IKSP records)", "Readiness 2.0 Report", "Documents (policies, strategies, AI innovative regulations)"], [
  ["SRC", "Stories from many members; community documents; policy corpus", "Data/model marketplace; AI for inclusion", "IPRA s51, s52(d); Data Privacy Act (RA 10173) on consent; World Bank (2024) on self-identification"],
  ["C", "Web and phone recorder, offline-first; separate sessions", "Digital infrastructure; Human interface", "Data Privacy Act; NPC Circular 2023-04 on consent; NCIP AO 1 s.2012 on researching and documenting indigenous knowledge systems and practices (IKSP); National Cybersecurity Plan 2023–2028 (EO 58); World Bank (2024) on isolated areas"],
  ["PP", "Voice reader, text reader (OCR), translation, entity extraction; policy knowledge base built with the ITU reference code", "Contextualization and regional impact; Generated content marketplace", "NPC Advisory 2024-04 (accuracy, bias); IPRA s52(g) on translation into the native language"],
  ["M", "Story matcher, bias check, policy adviser and institutional agents", "Cross-domain correlation analysis; Level of integration of AI in workflows", "NPC Advisory 2024-04; Delgamuukw (Canada) on oral evidence; EU AI Act Art. 14"],
  ["P", "Consent, controlled (tapu) or open (noa) marks, permitted use per record, human review and override", "AI and policies; Collaboration with AI; Impacts of humans in AI integration", "IPRA s3(g), s34; CARE Principles; Te Mana Raraunga; EU AI Act Art. 14"],
  ["D", "Routes outputs by role and consent; keeps private data out of the open knowledge base", "Strategy alignment", "IPRA s34 and s45; NPC Advisory 2024-04; National AI Strategy Roadmap 2.0"],
  ["SINK", "Consensus read-back, sample dossier, multi-agent simulation with a simulated timeline", "AI and policies (policy sandbox); Granular priorities", "IPRA s52(d), s52(k), s54, s59, s62; NCIP AO 4 s.2012 (delineation); Mining Act s16; UNDRIP Art. 32(2)"],
]));
children.push(p("Country documents also mapped: Mining Act (economic), IP Code (intellectual property), UNDRIP and the Convention on Biological Diversity (treaties), and World Bank (2024) data on labour and isolated areas. Full mapping and Readiness perspectives are in the full report.", { after: 60 }));
children.push(p("**ITU AI Readiness perspectives.**", { after: 40, keepNext: true }));
children.push(table([34, 66], ["Perspective", "How we address it"], [
  ["Open data and open source", "Open knowledge base built with the ITU reference code; community data stays private"],
  ["Generative AI content ecosystem", "Read-back story and IKSP summaries, always confirmed by the knowledge holders; original language kept"],
  ["Contextualization and regional focus", "Local languages (222 indigenous groups and 110 languages in NCIP's database) and customary law"],
  ["AI integration and cross-domain analysis", "Land, data protection, environment and mining, local government, disaster planning"],
  ["Human interaction and supervision", "Human review and override at the policy gate"],
  ["Policy and implementation opportunities", "Gap table in Section 6"],
  ["AI for social inclusion", "Many voices: women, youth, remote members; self-identification"],
  ["Digital infrastructure and energy", "Offline recording on mobile, sync later"],
]));

children.push(p("**Knowledge base.** Built with the ITU reference code (docling parsing, 256-word chunks, nomic-embed-text, ChromaDB). It adds 127 sources in eight folders (Philippine laws, NCIP rules, data privacy, strategies, jurisprudence, context data, IKSP publications, global practice), 68 of them from the team's IKSP reference register; each chunk tagged with source, issuer, year and section numbers, plus 26 key clauses, 16 key figures, 17 policy gaps and 5 gaps in current practice stored one per chunk for exact citation. A 38-question retrieval test must return the expected source in the top five. Community stories stay in a separate private store and are never published."));

// 5. Error scenarios
children.push(h1("5. Error scenarios"));
children.push(p("**Agents:** story agent, NCIP regional FPIC team, NCIP Commission en banc, DENR–MGB regional office (mining agreements and renewals), National Privacy Commission, local government and a legal adviser. The main script tests use case D; a policy reuse request tests use case C. The orchestrator releases events one at a time over 40 simulated days, each only to the agents that would receive it in real life."));
children.push(table([22, 22, 56], ["Agent", "Role", "Mandate"], [
  ["Story agent", "Application", "Household register, matching, bias check, read-back, dossier"],
  ["NCIP FPIC team agent", "Regional FPIC team", "Runs FPIC under the customary decision process; keeps the household register and consent count"],
  ["NCIP en banc agent", "Commission en banc", "Certification Precondition (s59), appeals, review of consent records; not a party to company arbitrations"],
  ["DENR–MGB agent", "Mining regulator (regional office)", "Mining agreements and renewals as contracting authority; must have NCIP certification first; geohazard and flood maps"],
  ["NPC agent", "Data protection", "Consent, data privacy, breach response"],
  ["LGU agent", "Local government", "Local records, zoning, local cybersecurity plan, local disaster risk reduction office"],
  ["Legal adviser", "Policy adviser", "Law, case law, gaps, global examples; labels non-binding guidance as a benchmark"],
]));
children.push(p("Each agent sees only the events routed to it and retrieves only from the knowledge-base folders its mandate allows; assessments are posted to a shared board, and conflicts escalate to human review.", { after: 60 }));
children.push(p("**Scenario 1: a mining agreement renewal inside an ancestral domain (use case D), released over 40 simulated days.**", { after: 40, keepNext: true }));
[
  "**Step-1 (day 0):** A mining company asks to renew its 25-year agreement, which covers part of an Indigenous community's ancestral domain, on the original terms. _Released to:_ DENR–MGB. _Expected:_ endorse to NCIP for FPIC and the Certification Precondition (IPRA s59) first. Test: does DENR–MGB ask NCIP?",
  "**Step-2 (day 5):** The company argues FPIC cannot apply because the agreement predates IPRA, and files for arbitration. _Released to:_ DENR–MGB, Legal adviser. _Expected:_ renewal depends on the law in force, and s59 covers renewals; DENR–MGB alerts NCIP, which is not a party. Test: does NCIP hear of it?",
  "**Step-3 (day 15):** NCIP's FPIC team opens FPIC; household representatives and elders are recorded separately, and most place the mine inside the domain. _Released to:_ NCIP FPIC team, Story agent. _Expected:_ household register and overlap map from matched accounts; customary decision process (s3(g); NCIP AO 3, s.2012).",
  "**Step-4 (day 25):** The arbitrators rule that FPIC and certification cannot be imposed and treat the agreement as renewed. _Released to:_ DENR–MGB. _Expected:_ share the ruling with NCIP and the legal adviser, hold the renewal while FPIC is pending, and ask a court to set it aside on public-policy grounds. Test: is the ruling shared?",
  "**Step-5 (day 30):** Two appointed representatives now say the community consented years ago. _Released to:_ Story agent. _Expected:_ bias check flags a change made only by representatives; human review checks it against the recorded consent of all households; nothing changes automatically.",
  "**Step-6 (day 40):** Escalation: the company offers benefits through those representatives in exchange for consent, and local officials ask to join the dispute. _Released to:_ All agents. _Expected:_ Legal adviser: no private ruling can waive FPIC or certification, which protect public policy; consent is the consensus of all members, free of manipulation (s3(g)); Mining Act s16; UNDRIP Art. 32(2). No renewal until both are complete (s59).",
].forEach((t) => children.push(num(t, "scen")));
children.push(p("In Scenario 1, step 6 turns a renewal dispute into a consent and ethics breach."));
children.push(p("**Scenario 2: flood stories versus the official hazard map (use case C).** The municipal disaster risk reduction office asks to use recorded flood stories to update its hazard map. The stories disagree with the official flood-susceptibility map in both directions: some places residents saw flooded are missing from the map, while elsewhere they describe a smaller flood-prone area than the map shows. _Expected handling:_ only records approved for policy use are shared, with context and the original language kept (NCIP AO 1, s.2012; community FPIC). The agent neither discards the stories because they conflict with the official map nor redraws hazard boundaries from them: it keeps both sources, flags each discrepancy and refers it to DENR–MGB and the knowledge holders for joint validation. The request, discrepancies and decisions are logged. This tests RA 10121 s2(j) against community control (IPRA s32–s35)."));
children.push(p("In both scenarios, corrective actions follow rules agreed before the simulation, not ad hoc choices. Every agent step is written to a hash-chained audit log with the sources, reasoning steps and clauses it relied on. Each entry records the simulated day and step, the agent and its mandate, the information it had seen, retrieved sources, reasoning steps, policy references, recommendation, confidence, human review outcome, and the previous entry\'s hash, so any later change breaks the chain."));
children.push(p("**Where it gets controversial.** In Scenario 1, flagging the representatives' changed accounts may look like distrust of traditional leaders. The response: flags go only to the community council and NCIP, are never published, and never reject testimony on their own. Elders can explain the change, and that explanation is recorded. In Scenario 2, community stories that contradict an official hazard map may look like a challenge to DENR–MGB's technical authority, or the official map may be used to dismiss residents' experience. The response: neither source overrides the other; discrepancies go to joint validation, DENR–MGB keeps authority over the technical map, and knowledge holders decide how their accounts are used."));

// 6. Gaps
children.push(h1("6. Policy gaps and standards gaps derived from the mapping exercise"));
children.push(table([42, 18, 40], ["Gap", "Type", "Global example"], [
  ["IPRA sets no minimum number or mix of tellers (s52(d))", "Legislative", "Canada, Delgamuukw (1997): oral history treated as equal to other evidence"],
  ["No rules for AI-processed evidence", "Standards", "EU AI Act Art. 14: humans can monitor and override high-risk AI (Annex III from 2 December 2027)"],
  ["No shared live register of pending CADT applications for DENR to check (s59)", "Unclear responsibility; coordination", "Australia: public, mapped Register of Native Title Claims"],
  ["Only 55 of 257 approved CADTs registered by early 2023 (World Bank, 2024)", "Coordination", "Australia's shared claims register"],
  ["National income, labour, poverty and health surveys have no ethnicity questions (World Bank, 2024)", "Data", "World Bank (2024): standard ethnicity variables, self-identification, FPIC in local languages"],
  ["Only NCIP has a mandate for indigenous data; efforts are uncoordinated (World Bank, 2024)", "Unclear responsibility", "CARE Principles"],
  ["Public NCIP research data (s45) versus community control of knowledge (s34)", "Conflict between objectives", "CARE Principles; Canada's OCAP®"],
  ["Recording sacred knowledge", "Standards", "New Zealand, Te Mana Raraunga: Māori decide which data are controlled (tapu) or open (noa); Philippines (local practice): Kalinga Digital Arang (2026) limits unauthorised AI training"],
  ["Mining Act \"prior consent\" (s16) versus IPRA consensus of all members (s3(g))", "Conflict between objectives", "UNDRIP Art. 32(2)"],
  ["Traditional knowledge in stories could be patented by others", "Legislative", "WIPO Treaty on IP, Genetic Resources and Associated Traditional Knowledge (2024; not yet in force)"],
  ["No structured way to compare evidence in boundary disputes (s62)", "Coordination", "Australia, Native Title Act: court-managed mediation; overlapping claims heard together (s67)"],
  ["IPRA s16 requires indigenous representation in local councils; the Local Government Code s41(c) makes it only one option for a sectoral seat", "Conflict between objectives", "Kenya, Community Land Act 2016: land decisions by an assembly of all adult members"],
  ["37% of indigenous people live in isolated areas (World Bank, 2024)", "Technology", "Offline-first design"],
  ["RA 10121 s2(j) requires sensitivity to indigenous knowledge but no process to document, validate or authorise IKSP for disaster plans", "Coordination; standards", "IPCC AR6 WGII (2022): inclusive planning with Indigenous knowledge helps avoid maladaptation"],
]));
children.push(p("Gaps on tellers, the register of pending applications, sacred content, boundary disputes and local representation are our reading of the law, not findings of a court or agency. IPRA s54 lets NCIP review and cancel fraudulently acquired titles on the community's written request; our bias check can support such reviews.", { after: 60 }));
children.push(p("**Sources:** World Bank (2024); IPRA; NPC Advisory 2024-04; ITU reference code. Global example sources are listed in the full report."));
children.push(h1("References"));
[
  "Daguitan, F., Batang-ay, M. J. C., Aquino, R. B., & Das-ilen, G. (2016). Mobilizing indigenous knowledge, innovations and practices of the Kalanguyas farming systems in Tinoc, Ifugao, the Philippines.",
  "EMRIP (2025). Indigenous Peoples' right to data (A/HRC/60/66). UN Expert Mechanism on the Rights of Indigenous Peoples.",
  "Göransson, M. B. (2022). Peace pacts and contentious politics: The Chico River Dam struggle in the Philippines, 1974–82. Journal of Southeast Asian Studies, 53(4).",
  "Ibrahim, H. O. (2026). Indigenous Peoples and artificial intelligence (E/C.19/2026/4). UN Permanent Forum on Indigenous Issues, 25th session.",
  "IPCC (2022). Climate Change 2022: Impacts, Adaptation and Vulnerability (AR6 WGII).",
  "ITU-T (2019). Recommendation Y.3172: Architectural framework for machine learning in future networks including IMT-2020. ITU AI Readiness Framework 2.0.",
  "Republic Act 8371 (1997), Indigenous Peoples' Rights Act; Republic Act 10121 (2010), Philippine Disaster Risk Reduction and Management Act, s2(j).",
  "UNESCO (2024). Decision 19.COM 6.A.4 (Buklog, thanksgiving ritual system of the Subanen).",
  "WHO (2026). Global Plan of Action for the Health of Indigenous Peoples (2027–2040), draft.",
  "World Bank (2024). No Data, No Story: Indigenous Peoples in the Philippines.",
].forEach((t) => children.push(new Paragraph({ children: runs(t, SMALL), spacing: { after: 20 }, indent: { left: 280, hanging: 280 } })));

const doc = new Document({
  creator: "Paul Alvarez",
  title: "AI for Good Sandbox Hackathon – IKSP Record Pipeline",
  styles: {
    default: { document: { run: { font: FONT, size: BODY } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: FONT, size: 26, bold: true, color: "1F3864" }, paragraph: { spacing: { before: 100, after: 40 }, keepNext: true, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: FONT, size: 21, bold: true, color: "1F3864" }, paragraph: { spacing: { before: 60, after: 40 }, keepNext: true, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [
    { reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 220 } } } }] },
    { reference: "steps", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } } } }] },
    { reference: "scen", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } } } }] },
  ] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 907, bottom: 907, left: 907, right: 907, header: 500, footer: 500 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: ["Page ", PageNumber.CURRENT], size: 16, font: FONT })] })] }) },
    children,
  }],
});
const out = process.argv[2] || path.join(__dirname, "..", "technical-report.docx");
Packer.toBuffer(doc).then((b) => { fs.writeFileSync(out, b); console.log("wrote", out); });
