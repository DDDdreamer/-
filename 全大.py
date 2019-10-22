def All_Big(cards):
    all_big = ['8','9','10','J','Q','K','A']
    for lst_i in cards:
        lst_i = lst_i.strip('&')
        lst_i = lst_i.strip('$')
        lst_i = lst_i.strip('#')
        lst_i = lst_i.strip('*')

        if lst_i not in all_big:
            return False
    return True