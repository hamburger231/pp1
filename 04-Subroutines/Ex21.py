import mykeyboard
import mymath


x = mykeyboard.read_number()
y = mymath.generate_number()
print("Random number:",y)
if x == y:
    print("g")
else:
    print("bad")
