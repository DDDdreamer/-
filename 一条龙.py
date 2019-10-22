def YiTiaoLong(cards):
    paishu = {'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'10':1,'J':1,'Q':1,'K':1,'A':1}
    for lst_i in cards:
        lst_i = lst_i.strip('*')
        lst_i = lst_i.strip('#')
        lst_i = lst_i.strip('$')
        lst_i = lst_i.strip('&')
        paishu[lst_i] -= 1
        if paishu[lst_i] < 0:
            return False
    return True
