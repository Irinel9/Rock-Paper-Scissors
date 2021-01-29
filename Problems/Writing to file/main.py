f_name = "test.txt"
my_string = "A string to be written to a file!"

# what to do with the file and the string
fisier = open(f_name, 'w')
print(my_string, file=fisier)
fisier.close()
