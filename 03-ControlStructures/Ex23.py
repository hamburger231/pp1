dogage = float(input("Enter the dog's age in human years: "))
if dogage <= 2:
    dogage = dogage*10.5
    print("The dog's age in human years:",dogage)
else:
    dogage = dogage-2 
    dogage = dogage*4 + 21
    dogage = int(dogage)
    print("The dog's age in human years:",dogage)