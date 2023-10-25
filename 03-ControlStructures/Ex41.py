attempt = 2

while attempt >= 0:
    a = input(str("Enter the pin code: "))
    if attempt == 0:
        print("No more attempts :(")
        break
    elif a == "0805":
        print("Correct pin! :)")
        break
    else:
        print("Invalid pin! :(")
        print(f"Attempts left: {attempt}")
        attempt -= 1
        continue