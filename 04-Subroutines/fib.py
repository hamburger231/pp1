def fib(n):
    num1 = 0
    num3 = 1
    num2 = 1
    for i in range(n-2):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    return num3

print(fib(100))