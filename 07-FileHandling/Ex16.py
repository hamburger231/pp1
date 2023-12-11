x = input("Provide file name: ")
with open(x,"r") as f:
    lines = 0
    for i in f:
        lines += 1
    print(lines)