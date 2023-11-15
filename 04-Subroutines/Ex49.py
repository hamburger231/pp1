def ricedoll(n):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    for i in range(len(n)):
        if n[i] == "1":
            a += 1
        elif n[i] == "2":
            b += 1
        elif n[i] == "3":
            c += 1
        elif n[i] == "4":
            d += 1
        elif n[i] == "5":
            e += 1
        elif n[i] == "6":
            f += 1
    if a > b and a > c and a > d and a > d and a > e and a > f:
        return 1
    elif b > a and b >c and b>d and b>e and b>f:
        return 2
    elif c>a and c>b and c>d and c>e and c>f:
        return 3
    elif d> a and d>b and d>c and d>e and d>f:
        return 4
    elif e>a and e>b and e>c and e>d and e>f:
        return 5
    elif f>a and f>b and f>c and f>d and f>e:
        return 6
    
print(ricedoll(("5233165554211")))
print(ricedoll("2133"))