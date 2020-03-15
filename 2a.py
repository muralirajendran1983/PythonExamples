def oddoreven(a):
    if(a%2 == 0):
        return 1
    else:
        return 0

num = int(input("Enter the number:"))
if(oddoreven(num)==1):
    print("The given number is even")
elif(oddoreven(num)==0):
    print("The given number is odd")
