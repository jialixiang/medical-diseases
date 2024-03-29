# -*- coding: utf-8 -*-

# 疾病名称 needed

target_names = [ 
    u"糖尿病",
    u"艾滋病",
    u"湿疹",
    u"荨麻疹",
    u"手足口病",
    u"高血压",
    u"前列腺炎",
    u"尖锐湿疣",
    u"梅毒",
    u"抑郁症",
    u"早泄",
    u"痛风",
    u"颈椎病",
    u"肺结核",
    u"肾结石",
    u"乳腺增生",
    u"口腔溃疡",
    u"白血病",
    u"子宫肌瘤",
    u"便秘",
    u"带状疱疹",
    u"脂肪肝",
    u"乳腺癌",
    u"阴道炎",
    u"鼻炎",
    u"痤疮",
    u"狂犬病",
    u"红斑狼疮",
    u"性病",
    u"肺癌",
    u"胃癌",
    u"白癜风",
    u"尿毒症",
    u"内分泌失调",
    u"胆囊炎",
    u"腰椎间盘突出",
    u"痛经",
    u"盆腔炎",
    u"低血压",
    u"强迫症",
    u"卵巢囊肿",
    u"肺炎",
    u"胃溃疡",
    u"水痘",
    u"支气管炎",
    u"霉菌性阴道炎",
    u"疝",
    u"宫颈癌",
    u"阳痿",
    u"尿路感染",
    u"鸡眼",
    u"淋病",
    u"贫血",
    u"甲状腺结节",
    u"阑尾炎",
    u"肩周炎",
    u"慢性咽炎",
    u"甲亢",
    u"痔疮",
    u"静脉曲张",
    u"过敏性鼻炎",
    u"耳鸣",
    u"腰肌劳损",
    u"毛囊炎",
    u"破伤风",
    u"咽炎",
    u"脑供血不足",
    u"神经衰弱",
    u"强直性脊柱炎",
    u"新生儿黄疸",
    u"癫痫",
    u"肝癌",
    u"腮腺炎",
    u"脑梗塞",
    u"黄疸",
    u"直肠癌",
    u"银屑病",
    u"坐骨神经痛",
    u"肾炎",
    u"扁平疣",
    u"中耳炎",
    u"脱发",
    u"胃炎",
    u"肝硬化",
    u"生殖器疱疹",
    u"胰腺炎",
    u"精神分裂症",
    u"青光眼",
    u"咳嗽",
    u"尿道炎",
    u"失眠",
    u"淋巴瘤",
    u"宫颈炎",
    u"结肠炎",
    u"胆囊息肉",
    u"心肌炎",
    u"结膜炎",
    u"包皮过长",
    u"慢性胃炎",
    u"大三阳",
    u"胆结石",
    u"麻疹",
    u"鼻咽癌",
    u"急性肠炎",
    u"肠炎",
    u"偏头痛",
    u"鼻窦炎",
    u"脂溢性皮炎",
    u"登革热",
    u"小三阳",
    u"腹泻",
    u"头晕",
    u"过敏性紫癜",
    u"脂肪瘤",
    u"肛裂",
    u"精索静脉曲张",
    u"早孕反应",
    u"子宫内膜异位症",
    u"心绞痛",
    u"麦粒肿",
    u"葡萄胎",
    u"神经性皮炎",
    u"疣",
    u"头痛",
    u"败血症",
    u"心肌缺血",
    u"腱鞘炎",
    u"牙周炎",
    u"焦虑症",
    u"宫外孕",
    u"风疹",
    u"宫颈糜烂",
    u"疥疮",
    u"白内障",
    u"食道癌",
    u"多囊卵巢综合征",
    u"十二指肠溃疡",
    u"扁桃体炎",
    u"肝炎",
    u"血管瘤",
    u"玫瑰糠疹",
    u"感冒",
    u"麻风",
    u"前列腺增生",
    u"脑出血",
    u"出血性脑卒中",
    u"风湿病",
    u"幼儿急疹",
    u"胰腺癌",
    u"冠心病",
    u"外阴瘙痒",
    u"老年痴呆",
    u"肾囊肿",
    u"胃病",
    u"附件炎",
    u"肺气肿",
    u"梦魇",
    u"散光",
    u"结肠癌",
    u"胸膜炎",
    u"腰痛",
    u"气胸",
    u"离婚",
    u"疟疾",
    u"风湿性关节炎",
    u"孕前检查",
    u"脑膜炎",
    u"先天愚型",
    u"甲状腺癌",
    u"甲减",
    u"肠梗阻",
    u"白带异常",
    u"股癣",
    u"缺铁性贫血",
    u"灰指甲",
    u"股骨头坏死",
    u"心肌梗死",
    u"更年期综合症",
    u"脚气",
    u"霍乱",
    u"猩红热",
    u"雀斑",
    u"鼠疫",
    u"先兆流产",
    u"植物神经紊乱",
    u"关节炎",
    u"天花",
    u"亚健康",
    u"慢性支气管炎",
    u"滴虫阴道炎",
    u"慢性浅表性胃炎",
    u"沙眼",
    u"鹅口疮",
    u"佝偻病",
    u"膀胱炎",
    u"系统性红斑狼疮",
    u"血友病",
    u"月经失调",
    u"神经官能症",
    u"子宫内膜炎",
    u"小儿湿疹",
    u"类风湿性关节炎",
    u"肠胃炎",
    u"流产",
    u"前列腺癌",
    u"痣",
    u"跖疣",
    u"皮脂腺囊肿",
    u"哮喘",
    u"细菌性阴道炎",
    u"骨质疏松",
    u"反流性食管炎",
    u"小儿咳嗽",
    u"黑色素瘤",
    u"角膜炎",
    u"斑秃",
    u"乙肝",
    u"肝血管瘤",
    u"胆囊结石",
    u"鱼鳞病",
    u"肾积水",
    u"痱子",
    u"乳腺炎",
    u"阴囊湿疹",
    u"发烧",
    u"小儿肺炎",
    u"分娩",
    u"包茎",
    u"黄褐斑",
    u"闭经",
    u"面瘫",
    u"丹毒",
    u"窦性心动过缓",
    u"小儿支气管炎",
    u"近视",
    u"高脂血症",
    u"牙痛",
    u"2型糖尿病",
    u"附睾炎",
    u"牙龈炎",
    u"先天性心脏病",
    u"包皮龟头炎",
    u"三叉神经痛",
    u"淋巴结炎",
    u"慢性淋巴结炎",
    u"鼻息肉",
    u"乳腺纤维瘤",
    u"地中海贫血",
    u"变性手术",
    u"再生障碍性贫血",
    u"脑萎缩",
    u"癔症",
    u"高原反应",
    u"皮肤癌",
    u"丘疹性荨麻疹",
    u"禽流感",
    u"骨癌",
    u"皮炎",
    u"干眼症",
    u"脑炎",
    u"根管治疗",
    u"内痔",
    u"皮肤过敏",
    u"胆汁反流性胃炎",
    u"慢性萎缩性胃炎",
    u"副乳",
    u"烤瓷牙",
    u"羊水栓塞",
    u"人流",
    u"输卵管堵塞",
    u"腱鞘囊肿",
    u"流感",
    u"补牙",
    u"膀胱癌",
    u"非淋菌性尿道炎",
    u"心衰",
    u"烫伤",
    u"急性房颤",
    u"慢性房颤",
    u"房颤",
    u"胃出血",
    u"试管婴儿",
    u"胃下垂",
    u"脑震荡",
    u"羊水穿刺",
    u"单纯疱疹",
    u"慢性结肠炎",
    u"心脏神经官能症",
    u"人工授精",
    u"肛瘘",
    u"自闭症",
    u"支气管扩张",
    u"寻常疣",
    u"畸胎瘤",
    u"休克",
    u"喉癌",
    u"弱视",
    u"小儿弱视",
    u"网球肘",
    u"莱姆病",
    u"小儿腹泻",
    u"肾盂肾炎",
    u"疖",
    u"子宫内膜癌",
    u"热射病",
    u"早恋",
    u"引产",
    u"嗜睡症",
    u"肋间神经痛",
    u"龋齿",
    u"肝病",
    u"鸡胸",
    u"肠易激综合征",
    u"风湿性心脏病",
    u"溃疡性结肠炎",
    u"百日咳",
    u"慢性肾小球肾炎",
    u"急性胰腺炎",
    u"骨折",
    u"慢性鼻炎",
    u"伤寒",
    u"丙肝",
    u"牙齿美白",
    u"苯丙酮尿症",
    u"产后抑郁",
    u"肠痉挛",
    u"克罗恩病",
    u"牙髓炎",
    u"动脉粥样硬化",
    u"前置胎盘",
    u"妇科检查",
    u"腋臭",
    u"臭汗症",
    u"睾丸癌",
    u"鼻中隔偏曲",
    u"甲状腺瘤",
    u"妇科炎症",
    u"妊娠合并糖尿病",
    u"急性白血病",
    u"肾病综合征",
    u"脊髓灰质炎",
    u"甲状腺炎",
    u"窦性心动过速",
    u"肋软骨炎",
    u"心律失常",
    u"子宫内膜增生",
    u"病毒性心肌炎",
    u"手癣",
    u"精囊炎",
    u"肛周脓肿",
    u"接触性皮炎",
    u"心理咨询",
    u"传染性软疣",
    u"瘙痒症",
    u"皮肤瘙痒",
    u"糖尿病足",
    u"失恋",
    u"外痔",
    u"腹痛",
    u"流行性出血热",
    u"低钾血症",
    u"结核性胸膜炎",
    u"肝腹水",
    u"炭疽",
    u"卵巢早衰",
    u"阴茎癌",
    u"脑积水",
    u"子宫腺肌症",
    u"筋膜炎",
    u"家庭暴力",
    u"溶血性贫血",
    u"玻璃体混浊",
    u"扁平足",
    u"霰粒肿",
    u"小儿疝气",
    u"重症肌无力",
    u"软下疳",
    u"子宫内膜息肉",
    u"功能性子宫出血",
    u"急性咽炎",
    u"酒精中毒",
    u"骨膜炎",
    u"急性上呼吸道感染",
    u"非霍奇金淋巴瘤",
    u"情感障碍",
    u"躁郁症",
    u"膝关节半月板损伤",
    u"社交恐惧症",
    u"新生儿肺炎",
    u"非器质性性交疼痛",
    u"酒糟鼻",
    u"胎停",
    u"急性支气管炎",
    u"肝内胆管结石",
    u"脱毛",
    u"网恋",
    u"血小板减少性紫癜",
    u"腹腔镜手术",
    u"铅中毒",
    u"体检",
    u"甲沟炎",
    u"屈光不正",
    u"桥本甲状腺炎",
    u"肾癌",
    u"外阴白斑",
    u"骨质增生",
    u"非典",
    u"近视眼手术",
    u"脑动脉硬化",
    u"肠息肉",
    u"阴虱",
    u"小儿腺样体肥大",
    u"白喉",
    u"肺动脉高压",
    u"胸腔积液",
    u"多发性骨髓瘤",
    u"牙龈萎缩",
    u"牙周病",
    u"间质性肺炎",
    u"血吸虫病",
    u"糖尿病肾病",
    u"直肠脱垂",
    u"心脏搭桥",
    u"胃穿孔",
    u"汗疱疹",
    u"静脉炎",
    u"小脑萎缩",
    u"躁狂症",
    u"干燥综合征",
    u"胃食管反流病",
    u"垂体瘤",
    u"尿崩症",
    u"一氧化碳中毒",
    u"蛛网膜下腔出血",
    u"帕金森",
    u"1型糖尿病",
    u"脑栓塞",
    u"子宫脱垂",
    u"水中毒",
    u"婆媳关系",
    u"窦性心律不齐",
    u"肺栓塞",
    u"病毒性肝炎",
    u"消化不良",
    u"功能性消化不良",
    u"宫腔镜",
    u"室性早搏",
    u"肝囊肿",
    u"突发性聋",
    u"剖腹产",
    u"皮肌炎",
    u"开眼角",
    u"鞘膜积液",
    u"肠套叠",
    u"拔牙",
    u"脑疝",
    u"硬皮病",
    u"肝性脑病",
    u"假性湿疣",
    u"神经炎",
    u"植发",
    u"性功能障碍",
    u"血液病",
    u"鳞状细胞癌",
    u"尿失禁",
    u"神经性耳聋",
    u"斜视",
    u"小儿斜视",
    u"疤痕",
    u"宫颈癌前病变",
    u"血管炎",
    u"O型腿",
    u"传染性单核细胞增多症",
    u"双眼皮手术",
    u"脓疱疮",
    u"尿道结石",
    u"尿结石",
    u"前庭大腺囊肿",
    u"延迟性心因性反应",
    u"肺纤维化",
    u"婚外恋",
    u"花斑癣",
    u"卵巢癌",
    u"骨髓移植",
    u"慢性扁桃体炎",
    u"植物人",
    u"义眼",
    u"亚急性甲状腺炎",
    u"白色糠疹",
    u"病毒性脑炎",
    u"病毒性脑膜炎",
    u"胆囊癌",
    u"颞下颌关节紊乱病",
    u"隆胸",
    u"单纯性甲状腺肿",
    u"阴茎延长",
    u"隆鼻",
    u"肥胖症",
    u"痈",
    u"肾功能衰竭",
    u"甲肝",
    u"放疗",
    u"骨髓炎",
    u"早产",
    u"结节性红斑",
    u"声带息肉",
    u"过敏性结膜炎",
    u"冠状动脉造影",
    u"呼吸衰竭",
    u"尘肺",
    u"小细胞肺癌",
    u"滑囊炎",
    u"不孕不育",
    u"不孕症",
    u"风湿热",
    u"人格障碍",
    u"恐惧症",
    u"色素痣",
    u"黑痣",
    u"体癣",
    u"漏斗胸",
    u"性施虐症与性受虐症",
    u"声带小结",
    u"神经性厌食症",
    u"腹膜炎",
    u"细菌性痢疾",
    u"习惯性流产",
    u"四环素牙",
    u"小儿感冒",
    u"肺水肿",
    u"低血糖症",
    u"蛲虫病",
    u"多汗症",
    u"主动脉夹层",
    u"急性扁桃体炎",
    u"IGA肾病",
    u"扁平苔藓",
    u"多囊肾",
    u"鼻出血",
    u"晕动病",
    u"脉管炎",
    u"预激综合征",
    u"恙虫病",
    u"滑膜炎",
    u"头癣",
    u"消化道出血",
    u"营养不良",
    u"老年性阴道炎",
    u"阵发性室上性心动过速",
    u"喉炎",
    u"马凡氏综合征",
    u"脑电图",
    u"蛔虫病",
    u"慢性肝炎",
    u"肛门湿疹",
    u"急性淋巴细胞白血病",
    u"脑血栓",
    u"肺心病",
    u"舌癌",
    u"新生儿溶血",
    u"小儿多动症",
    u"骨肉瘤",
    u"脑肿瘤",
    u"脐疝",
    u"脑膜瘤",
    u"萎缩性鼻炎",
    u"布氏杆菌病",
    u"卵巢肿瘤",
    u"短暂性脑缺血发作",
    u"肾小球肾炎",
    u"视网膜脱落",
    u"肋骨骨折",
    u"急性肾小球肾炎",
    u"心包积液",
    u"乙脑",
    u"惊厥",
    u"慢性腹泻",
    u"嗜铬细胞瘤",
    u"霍奇金淋巴瘤",
    u"骨结核病",
    u"肠粘连",
    u"小儿癫痫",
    u"脑水肿",
    u"梦游症",
    u"骨髓增生异常综合征",
    u"肺炎球菌肺炎",
    u"大叶性肺炎",
    u"去眼袋",
    u"隐睾",
    u"小儿脑瘫",
    u"地图舌",
    u"胆管癌",
    u"肾上腺肿瘤",
    u"烧伤",
    u"晕厥",
    u"小儿疱疹性咽峡炎",
    u"运动神经元病",
    u"慢性胰腺炎",
    u"库欣综合征",
    u"原发性肝癌",
    u"老花眼",
    u"混合痔",
    u"高钾血症",
    u"分泌性中耳炎",
    u"小儿哮喘",
    u"腹股沟疝",
    u"腕管综合征",
    u"睡眠障碍",
    u"胆管结石",
    u"酒精性脂肪肝",
    u"酒精肝",
    u"慢性粒细胞白血病",
    u"网瘾",
    u"结缔组织病",
    u"结节病",
    u"新生儿败血症",
    u"肝癌介入",
    u"矽肺",
    u"多发性硬化",
    u"胶质瘤",
    u"肝豆状核变性",
    u"法洛四联症",
    u"膀胱肿瘤",
    u"胎盘早剥",
    u"褥疮",
    u"跟腱断裂",
    u"弥散性血管内凝血",
    u"结核性脑膜炎",
    u"胸腺瘤",
    u"膀胱结石",
    u"单亲儿童心理问题",
    u"二尖瓣关闭不全",
    u"性早熟",
    u"烟雾病",
    u"乳腺肿瘤",
    u"先天性巨结肠",
    u"脊髓空洞症",
    u"面肌痉挛",
    u"肾错构瘤",
    u"巨人症",
    u"直肠息肉",
    u"弓形虫病",
    u"股骨颈骨折",
    u"慢性肾功能衰竭",
    u"耳聋",
    u"心肌病",
    u"格林巴利综合征",
    u"耵聍栓塞",
    u"支原体肺炎",
    u"翼状胬肉",
    u"颅内压增高",
    u"泪囊炎",
    u"瘢痕疙瘩",
    u"房室传导阻滞",
    u"糖尿病酮症酸中毒",
    u"心理障碍",
    u"克山病",
    u"先天性耳前瘘管",
    u"根尖周炎",
    u"室间隔缺损",
    u"痒疹",
    u"神经母细胞瘤",
    u"黄斑变性",
    u"牙龈癌",
    u"真菌性皮肤病",
    u"原发孔型房间隔缺损",
    u"房间隔缺损",
    u"太田痣",
    u"拇外翻",
    u"麻醉",
    u"男性不育",
    u"继发性高血压",
    u"宫颈锥切术",
    u"药物性皮炎",
    u"脊髓小脑变性症",
    u"产前检查",
    u"阻生齿",
    u"肠结核",
    u"癣",
    u"老年斑",
    u"脊柱侧弯",
    u"纤维瘤",
    u"子宫颈息肉",
    u"下肢静脉血栓",
    u"天疱疮",
    u"偏瘫",
    u"甲状腺腺瘤",
    u"扩张型心肌病",
    u"流行性脑脊髓膜炎",
    u"鼓膜穿孔",
    u"产后出血",
    u"急性喉炎",
    u"锁骨骨折",
    u"头虱",
    u"小儿急性喉炎",
    u"巨乳症",
    u"Behcet病",
    u"白塞氏病",
    u"唇腭裂",
    u"输卵管炎",
    u"高泌乳素血症",
    u"低钠血症",
    u"动脉导管未闭",
    u"口腔扁平苔藓",
    u"特发性血小板减少性紫癜",
    u"粟丘疹",
    u"肾肿瘤",
    u"视神经萎缩",
    u"紫癜性肾炎",
    u"贲门失驰症",
    u"死胎",
    u"动脉瘤",
    u"妊高症",
    u"日光性皮炎",
    u"远视",
    u"二尖瓣狭窄",
    u"过敏性休克",
    u"肾结核",
    u"多形红斑",
    u"基底细胞癌",
    u"喉神经纤维瘤",
    u"倒睫",
    u"肺脓肿",
    u"葡萄膜炎",
    u"胎膜早破",
    u"性心理障碍",
    u"丝虫病",
    u"人工耳蜗",
    u"急性呼吸窘迫综合征",
    u"自身免疫性肝炎",
    u"吸脂",
    u"不安腿综合症",
    u"小儿先天性髋关节脱位",
    u"先天性髋关节脱位",
    u"软骨瘤",
    u"无脑儿",
    u"家庭心理问题",
    u"尿道下裂",
    u"异位性皮炎",
    u"睡眠呼吸暂停综合征",
    u"隐翅虫皮炎",
    u"骨肿瘤",
    u"小儿肠炎",
    u"特发性震颤",
    u"脊髓损伤",
    u"梨状肌综合征",
    u"睾丸扭转",
    u"小儿鼻炎",
    u"骨瘤",
    u"原发性醛固酮增多症",
    u"钩端螺旋体病",
    u"冻伤",
    u"黑热病",
    u"脾功能亢进",
    u"急性胃炎",
    u"肝脓肿",
    u"Graves病",
    u"主动脉瓣关闭不全",
    u"眼球震颤",
    u"手部湿疹",
    u"儿童鼻窦炎",
    u"小叶性肺炎",
    u"小儿支气管肺炎",
    u"小儿败血症",
    u"儿童白血病",
    u"真性红细胞增多症",
    u"肩关节脱位",
    u"X型腿",
    u"外耳道炎",
    u"疼痛",
    u"进行性肌营养不良症",
    u"急腹症",
    u"圆锥角膜",
    u"颈动脉狭窄",
    u"肝肿瘤",
    u"急性鼻炎",
    u"脑血管病",
    u"舌下腺囊肿",
    u"小儿贫血",
    u"髌骨骨折",
    u"慢阻肺",
    u"结核性腹膜炎",
    u"狼疮性肾炎",
    u"阴道紧缩",
    u"踝部扭伤",
    u"急性肾功能衰竭",
    u"病毒性肺炎",
    u"输尿管结石",
    u"感染性休克",
    u"成骨不全",
    u"多发性肌炎",
    u"慢性淋巴细胞白血病",
    u"结节性痒疹",
    u"鲜红斑痣",
    u"中医减肥",
    u"肾移植",
    u"外阴湿疹",
    u"高血压肾病",
    u"绒毛膜癌",
    u"肺肿瘤",
    u"造血干细胞移植",
    u"角膜移植",
    u"发育迟缓",
    u"脑血管畸形",
    u"肢端肥大症",
    u"外阴癌",
    u"化脓性脑膜炎",
    u"皮肤纤维瘤",
    u"失血性休克",
    u"低血容量性休克",
    u"鼓膜内陷",
    u"钩虫病",
    u"腮腺混合瘤",
    u"多形性腺瘤",
    u"产后风湿",
    u"脚气病",
    u"室性心动过速",
    u"智力障碍",
    u"口腔修复",
    u"骨巨细胞瘤",
    u"房性早搏",
    u"急性会厌炎",
    u"高甘油三酯血症",
    u"有机磷杀虫药中毒",
    u"门静脉高压症",
    u"肾病",
    u"心脏骤停",
    u"矮小症",
    u"花粉症",
    u"糖尿病神经病变",
    u"前庭大腺炎",
    u"心肌桥",
    u"生涯规划",
    u"手足皲裂",
    u"中毒",
    u"斜颈",
    u"上睑下垂",
    u"胎儿窘迫",
    u"心包炎",
    u"急性短暂性精神障碍",
    u"腰腿痛",
    u"成人斯蒂尔病",
    u"关节镜",
    u"动脉硬化闭塞症",
    u"听神经瘤",
    u"眼底病",
    u"躯体形式障碍",
    u"牙龈瘤",
    u"臂丛神经损伤",
    u"肝衰竭",
    u"反应性关节炎",
    u"视网膜母细胞瘤",
    u"急性脊髓炎",
    u"乳房湿疹",
    u"除皱",
    u"肺部疾病",
    u"慢性喉炎",
    u"心脏移植",
    u"视神经炎",
    u"克汀病",
    u"骨髓纤维化",
    u"雷诺综合征",
    u"髋关节脱位",
    u"腰椎管狭窄",
    u"川崎病",
    u"新生儿窒息",
    u"小儿肺炎支原体肺炎",
    u"纵隔肿瘤",
    u"大疱性表皮松解症",
    u"甲状旁腺机能亢进",
    u"骨软骨瘤",
    u"胆脂瘤型中耳炎",
    u"高血压脑病",
    u"巩膜炎",
    u"肝移植",
    u"胰腺囊肿",
    u"腹主动脉瘤",
    u"原发性胆汁性肝硬化",
    u"骨盆骨折",
    u"心脏瓣膜性疾病",
    u"骶管囊肿",
    u"腺性膀胱炎",
    u"慢性化脓性中耳炎",
    u"夜惊",
    u"红皮病",
    u"会厌囊肿",
    u"脑外伤",
    u"横纹肌肉瘤",
    u"病态窦房结综合征",
    u"脑动脉瘤",
    u"内眦赘皮",
    u"学习障碍",
    u"巨大胎儿",
    u"外阴尖锐湿疣",
    u"银屑病性关节炎",
    u"原发性血小板增多症",
    u"糖尿病视网膜病变",
    u"截瘫",
    u"自身免疫性肝病",
    u"发作性睡病",
    u"脊柱裂",
    u"胸膜间皮瘤",
    u"人工关节置换术",
    u"脂膜炎",
    u"口腔粘膜病",
    u"两性畸形",
    u"肾母细胞瘤",
    u"鼻骨骨折",
    u"应激性溃疡",
    u"痴呆",
    u"胃肠道间质瘤",
    u"先天性胆道闭锁",
    u"新生儿听力筛查",
    u"新生儿缺氧缺血性脑病",
    u"尺神经损伤",
    u"维生素A缺乏病",
    u"高胆固醇血症",
    u"胫骨平台骨折",
    u"脾破裂",
    u"颅内血肿",
    u"血管性痴呆",
    u"颅咽管瘤",
    u"多发性大动脉炎",
    u"大动脉炎",
    u"子宫破裂",
    u"厌学",
    u"主动脉瓣狭窄",
    u"自身免疫性溶血性贫血",
    u"鼻前庭炎",
    u"颅骨骨折",
    u"夏季皮炎",
    u"心身疾病",
    u"肾上腺皮质功能减退症",
    u"尤文肉瘤",
    u"子宫畸形",
    u"激素依赖性皮炎",
    u"口腔白斑病",
    u"急性心力衰竭",
    u"先天性肾上腺皮质增生症",
    u"三尖瓣关闭不全",
    u"儿童保健",
    u"桡神经损伤",
    u"面部吸脂",
    u"噬血细胞综合征",
    u"骨囊肿",
    u"职业发展",
    u"嗜酸性粒细胞增多症",
    u"新生儿巨细胞病毒感染",
    u"烟酸缺乏病",
    u"韧带损伤",
    u"过期妊娠",
    u"华支睾吸虫病",
    u"神经原性膀胱",
    u"副伤寒",
    u"粘连性肠梗阻",
    u"外耳湿疹",
    u"妊娠合并贫血",
    u"先天性喉喘鸣",
    u"多发性神经纤维瘤",
    u"腓总神经损伤",
    u"电击",
    u"气性坏疽",
    u"皮脂腺痣",
    u"肝包虫病",
    u"结节性硬化症",
    u"皮肤卟啉病",
    u"小儿疱疹性口炎",
    u"坏死性筋膜炎",
    u"水电解质紊乱和酸碱平衡",
    u"螨皮炎",
    u"舌系带过短",
    u"老年病",
    u"二尖瓣脱垂综合症",
    u"神经性呕吐",
    u"亲子关系",
    u"恶性贫血",
    u"隐匿性肾小球肾炎",
    u"酒精性肝硬化",
    u"心内膜炎",
    u"艾森曼格综合征",
    u"儿童中耳炎",
    u"肌张力障碍",
    u"风湿性多肌痛",
    u"枕神经痛",
    u"脑脊液鼻漏",
    u"男性乳房肥大",
    u"股疝",
    u"高钠血症",
    u"粘多糖代谢障碍",
    u"肠瘘",
    u"新生儿呕吐",
    u"黄斑裂孔",
    u"三高症",
    u"毛周角化病",
    u"侵蚀性葡萄胎",
    u"急性化脓性中耳炎",
    u"肾动脉狭窄",
    u"胎儿宫内发育迟缓",
    u"心脏瓣膜手术",
    u"滑膜肉瘤",
    u"肾下垂",
    u"免疫缺陷病",
]

