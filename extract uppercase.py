#WAP to extract all the lowercase characters from a string
s = input("Enter a string: ")
for char in s:
    if char.islower():
        print(char)
