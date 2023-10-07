"""
s=0
l1=[]
p=0
while p<5:
    n=int(input("num:"))
    if n<10:
        print("Error")
    else:
        s+=n
        l1.append(s)
        p+=1
print(l1)
print(s)
"""
"""
num=int(input("n:"))
l1=[]
for i in range(num):
    element=input("element:")
    l1.append(element)
print(l1)
"""
"""
l=[12,22,32,11,13,16,17]
for i in range(len(l)):
    if l[i]%2 ==0:
        l[i]="*"
print(l)
"""
"""
#print star in pattern
num=int(input("num:"))
for i in range(num+1):
    for j in range(i):
        print("*",end="")
    print()
"""
"""
x=[1,2,3,4,5,6,7,8]
for i in x:
    x.replace(i:"*")
print(x)
"""
x=aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ
l=[]
for i in x:
    l.append(i)
print(l)