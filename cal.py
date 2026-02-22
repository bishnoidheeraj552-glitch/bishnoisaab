# bishnoisaab
print("welcome")
print("a = sum \n b= diffrence \n c = devide \n d = mltiply")

a = "sum"
b = "difference"
c = "divide"
d =  "multiply"
choice = str(input("select in a/b/c/d"))
val1= float(input("your first number "))
val2= float(input("your second number "))
if(choice=="a"):
    print("result :",val1+val2)
elif(choice=="b"):
    print("result :",val1-val2)
elif(choice=="c"):
    if(val2==0):
        print("not define")
    else:
        print("result :",val1/val2)
elif(choice=="d"):
    print("result :",val1*val2)
else:
    print("chose carecet type i a/b/c/d")
print("proggram ends")

