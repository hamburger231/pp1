ar1 = [4,36,12,28,9,44,5]
ar2 = [5,1,36]
x = []
for i in ar1:
    if i not in ar2:
        x.append(i)
print(x)