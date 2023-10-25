q = int(input("Number of products: "))
cost = float(input("Product price: "))
if q > 2:
    final_price = q*cost*0.75
    print("Amount to pay:",final_price)
else:
    final_price = q*cost
    print("Amount to pay:",final_price)