# 慢性病
chronic = [
    u"内分泌及代谢疾病",
    u"甲状腺机能障碍",
    u"糖尿病",
    u"高血脂症",
    u"威尔逊氏",
    u"痛风",
    u"天疱疮",
    u"皮肌炎",
    u"泌乳素过高症",
    u"先天性代谢异常疾病",
    u"肾上腺病变引发内分泌障碍",
    u"脑下垂体病变引发内分泌障碍",
    u"性早熟",
    u"副甲状腺机能低下症",
    u"性腺低能症",
    u"精神疾病",
    u"精神病",
    u"神经系统疾病",
    u"脑瘤并发神经功能障碍",
    u"巴金森氏症",
    u"饥僵直萎缩症",
    u"多发性硬化症",
    u"婴儿脑性麻痹",
    u"癫痫",
    u"重症肌无力",
    u"多发性周边神经病变",
    u"神经丛病变",
    u"三叉神经病",
    u"偏头痛",
    u"脊髓损伤",
    u"心脏病",
    u"高血压",
    u"脑血管病变",
    u"动脉粥样硬化",
    u"动脉栓塞及血栓症",
    u"雷诺氏病",
    u"慢性鼻窦炎",
    u"慢性支气管炎",
    u"肺气肿",
    u"哮喘",
    u"支气管扩张症",
    u"满性阻塞性肺炎",
    u"过敏性鼻炎",
    u"消化性溃疡",
    u"肝硬化",
    u"慢性肝炎",
    u"胃肠机能性障碍",
    u"慢性胆道炎",
    u"肾脏炎",
    u"肾脏感染",
    u"干戒烟",
    u"多发性肌炎",
    u"骨质疏松症",
    u"系统性红斑狼疮",
    u"慢性骨髓炎",
    u"骨髓分化不良症候群",
    u"青光眼",
    u"干眼症",
    u"视网膜变形",
    u"角膜变形",
    u"黄斑部变性",
    u"葡萄膜炎",
    u"结核",
    u"先天畸形",
    u"干藓",
    u"湿疹",
    u"皮肤炎",
    u"乌脚病",
    u"白斑",
    u"贫血",
    u"血小板增生症",
    u"中耳炎",
    u"痔疮",
    u"尿失禁",
    u"子宫内膜异位症",
    u"前列腺肥大",
    u"停经症候群",
    u"前列腺炎",
]

