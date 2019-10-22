def LiuDuiBan(cards):
    duizi_num = 0
    card_dic = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'Q':0,'K':0,'A':0}
    for lst_i in cards:
        lst_i = lst_i.strip('*')
        lst_i = lst_i.strip('#')
        lst_i = lst_i.strip('$')
        lst_i = lst_i.strip('&')
        card_dic[lst_i] += 1
        if card_dic[lst_i] == 2:
            duizi_num += 1
        if card_dic[lst_i] > 2:
            return False
    if duizi_num == 6:
        return True
    return False