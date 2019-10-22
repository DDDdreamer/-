def ZhiZunQingLONG(cards):
    pai = ""
    for card in cards:
        pai += card
    zhizunqingLong = ["&2&3&4&5&6&7&8&9&10&J&Q&K&A", "#2#3#4#5#6#7#8#9#10#J#Q#K#A",
                      "*2*3*4*5*6*7*8*9*10*J*Q*K*A", "$2$3$4$5$6$7$8$9$10$J$Q$K$A"]
    if pai in zhizunqingLong:
        return True
    return False
