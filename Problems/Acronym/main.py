fisier = open('test.txt', 'r')
for i in fisier.readlines():
    print(i[0])
fisier.close()
