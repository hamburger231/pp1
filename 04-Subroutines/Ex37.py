def n_of_fib(n):
    num0 = 0
    num1 = 1
    num2 = 1
    for i in range(1,n):
        num2 = num1+num0
        num0 = num1
        num1 = num2
    return num2

print(n_of_fib(12))
