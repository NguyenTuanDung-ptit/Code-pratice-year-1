game = ('J', 'Q', 'K')
list = []
input = input()
for i in input:
    list.append(i)

A = list[0]
B = list[1]
if game.index(A) < game.index(B):
    print("B")
else:
    print("A")