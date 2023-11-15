def primecheck(n):
    number = 3
    rightnow = 5
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 7
    elif n > 4:
        for i in range(5,1000000):
            if i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0 or :
                continue
            else:
                number += 1
            if number == n:
                break
    if number == n:
        return number

            







print(primecheck(4))
print(primecheck(5))
print(primecheck(6))
