import rangecheck

x = int(input("Provide number: "))



if rangecheck.range_check(x) == True:
    print("Number in range <2,15>: Yes")
else:
    print("Number in range <2,15>: No")

