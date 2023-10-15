x = str(input("Enter binary:"))
z = 0
if x[3] == "1":
    z = z + 1
if x[2] == "1":
    z = z + 2
if x[1] == "1":
    z = z + 4
if x[0] == "1":
    z = z + 8
print(z)