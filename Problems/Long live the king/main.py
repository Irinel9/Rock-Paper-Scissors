x, y = int(input()), int(input())
if [x, y] in [[1, 1], [8, 1], [8, 8], [1, 8]]:
    print('3')
elif [x, y] in [[i, y] for i in range(1, 9, 7) for y in range(2, 8)] + [[i, y] for i in range(2, 8) for y in range(1, 9, 7)]:
    print('5')
else:
    print('8')



c1 = 1 < int(input()) < 8
c2 = 1 < int(input()) < 8
print(8 if c1 and c2 else 5 if c1 ^ c2 else 3)

x, y = int(input()), int(input())
x_free = 3 if 1 < x < 8 else 2
y_free = 3 if 1 < y < 8 else 2
print(x_free * y_free - 1)


a, b = int(input()), int(input())
print([8, 5, 3][(a in (1, 8)) + (b in (1, 8))])
