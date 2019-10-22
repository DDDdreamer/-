#牌型大小：同花顺 > 炸弹 > 葫芦 > 同花 > 顺子 > 三条 > 两对 > 一对 > 散牌
from shunzi_judge import *
from copy import *
def quhuase(cards):#去花色
    new_cards = []
    for card in cards:
        card = card.strip('*')
        card = card.strip('#')
        card = card.strip('$')
        card = card.strip('&')
        new_cards.append(card)
    return new_cards

def isyidui(cards, l):          #是否为一对
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    duizi = []
    danpai = []
    danpai_num = 0
    duizi_num = 0
    for card in cards:
        # card = card.strip('*')
        # card = card.strip('#')
        # card = card.strip('$')
        # card = card.strip('&')
        card = card[1:]
        card_dic[card] += 1
        if card_dic[card] == 1:
            danpai.append(card)
            danpai_num += 1
        elif card_dic[card] == 2:
            danpai.pop(-1)
            danpai_num -= 1
            duizi_num += 1
            duizi.append(card)
        elif card_dic[card] > 2:
            return [False, duizi, danpai]
    if l == 3:
        if danpai_num == 1 and duizi_num == 1:
            return [True, duizi, danpai]
    elif l == 5:
        if danpai_num == 3 and duizi_num == 1:
            return [True, duizi, danpai]
    return [False, duizi, danpai]

def isliangdui(cards):
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    duizi = []
    danpai = []
    danpai_num = 0
    duizi_num = 0
    for l in cards:
        # l = l.strip('*')
        # l = l.strip('#')
        # l = l.strip('$')
        # l = l.strip('&')
        l = l[1:]
        card_dic[l] += 1
        if card_dic[l] == 1:
            danpai.append(l)
            danpai_num += 1
        elif card_dic[l] == 2:
            danpai.pop(-1)
            danpai_num -= 1
            if l in duizi:
                return [False, duizi, danpai,""]
            else:
                duizi_num += 1
                duizi.append(l)
        elif card_dic[l] > 2:
            return [False, duizi, danpai,""]
    if duizi_num == 2 and danpai_num == 1:
        if duizi in [['2','3'],['3','4'],['4','5'],['5','6'],['6','7'],['7','8'],['8','9'],['9','10'],['10','J'],['J','Q'],['Q','K'],['K','A']]:
            return [True, duizi ,danpai, "连对"]
        else:
            return [True, duizi, danpai, "两对"]
    return [False, duizi, danpai, ""]

def issantiao(cards, l):       #是否为三条
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    danpai = []
    santiao = []
    danpai_num = 0
    santiao_num = 0
    for card in cards:
        # card = card.strip('*')
        # card = card.strip('#')
        # card = card.strip('$')
        # card = card.strip('&')
        card = card[1:]
        card_dic[card] += 1
        if card_dic[card] == 1:
            danpai.append(card)
            danpai_num += 1
        elif card_dic[card] == 3:
            danpai.pop(-1)
            danpai_num -= 1
            santiao.append(card)
            santiao_num += 1
        elif card_dic[card] > 3:
            return [False, santiao, danpai]

    if l == 3:
        if santiao_num == 1 and danpai_num == 0:
            return [True, santiao, danpai]
    elif l == 5:
        if santiao_num == 1 and danpai_num == 2:
            return [True, santiao, danpai]
    return [False, santiao, danpai]

def isshunzi(cards):            #判断是否为顺子
    pai = ""
    for card in cards:
        # card = card.strip('*')
        # card = card.strip('#')
        # card = card.strip('$')
        # card = card.strip('&')
        card = card[1:]
        pai += card
    if ShunZi_Judge(pai,len(cards)) > 0:
        return True
    return False

def istonghua(cards):           #是否为同花
    huase = []
    for card in cards:
        if card[0] not in huase:
            if len(huase) == 0:
                huase.append(card[0])
            else:
                return False
    return True

