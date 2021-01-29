fisier = open('sums1.txt', 'r+')
# for i in fisier.readlines():
#     suma = i.split()
#     print(int(suma[0]) + int(suma[1]))

# lista = ['a', 's', 'd', 'f', 'g', 'h', 'w']
#
# for lit in lista:
#     fisier.writelines(lit + '\n')
# print(fisier.readlines())
# fisier.close()
color_list = ['cyan\n', 'magenta\n', 'yellow\n', 'key color']

cymk_file = open('CMYK.txt', 'r+', encoding='utf-8')
cymk_file.writelines(color_list)
print(cymk_file.readlines())
cymk_file.close()