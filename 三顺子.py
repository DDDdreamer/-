def SanShunZi(cards):
    card_dic = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0, 'A': 0}
    card_list = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    #对手牌进行排列，凑出顺子阵容
    for lst_i in cards:
        # l = lst_i.strip('*')
        # l = lst_i.strip('#')
        # l = lst_i.strip('$')
        # l = lst_i.strip('&')
        card_dic[lst_i[1:]] += 1

    new_pai = []
    count = 13
    while(count):
        pai = ""
        for i in range(13):
            if card_dic[card_list[i]] != 0:
                pai += card_list[i]
                card_dic[card_list[i]] -= 1
                count -= 1
        if pai != "":
            new_pai.append(pai)

    new_shoupai = new_pai[0]
    for i in range(1,len(new_pai)):
        l = len(new_pai[i])
        f = new_shoupai.find(new_pai[i])
        if f != -1:
            new_shoupai = new_shoupai[:f + l] + new_pai[i] + new_shoupai[f + l:]

    ###判断是否为三顺子
    shunzi_5 = ['23456', '34567', '45678', '56789', '678910', '78910J', '8910JQ', '910JQK', '10JQKA']
    shunzi_3 = ['234', '345', '456', '567', '678', '789', '8910', '910J', '10JQ', 'JQK', 'QKA']
    shun3 = ""
    shun5 = ""
    for shunzi3 in shunzi_3:
        new_shoupai_copy = new_shoupai
        shunzi_3_num = 0
        shunzi_5_num = 0
        if new_shoupai_copy.find(shunzi3) != -1:
            shunzi_3_num += 1
            #shun3 = shunzi3
            new_shoupai_copy2 = new_shoupai_copy.replace(shunzi3,"")
            for shunzi5 in shunzi_5:
                if new_shoupai_copy2.find(shunzi5) != -1:
                    new_shoupai_copy2 = new_shoupai_copy2.replace(shunzi5,"")
                    shunzi_5_num += 1
                    #shun5 += shunzi5
                    if shunzi_3_num == 1 and shunzi_5_num == 2:
                        return True
    return False
