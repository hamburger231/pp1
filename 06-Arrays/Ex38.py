array = [1,636,12,4,12,56,8,9,4345,33]
x = int(input("Provide the value: "))
count = 0
for i in array:
    if i > x:
        count += 1
print(count)
