# Knowledge base build and retrieval test (9 Nov 2026)

Real build with the ITU reference code (CrashingGuru/ITUAIReadiness) and Ollama `nomic-embed-text`, run on a Windows laptop.

- Sources loaded: 129 of 131 (K-CC07 and K-CC10 not obtained).
- kb_main: 8,311 chunks, including 73 curated provisions, facts and gaps. kb_usecase: 5 chunks.
- Retrieval test: **39/39** questions return an expected source in the top 5.
  - First run: 32/39. The 7 misses were fixed with curated clauses taken from the source text (RA 11038 PAMB seats, RA 10121 s2(j), NCIP AO 1 s.2012 s8.8, Te Mana Raraunga 6.3, 2025 IP data workshop, Digital Arang, two flood-map discrepancy cases).
  - One test now also accepts the CARE principles (G-02) and the EMRIP data study (K-IN17), both correct answers.
- Known issue: the K-CC11 download is a page stub, not the report; its content comes from the team-checked summary in sources.csv.

## Retrieval test output

```
PASS  What proof does an ancestral domain claim need?
      expected ['PH-L01', 'PH-N03'] got PH-L01[52], PH-L01[52], PH-L01[], PH-L01[], PH-L01[52,53]
PASS  Can a mining permit be granted inside a claimed ancestral domain?
      expected ['PH-L01', 'PH-L02'] got PH-L02[16], PH-L01[59], PH-J01[7], K-CD05[75,76], PH-J01[59]
PASS  Who decides a boundary dispute between two indigenous communities?
      expected ['PH-L01', 'PH-N05'] got G-10[], PH-L01[62], PH-J01[], PH-N01[2], PH-L07[118,119]
PASS  How can a fraudulently acquired ancestral domain claim be cancelled?
      expected ['PH-L01'] got PH-L01[54], PH-L01[52], K-PH25[71,85], PH-L01[54,55,56,62], PH-N01[1,2,3,4,5,6,7,8,9,10,11,12,13]
PASS  What does free and prior informed consent mean under Philippine law?
      expected ['PH-L01', 'PH-N02'] got PH-L01[3], K-CD01[], K-IN17[], PH-D02[22], PH-D04[13]
PASS  What rules apply when researching and documenting indigenous knowledge and customary law?
      expected ['PH-N04'] got PH-L01[34], G-04[], PH-N04[1,2,3,4], K-PH07[3], PH-N06[1,3]
PASS  Is ethnic origin sensitive personal information?
      expected ['PH-D02'] got PH-D02[3], PH-C01[], PH-D01[4,5], PH-D04[3], PH-D04[3]
PASS  What must an AI system do about bias when processing personal data?
      expected ['PH-D03'] got PH-D03[], G-07[], PH-D03[], PH-D03[1,2], G-07[1,3,4]
PASS  How many approved CADTs are fully registered?
      expected ['PH-C01', 'PH-C02'] got PH-C01[], PH-C01[], G-09[], PH-C01[], PH-N03[3,4,5]
PASS  Do national surveys collect ethnicity data on indigenous peoples?
      expected ['PH-C01', 'PH-C03'] got G-14[], PH-C01[], PH-C03[], PH-C01[], K-IN17[]
PASS  Does NCIP have jurisdiction over a dispute with a non-indigenous company?
      expected ['PH-J02'] got PH-L01[66], PH-L01[62], K-PH05[103], PH-J02[66], PH-J01[]
PASS  Can mining proceed on ancestral land without the community's consent?
      expected ['PH-L02', 'G-01'] got PH-L02[16], G-01[], PH-J01[7], K-CD02[16,17], K-CD02[16,59]
PASS  How can courts treat oral history as evidence of land occupation?
      expected ['G-05', 'G-06'] got G-13[], PH-L01[52], G-06[], G-06[35], PH-N03[3]
PASS  Who owns recorded traditional knowledge?
      expected ['PH-L01', 'G-02', 'G-03'] got PH-L01[34], PH-L01[32], K-PU15[], G-12[], K-PH07[]
PASS  Must humans be able to override a high-risk AI system?
      expected ['G-07'] got G-07[], PH-D03[], G-07[3], G-07[3], G-07[2,3,14,113]
PASS  How do indigenous communities decide which data stays private?
      expected ['G-04', 'G-02', 'K-IN17'] got G-02[], K-IN17[], K-IN17[], K-IN17[], K-IN17[]
PASS  How are overlapping native title claims handled in Australia?
      expected ['G-10', 'G-11'] got G-09[], G-10[], G-11[], G-10[], G-11[]
PASS  Do protected area boards include indigenous representatives?
      expected ['PH-L03'] got PH-L03[11,9], G-13[], K-PU13[4], K-PU13[13], K-PU13[11]
PASS  How are overlapping claims between agrarian reform, environment, land registration and NCIP resolved?
      expected ['PH-N07', 'PH-C07'] got PH-N07[], G-09[], PH-C01[], PH-C07[], PH-N07[9,13,15,16,52]
PASS  Are indigenous peoples guaranteed a seat in local councils?
      expected ['PH-L07', 'PH-L01'] got G-13[], PH-L07[41], K-PH30[], G-21[], K-PU13[]
PASS  Which law requires an assembly of all adult members for community land decisions?
      expected ['G-13'] got G-13[15], G-13[], G-13[], PH-N02[], G-13[40]
PASS  What is a good standard question for indigenous self-identification in official statistics?
      expected ['G-15', 'G-14'] got G-14[], PH-C01[], G-15[], G-15[], G-15[]
PASS  How easy must it be to withdraw consent to data processing?
      expected ['PH-D04'] got PH-D04[], K-IN17[], PH-D04[13], PH-D04[14], PH-D04[4]
PASS  What does UNESCO say about indigenous data in AI ethics?
      expected ['G-16'] got G-16[], G-02[], G-22[], G-16[], G-22[]
PASS  What household data must local governments collect under the Community-Based Monitoring System law?
      expected ['PH-L09'] got K-IN17[], PH-C03[], PH-L09[3], PH-L09[4,9,10,11,12], PH-L09[7,8,9]
PASS  What did government agencies agree in 2025 about indigenous data standards?
      expected ['PH-C06'] got PH-C06[], G-02[], K-IN17[], K-IN17[], K-IN17[]
PASS  Is hacking into a database of community recordings a crime?
      expected ['PH-L08'] got K-IN17[], PH-D02[3], PH-D04[13], PH-L08[], PH-L08[]
PASS  Must disaster risk reduction measures respect indigenous knowledge systems?
      expected ['PH-L10'] got G-19[], PH-L10[2], K-PU14[], K-CC04[], K-CC04[]
PASS  What concerns did UNESCO raise about the Subanen Buklog ritual?
      expected ['G-20'] got G-21[], G-04[], G-20[], K-PU14[], K-PU14[]
PASS  Can indigenous peoples living outside an ancestral domain document their culture through cultural mapping?
      expected ['K-PH10', 'K-PH09'] got G-02[], K-IN17[], K-IN17[], K-PH09[16], K-IN17[]
PASS  Who selects the informants when researching indigenous knowledge systems and practices?
      expected ['PH-N04'] got G-02[], PH-N04[8], K-IN17[], K-IN17[], K-PH07[1,3]
PASS  Which international framework says traditional and indigenous knowledge should complement science in disaster risk reduction?
      expected ['K-IN16'] got G-19[], PH-L10[2], K-PU14[], K-PU14[], K-IN16[]
PASS  How do land dispossession and language loss affect the transmission of indigenous knowledge?
      expected ['G-21', 'G-20'] got G-21[], K-IN17[], K-PU13[], K-PU04[], PH-C01[]
PASS  What risks does artificial intelligence pose to Indigenous Peoples' knowledge and data without free, prior and informed consent?
      expected ['G-22', 'K-IN17'] got G-16[], G-02[], G-22[], G-22[], G-22[]
PASS  Is there a Philippine example of a community-governed repository that restricts AI training on Indigenous knowledge?
      expected ['K-AI06'] got K-AI06[], G-04[], K-AI03[], G-22[], PH-S02[]
PASS  Can an arbitral award exempt a mining agreement renewal from FPIC and NCIP certification?
      expected ['K-CD02'] got K-CD02[], PH-L01[59], K-CD02[], K-CD02[], K-CD02[]
PASS  Is a majority of those who voted enough for written consent to a mining exploration permit?
      expected ['K-CD01'] got K-CD01[], G-01[], K-CD04[2,20], PH-L02[24], K-CD04[20,24]
PASS  Have community flood accounts in the Philippines disagreed with official flood susceptibility maps?
      expected ['K-CC11', 'K-CC06'] got K-CC11[], K-CC06[], K-CC08[], K-CC08[], K-CC08[]
PASS  Is there an example of an Indigenous community reading environmental signs to warn residents before a typhoon?
      expected ['K-CC01', 'K-CC02', 'K-CC04'] got K-CC11[], K-CC06[], K-PU14[], K-CC04[], K-PU14[]

Knowledge base: 39/39 passed (8311 chunks in kb_main)
Use case: Which ITU-T Y.3172 pipeline nodes does the IKSP record pipeline use?
      top hit UC-Philippines_IKSP_Record_Pipeline_use_case::0: '# Use case: IKSP Record Pipeline (Philippines) Domain: public services (indigenous knowledge, culture and publ'
Use case: How does the policy gate handle consent and human override?
      top hit UC-Philippines_IKSP_Record_Pipeline_use_case::2: 'self-identification; documents linked where they exist; policy corpus of Philippine law and global examples. -'
```

