def palindrom(n):
    x = ""
    y = range(0,len(n))
    for i in y[::-1]:
        x = x + str(n[i])
    if n == x:
        return True
    else:
        return False
print(palindrom("radar"))

