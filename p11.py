x="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
l=[]
for i in x:
    l.append(i)
while True:
    p=input("ENTER A ALPHABET OR 9 TO EXIT:")
    if p in l:
        r=l.index(p)
        print("preceding:",l[r-1])
        print("succeeding:",l[r+1])
    elif p=="9":
        break
    else:
        print("PLEASE ENTER A ALPHABET")
