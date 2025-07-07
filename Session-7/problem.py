def prime(a):
    c=0
    if a==1:
        return True
    for i in range(1,int(a**(0.5))+1):
        if a%i==0:
            if(i==(a//i)):
                c+=1
            else:
                c+=2
    if(c==2):
        return True
    else:
        return False
a=int(input("given value:"))
print(prime(a))

def factorofnum(a):
    for i in range(1,a+1):
        if a%i==0:
            print(i,end=" ")
factorofnum(a)

# def prime(a):
#     c=0
#     for i in range(1,int(a**1/2)):
#         if a%i==0:
#             c+=1
#     if c>1:
#         return False
#     else:
#         return True
# a=int(input("given value:"))
# print(prime(a))
# def factorofnum(a):
#     l1=[]
#     for i in range(1,a+1):
#         if a%i==0:
#             l1.append(i)
#     return l1
# print(factorofnum(a))