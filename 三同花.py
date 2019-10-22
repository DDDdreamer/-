def SanTongHua(cards):
    meihua_num = 0
    heitao_num = 0
    hongtao_num = 0
    fangkuai_num = 0
    for lst_i in cards:
        if lst_i.find('*')!=-1:
            meihua_num += 1
            if meihua_num > 5:
                return False
        elif lst_i.find('$')!=-1:
            heitao_num += 1
            if heitao_num > 5:
                return False
        elif lst_i.find('&')!=-1:
            hongtao_num += 1
            if heitao_num > 5:
                return False
        else:
            fangkuai_num += 1
            if fangkuai_num > 5:
                return False

    if meihua_num==3 and heitao_num==5 and hongtao_num==5 :
        return True
    if meihua_num==5 and heitao_num==3 and hongtao_num==5 :
        return True
    if meihua_num==5 and heitao_num==5 and hongtao_num==3 :
        return True
    if meihua_num==3 and heitao_num==5 and fangkuai_num==5 :
        return True
    if meihua_num==5 and heitao_num==3 and fangkuai_num==5 :
        return True
    if meihua_num==5 and heitao_num==5 and fangkuai_num==3 :
        return True
    if meihua_num==3 and hongtao_num==5 and fangkuai_num==5 :
        return True
    if meihua_num==5 and hongtao_num==3 and fangkuai_num==5 :
        return True
    if meihua_num==5 and hongtao_num==5 and fangkuai_num==3 :
        return True
    if heitao_num==3 and hongtao_num==5 and fangkuai_num==5 :
        return True
    if heitao_num==5 and hongtao_num==3 and fangkuai_num==5 :
        return True
    if heitao_num==5 and hongtao_num==5 and fangkuai_num==3 :
        return True
    return False