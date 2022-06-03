from curses.ascii import isalpha

str1 = input("Is the string a palindrome? ")
flag = True

new_string = ""
for x in str1:
    if(isalpha(x) == False):
        continue
    new_string = new_string + x
new_string = new_string.lower()

backwards = new_string[::-1]
for i,x in enumerate(new_string):
    if(new_string[i] != backwards[i]):
        flag = False
        break

if flag == False:
    print(str1, "is not a palindrome")
else:
    print(str1, "is a palindrome")