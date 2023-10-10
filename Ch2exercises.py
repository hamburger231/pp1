ex = input("Which exercise to check(2-5): ").strip()
ex = int(ex)

if ex==2:
    name = input(str("What's your name: ")).strip()
    print("Hello " + name)
    exit()

if ex==3:
    x = input("Enter hours: ")
    y = input("Enter rate: ")
    x = float(x)
    y = float(y)
    z = x * y
    print("Pay: ", z)
    exit()
if ex==4:
    width = 17
    height = 12.0

    print(width//2)
    print(width/2.0)
    print(height/3)
    print(1 + 2 * 5)
    exit()

if ex==5:
    celsius = input("Provide the Celsius temperature: ").strip()
    celsius = float(celsius)
    fh = celsius * 1.8 + 32
    print("Temperature in Fahrenheit is: ", fh)
    exit()
    
else:
    print("There's no such exercise")