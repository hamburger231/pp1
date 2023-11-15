def passcheck(n):
    x = ""
    if len(n) < 6:
        return False
    for i in range(len(n)-1):
        if n[i] in x:
            return False
        else:        
            x += n[i]
    for j in range(len(n),len(n)):
        if n[j] in x:
            return False
        else:
            return True
print(passcheck("1234567"))
