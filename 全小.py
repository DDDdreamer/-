def All_Small(cards):
    all_small = ['2','3','4','5','6','7','8']
    for lst_i in cards:
        lst_i = lst_i.strip('&')
        lst_i = lst_i.strip('$')
        lst_i = lst_i.strip('#')
        lst_i = lst_i.strip('*')

        if lst_i not in all_small:
            return False
    return True