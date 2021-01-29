scores = input().split()
co = 0
inco = 0
contor = 0
for i in scores:
    if i == 'I':
        inco += 1
        if inco == 3:
            print('Game over')
            print(co)
            break
    elif i == 'C':
        co += 1
        if contor == len(scores) - 1:
            print('You won')
            print(co)
    contor += 1
