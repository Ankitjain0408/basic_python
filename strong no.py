n=int(input("n:"))
x=n
f=1
sum=0
j=1
i=0
while i!=0:
    i=n%10
    for j in range(1,i+1):
        f=f*j
    sum+=f
    n=n-i
    n=n//10
if sum==x:
    print("yes")
else:
    print("no")
