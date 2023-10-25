current_price = 140
previous_price = 200
discount =  (current_price/previous_price)-1
discount = int(discount*(-100))
if discount > 10:
    print("Buy the product!!!!!!!!!!!!!!!")
    print(f'Product price reduced by {discount}%')
