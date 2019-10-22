from sort_cards import *
from compare_cards import *
from itertools import *
from copy import *

def item_delete(items, cards):
    Cards = copy(cards)
    for item in items:
        Cards.remove(item)
    return Cards

#算法思想：利用组合的思想对所有牌型进行比较，择取最优牌型
def best_cards_type(cards):
    Cards_s = sort_Cards(cards)
    #Cards_s = cards
    best_cards = {}
    cur_cards = {}
    for shangdun in combinations(Cards_s,3):
        cur_shangdun = list(shangdun)
        cur_cards['shangdun'] = cur_shangdun
        Cards_ss = item_delete(cur_shangdun, copy(Cards_s))
        for zhongdun in combinations(Cards_ss, 5):
            cur_zhongdun = list(zhongdun)
            cur_cards['zhongdun'] = cur_zhongdun
            cur_xiadun  = item_delete(cur_zhongdun, copy(Cards_ss))
            cur_cards['xiadun'] = cur_xiadun
            cur_cards['type'] = ""
            if len(best_cards) == 0:
               if isleagle(cur_cards)[0]:
                   best_cards = copy(cur_cards)
                   best_cards['type'] = [cards_type(best_cards['shangdun'])[0], cards_type(best_cards['zhongdun'])[0],cards_type(best_cards['xiadun'])[0]]

            else:
                cur_res = Compare(best_cards,cur_cards)
                if cur_res[0]:
                    best_cards = copy(cur_res[1])

    shang = ""
    zhong = ""
    xia = ""
    best_cards_Type = []
    shang += best_cards['shangdun'][0] + ' ' + best_cards['shangdun'][1] + ' ' + best_cards['shangdun'][2]
    zhong += best_cards['zhongdun'][0] + ' ' + best_cards['zhongdun'][1] + ' ' + best_cards['zhongdun'][2] + ' ' + best_cards['zhongdun'][3] + ' ' + best_cards['zhongdun'][4]
    xia += best_cards['xiadun'][0] + ' ' + best_cards['xiadun'][1] + ' ' + best_cards['xiadun'][2] + ' ' + best_cards['xiadun'][3] + ' ' + best_cards['xiadun'][4]
    best_cards_Type.append(shang)
    best_cards_Type.append(zhong)
    best_cards_Type.append(xia)
    print(best_cards)
    return best_cards_Type