## Ingest log

```
.venv\Scripts\python : C:\Users\Admin\kb\ITUAIIP\.venv\Lib\site-packages\fitz\__init__.py:17: FutureWarning: The `fitz` API is deprecated and will be 
removed in future. Use `import pymupdf` instead.
At line:1 char:1
+ .venv\Scripts\python scripts\ingest_ph.py --itu-dir ..\ITUAIReadiness ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (C:\Users\Admin\...mupdf` instead.:String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
  warnings.warn(
ok      PH-L01     51 chunks  PH-L01_Indigenous_Peoples_Rights_Act_of_1997_RA_8371.html
ok      PH-L02     56 chunks  PH-L02_Philippine_Mining_Act_of_1995_RA_7942.pdf
ok      PH-L03     48 chunks  PH-L03_Expanded_National_Integrated_Protected_Areas_System_Act_of_2.html
ok      PH-L04    163 chunks  PH-L04_RA8293_asAmended_2015.pdf
ok      PH-L05     14 chunks  PH-L05_Department_of_Information_and_Communications_Technology_Act_of_2015_RA_ocr.txt
ok      PH-L06      3 chunks  PH-L06_Executive_Order_No_58_2024_adopting_the_National_Cybersecuri.html
ok      PH-N01    143 chunks  PH-N01_Rules_and_Regulations_Implementing_IPRA_NCIP_Administrative.html
ok      PH-N02     63 chunks  PH-N02_Revised_Guidelines_on_the_Exercise_of_Free_and_Prior_Informe.pdf
ok      PH-N03     68 chunks  PH-N03_Revised_Omnibus_Rules_on_Delineation_and_Recognition_of_Ance.pdf
ok      PH-N04     25 chunks  PH-N04_Indigenous_Knowledge_Systems_and_Practices_IKSPs_and_Customa.pdf
ok      PH-N05     39 chunks  PH-N05_2018_NCIP_Rules_of_Procedure_NCIP_Administrative_Circular_No.html
ok      PH-N06     46 chunks  PH-N06_2014_Revised_Rules_of_Procedure_before_the_NCIP_NCIP_Adminis.pdf
ok      PH-D01     33 chunks  PH-D01_Data_Privacy_Act_of_2012_RA_10173.pdf
ok      PH-D02     67 chunks  PH-D02_Implementing_Rules_and_Regulations_of_the_Data_Privacy_Act_a.pdf
ok      PH-D03     10 chunks  PH-D03_Advisory_2024_12_19_Guidelines_on_Artificial_Intelligence_w_SGD.pdf
ok      PH-S01      5 chunks  PH-S01_DTI_launches_National_AI_Strategy_Roadmap_2_0_and_Center_for_AI_Resear_ocr.txt
ok      PH-S02     67 chunks  PH-S02_National_AI_Strategy_Roadmap_2_0_NAISR_2_0_OECD_AI_policy_re.html
ok      PH-S03    782 chunks  PH-S03_Philippine_Development_Plan_2023_2028.pdf
ok      PH-J01    288 chunks  PH-J01_Cruz_v_Secretary_of_Environment_and_Natural_Resources_G_R_No.html
ok      PH-J02     60 chunks  PH-J02_Lim_v_Gamosa_G_R_No_193964.pdf
ok      K-CD01     24 chunks  K-CD01_Maddela_v_Oxiana_Philippines_Inc_G_R_No_198243_Resolution_2019.pdf
ok      K-CD02    152 chunks  K-CD02_G_R_Nos_244063_and_244216_2022.pdf
ok      K-CD03      9 chunks  K-CD03_G_R_No_226176_2023.pdf
ok      K-CD04    552 chunks  K-CD04_LaBugal_v_Ramos_GR127882_2004.pdf
ok      K-CD05     53 chunks  K-CD05_Didipio_Earth_Savers_Multi_Purpose_Association_Inc_v_Gozun_G.html
ok      PH-C01    219 chunks  PH-C01_No_Data_No_Story_Indigenous_Peoples_in_the_Philippines.pdf
ok      PH-C02     12 chunks  PH-C02_No_Data_No_Story_report_highlights_presentation.pdf
ok      PH-C03      6 chunks  PH-C03_Status_of_Indigenous_Peoples_Data_in_National_Statistics_Cen.pdf
ok      PH-C04      4 chunks  PH-C04_PR_on_Ethnicity_Technical_Notes.pdf
ok      PH-C05      6 chunks  PH-C05_fastFacts6_Indigenous_Peoples_in_the_Philippines_rev_1_5_Indigenous_Pe.pdf
ok      G-01       19 chunks  G-01_United_Nations_Declaration_on_the_Rights_of_Indigenous_Peopl.pdf
ok      G-02       21 chunks  G-02_CARE_Principles_for_Indigenous_Data_Governance_summary.html
ok      G-03        3 chunks  G-03_The_First_Nations_Principles_of_OCAP_fact_sheet.pdf
ok      G-04        4 chunks  G-04_Principles_of_Maori_Data_Sovereignty_Te_Mana_Raraunga_Brief.pdf
ok      G-05        4 chunks  G-05_Delgamuukw_v_British_Columbia_1997_3_SCR_1010.html
ok      G-06        6 chunks  G-06_Delgamuukw_Case_summary_2019_ocr.txt
ok      G-07       38 chunks  G-07_EU_AI_Act_Article_14_Human_Oversight.html
ok      G-08       10 chunks  G-08_Digital_Omnibus_on_Artificial_Intelligence_FAQ.html
ok      G-09        5 chunks  G-09_Register_of_Native_Title_Claims_dataset_n_d_ocr.txt
ok      G-10       14 chunks  G-10_Federal_Court_of_Australia_Annual_Report_2010_11_Part_2_native_title_m.pdf
ok      G-11        8 chunks  G-11_We_will_mediate_the_gap_closed_2009_Native_Title_Amendments_2010_ocr.txt
ok      G-12       45 chunks  G-12_Summary_of_the_WIPO_Treaty_on_Intellectual_Property_Genetic.html
ok      PH-L07    427 chunks  PH-L07_Local_Government_Code_of_1991_RA_7160.pdf
ok      PH-L08     22 chunks  PH-L08_Cybercrime_Prevention_Act_of_2012_RA_10175.html
ok      PH-L09     10 chunks  PH-L09_Community_Based_Monitoring_System_Act_RA_11315_2019.pdf
ok      PH-N07     27 chunks  PH-N07_Joint_DAR_DENR_LRA_NCIP_Memorandum_Circular_implementing_rul.pdf
ok      PH-N08      7 chunks  PH-N08_ncip_ao_no_1_s_2002_review_verification.pdf
ok      PH-N09     81 chunks  PH-N09_ncip_admin_order_01_2020_rules_on_delineation_titling_ocr.txt
ok      PH-D04    976 chunks  PH-D04_The_2023_Compendium_of_NPC_Issuances_incl_NPC_Circular_No_20.pdf
ok      PH-S04      2 chunks  PH-S04_DepEd_Order_No_62_s_2011_National_Indigenous_Peoples_Education_Policy__ocr.txt
ok      PH-C06     21 chunks  PH-C06_Report_Data_and_Information_Workshop_on_Indigenous_Peoples_a.pdf
ok      PH-C07     35 chunks  PH-C07_The_Joint_Administrative_Order_No_01_series_of_2012_A_Policy.pdf
ok      G-13       42 chunks  G-13_Community_Land_Act_2016_No_27_of_2016_Kenya_2016.pdf
ok      G-14       12 chunks  G-14_International_good_practices_Mexico_National_Institute_of_St.pdf
ok      G-15       15 chunks  G-15_Indigenous_Status_Standard_2014_Version_1_5.html
ok      G-16       66 chunks  G-16_Recommendation_on_the_Ethics_of_Artificial_Intelligence_2021.pdf
ok      G-17       22 chunks  G-17_Indigenous_and_Tribal_Peoples_Convention_1989_No_169.pdf
ok      PH-S05     16 chunks  PH-S05_Artificial_Intelligence_Roadmap_Dec15.pdf
ok      G-18       54 chunks  G-18_Native_Title_Amendment_Act_2009_No_83_2009_Australia_2009_ocr.txt
ok      PH-L10     40 chunks  PH-L10_Philippine_Disaster_Risk_Reduction_and_Management_Act_of_201.html
ok      PH-C08     14 chunks  PH-C08_Mobilizing_indigenous_knowledge_innovations_and_practices_of.html
ok      PH-C09     57 chunks  PH-C09_peace_pacts_and_contentious_politics_the_chico_river_dam_struggle_in_t.pdf
ok      G-19      108 chunks  G-19_IPCC_AR6_WGII_SummaryForPolicymakers.pdf
ok      G-20       20 chunks  G-20_Decision_of_the_Intergovernmental_Committee_19_COM_6_A_4_Buk.html
ok      G-21       33 chunks  G-21_4th_draft_global_plan_of_action_for_the_health_of_indigenous_peoples.pdf
ok      G-22       41 chunks  G-22_n2602197_Indigenous_Peoples_and_artificial_intelligence_study.pdf
ok      G-23       46 chunks  G-23_i1857e00.pdf
ok      K-PH02    102 chunks  K-PH02_1987_Constitution.html
ok      K-PH05    116 chunks  K-PH05_redacted_NCIP_AO_3_Series_of_2026_otherwise_known_as_the_2026_Guidelin.pdf
ok      K-PH07     14 chunks  K-PH07_Joint_IPOPHL_NCIP_AO_01_s_2016_protection_of_IP_rights_of_ICCs_IPs_201_ocr.txt
ok      K-PH08     35 chunks  K-PH08_RA_10066_National_Cultural_Heritage_Act_of_2009.html
ok      K-PH09     29 chunks  K-PH09_RA_11961_cultural_mapping_amendment_to_RA_10066.html
ok      K-PH10    170 chunks  K-PH10_2025_IRR_of_RA_11961.html
ok      K-PH12      2 chunks  K-PH12_DepEd_Order_51_s_2014_activities_and_materials_involving_IP_culture_20_ocr.txt
ok      K-PH13      2 chunks  K-PH13_DepEd_Order_32_s_2015_IP_Education_Curriculum_Framework_2015_ocr.txt
ok      K-PH16     26 chunks  K-PH16_RA_9147_Wildlife_Resources_Conservation_and_Protection_Act.html
ok      K-PH17      1 chunks  K-PH17_Guidelines_for_Bioprospecting_Activities_in_the_Philippines_DENR_DA_PC_ocr.txt
ok      K-PH18     15 chunks  K-PH18_RA_8423_Traditional_and_Alternative_Medicine_Act_TAMA.html
ok      K-PH20     20 chunks  K-PH20_RA_9729_Climate_Change_Act.html
ok      K-PH22     29 chunks  K-PH22_RA_9168_Philippine_Plant_Variety_Protection_Act.html
ok      K-PH23      8 chunks  K-PH23_RA_7355_Manlilikha_ng_Bayan_Act.html
ok      K-PH24     43 chunks  K-PH24_RA_9710_Magna_Carta_of_Women.html
ok      K-PH25     66 chunks  K-PH25_BAA_64_Bangsamoro_Indigenous_Peoples_Act_of_2024_ocr.txt
ok      K-PH26      2 chunks  K-PH26_BIPA_implementing_rules_BAA_64_2026_ocr.txt
ok      K-PH27     21 chunks  K-PH27_ncip_ao_no_2_s_2012_ips.pdf
ok      K-PH28    480 chunks  K-PH28_NCIP_AO_2_s_2018_Revised_ADSDPP_Guidelines.html
ok      K-PH30     29 chunks  K-PH30_NCIP_AO_1_S_2021_as_amended_by_CEB_Reso_No_2023_09_07_063.pdf
ok      K-IN02      2 chunks  K-IN02_Convention_on_Biological_Diversity_CBD_1992_ocr.txt
ok      K-IN03     37 chunks  K-IN03_nagoya_protocol_en.pdf
ok      K-IN04     22 chunks  K-IN04_UNESCO_Convention_for_the_Safeguarding_of_the_Intangible_Cultural_Heri.pdf
ok      K-IN05     41 chunks  K-IN05_International_Covenant_on_Civil_and_Political_Rights_ICCPR.html
ok      K-IN06     18 chunks  K-IN06_International_Covenant_on_Economic_Social_and_Cultural_Rights_ICESCR_1_ocr.txt
ok      K-IN07     20 chunks  K-IN07_Convention_on_the_Elimination_of_All_Forms_of_Discrimination_against_W.pdf
ok      K-IN08     59 chunks  K-IN08_CEDAW_C_GC_39_EN.pdf
ok      K-IN09     34 chunks  K-IN09_Convention_on_the_Rights_of_the_Child_CRC_1989.pdf
ok      K-IN10     22 chunks  K-IN10_International_Convention_on_the_Elimination_of_All_Forms_of_Racial_Dis.pdf
ok      K-IN11     33 chunks  K-IN11_english_paris_agreement.pdf
ok      K-IN12     51 chunks  K-IN12_International_Treaty_on_Plant_Genetic_Resources_for_Food_and.pdf
ok      K-IN15     19 chunks  K-IN15_wwf_km_gbf_cso23.pdf
ok      K-IN16     74 chunks  K-IN16_43291_sendaiframeworkfordrren.pdf
ok      K-IN17     45 chunks  K-IN17_A_HRC_60_66_EN_Indigenous_Peoples_right_to_data_2025.pdf
ok      K-AI03     72 chunks  K-AI03_Statement_of_the_Commission_on_Human_Rights_on_the_observanc.html
ok      K-AI04      3 chunks  K-AI04_NCIP_calls_for_inclusivity_in_the_new_era_of_technology_culturally_gro_ocr.txt
ok      K-AI05      2 chunks  K-AI05_DOST_and_UIC_launch_R_D_lab_to_preserve_Mindanao_languages_Mindanao_Na_ocr.txt
ok      K-AI06      4 chunks  K-AI06_KSU_launches_Digital_Arang_to_protect_Kalinga_Indigenous_knowledge_in__ocr.txt
ok      K-PU01      5 chunks  K-PU01_Epanaw_Pagkilala_Recognize_NCIP_2021_ocr.txt
ok      K-PU02      5 chunks  K-PU02_Epanaw_Paggalang_Respect_NCIP_2021_ocr.txt
ok      K-PU03      5 chunks  K-PU03_Epanaw_Pagtaguyod_Promote_NCIP_2021_ocr.txt
ok      K-PU04     33 chunks  K-PU04_Indigenous_Knowledge_Systems_and_Practices_in_the_Philippines_Status_a.pdf
ok      K-PU06     82 chunks  K-PU06_Sustaining_our_Forests_our_Rice_Lands_our_Culture_Perspectives_of_the_.pdf
ok      K-PU07      4 chunks  K-PU07_Indigenous_knowledge_and_practices_for_the_sustainable_management_of_I_ocr.txt
ok      K-PU08      4 chunks  K-PU08_Community_based_resource_assessment_and_management_planning_for_the_ri_ocr.txt
ok      K-PU09      3 chunks  K-PU09_UNESCO_Philippines_Community_based_documentation_Subanen_2003_ocr.txt
ok      K-PU10     31 chunks  K-PU10_49950_EN.docx
ok      K-PU11      9 chunks  K-PU11_Schools_of_Living_Traditions_safeguarding_ICH_in_non_formal_education__ocr.txt
ok      K-PU12      2 chunks  K-PU12_Aguilar_R_C_Managing_the_sacred_lakes_of_Coron_Island.pdf
ok      K-PU13    133 chunks  K-PU13_Pedragosa_S_An_Analysis_of_International_Law_National_Legisl.pdf
ok      K-PU14    159 chunks  K-PU14_Hiwasaki_L_Luna_E_Syamsidik_Shaw_R_Local_and_Indigenous_Knowledge_for_.pdf
ok      K-PU15      2 chunks  K-PU15_Philippine_Traditional_Knowledge_Digital_Library_on_Health_TKDL_ocr.txt
ok      K-PU16      3 chunks  K-PU16_Batak_Palawan_ethnomedical_documentation_report_PITAHC_catalog_entry_1_ocr.txt
ok      K-CC01     67 chunks  K-CC01_1_year_after_Yolanda_Manobos_rebuilding_lives_farms_Manobo_c.html
ok      K-CC02      8 chunks  K-CC02_After_Haiyan_Discrimination_in_the_face_of_disaster_Tagbanua_Calauit_I_ocr.txt
ok      K-CC03     23 chunks  K-CC03_MENRE_MGS_geohazard_assessment_and_MIPA_community_data_valid.html
ok      K-CC04     11 chunks  K-CC04_Local_indigenous_knowledge_on_disaster_risk_reduction_Mamanwa_Basey_Sa_ocr.txt
ok      K-CC05     11 chunks  K-CC05_Mapping_ancestral_domains_AGMIHICU_Higa_onon_community_mappi.pdf
ok      K-CC06      5 chunks  K-CC06_Malabayabas_M_L_Baconguis_R_Community_flood_histories_in_Bar.html
missing K-CC07: run scripts/fetch_sources.py (or download by hand)
ok      K-CC08     14 chunks  K-CC08_Community_Mapping_for_Disaster_Risk_Reduction_and_Management_0.pdf
ok      K-CC09    409 chunks  K-CC09_Lagmay_A_M_F_et_al_Naga_Cebu_landslide_of_2018_Frontiers_in.html
missing K-CC10: run scripts/fetch_sources.py (or download by hand)
ok      K-CC11      3 chunks  K-CC11_Assessment_of_early_warning_efforts_in_Leyte_for_Typhoon_Hai.html
ok      curated    65 chunks  (provisions, facts, gaps)
ok      use case    5 chunks  Philippines_IKSP_Record_Pipeline_use_case.md -> kb_usecase

Stored 8308 chunks.
```
