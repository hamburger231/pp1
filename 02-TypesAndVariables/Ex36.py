a = float(input("Enter EUR buy price: "))
b = float(input("Enter EUR sell price: "))
spr = b-a
spr = str(spr)
print("EUR buy price:",a)
print("EUR sale price:",b)
print("Spread:",spr[0:6])