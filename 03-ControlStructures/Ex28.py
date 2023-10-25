x = int(input("Enter EAN-13 article number: "))
x = str(x)
y = x[0:3]
if len(x) == 13:
    if y == "590":
        print("Product from Poland")
    else:
        print("Product not from Poland")
else:
    print("Incorrect number")
    
