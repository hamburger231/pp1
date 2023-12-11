f1 = open('MeatAndFish.txt',"r")
f2 = open('GrainsAndBread.txt',"r")
f3 = open('allproducts.txt',"w")
for i in f1:
    f3.write(i)
for j in f2:
    f3.write(j)
f1.close()
f2.close()