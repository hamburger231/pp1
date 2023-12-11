def month(n):
    month_name = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return month_name[n-1]

x = int(input("Provide the month's number: "))
print(month(x))