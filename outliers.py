# -*- coding: utf-8 -*-

# 无法通过章节找到的疾病名称

unmatched = [    
    u"多囊肾",
    u"喉神经纤维瘤",
    u"吸脂",
    u"脑脊液鼻漏",
    u"脑萎缩",
    u"人工耳蜗",
    u"鼠疫",
    u"扁桃体炎",
    u"牙龈癌",
    u"脱毛",
    u"先天性巨结肠",
    u"晕动病",
    u"弱视",
    u"新生儿呕吐",
    u"拇外翻",
    u"网恋",
    u"滑膜肉瘤",
    u"过敏性结膜炎",
    u"膝关节半月板损伤",
    u"鼓膜内陷",
    u"鼻前庭炎",
    u"有机磷杀虫药中毒",
    u"高原反应",
    u"二尖瓣狭窄",
    u"慢阻肺",
    u"腱鞘囊肿",
    u"胆囊结石",
    u"胸膜炎",
    u"尤文肉瘤",
    u"儿童中耳炎",
    u"腮腺炎",
    u"神经母细胞瘤",
    u"冠心病",
    u"三高症",
    u"离婚",
    u"脑梗塞",
    u"中耳炎",
    u"化脓性脑膜炎",
    u"嗜酸性粒细胞增多症",
    u"脊柱侧弯",
    u"肠粘连",
    u"胸腺瘤",
    u"疟疾",
    u"三叉神经痛",
    u"粟丘疹",
    u"肺水肿",
    u"家庭心理问题",
    u"功能性子宫出血",
    u"神经性耳聋",
    u"结节病",
    u"神经炎",
    u"儿童鼻窦炎",
    u"肛瘘",
    u"口腔扁平苔藓",
    u"老年病",
    u"性早熟",
    u"急性鼻炎",
    u"颅咽管瘤",
    u"新生儿黄疸",
    u"延迟性心因性反应",
    u"急性胃炎",
    u"水电解质紊乱和酸碱平衡",
    u"除皱",
    u"瘢痕疙瘩",
    u"恙虫病",
    u"Behcet病",
    u"多发性肌炎",
    u"口腔粘膜病",
    u"脊髓空洞症",
    u"脑电图",
    u"颞下颌关节紊乱病",
    u"外阴癌",
    u"甲减",
    u"鼻炎",
    u"亲子关系",
    u"疝",
    u"隐睾",
    u"鼻出血",
    u"慢性结肠炎",
    u"小儿疱疹性口炎",
    u"血液病",
    u"肺纤维化",
    u"家庭暴力",
    u"早恋",
    u"内眦赘皮",
    u"过敏性鼻炎",
    u"颅内压增高",
    u"膀胱癌",
    u"牙齿美白",
    u"类风湿性关节炎",
    u"甲状旁腺机能亢进",
    u"耳聋",
    u"牙痛",
    u"白喉",
    u"网瘾",
    u"酒精性脂肪肝",
    u"感冒",
    u"小儿感冒",
    u"脑炎",
    u"川崎病",
    u"骨结核病",
    u"视神经萎缩",
    u"人流",
    u"肾母细胞瘤",
    u"前置胎盘",
    u"矽肺",
    u"甲肝",
    u"试管婴儿",
    u"脑震荡",
    u"急性会厌炎",
    u"心理咨询",
    u"口腔白斑病",
    u"脑供血不足",
    u"胎停",
    u"发作性睡病",
    u"肝豆状核变性",
    u"流感",
    u"拔牙",
    u"矮小症",
    u"子宫畸形",
    u"生涯规划",
    u"异位性皮炎",
    u"药物性皮炎",
    u"失血性休克",
    u"滑囊炎",
    u"猩红热",
    u"风湿性心脏病",
    u"肠胃炎",
    u"慢性喉炎",
    u"日光性皮炎",
    u"胎盘早剥",
    u"钩虫病",
    u"慢性肾功能衰竭",
    u"狂犬病",
    u"急性扁桃体炎",
    u"结核性胸膜炎",
    u"多形性腺瘤",
    u"疖",
    u"疼痛",
    u"神经性皮炎",
    u"小儿弱视",
    u"乙脑",
    u"早泄",
    u"人格障碍",
    u"小儿支气管炎",
    u"心脏神经官能症",
    u"腰痛",
    u"气性坏疽",
    u"骨囊肿",
    u"卵巢癌",
    u"丹毒",
    u"坏死性筋膜炎",
    u"脂肪肝",
    u"补牙",
    u"急性咽炎",
    u"天花",
    u"小儿先天性髋关节脱位",
    u"孕前检查",
    u"听神经瘤",
    u"黄斑裂孔",
    u"皮脂腺囊肿",
    u"新生儿听力筛查",
    u"鼻咽癌",
    u"心肌缺血",
    u"烤瓷牙",
    u"晕厥",
    u"斜视",
    u"窦性心律不齐",
    u"马凡氏综合征",
    u"流行性出血热",
    u"胰腺囊肿",
    u"牙龈炎",
    u"艾森曼格综合征",
    u"鳞状细胞癌",
    u"小儿败血症",
    u"骨软骨瘤",
    u"布氏杆菌病",
    u"梦游症",
    u"股疝",
    u"克汀病",
    u"头晕",
    u"妇科炎症",
    u"心肌梗死",
    u"胎儿窘迫",
    u"前列腺炎",
    u"高血压肾病",
    u"隆鼻",
    u"突发性聋",
    u"运动神经元病",
    u"脐疝",
    u"成人斯蒂尔病",
    u"牙周炎",
    u"婚外恋",
    u"去眼袋",
    u"子宫内膜炎",
    u"应激性溃疡",
    u"病毒性心肌炎",
    u"皮肤过敏",
    u"多发性硬化",
    u"踝部扭伤",
    u"小儿急性喉炎",
    u"视神经炎",
    u"血管瘤",
    u"阻生齿",
    u"小儿斜视",
    u"IGA肾病",
    u"羊水栓塞",
    u"鸡胸",
    u"紫癜性肾炎",
    u"学习障碍",
    u"蛔虫病",
    u"儿童保健",
    u"牙龈瘤",
    u"帕金森",
    u"肾错构瘤",
    u"冠状动脉造影",
    u"脉管炎",
    u"慢性浅表性胃炎",
    u"房室传导阻滞",
    u"肾囊肿",
    u"卵巢早衰",
    u"高钾血症",
    u"甲亢",
    u"胃溃疡",
    u"肾癌",
    u"激素依赖性皮炎",
    u"丝虫病",
    u"酒精肝",
    u"白带异常",
    u"特发性震颤",
    u"腰椎管狭窄",
    u"结缔组织病",
    u"巨乳症",
    u"耵聍栓塞",
    u"急性短暂性精神障碍",
    u"月经失调",
    u"发烧",
    u"阴茎延长",
    u"牙周病",
    u"骨瘤",
    u"腹痛",
    u"脚气",
    u"植发",
    u"传染性单核细胞增多症",
    u"新生儿缺氧缺血性脑病",
    u"病态窦房结综合征",
    u"皮脂腺痣",
    u"植物神经紊乱",
    u"褥疮",
    u"先兆流产",
    u"黑热病",
    u"低钠血症",
    u"阳痿",
    u"脑血管畸形",
    u"脑水肿",
    u"霰粒肿",
    u"小儿肠炎",
    u"颈动脉狭窄",
    u"甲沟炎",
    u"性心理障碍",
    u"非典",
    u"侵蚀性葡萄胎",
    u"亚健康",
    u"纤维瘤",
    u"静脉炎",
    u"扁平足",
    u"小儿癫痫",
    u"睾丸扭转",
    u"一氧化碳中毒",
    u"莱姆病",
    u"窦性心动过缓",
    u"舌下腺囊肿",
    u"前庭大腺囊肿",
    u"小三阳",
    u"肝内胆管结石",
    u"脑出血",
    u"地图舌",
    u"葡萄胎",
    u"产后风湿",
    u"失恋",
    u"梦魇",
    u"癔症",
    u"子宫破裂",
    u"肠瘘",
    u"色素痣",
    u"耳鸣",
    u"网球肘",
    u"腮腺混合瘤",
    u"习惯性流产",
    u"白塞氏病",
    u"腰肌劳损",
    u"眼底病",
    u"腹股沟疝",
    u"肠痉挛",
    u"胆管结石",
    u"风湿性多肌痛",
    u"骨质增生",
    u"咳嗽",
    u"黑色素瘤",
    u"甲状腺瘤",
    u"维生素A缺乏病",
    u"胆汁反流性胃炎",
    u"心理障碍",
    u"心脏瓣膜性疾病",
    u"尘肺",
    u"粘多糖代谢障碍",
    u"慢性胃炎",
    u"出血性脑卒中",
    u"黑痣",
    u"小儿疱疹性咽峡炎",
    u"脑膜瘤",
    u"桥本甲状腺炎",
    u"屈光不正",
    u"多发性神经纤维瘤",
    u"免疫缺陷病",
    u"隆胸",
    u"短暂性脑缺血发作",
    u"皮肤癌",
    u"心身疾病",
    u"职业发展",
    u"宫颈锥切术",
    u"副乳",
    u"人工授精",
    u"厌学",
    u"噬血细胞综合征",
    u"烫伤",
    u"圆锥角膜",
    u"骨膜炎",
    u"心肌桥",
    u"脑栓塞",
    u"尿失禁",
    u"克山病",
    u"横纹肌肉瘤",
    u"宫外孕",
    u"喉癌",
    u"社交恐惧症",
    u"预激综合征",
    u"胶质瘤",
    u"夜惊",
    u"肝衰竭",
    u"病毒性脑炎",
    u"动脉硬化闭塞症",
    u"丙肝",
    u"牙龈萎缩",
    u"情感障碍",
    u"胆囊息肉",
    u"畸胎瘤",
    u"过敏性休克",
    u"狼疮性肾炎",
    u"自身免疫性肝病",
    u"阵发性室上性心动过速",
    u"烟酸缺乏病",
    u"骨癌",
    u"输尿管结石",
    u"手足皲裂",
    u"巩膜炎",
    u"败血症",
    u"慢性咽炎",
    u"苯丙酮尿症",
    u"反应性关节炎",
    u"内分泌失调",
    u"胫骨平台骨折",
    u"太田痣",
    u"脾破裂",
    u"腱鞘炎",
    u"变性手术",
    u"皮肤纤维瘤",
    u"舌系带过短",
    u"高胆固醇血症",
    u"红皮病",
    u"牙髓炎",
    u"结节性红斑",
    u"慢性鼻炎",
    u"乳腺纤维瘤",
    u"尿道下裂",
    u"基底细胞癌",
    u"脂肪瘤",
    u"体癣",
    u"先天性喉喘鸣",
    u"强迫症",
    u"关节镜",
    u"喉炎",
    u"原发孔型房间隔缺损",
    u"单亲儿童心理问题",
    u"体检",
    u"睡眠呼吸暂停综合征",
    u"肩关节脱位",
    u"室性心动过速",
    u"近视",
    u"躁郁症",
    u"唇腭裂",
    u"筋膜炎",
    u"桡神经损伤",
    u"宫腔镜",
    u"咽炎",
    u"心包积液",
    u"进行性肌营养不良症",
    u"声带小结",
    u"脑动脉硬化",
    u"妊高症",
    u"头痛",
    u"脑血管病",
    u"食道癌",
    u"羊水穿刺",
    u"慢性淋巴结炎",
    u"流行性脑脊髓膜炎",
    u"龋齿",
    u"Graves病",
    u"百日咳",
    u"X型腿",
    u"黄疸",
    u"失眠",
    u"附睾炎",
    u"鼻骨骨折",
    u"妇科检查",
    u"会厌囊肿",
    u"男性乳房肥大",
    u"淋巴结炎",
    u"腹腔镜手术",
    u"腓总神经损伤",
    u"义眼",
    u"酒糟鼻",
    u"脊柱裂",
    u"低钾血症",
    u"包皮龟头炎",
    u"坐骨神经痛",
    u"腰腿痛",
    u"胃肠道间质瘤",
    u"肾功能衰竭",
    u"小儿鼻炎",
    u"早产",
    u"鼻中隔偏曲",
    u"臂丛神经损伤",
    u"髌骨骨折",
    u"高血压脑病",
    u"伤寒",
    u"皮肤瘙痒",
    u"乙肝",
    u"口腔修复",
    u"慢性萎缩性胃炎",
    u"产前检查",
    u"声带息肉",
    u"卵巢囊肿",
    u"结节性硬化症",
    u"老年斑",
    u"二尖瓣关闭不全",
    u"睡眠障碍",
    u"外耳道炎",
    u"青光眼",
    u"华支睾吸虫病",
    u"软骨瘤",
    u"低血压",
    u"引产",
    u"脂膜炎",
    u"弓形虫病",
    u"视网膜脱落",
    u"不孕不育",
    u"弥散性血管内凝血",
    u"扁平苔藓",
    u"老年痴呆",
    u"隐翅虫皮炎",
    u"酒精中毒",
    u"尺神经损伤",
    u"水痘",
    u"腕管综合征",
    u"肩周炎",
    u"子宫内膜增生",
    u"散光",
    u"胆脂瘤型中耳炎",
    u"钩端螺旋体病",
    u"心肌炎",
    u"神经官能症",
    u"扩张型心肌病",
    u"破伤风",
    u"反流性食管炎",
    u"成骨不全",
    u"早孕反应",
    u"子宫腺肌症",
    u"远视",
    u"细菌性阴道炎",
    u"甲状腺腺瘤",
    u"翼状胬肉",
    u"先天性耳前瘘管",
    u"开眼角",
    u"放疗",
    u"神经原性膀胱",
    u"胃病",
    u"胃穿孔",
    u"痴呆",
    u"躁狂症",
    u"外阴白斑",
    u"疤痕",
    u"烟雾病",
    u"结肠癌",
    u"嗜睡症",
    u"风疹",
    u"隐匿性肾小球肾炎",
    u"无脑儿",
    u"霉菌性阴道炎",
    u"股癣",
    u"滑膜炎",
    u"偏头痛",
    u"输卵管堵塞",
    u"子宫内膜息肉",
    u"低血容量性休克",
    u"血吸虫病",
    u"热射病",
    u"肾结核",
    u"幼儿急疹",
    u"腋臭",
    u"主动脉瓣关闭不全",
    u"子宫颈息肉",
    u"水中毒",
    u"铅中毒",
    u"智力障碍",
    u"干眼症",
    u"先天愚型",
    u"泪囊炎",
    u"高脂血症",
    u"性施虐症与性受虐症",
    u"小儿疝气",
    u"鼻窦炎",
    u"脚气病",
    u"先天性肾上腺皮质增生症",
    u"更年期综合症",
    u"鹅口疮",
    u"植物人",
    u"胆结石",
    u"老花眼",
    u"视网膜母细胞瘤",
    u"休克",
    u"偏瘫",
    u"神经衰弱",
    u"人工关节置换术",
    u"窦性心动过速",
    u"跟腱断裂",
    u"高泌乳素血症",
    u"根管治疗",
    u"肝癌介入",
    u"剖腹产",
    u"肝腹水",
    u"头虱",
    u"麦粒肿",
    u"脑外伤",
    u"房颤",
    u"输卵管炎",
    u"根尖周炎",
    u"小儿多动症",
    u"肋间神经痛",
    u"三尖瓣关闭不全",
    u"眼球震颤",
    u"鲜红斑痣",
    u"高钠血症",
    u"神经性呕吐",
    u"心衰",
    u"尿毒症",
    u"小儿腺样体肥大",
    u"梨状肌综合征",
    u"肛周脓肿",
    u"骨髓移植",
    u"恐惧症",
    u"雷诺综合征",
    u"股骨头坏死",
    u"胎膜早破",
    u"脑血栓",
    u"胸膜间皮瘤",
    u"角膜炎",
    u"急性肠炎",
    u"先天性髋关节脱位",
    u"腺性膀胱炎",
    u"胃下垂",
    u"面肌痉挛",
    u"产后抑郁",
    u"萎缩性鼻炎",
    u"骶管囊肿",
    u"躯体形式障碍",
    u"截瘫",
    u"小儿哮喘",
    u"急性支气管炎",
    u"脑疝",
    u"白内障",
    u"肝脓肿",
    u"慢性扁桃体炎",
    u"痣",
    u"高甘油三酯血症",
    u"病毒性脑膜炎",
    u"附件炎",
    u"鼓膜穿孔",
    u"口腔溃疡",
    u"二尖瓣脱垂综合症",
    u"癫痫",
    u"宫颈糜烂",
    u"阴虱",
    u"自闭症",
    u"结膜炎",
    u"绒毛膜癌",
    u"贲门失驰症",
    u"慢性房颤",
    u"房性早搏",
    u"肠套叠",
    u"痈",
    u"葡萄膜炎",
    u"倒睫",
    u"四环素牙",
    u"角膜移植",
    u"O型腿",
    u"慢性化脓性中耳炎",
    u"枕神经痛",
    u"玻璃体混浊",
    u"花粉症",
    u"中医减肥",
    u"舌癌",
    u"关节炎",
    u"骨肉瘤",
    u"鼻息肉",
    u"血管性痴呆",
    u"阴道紧缩",
    u"胆管癌",
    u"近视眼手术",
    u"分泌性中耳炎",
    u"夏季皮炎",
    u"婆媳关系",
    u"下肢静脉血栓",
    u"胃出血",
    u"风湿性关节炎",
    u"膀胱炎",
    u"急性肾功能衰竭",
    u"尿结石",
    u"不安腿综合症",
    u"急性喉炎",
    u"胆囊癌",
    u"鸡眼",
    u"炭疽",
    u"室性早搏",
    u"小儿咳嗽",
    u"黄斑变性",
    u"急性化脓性中耳炎",
    u"慢性肝炎",
    u"螨皮炎",
    u"小儿脑瘫",
    u"神经性厌食症",
    u"乳腺增生",
    u"禽流感",
    u"新生儿败血症",
    u"脊髓小脑变性症",
    u"肝包虫病",
    u"登革热",
    u"髋关节脱位",
    u"急性脊髓炎",
    u"真菌性皮肤病",
    u"上睑下垂",
    u"心脏搭桥",
    u"灰指甲",
    u"精囊炎",
    u"风湿热",
    u"副伤寒",
    u"韧带损伤",
    u"蛲虫病",
    u"心脏瓣膜手术",
    u"大三阳",
    u"霍乱",
    u"睾丸癌",
    u"面部吸脂",
    u"非器质性性交疼痛",
    u"急性房颤",
    u"格林巴利综合征",
    u"感染性休克",
    u"小脑萎缩",
    u"房间隔缺损",
    u"主动脉瓣狭窄",
    u"漏斗胸",
    u"肌张力障碍",
    u"肝血管瘤",
    u"面瘫",
    u"双眼皮手术",
]


