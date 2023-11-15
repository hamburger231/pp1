def sum(number,even):
    suma = 0
    if even == True:
        for i in range(len(number)):
            x = number[i]
            if int(x)%2 == 0:
                suma += int(number[i])
    elif even == False:
        for j in range(len(number)):
            x = number[j]
            if int(x)%2 != 0:
                suma += int(number[i])
    return suma

x = str(input("nUmber!!!: "))
print(f"Sum of the digits: {sum(x, True)}")