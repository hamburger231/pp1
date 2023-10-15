amount = float(input("Enter the whole amount:"))
vat = amount*0.23
novat = amount - vat
vat = str(vat)
x = vat.find(".")
novat = str(novat)
y = novat.find(".")
print("Amount w/o VAT:",novat[0:y+3])
print("VAT:",vat[0:x+3])