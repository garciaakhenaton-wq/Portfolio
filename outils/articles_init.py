# Génère le premier veille.json (articles vérifiés le 19 octobre 2026)
import json, os
A = []
def art(topic, date, source, lang, title, url, fr, en, ja, zh):
    slug = "".join(ch for ch in source.lower() if ch.isalnum())[:16]
    A.append({"id": f"{topic}-{date}-{slug}", "topic": topic, "date": date, "source": source, "lang": lang,
              "title": title, "url": url, "summary": {"fr": fr, "en": en, "ja": ja, "zh": zh}})

# ---------------- Prix de la RAM et IA ----------------
art("ram", "2026-10-19", "Startup Fortune", "en", "Samsung's own memory chief says the RAM shortage won't peak until 2028",
    "https://startupfortune.com/samsungs-own-memory-chief-says-the-ram-shortage-wont-peak-until-2028",
    "Le responsable des ventes mémoire de Samsung prévoit que la pénurie de DRAM et de HBM va s'aggraver en 2027 et rester forte jusqu'en 2028, faute de nouvelles capacités de production.",
    "Samsung's memory sales chief expects the DRAM and HBM shortage to worsen through 2027 and stay tight into 2028, with no significant new supply before then.",
    "Samsungのメモリ営業責任者は、DRAMとHBMの不足が2027年にかけて深刻化し、2028年まで続くと予測。それまで大幅な供給増は見込めないという。",
    "三星存储业务销售负责人预计，DRAM和HBM短缺将在2027年加剧，并持续到2028年，在此之前不会有明显的新增产能。")
art("ram", "2026-10-14", "The Motley Fool", "en", "As AI Devours Memory Chips, the Companies That Make Them Hold the Pricing Power",
    "https://www.fool.com/investing/2026/10/14/as-ai-devours-memory-chips-the-companies-that-make/",
    "Samsung, SK hynix et Micron produisent plus de 95 % de la DRAM mondiale et orientent leurs usines vers la HBM pour l'IA. SK hynix dit avoir déjà vendu toute sa capacité de 2026.",
    "Samsung, SK hynix and Micron make over 95% of the world's DRAM and are shifting their fabs towards HBM for AI. SK hynix says its 2026 capacity is essentially sold out.",
    "Samsung、SK hynix、Micronは世界のDRAMの95%以上を生産し、工場をAI向けHBMへ振り向けている。SK hynixは2026年の生産能力が事実上完売したという。",
    "三星、SK海力士和美光生产了全球95%以上的DRAM，并把产能转向用于人工智能的HBM。SK海力士表示其2026年产能已基本售罄。")
art("ram", "2026-10-13", "Tom's Hardware FR", "fr", "Les prix de la RAM deviennent incontrôlables, et la pénurie pourrait durer encore trois ans",
    "https://www.tomshardware.fr/les-prix-de-la-ram-deviennent-incontrolables-et-la-penurie-pourrait-durer-encore-trois-ans/",
    "Selon Barclays, les prix contractuels de la DDR4 ont pris 24 % en trois mois (+20 % pour la DDR5). Citi prévoit un pic du déficit de DRAM fin 2027.",
    "According to Barclays, DDR4 contract prices rose 24% in three months (DDR5 +20%). Citi expects the DRAM deficit to peak in late 2027.",
    "Barclaysによると、DDR4の契約価格は3か月で24%上昇(DDR5は20%)。Citiは、DRAMの供給不足が2027年末にピークを迎えると予測している。",
    "据巴克莱银行数据，DDR4合约价格三个月上涨24%（DDR5上涨20%）。花旗预计DRAM供应缺口将在2027年底达到峰值。")
art("ram", "2026-10-01", "Pause Hardware", "fr", "Prix de la mémoire : la demande IA maintient la hausse au quatrième trimestre 2026",
    "https://pausehardware.com/prix-memoire-hausse-ia-fin-2026/",
    "TrendForce prévoit encore +10 à 15 % sur les prix de la DRAM et +15 à 20 % sur la NAND au 4e trimestre 2026, portés par les serveurs d'IA.",
    "TrendForce still forecasts +10–15% for DRAM and +15–20% for NAND contract prices in Q4 2026, driven by AI servers.",
    "TrendForceは、AIサーバーの需要により、2026年第4四半期もDRAMが10〜15%、NANDが15〜20%値上がりすると予測。",
    "TrendForce预测，在AI服务器需求推动下，2026年第四季度DRAM合约价格仍将上涨10–15%，NAND上涨15–20%。")
