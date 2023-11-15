def amount_to_pay(amount):
    a = 5
    b = 2
    c = 1

    x = amount//a
    y = (amount-x*a)//b
    z = (amount-(y*b)-(x*a))//c
    sum = x+y+z
    return sum


x = int(input("Provide the amount: "))
print(f"Minimum amount of coins:{amount_to_pay(x)}")