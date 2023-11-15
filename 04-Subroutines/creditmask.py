def secret(n):
    if len(n) > 16:
        a,b,c,d = n.split()
        print(a[0:2],"*"*4,"*"*4,d)
    if len(n) == 16:
        print(n[0:2],"*"*8,n[12:16], sep="")


