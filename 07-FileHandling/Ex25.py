import re
sum = 0
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
for i in temperatures:
    sum += int(i)

print(sum/len(temperatures))
