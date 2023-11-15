def divsum(x,y):
    sum = 0
    for i in range(x,y):
        if i%2 == 0 and i%3 == 0 and i%4 != 0:
            sum = sum+i
    return sum

print(divsum(10,34))
