n,f = input().split()
n=int(n)
f=int(f)
if n >=1 and f>=0 and n<=100000 and f<= n:
    product=[]
    customer=[]
    sold1=[]
    for i in range(n):
        a,b=input().split()
        a=int(a)
        b=int(b)
        product.append(a)
        customer.append(b)
    for i in range(len(product)):
        product[i]=product[i]*2

    for i in range(n):
        dump = product[i]-customer[i]
        if product[i]>customer[i]:
            sold = customer[i]
        else:
            sold=product[i]
        profit =  sold - abs(dump)
        if profit>0:
            sellout = 1
        else:
            sellout =0
        if sellout==1:
            sold1.append(sold)
        else:
            if product[i] / 2 > customer[i]:
                sold = customer[i]
            else:
                sold = product[i] / 2
            sold1.append(sold)

    ans=0
    for i in sold1:
        ans+=i
    print(int(ans))


        

