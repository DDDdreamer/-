def SanFenTianXia(cards):
    boom = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'Q':0,'K':0,'A':0}
    boom_num = 0
    for lst_i in cards:
        lst_i = lst_i.strip('*')
        lst_i = lst_i.strip('#')
        lst_i = lst_i.strip('&')
        lst_i = lst_i.strip('$')
        boom[lst_i] += 1
        if boom[lst_i] == 4:
            boom_num += 1
    if boom_num == 3:
        return True
    return False

