import random
a = random.randrange(1,7)
b = int(input("Enter your guess:"))
if b == a:
    print(True)
else:
    print(False)
    print("The correct guess was:",a)