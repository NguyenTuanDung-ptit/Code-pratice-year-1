game = ('J', 'Q', 'K')
card_list = []
while True:
    cards = input()
    if cards not in 'JQK':
        break
    else: 
        for i in cards:
            card_list.append(i)

    A = card_list[0]
    B = card_list[1]
    if game.index(A) < game.index(B):
        print("B")
    else:
        print("A") 