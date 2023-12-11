name = "Dawid Szmitka"
university = "UEK"
field = "Applied Informatics"

f = open("student.txt","w")
f.write(name+"\n"+university+"\n"+field)
f.close()