art("ram", "2026-08-05", "RTBF", "fr", "Crise de la RAM : 2026 était déjà difficile, mais Samsung annonce une situation encore pire en 2027",
    "https://www.rtbf.be/article/crise-de-la-ram-2026-etait-deja-difficile-mais-samsung-annonce-une-situation-encore-pire-en-2027-11766293",
    "Samsung, qui produit environ un tiers des puces mémoire, annonce des tensions encore plus fortes en 2027. PC, cartes graphiques, consoles et smartphones risquent de coûter plus cher.",
    "Samsung, which makes about a third of the world's memory chips, expects even tighter supply in 2027. PCs, graphics cards, consoles and smartphones may cost more.",
    "世界のメモリチップの約3分の1を生産するSamsungは、2027年にさらに供給がひっ迫すると発表。PC、グラフィックカード、ゲーム機、スマートフォンの値上がりが懸念される。",
    "生产全球约三分之一存储芯片的三星表示，2027年供应将更加紧张。电脑、显卡、游戏机和手机都可能涨价。")
art("ram", "2026-07-03", "TrendForce", "en", "AI Server Demand Continues to Support Memory Prices in 3Q26, but Gains Moderate",
    "https://www.trendforce.com/presscenter/news/20260703-13134.html",
    "Les prix de la DRAM devaient encore monter de 13 à 18 % au 3e trimestre 2026 : la hausse ralentit car les fabricants de PC et de smartphones atteignent leurs limites.",
    "DRAM contract prices were expected to rise another 13–18% in Q3 2026: growth is slowing as PC and smartphone makers hit their affordability limits.",
    "2026年第3四半期のDRAM契約価格はさらに13〜18%上昇する見通し。PCやスマートフォンのメーカーが購入の限界に近づき、上昇ペースは鈍化している。",
    "2026年第三季度DRAM合约价格预计再涨13–18%：由于电脑和手机厂商已接近承受极限，涨势有所放缓。")
art("ram", "2026-06-30", "LearnUp", "fr", "RAM : prix de la mémoire en hausse de 50 % en 2026",
    "https://www.learnup.fr/ram-prix-hausse-2026-jefferies",
    "La banque Jefferies prévoit +40 à 50 % sur la DRAM et la NAND au 3e trimestre 2026, puis +30 à 40 % au 4e, et pas de baisse avant 2028.",
    "Jefferies forecasts +40–50% for DRAM and NAND in Q3 2026, then +30–40% in Q4, with no decline expected before 2028.",
    "Jefferiesは、DRAMとNANDが2026年第3四半期に40〜50%、第4四半期に30〜40%値上がりし、2028年までは下がらないと予測。",
    "Jefferies预测，2026年第三季度DRAM和NAND价格将上涨40–50%，第四季度再涨30–40%，2028年前不会下降。")
art("ram", "2026-03-31", "I-Connect007 · TrendForce", "en", "AI Server Demand to Drive Memory Contract Price Increases in 2Q26",
    "https://iconnect007.com/article/149414/ai-server-demand-to-drive-memory-contract-price-increases-in-2q26-as-csps-secure-supply-via-longterm-agreements/149411/pcb",
    "TrendForce annonçait +58 à 63 % sur la DRAM et +70 à 75 % sur la NAND au 2e trimestre 2026 : les fabricants réservent leur production aux serveurs d'IA.",
    "TrendForce forecast +58–63% for DRAM and +70–75% for NAND in Q2 2026, as makers reserve production for AI servers.",
    "TrendForceは2026年第2四半期にDRAMが58〜63%、NANDが70〜75%上昇すると予測。メーカーは生産をAIサーバー向けに優先している。",
    "TrendForce预测2026年第二季度DRAM上涨58–63%，NAND上涨70–75%，因为厂商将产能优先留给AI服务器。")
art("ram", "2026-02-26", "Gartner", "en", "Gartner Says Surging Memory Costs Will Reduce Global PC and Smartphone Shipments in 2026",
    "https://www.gartner.com/en/newsroom/press-releases/2026-02-26-gartner-says-surging-memory-costs-will-reduce-global-pc-and-smartphone-shipments-in-2026",
    "Gartner prévoit des PC 17 % plus chers fin 2026, car la mémoire et les SSD coûtent 130 % de plus. Les ventes de PC baisseraient de plus de 10 %.",
    "Gartner expects PCs to cost 17% more by the end of 2026 because memory and SSDs cost 130% more. PC shipments could fall by over 10%.",
    "Gartnerは、メモリとSSDの価格が130%上昇するため、2026年末までにPCが17%値上がりすると予測。PC出荷台数は10%以上減少する可能性がある。",
    "Gartner预计，由于内存和固态硬盘价格上涨130%，到2026年底电脑价格将上涨17%，电脑出货量可能下降超过10%。")
