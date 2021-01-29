word = list(input())
invers_word = word[::-1]
if word == invers_word:
    print('Palindrome')
else:
    print('Not palindrome')
