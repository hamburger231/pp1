i = 7
a = 0
while 3 < i <= 7:
    print(f'{i+a}', end = " ")
    a = a + 1
    if a == 3:
        i = i-3
        a = a-3
        print()
    while 1 < i <=4:
        print(f'{i+a}', end = " ")
        a = a + 1
        if a == 3:
            i = i-3
            a = a-3
            print()
        while -2 < i <=1:
            print(f'{i+a}', end=" ")
            a = a + 1
            if a == 3:
                i = i-3
                a = a-3
