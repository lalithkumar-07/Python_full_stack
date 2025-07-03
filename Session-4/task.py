for i in range(0,11):
    n=int(input("Guess the number:"))
    if n==36:
        print("Correct Number!!")
        break
    else:
        print("Wrong answer!! Try again!!")
else:
    print("Bad Luck!! Your chances are over!!")

while True:
    ch=int(input("guess the value:"))
    if(ch==36):
        print("Correct")
        break
    else:
        print("Not the number")