art("ram", "2025-12-04", "iPhoneSoft", "fr", "Crise de la mémoire : Micron annonce que la marque Crucial va disparaître",
    "https://iphonesoft.fr/2025/12/04/crise-memoire-micron-annonce-marque-crucial-disparaitre",
    "Micron arrête sa marque grand public Crucial (RAM et SSD) d'ici février 2026 pour réserver sa production aux centres de données d'IA.",
    "Micron is ending its Crucial consumer brand (RAM and SSDs) by February 2026 to reserve its production for AI data centres.",
    "Micronは2026年2月までに一般向けブランドCrucial(RAMとSSD)を終了し、生産をAIデータセンター向けに集中させる。",
    "美光将在2026年2月前停止其消费级品牌Crucial（内存和固态硬盘），把产能留给人工智能数据中心。")

# ---------------- AI Act ----------------
art("act", "2026-10-15", "ActuIA", "fr", "AI Act : les enquêtes pourraient prolonger le délai de sanction",
    "https://www.actuia.com/actualite/ai-act-les-enquetes-pourraient-prolonger-le-delai-de-sanction/",
    "La Commission consulte jusqu'au 9 novembre 2026 sur les règles d'enquête de l'AI Act : chaque acte d'enquête pourrait relancer le délai de 5 ans pour sanctionner un fournisseur.",
    "The Commission is consulting until 9 November 2026 on AI Act investigation rules: each investigative step could restart the 5-year limit for sanctioning a provider.",
    "欧州委員会は2026年11月9日までAI法の調査規則について意見を募集中。調査のたびに、事業者を制裁できる5年の期限がリセットされる可能性がある。",
    "欧盟委员会正就《人工智能法》调查规则征求意见，截止2026年11月9日：每次调查行动都可能让处罚供应商的5年时效重新计算。")
art("act", "2026-10-13", "Données Personnelles", "fr", "Actualité IA et AI Act 2026 : calendrier et obligations",
    "https://www.donneespersonnelles.fr/actualite-ia-2026",
    "Début septembre 2026, la Commission a envoyé des demandes d'informations à plus de 30 fournisseurs d'IA : première utilisation de ses pouvoirs de contrôle depuis août 2026.",
    "In early September 2026, the Commission sent information requests to more than 30 AI providers: its first use of enforcement powers since August 2026.",
    "2026年9月初め、欧州委員会は30社以上のAI事業者に情報提供を要請した。2026年8月以降、執行権限を初めて行使したことになる。",
    "2026年9月初，欧盟委员会向30多家人工智能供应商发出信息索取请求，这是其自2026年8月以来首次行使执法权。")
art("act", "2026-10-07", "Behaviture", "en", "The EU AI Act in October 2026: What Companies Need to Do Now",
    "https://behaviture.com/insights/the-eu-ai-act-in-october-2026-what-companies-need-to-do-now",
    "Les amendes vont jusqu'à 35 millions d'euros ou 7 % du chiffre d'affaires mondial pour une pratique interdite, et 15 millions ou 3 % pour un manque de transparence (article 50).",
    "Fines reach up to €35 million or 7% of worldwide turnover for a prohibited practice, and €15 million or 3% for transparency breaches (Article 50).",
    "罰金は、禁止行為の場合最大3,500万ユーロまたは世界売上高の7%、透明性違反(第50条)の場合1,500万ユーロまたは3%に達する。",
    "违反禁止性规定的罚款最高可达3500万欧元或全球年营业额的7%，违反透明度义务（第50条）最高1500万欧元或3%。")
art("act", "2026-10-06", "ActuIA", "en", "AI Act: obligations in force and delays under omnibus 2026/1744",
    "https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/",
    "Prochaine échéance le 2 décembre 2026 : les IA génératives déjà sur le marché devront marquer leurs contenus, et deux nouvelles interdictions entreront en vigueur.",
    "Next deadline on 2 December 2026: generative AI already on the market must mark its content, and two new prohibitions take effect.",
    "次の期限は2026年12月2日。既に市場にある生成AIはコンテンツへの表示が義務となり、2つの新たな禁止事項が施行される。",
    "下一个截止日期是2026年12月2日：已上市的生成式人工智能必须为其内容加标识，两项新的禁令也将生效。")
