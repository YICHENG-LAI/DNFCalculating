from math import *
from PublicReference.base import *

class 缔造者技能0(主动技能):
    名称 = '烈火燎原'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    基础 = 810
    成长 = 261
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 7

class 缔造者技能1(主动技能):
    名称 = '炽炎星陨'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    基础 = 1057
    成长 = 238
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 7

class 缔造者技能2(主动技能):
    名称 = '冰霜之球'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 1764
    成长 = 210
    CD = 10.0
    TP成长 = 0.08
    TP上限 = 7


class 缔造者技能3(主动技能):
    名称 = '冰天震地'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 3406
    成长 = 470
    CD = 10.0
    TP成长 = 0.08
    TP上限 = 7


class 缔造者技能4(被动技能):
    名称 = '幻想之境'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.01 * self.等级 , 5)


class 缔造者技能5(被动技能):
    名称 = '具象强化'
    所在等级 = 25
    等级上限 = 40
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.025 * self.等级, 5)


class 缔造者技能6(主动技能):
    名称 = '烈焰飓风'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4980
    成长 = 504
    CD = 20
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.0

class 缔造者技能7(主动技能):
    名称 = '极冰护盾'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2579
    成长 = 261
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7

class 缔造者技能8(主动技能):
    名称 = '超能旋风波'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 11594
    成长 = 1190
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.23

class 缔造者技能9(主动技能):
    名称 = '风暴漩涡'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 10024
    成长 = 1014
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 7


class 缔造者技能10(被动技能):
    名称 = '洞悉'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.02 * self.等级, 5)



class 缔造者技能11(主动技能):
    名称 = '末日虫洞'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 19
    基础 = 13788
    成长 = 2175
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.20

class 缔造者技能12(主动技能):
    名称 = '冰雪降临'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 36
    基础 = 28650
    成长 = 2175
    CD = 31.5
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.28


class 缔造者技能13(主动技能):
    名称 = '时空链接'
    所在等级 = 70
    等级上限 = 60
    基础等级 = 36
    基础 = 55964
    成长 = 5642
    CD = 54
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.24


class 缔造者技能14(被动技能):
    名称 = '创世之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.02 * self.等级, 5)


class 缔造者技能15(主动技能):
    名称 = '时空禁制'
    所在等级 = 80
    等级上限 = 60
    基础等级 = 9
    基础 = 42361
    成长 = 6737
    CD = 45.0



class 缔造者技能16(主动技能):
    名称 = '创世'
    所在等级 = 85
    等级上限 = 60
    基础等级 = 5
    基础 = 110508
    成长 = 25644
    CD = 180.0

class 缔造者技能17(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 缔造者技能18(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 缔造者技能19(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


缔造者技能列表 = []
i = 0
while i >= 0:
    try:
        exec('缔造者技能列表.append(缔造者技能' + str(i) + '())')
        i += 1
    except:
        i = -1

缔造者技能序号 = dict()
for i in range(len(缔造者技能列表)):
    缔造者技能序号[缔造者技能列表[i].名称] = i

缔造者一觉序号 = 16
缔造者二觉序号 = 16
缔造者三觉序号 = 19

缔造者护石选项 = ['无']
for i in 缔造者技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        缔造者护石选项.append(i.名称)

缔造者符文选项 = ['无']
for i in 缔造者技能列表:
    if i.所在等级 >= 1 and i.所在等级 <= 75  and i.是否有伤害 == 1:
        缔造者符文选项.append(i.名称)


class 缔造者角色属性(角色属性):
    职业名称 = '缔造者'

    武器选项 = ['魔杖','法杖','棍棒','矛','扫把']

    # '物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法固伤']

    # 默认
    伤害类型 = '魔法固伤'
    防具类型 = '板甲'
    防具精通属性 = ['智力']

    主BUFF = 1.66

    # 基础属性(含唤醒)
    基础力量 = 819.0
    基础智力 = 926.0

    # 适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    # 人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    远古记忆 = 0

    def __init__(self):
        self.技能栏 = deepcopy(缔造者技能列表)
        self.技能序号 = deepcopy(缔造者技能序号)

class 缔造者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 缔造者角色属性()
        self.角色属性A = 缔造者角色属性()
        self.角色属性B = 缔造者角色属性()
        self.一觉序号 = 缔造者一觉序号
        self.二觉序号 = 缔造者二觉序号
        self.三觉序号 = 缔造者三觉序号
        self.护石选项 = deepcopy(缔造者护石选项)
        self.符文选项 = deepcopy(缔造者符文选项)
