dec = str(input("Provide decimal number: "))
dec = int(dec)
bin = ""
while dec > 1:
    r = dec%2
    r = int(r)
    r = str(r)
    bin = bin+r
    dec = dec/2
print(bin[::-1])