def ishulu(cards):              #判断是否为葫芦
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    duizi = []
    santiao = []
    duizi_num = 0
    santiao_num = 0
    for l in cards:
        # l = l.strip('*')
        # l = l.strip('#')
        # l = l.strip('$')
        # l = l.strip('&')
        l = l[1:]
        card_dic[l] += 1
        if card_dic[l] == 2:
            duizi.append(l)
            duizi_num += 1
        elif card_dic[l] == 3:
            duizi.pop(-1)
            duizi_num -= 1
            santiao.append(l)
            santiao_num += 1
        elif card_dic[l] > 3:
            return [False, santiao, duizi]

    if santiao_num == 1 and duizi_num == 1:
        return [True, santiao, duizi]
    return [False, santiao, duizi]

def isboom(cards):              #判断是否为炸弹
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    danpai = []
    boom = []
    danpai_num = 0
    boom_num = 0
    for l in cards:
        # l = l.strip('*')
        # l = l.strip('#')
        # l = l.strip('$')
        # l = l.strip('&')
        l = l[1:]
        card_dic[l] += 1
        if card_dic[l] == 1:
            danpai.append(l)
            danpai_num += 1
        elif card_dic[l] == 4:
            danpai.pop(-1)
            danpai_num -= 1
            boom.append(l)
            boom_num += 1

    if boom_num == 1 and danpai_num == 1:
        return [True, boom, danpai]
    return [False, boom, danpai]

def istonghuashun(cards):       #判断是否为同花顺
    huase_dic = {'*':'','#':'','$':'','&':''}
    len_huase = {'*':0,'#':0,'$':0,'&':0}
    for card in cards:
        huase_dic[card[:1]] += card[1:]
        len_huase[card[:1]] += 1

    for key in huase_dic:
        if huase_dic[key] != '':
            if ShunZi_Judge(huase_dic[key],len_huase[key]) == 5:
                return True
    return False

def cards_type(cards):      #判断每墩牌型
    if len(cards) == 3:
        #判断是否为三条
        case1 = issantiao(cards, 3)
        if case1[0]:
            res = copy(case1[2])
            for i in case1[1]:
                res.append(i)
            return ["三条", case1[1], case1[2], res]

        # 判断是否为一对
        case2 = isyidui(cards, 3)
        if case2[0]:
            res = copy(case2[2])
            for i in case2[1]:
                res.append(i)
            return ["一对", case2[1], case2[2], res]
        #其余情况为散牌
        return ["散牌",cards]
    else:
        if istonghuashun(cards):
            return ["同花顺", cards]

        case1 = isboom(cards)
        if case1[0]:
            res = copy(case1[2])
            for i in case1[1]:
                res.append(i)
            return ["炸弹", case1[1], case1[2], res]

        case2 = ishulu(cards)
        if case2[0]:
            res = copy(case2[2])
            for i in case2[1]:
                res.append(i)
            return ["葫芦", case2[1], case2[2], res]

        if istonghua(cards):
            return ["同花",cards]

        if isshunzi(cards):
            return ["顺子",cards]

        case3 = issantiao(cards, 5)
        if case3[0]:
            res = copy(case3[2])
            for i in case3[1]:
                res.append(i)
            return ["三条", case3[1], case3[2],res]

        case4 = isliangdui(cards)
        if case4[0]:
            res = copy(case4[2])
            for i in case4[1]:
                res.append(i)
            return [case4[3], case4[1], case4[2],res]

        case5 = isyidui(cards, 5)
        if case5[0]:
            res = copy(case5[2])
            for i in case5[1]:
                res.append(i)
            return ["一对", case5[1], case5[2], res]

        return ["散牌", cards]

def cards_cmp(cards1,cards2):  #牌型相同比较牌面大小
    card_dic = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12,'A':13}
    cards1 = quhuase(cards1)
    cards2 = quhuase(cards2)
    l = min(len(cards1),len(cards2))
    for i in range(l - 1, -1, -1):
        if card_dic[cards1[i]] > card_dic[cards2[i]]:
            return -1
        elif card_dic[cards1[i]] < card_dic[cards2[i]]:
            return 1
    if len(cards1) > len(cards2):#较小墩牌较大
        return -1
    elif len(cards1) < len(cards2):#较小墩牌较小
        return 1
    return 0    #牌型相等

