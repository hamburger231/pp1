f = open('iso_8859-1.txt','r')
z = f.readlines()
n = 1
for i in z:
    if n%5 == 0:
        print(i,end='')
        x = input("Press enter to continue: ")
        n +=1
    else:
        print(i,end='')
        n += 1
f.close()





