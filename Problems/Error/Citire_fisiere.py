file = open('stars.txt', 'r')
# print(file.read())
favorite_animal = file.readlines()
print(favorite_animal[2], favorite_animal[5], favorite_animal[1], sep='')
# print(file.readline(2))
# print(file.readline(3))
# print(file.readline(2))
# print(file.readline(3))
# print(file.readline(3))
# print(file.readline(3))

# for i in file:
#     print(i)
file.close()