def cards_value(cards):
    value = 0.0
    card_dic = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12,'A':13}
    for card in cards:
        card = card.strip('*')
        card = card.strip('#')
        card = card.strip('$')
        card = card.strip('&')
        value += card_dic[card]/100.0
    return value

def isleagle(cards):
    cards_order = {'散牌':0, '一对':1, '两对':2, '连对':3, '三条':4, '顺子':5, '同花':6, '葫芦':7, '炸弹':8, '同花顺':9}
    shangdun_type = cards_type(cards['shangdun'])
    zhongdun_type = cards_type(cards['zhongdun'])
    xiadun_type = cards_type(cards['xiadun'])

    if cards_order[shangdun_type[0]] < cards_order[zhongdun_type[0]]:
        res = 0
        if cards_order[zhongdun_type[0]] < cards_order[xiadun_type[0]]:
            return [True, [shangdun_type[0], zhongdun_type[0], xiadun_type[0]],
                    [shangdun_type, zhongdun_type, xiadun_type]]
        elif cards_order[zhongdun_type[0]]> cards_order[xiadun_type[0]]:
            return [False, []]
        else:
            cards1 = []
            cards2 = []
            if zhongdun_type[0] == "同花顺" or zhongdun_type[0] == "同花" or zhongdun_type[0] == "顺子" or zhongdun_type[0] == "散牌":
                cards1 = cards['zhongdun']
                cards2 = cards['xiadun']
                res = cards_cmp(cards1,cards2)
            else:
                cards1 = zhongdun_type[2]
                for card in zhongdun_type[1]:
                    cards1.append(card)
                cards2 = xiadun_type[2]
                for card in xiadun_type[1]:
                    cards2.append(card)
                res = cards_cmp(cards1,cards2)

            if res == -1 or res == 0:
                return [False,[]]
            else:
                return [True, [shangdun_type[0], zhongdun_type[0], xiadun_type[0]], [shangdun_type, zhongdun_type, xiadun_type]]

    elif cards_order[shangdun_type[0]] == cards_order[zhongdun_type[0]]:
        cards1 = copy(shangdun_type[1])
        cards2 = copy(zhongdun_type[1])
        if cards_cmp(cards1,cards2) == 1:
            if cards_order[zhongdun_type[0]] < cards_order[xiadun_type[0]]:
                return [True, [shangdun_type[0], zhongdun_type[0], xiadun_type[0]],[shangdun_type, zhongdun_type, xiadun_type]]
            elif cards_order[zhongdun_type[0]] > cards_order[xiadun_type[0]]:
                return [False,[]]
            else:
                if zhongdun_type[0] == "同花顺" or zhongdun_type[0] == "同花" or zhongdun_type[0] == "顺子" or zhongdun_type[0] == "散牌":
                    cards1 = cards['zhongdun']
                    cards2 = cards['xiadun']
                    res = cards_cmp(cards1, cards2)
                else:
                    cards1 = zhongdun_type[2]
                    for card in zhongdun_type[1]:
                        cards1.append(card)
                    cards2 = xiadun_type[2]
                    for card in xiadun_type[1]:
                        cards2.append(card)
                    res = cards_cmp(cards1, cards2)
                if res == -1 or res == 0:
                    return [False, []]
                else:
                    return [True, [shangdun_type[0], zhongdun_type[0], xiadun_type[0]],[shangdun_type, zhongdun_type, xiadun_type]]
        else:
            return [False, []]
    return [False,[]]

