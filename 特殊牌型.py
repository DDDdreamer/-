from 至尊青龙 import *
from 一条龙 import *
from 十二皇族 import *
from 三同花顺 import *
from 三分天下 import *
from 全大 import *
from 全小 import *
from 凑一色 import *
from 双怪冲三 import *
from 四套三条 import *
from 五对三条 import *
from 六对半 import *
from 三顺子 import *
from 三同花 import *
from sort_cards import *
#用1-14依次标识特殊牌型
def cards2string(cards):
    shangdun = cards[0] + ' ' + cards[1] + ' ' + cards[2]
    zhongdun = cards[3] + ' ' + cards[4] + ' ' + cards[5] + ' ' + cards[6] + ' ' + cards[7]
    xiadun = cards[8] + ' ' + cards[9] + ' ' + cards[10] + ' ' + cards[11] + ' ' + cards[12]
    return [shangdun, zhongdun, xiadun]

def special_cards_type(cards):
    Cards = sort_Cards(cards)
    best_cards = ""
    if ZhiZunQingLONG(Cards):
        print('1')
        return [True,cards2string(Cards)]
    elif YiTiaoLong(Cards):
        print('2')
        return [True,cards2string(Cards)]
    elif ShiErHuangZu(Cards):
        print('3')
        return [True,cards2string(Cards)]
    elif SanTongHuaShun(Cards):         ###考虑是否要特殊处理
        print('4')
        return [True,cards2string(Cards)]
    elif SanFenTianXia(Cards):
        print('5')
        return [True,cards2string(Cards)]
    elif All_Big(Cards):
        print('6')
        return [True,cards2string(Cards)]
    elif All_Small(Cards):
        print('7')
        return [True,cards2string(Cards)]
    elif CouYiSe(Cards):                ###考虑是否要特殊处理
        print('8')
        return [True,cards2string(Cards)]
    elif ShuangGuaiChongSan(Cards):     ###考虑是否要特殊处理
        print('9')
        return [True,cards2string(Cards)]
    elif SiTaoSanTiao(Cards):
        print('10')
        return [True,cards2string(Cards)]
    elif WuDuiSanTiao(Cards):
        print('11')
        return [True,cards2string(Cards)]
    elif LiuDuiBan(Cards):
        print('12')
        return [True,cards2string(Cards)]
    elif SanShunZi(Cards):
        print('13')
        return [True,cards2string(Cards)]
    elif SanTongHua(Cards):
        print('14')
        return [True,cards2string(Cards)]
    return [False,[]]
