def binary_number(n):
    for i in range(1,len(n)):
        if n[i] == "1" or n[i] == "0":
            return True
        else:
            return False
        
x = str(input("Provide a number: "))
print("Number is binary:",binary_number(x))