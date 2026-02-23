# new version of caluculator
print("welcome to my new progrram")
print("we e trying a  new proggram")
print("first we introcued us")
name = input("what is your name : ")
print("hello ", name)
print("we are trying to learn math")
print("we are caluculate some value they began in your mind")
val1 = int(input("enter your first number ; "))
val2 = int(input("enter your second number ; "))
a = "sum"
b = "diffrence"
c = "devision"
d = "multiplication"
print("a = sum \nb = diffrence \nc = devision \nd = multiplication  \nchoice one of them")
choice = input("enter your choice  ; ")
if choice == "a":
    print("the sum of ", val1, "and", val2, "is", val1 + val2)
elif choice == "b":
    print("the diffrence of ", val1,"and", val2, "is", val1-val2)
elif choice == "c":
    if val2 == 0:
        print("error: division by zero not allowed")
    else:
        print("the devision of ", val1,"and", val2, "is", val1/val2)
elif choice == "d":
    print("the multiplication of ", val1,"and", val2, "is", val1*val2)
else:
    print("invalid choice")
