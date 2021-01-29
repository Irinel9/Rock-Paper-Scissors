# read animals.txt
fisier_animale = open('animals.txt', 'r')
fisier_new_animals = open('animals_new.txt', 'w+')

for i in fisier_animale:
    fisier_new_animals.write(i.replace('\n', ' '))

fisier_animale.close()
fisier_new_animals.close()
