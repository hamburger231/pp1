x = float(input("Enter your height in cm: "))
y = float(input("Enter your weight in kg: "))
bmi = y/((x/100)**2)
print("Your BMI index:", bmi)
print("Correct weight:",18.9 <= bmi <=25)