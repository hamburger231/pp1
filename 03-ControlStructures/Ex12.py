n1 = str(input("Enter first persons name: "))
a1 = int(input("Enter first persons age: "))
n2 = str(input("Enter second persons name: "))
a2 = int(input("Enter second persons age: "))

if a1 >= 18 and a2 >= 18:
    print("Both Peter and Ann are adults")
else:
    print("One person is not an adult yet")