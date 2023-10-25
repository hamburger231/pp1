normal = input("Enter time (24-hour format): ")
if len(normal) != 5:
    z = "0"+normal
x = int(z[0:2])
if x > 12:
    y = z-12
    print(y,z[2:5],"pm",sep="")
else:
    print(z,"am",sep="")