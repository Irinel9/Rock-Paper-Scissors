fisier = open('input.txt', 'w')
linie = input()
fisier.write(linie)

for i in range(3):
    print(i, file=fisier, flush=True)
fisier.close()
