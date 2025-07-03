for i in range(0,11,2):
    print(i)
for i in range(10,-1,-2):
    print(i)
n=int(input("Enter a value: "))
for i in range(0,n):
    print("* "*n)


for i in range(0,n):
    print("* "*i)


for i in range(n,0,-1):
    print("* "*i)


for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()


for j in range(1,n+1):
    for k in range(1,j+1):
        print('*',end=' ')
    print()