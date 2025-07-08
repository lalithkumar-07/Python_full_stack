# st=' India is my country '
# print(st.lower())
# print(st.upper())
# print(st.split(" "))
# print(st.strip())
# def maxi():
#     p=list(map(int,input().split()))
#     maxm=p[0]
#     for i in range(len(p)):
#         if p[i]>maxm:
#             maxm=p[i]
#     return maxm

# print(maxi())
        
# def rev():
#     p=list(map(int,input().split()))
#     for i in range(int(len(p)/2)):
#         j=len(p)-i-1
#         temp=p[i]
#         p[i]=p[j]
#         p[j]=temp
#         if i==j:
#             break
#     return p
# print(rev())

def comma(n):
    for i in range(1,n+1):
        print(i,end=",")
    else:
        print(".")
n=int(input("enter a value:"))
comma(n)

