shoes = 20
jacket = 40
underwear = 70
rinsetime = 15
spintime = 9
washing_product = "shoes"
rinse = True
spin = False
if washing_product == "shoes":
    if rinse == True and spin == True:
        total_time = shoes + rinsetime + spintime
    elif rinse == True and spin == False:
        total_time = shoes+rinsetime
    elif rinse == False and spin == True:
        total_time = shoes+spintime
    elif rinse == False and spin == True:
        total_time = shoes
elif washing_product == "jacket":
    if rinse == True and spin == True:
        total_time = jacket + rinsetime + spintime
    elif rinse == True and spin == False:
        total_time = jacket+rinsetime
    elif rinse == False and spin == True:
        total_time = jacket+spintime
    elif rinse == False and spin == True:
        total_time = jacket
elif washing_product == "underwear":
    if rinse == True and spin == True:
        total_time = underwear + rinsetime + spintime
    elif rinse == True and spin == False:
        total_time = underwear+rinsetime
    elif rinse == False and spin == True:
        total_time = underwear+spintime
    elif rinse == False and spin == True:
        total_time = underwear
    
print("Total washing time:", total_time)


