oddeven = [144,32,13,52,443,223,553,100,20]
new = []
even = []
odd = []
for i in oddeven:
    if i%2 == 0:
        new.append(i)
for i in oddeven:
    if i%2 != 0:
        new.append(i)

print(new)