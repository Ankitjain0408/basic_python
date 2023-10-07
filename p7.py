num=int(input("num:"))
l1=[]
d=0
while num!=0:
    d=num%10
    l1.append(d)
    num=num-d
    num=num//10
print(sum(l1))
