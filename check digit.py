# WAP to check whether the integer is single digit or double digit or triple digit or more than three digits including negative numbers

num=int(input("Enter an integer: "))
if num<10:
    print(num,"is a single digit number")
elif num<100:
    print(num,"is a double digit number")
elif num<1000:
    print(num,"is a triple digit number")
else:
    print(num,"has more than three digits")
