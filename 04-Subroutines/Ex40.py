def samedigitsum(n):
    sum = 0
    n = str(n)
    a = n.count("1")
    b = n.count("2")
    c = n.count("3")
    d = n.count("4")
    e = n.count("5")
    f = n.count("6")
    g = n.count("7")
    h = n.count("8")
    i = n.count("9")
    if a >= 2:
        sum += 1*a
    if b >= 2:
        sum += 2*b
    if c >= 2:
        sum += 3*c
    if d >= 2:
        sum += 4*d
    if e >= 2:
        sum += 5*e
    if f >= 2:
        sum += 6*f
    if g >= 2:
        sum += 7*g
    if h >= 2:
        sum += 8*h
    if i >= 2:
        sum += 9*i
    return sum

print(samedigitsum(230335))