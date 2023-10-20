x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

if x < 0 and y < 0:
    print("Both numbers are negative or equal to 0")
else:
    print(f'At least one of the numbers {x} and {y} - is positive')