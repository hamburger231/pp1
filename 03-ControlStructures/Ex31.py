x = input("Provide the coordinates of the point (x,y): ")
y = x[1:len(x)-1]
a , b = y.split(",")
a = int(a)
b = int(b)
if a > 0 and b > 0:
    print(f"The point {x} is located in the 1st quadrant")
elif a < 0 and b > 0:
    print(f"The point {x} is located in the 2nd quadrant")
elif a < 0 and b < 0:
    print(f"The point {x} is located in the 3rd quadrant")
else: 
    print(f"The point {x} is located in the 4th quadrant")