# 流行病
epidemic = [
   u"禽流感",
   u"霍乱",
   u"冠状病毒感染（中东呼吸综合症、SARS）",
   u"埃博拉",
   u"亨德拉病毒感染",
   u"流感",
   u"钩端螺旋体病",
   u"脑膜炎",
   u"尼帕病毒感染",
   u"鼠疫",
   u"裂谷热",
   u"天花和人类猴痘",
   u"嗜酸性粒细胞减少症",
   u"病毒性出血热",
   u"黄热",
   u"寨卡病毒",
]

# 传染病
infection = [
    u"鼠疫",
    u"霍乱",
    u"传染性非典型肺炎",
    u"艾滋病",
    u"病毒性肝炎",
    u"脊髓灰质炎",
    u"人感染高致病性禽流感",
    u"人感染H7N9禽流感",
    u"麻疹",
    u"流行性出血热",
    u"狂犬病",
    u"流行性乙型脑炎",
    u"登革热",
    u"炭疽",
    u"痢疾",
    u"肺结核",
    u"伤寒副伤寒",
    u"流行性脑脊髓膜炎",
    u"百日咳",
    u"白喉",
    u"新生儿破伤风",
    u"猩红热",
    u"布鲁氏菌病",
    u"淋病",
    u"梅毒",
    u"钩端螺旋体病",
    u"血吸虫病",
    u"疟疾",
    u"流行性感冒",
    u"流行性腮腺炎",
    u"风疹",
    u"急性出血性结膜炎",
    u"麻风病",
    u"斑疹伤寒",
    u"黑热病",
    u"丝虫病",
    u"包虫病",
    u"其他感染性腹泻",
    u"手足口病",
    u"水痘",
    u"尖锐湿疣",
    u"生殖器疱疹",
    u"生殖道沙眼衣原体感染",
    u"肝吸虫病",
    u"恙虫病",
    u"森林脑炎",
    u"结核性胸膜炎",
    u"非淋菌性尿道炎",
    u"人感染猪链球菌病",
    u"埃博拉病",
    u"猴痘",
    u"黄热病",
    u"人变异性克雅氏病",
    u"鼻疽和类鼻疽",
    u"基孔肯雅热",
    u"广州管圆线虫病",
    u"AFP病例",
    u"不明原因肺炎",
]

# For parsing docs

number_words = [u"一", u"二", u"三", u"四", u"五", u"六", u"七", u"八", u"九", u"十"]

filter_words = [u"概述", u"概论"]

gender_words = [u"性别", u"男", u"女", u"遗传", u"家族"]

age_words = [u"年龄", u"岁", u"婴儿", u"小儿", u"幼儿", u"婴幼儿", u"少年", u"青年", u"中年", u"老年", u"遗传", u"家族"]

season_words = [u"季", u"春", u"夏", u"秋", u"冬"]

caserate_words = [u"患病"]

incidence_words = [u"发病率"]

mapping = {
    "gender": u"性别",
    "age": u"年龄段",
#    "season": u"是否为流行病",
#    "caserate": u"患病率",
#    "incidence": u"发病率",
}

