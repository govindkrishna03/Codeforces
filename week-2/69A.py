n = int(input())
lst=[]
a=0
b=0
c=0
for i in range(n):
    f= list(map(int,input().split()))
    lst.append(f)
    
for i in lst:
    a += i[0]
    b += i[1]
    c += i[2]
if a==b==c==0:
     print("YES")
else:
    print("NO")
        
