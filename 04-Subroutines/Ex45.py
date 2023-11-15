def exp(a): 
    sum = 0 + int(a[0])
    for i in range(1,len(a)):
        if a[i] == "+":
           sum += int(a[i+1])
        elif a[i] == "-":
           sum -= int(a[i+1])
    return sum
print(exp("3+8+1"))