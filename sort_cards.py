def sort_cmp(x):
    sort_dict = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'J':10,'Q':11,'K':12,'A':13}
    x = x.strip('*')
    x = x.strip('#')
    x = x.strip('$')
    x = x.strip('&')
    return sort_dict[x]

def sort_Cards(cards):  #对给定的牌按升序排序
    card = cards.split(' ')
    shoupai = ''
    cards = sorted(card,key=sort_cmp)
    return cards        #返回列表
