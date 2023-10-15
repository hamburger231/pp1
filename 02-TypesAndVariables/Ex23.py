a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))
s = (a+b+c)/2
cf = a+b+c
x = (s*(s-a)*(s-b)*(s-c))**(1/2)
if x <= 0:
    print("This triangle does not exist")
else:
    print("Triangle circumference:",cf)
    print("Triangle area:",x)