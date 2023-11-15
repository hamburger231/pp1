def codecheck(n):
    x = (int(n[0]) + int(n[1]) + int(n[2])%7)
    if int(n[3]) == x:
        return True
    else:
        return False
    
print(codecheck("1082"))
print(codecheck("2035"))
print(codecheck("1114"))
print(codecheck("7071")) 
