# if the character is in uppercase, print its ASCII value
ch=input("enter the character: ")
if ch.isupper():
    print(ord(ch))
    
if 'A' <= ch <= 'Z':
    print(ord(ch))
