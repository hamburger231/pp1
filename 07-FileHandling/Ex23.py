f = open("power.txt","w")
for i in range(1,11):
    f.write(f'{i},{i**2},{i**3}'+"\n")