t=int(input())
for i in range(t):
    n=int(input())
    if n ==1:
        print('0')
    count1=0
    count2=0
    while n%2 ==0:
        count1+=1
        n =n//2
    while n%3 ==0:
        count2+=1
        n=n//3
    if (count2>=count1 and n==1):
        print(2*count2-count1)