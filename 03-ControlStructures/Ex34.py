amount = int(input("Enter the amount in PLN: "))
a = 5
b = 2
c = 1

x = amount//a
print("5 PLN coins:",x)
y = (amount-x*a)//b
print("2 PLN coins:",y)
z = (amount-(y*b)-(x*a))//c
print("1 PLN coins:",z)