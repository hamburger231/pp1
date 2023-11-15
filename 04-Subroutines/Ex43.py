def acronym(n):
    x = ""
    x += n[0]
    for i in range(1,len(n)):
        if n[i] == " ":
            x += n[i+1]
    return x
print(acronym("For Your Information"))