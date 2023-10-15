cm_h = int(175)
feet_h = str(0.0328*cm_h)
a, b = feet_h.split(".")
print(f'I am 175cm tall, i.e. {a} feet and {b[0]} inches tall')
