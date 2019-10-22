def CouYiSe(cards):
    meihua_and_fangkuai_num = 0
    hongtao_and_heitao_num = 0

    for lst_i in cards:
        if lst_i.find('*')!=-1 or lst_i.find('#')!=-1:
            meihua_and_fangkuai_num += 1
            if hongtao_and_heitao_num != 0:
                return False
        else :
            hongtao_and_heitao_num += 1
            if meihua_and_fangkuai_num != 0:
                return False
    return True