def ShiErHuangZu(cards):
    count = 0
    i = 0
    shierhuangzu = ['J','Q','K','A']
    for lst_i in cards:
        i += 1
        lst_i = lst_i.strip('*')
        lst_i = lst_i.strip('#')
        lst_i = lst_i.strip('$')
        lst_i = lst_i.strip('&')
        if lst_i in shierhuangzu:
            count += 1
            if count >= 12:
                return True
        if i - count >= 2:
            return False
    return False
