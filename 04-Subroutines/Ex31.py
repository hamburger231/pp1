def n_even_sum(a,b):
    sum = 0
    for i in range(a,b):
        if i%2 == 0 and i<0:
            sum += 1
    return sum

print(n_even_sum(-10,3))


    