# 未在任何一个文档出现的疾病名称
unknown = [
    u"口腔修复",
    u"酒糟鼻",
    u"桡神经损伤",
    u"小儿支气管炎",
    u"原发孔型房间隔缺损",
    u"牙痛",
    u"马凡氏综合征",
    u"急性会厌炎",
    u"妊高症",
    u"去眼袋",
    u"麦粒肿",
    u"会厌囊肿",
    u"乳腺纤维瘤",
    u"小儿多动症",
    u"不孕不育",
    u"离婚",
    u"肝癌介入",
    u"老年痴呆",
    u"踝部扭伤",
    u"阻生齿",
    u"变性手术",
    u"股疝",
    u"高泌乳素血症",
    u"唇腭裂",
    u"动脉硬化闭塞症",
    u"牙齿美白",
    u"声带小结",
    u"小儿支气管肺炎",
    u"O型腿",
    u"小儿疱疹性口炎",
    u"新生儿巨细胞病毒感染",
    u"进行性肌营养不良症",
    u"产后抑郁",
    u"心脏瓣膜性疾病",
    u"开眼角",
    u"视网膜母细胞瘤",
    u"性施虐症与性受虐症",
    u"视网膜脱落",
    u"先天性耳前瘘管",
    u"激素依赖性皮炎",
    u"小儿腺样体肥大",
    u"噬血细胞综合征",
    u"上睑下垂",
    u"儿童鼻窦炎",
    u"老年斑",
    u"腱鞘囊肿",
    u"婚外恋",
    u"鼻前庭炎",
    u"IGA肾病",
    u"产后风湿",
    u"胃下垂",
    u"外阴白斑",
    u"烤瓷牙",
    u"近视眼手术",
    u"网瘾",
    u"职业发展",
    u"高血压肾病",
    u"梦游症",
    u"牙周病",
    u"儿童中耳炎",
    u"梨状肌综合征",
    u"孕前检查",
    u"肠胃炎",
    u"义眼",
    u"心脏搭桥",
    u"小儿鼻炎",
    u"口腔粘膜病",
    u"补牙",
    u"牙龈癌",
    u"羊水穿刺",
    u"新生儿呕吐",
    u"厌学",
    u"双眼皮手术",
    u"小脑萎缩",
    u"成人斯蒂尔病",
    u"髋关节脱位",
    u"先天性喉喘鸣",
    u"小儿癫痫",
    u"慢性喉炎",
    u"结节性硬化症",
    u"乙脑",
    u"小儿脑瘫",
    u"亲子关系",
    u"人工耳蜗",
    u"小儿先天性髋关节脱位",
    u"小儿咳嗽",
    u"小儿湿疹",
    u"隆胸",
    u"老花眼",
    u"小儿感冒",
    u"肝腹水",
    u"亚健康",
    u"颞下颌关节紊乱病",
    u"网恋",
    u"小儿斜视",
    u"自闭症",
    u"单亲儿童心理问题",
    u"大三阳",
    u"更年期综合症",
    u"神经原性膀胱",
    u"宫颈癌前病变",
    u"肛瘘",
    u"三高症",
    u"新生儿听力筛查",
    u"声带息肉",
    u"髌骨骨折",
    u"妇科炎症",
    u"小三阳",
    u"散光",
    u"二尖瓣脱垂综合症",
    u"牙周炎",
    u"延迟性心因性反应",
    u"口腔白斑病",
    u"黄斑裂孔",
    u"早恋",
    u"X型腿",
    u"梦魇",
    u"霰粒肿",
    u"倒睫",
    u"家庭心理问题",
    u"子宫颈息肉",
    u"格林巴利综合征",
    u"花粉症",
    u"学习障碍",
    u"婆媳关系",
    u"烟酸缺乏病",
    u"泪囊炎",
    u"小儿哮喘",
    u"小儿弱视",
    u"腹股沟疝",
    u"儿童白血病",
    u"子宫腺肌症",
    u"阴茎延长",
    u"过敏性结膜炎",
    u"食道癌",
    u"玻璃体混浊",
    u"突发性聋",
    u"舌癌",
    u"甲状旁腺机能亢进",
    u"植物神经紊乱",
    u"面部吸脂",
    u"贲门失驰症",
    u"骶管囊肿",
    u"非器质性性交疼痛",
    u"耵聍栓塞",
    u"先天性髋关节脱位",
    u"舌下腺囊肿",
    u"牙龈萎缩",
    u"喉神经纤维瘤",
    u"房性早搏",
    u"神经性呕吐",
    u"小儿肠炎",
    u"甲肝",
    u"舌系带过短",
    u"根管治疗",
    u"社交恐惧症",
    u"小儿疝气",
    u"膝关节半月板损伤",
    u"弱视",
    u"多形性腺瘤",
    u"枕神经痛",
    u"粘多糖代谢障碍",
    u"糖尿病神经病变",
    u"糖尿病足",
    u"急性短暂性精神障碍",
    u"霉菌性阴道炎",
    u"牙龈瘤",
    u"白塞氏病",
    u"远视",
    u"小儿急性喉炎",
    u"阴道紧缩",
    u"骨癌",
    u"神经性厌食症",
    u"莱姆病",
    u"银屑病性关节炎",
    u"特发性震颤",
    u"小叶性肺炎",
    u"急性化脓性中耳炎",
    u"牙髓炎",
    u"酒精肝",
    u"胆脂瘤型中耳炎",
    u"鼓膜内陷",
    u"黄斑变性",
    u"小儿疱疹性咽峡炎",
    u"萎缩性鼻炎",
    u"家庭暴力",
    u"根尖周炎",
    u"地图舌",
    u"心脏瓣膜手术",
    u"小儿肺炎支原体肺炎",
    u"克汀病",
    u"生涯规划",
    u"中医减肥",
    u"不安腿综合症",
    u"急性脊髓炎",
    u"巨乳症",
    u"肾错构瘤",
    u"小儿败血症",
    u"脊髓小脑变性症",
    u"角膜移植",
    u"男性乳房肥大",
    u"跟腱断裂",
    u"水电解质紊乱和酸碱平衡",
    u"灰指甲",
    u"鼻骨骨折",
    u"糖尿病视网膜病变",
    u"外耳湿疹",
    u"干眼症",
    u"腓总神经损伤",
    u"圆锥角膜",
    u"分泌性中耳炎",
]
