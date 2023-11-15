def pplcheck(n):
    x = 0
    for i in range(len(n)):
        if n[i] == "+":
            x = x + 1
        elif n[i] == "-":
            x = x - 1
        if x>= 3:
            break
    if x >= 3:
        return True
    else:
        return False
print(pplcheck("+-+++-+---"))
print(pplcheck("+-+-+-+-"))
print(pplcheck("+-++-+--"))