art("act", "2026-10-06", "ActuIA · Éthique", "fr", "Éthique et régulation de l'IA : le point au 6 octobre 2026",
    "https://www.actuia.com/actualite/ethique-et-regulation-de-lia-le-point-au-6-octobre-2026/",
    "OpenAI va ajouter un filigrane aux textes de ChatGPT dans l'Union européenne pour respecter l'article 50 de l'AI Act sur la transparence.",
    "OpenAI will add a watermark to ChatGPT texts in the European Union to comply with the AI Act's Article 50 on transparency.",
    "OpenAIは、AI法第50条の透明性義務に対応するため、EU域内でChatGPTの文章に透かしを入れる。",
    "OpenAI将在欧盟为ChatGPT生成的文本添加水印，以遵守《人工智能法》第50条的透明度要求。")
art("act", "2026-09-29", "Playmoweb", "fr", "AI Act : depuis le 2 août 2026, votre chatbot doit dire qu'il est une IA",
    "https://playmoweb.com/ai-act-2-aout-2026-obligations-transparence-application/",
    "Depuis le 2 août 2026, un chatbot doit dire qu'il est une IA dès la première interaction, et les deepfakes doivent être signalés. Conseils concrets pour les développeurs.",
    "Since 2 August 2026, a chatbot must say it is an AI from the first interaction, and deepfakes must be labelled. Practical tips for developers.",
    "2026年8月2日以降、チャットボットは最初のやり取りでAIであることを示し、ディープフェイクには表示が必要になった。開発者向けの具体的な助言もある。",
    "自2026年8月2日起，聊天机器人必须在首次交互时表明自己是人工智能，深度伪造内容也必须加以标注。文章还为开发者提供了具体建议。")
art("act", "2026-09-04", "AI Act Insight", "fr", "Digital Omnibus : ce qui est reporté dans l'AI Act",
    "https://aiactinsight.eu/fr/ai-act/digital-omnibus/",
    "Le règlement (UE) 2026/1744, publié le 24 juillet 2026, reporte les règles « haut risque » au 2 décembre 2027 et au 2 août 2028.",
    "Regulation (EU) 2026/1744, published on 24 July 2026, postpones the high-risk rules to 2 December 2027 and 2 August 2028.",
    "2026年7月24日に公布された規則(EU)2026/1744により、高リスク規則は2027年12月2日と2028年8月2日に延期された。",
    "2026年7月24日公布的欧盟第2026/1744号条例，将高风险规则推迟至2027年12月2日和2028年8月2日。")
art("act", "2026-07-22", "Quantic Avocats", "fr", "AI Act : le calendrier des obligations haut risque officiellement reporté",
    "https://www.quantic-avocats.com/2026/07/22/ai-act-digital-omnibus-report-obligations-haut-risque/",
    "Le Parlement (16 juin) puis le Conseil (29 juin 2026) ont adopté le report : les systèmes à haut risque de l'annexe III passent au 2 décembre 2027.",
    "Parliament (16 June) and then the Council (29 June 2026) adopted the delay: Annex III high-risk systems move to 2 December 2027.",
    "欧州議会(6月16日)と理事会(2026年6月29日)が延期を採択。附属書IIIの高リスクシステムは2027年12月2日に延期された。",
    "欧洲议会（6月16日）和理事会（2026年6月29日）先后通过推迟方案：附件三中的高风险系统推迟至2027年12月2日。")
art("act", "2024-07-12", "EUR-Lex", "fr", "Règlement (UE) 2024/1689 sur l'intelligence artificielle",
    "https://eur-lex.europa.eu/eli/reg/2024/1689/oj",
    "Le texte officiel de l'AI Act, publié au Journal officiel de l'UE le 12 juillet 2024 : la référence à consulter en cas de doute.",
    "The official text of the AI Act, published in the EU Official Journal on 12 July 2024: the reference to check when in doubt.",
    "2024年7月12日にEU官報で公布されたAI法の正式な条文。迷ったときに確認すべき基準となる資料。",
    "《人工智能法》官方文本，于2024年7月12日在欧盟官方公报上公布，有疑问时应查阅的权威参考。")

data = {"updated": "2026-10-19", "max_par_sujet": 10, "articles": A}
out = os.path.join(os.path.dirname(__file__), "..", "veille.json")
json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(A), "articles")
