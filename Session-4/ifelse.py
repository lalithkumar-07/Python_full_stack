a=int(input("enter a number:"))
if (a%3==0 and a%5==0 and a%7==0):
    print("Divisible by 3 and 5 and 7")
elif (a%3==0 and a%5==0 and a%7!=0):
    print("Divisible by 3 and 5")
elif (a%3==0 and a%5!=0 and a%7==0):
    print("Divisible by 3 and 7")
elif (a%3!=0 and a%5==0 and a%7==0):
    print("Divisible by 5 and 7")
elif (a%3!=0 and a%5==0 and a%7!=0):
    print("Divisible by 5")
elif (a%3!=0 and a%5!=0 and a%7==0):
    print("Divisible 7")
elif (a%3==0 and a%5!=0 and a%7!=0):
        print("Divisible by 3")
else:
    print("Not Divisible by any number")