arr1 = [112,525,636,344]
arr2 = [12,563,112,344,636,344,525]
c = 0
for i in arr1:
    if i in arr2:
        c += 1
if c == len(arr1):
    print("True")