def Compare(old, new):
    cards_order = {'散牌':10, '一对':20, '两对':30, '连对':40, '三条':50, '顺子':60, '同花':70, '葫芦':80, '炸弹':100, '同花顺':120}

    leagle_new = isleagle(new)#判断牌型是否合法
    if not leagle_new[0]:#牌型不合法
        return [False,[]]
    else:
        new['type'] = leagle_new[1]
        new['info'] = leagle_new[2]
        type_old = old['type']  #原牌牌型
        type_new = new['type']  #新牌牌型
        card_profit = {
            'shangdun':{'散牌':1,'一对':1,"三条":1},
            'zhongdun':{'散牌':1,'一对':1,"两对":1,"连对":1,"三条":1,"顺子":1,"同花":1,"葫芦":2,"炸弹":8,"同花顺":10},
            'xiadun':{'散牌':1,'一对':1,"两对":1,"连对":1,"三条":1,"顺子":1,"同花":1,"葫芦":1,"炸弹":4,"同花顺":5}
        }

        if(old['cards_profit'] == 0.0):
            p1 = p2 = p3 = 0.0
            #计算上墩权值
            if type_old[0] == '散牌':
                p1 = cards_order['散牌'] + cards_value(old['info'][0][1]) * card_profit['shangdun']['散牌']
            else:
                p1 = cards_order[type_old[0]]  + (cards_value(old['info'][0][1])*10.0 + cards_value(old['info'][0][2])) * card_profit['shangdun'][type_old[0]]
            #计算中墩权值
            if type_old[1] == "散牌" or type_old[1] == "同花" or type_old[1] == "顺子" or type_old[1] == "同花顺":
                p2 = cards_order[type_old[1]] + cards_value([old['info'][1][1][-1]]) * card_profit['zhongdun'][type_old[1]]
            else:
                p2 = cards_order[type_old[1]] + (cards_value(old['info'][1][1]) *10 + cards_value(old['info'][1][2])) * card_profit['zhongdun'][type_old[1]]
            #计算下墩权值
            if type_old[2] == "散牌" or type_old[2] == "同花" or type_old[2] == "顺子" or type_old[2] == "同花顺":
                p2 = cards_order[type_old[2]] + cards_value([old['info'][2][1][-1]]) * card_profit['xiadun'][type_old[2]]
            else:
                p2 = cards_order[type_old[2]] + (cards_value(old['info'][2][1]) * 10 + cards_value(old['info'][2][2]) )* card_profit['xiadun'][type_old[2]]
            old['cards_profit'] = p1 + p2 + p3

        p1 = p2 = p3 = 0.0
        # 计算上墩权值
        if type_new[0] == '散牌':
            p1 = cards_order['散牌'] + cards_value(new['info'][0][1]) * card_profit['shangdun']['散牌']
        else:
            p1 = cards_order[type_new[0]] + (cards_value(new['info'][0][1]) * 10.0 + cards_value(new['info'][0][2])) * \
                 card_profit['shangdun'][type_new[0]]
        # 计算中墩权值
        if type_new[1] == "散牌" or type_new[1] == "同花" or type_new[1] == "顺子" or type_new[1] == "同花顺":
            p2 = cards_order[type_new[1]]  + cards_value([new['info'][1][1][-1]]) * card_profit['zhongdun'][
                type_new[1]]
        else:
            p2 = cards_order[type_new[1]]  + (cards_value(new['info'][1][1]) * 10 + cards_value(new['info'][1][2])) * \
                 card_profit['zhongdun'][type_new[1]]
        # 计算下墩权值
        if type_new[2] == "散牌" or type_new[2] == "同花" or type_new[2] == "顺子" or type_new[2] == "同花顺":
            p2 = cards_order[type_new[2]]  + cards_value([new['info'][2][1][-1]]) * card_profit['xiadun'][
                type_new[2]]
        else:
            p2 = cards_order[type_new[2]]  + (cards_value(new['info'][2][1]) * 10 + cards_value(new['info'][2][2])) * \
                 card_profit['xiadun'][type_new[2]]
        new['cards_profit']  = p1 + p2 +p3


        if new['cards_profit']  > old['cards_profit']:
            return [True,new]
        return [False,old]
