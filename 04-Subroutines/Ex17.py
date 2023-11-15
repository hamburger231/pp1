
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

def different(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n3 != n1:
        return True
    else:
        return False
    
if different(n1,n2,n3):
    print(f'Numbers {n1},{n2},{n3}, are all different')
else: 
    print("Some of the numbers are the same")