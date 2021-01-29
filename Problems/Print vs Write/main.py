numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
file_number = open('file_with_list.txt', 'w')
file_number.write(str(numbers))
file_number.close()
