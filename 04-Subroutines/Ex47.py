def signstr(n):
    x = ""
    if len(n)>1:
        for i in range(len(n)-1):
            x += n[i]
            x += "-"
    else:
        return n
    x += n[-1]
    return x

print(signstr("x"))