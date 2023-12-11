f1 = open('iso_8859-1.txt',"r")
f2 = open("copy.txt","w")
f1r = f1.readlines()
for i in f1r:
    f2.write(i)
f1.close()
f2.close()