Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]
def hotel_list(hotels):
    if hotels == "Kraków":
        for i in range(len(Hotels_in_Krakow)):
            print(Hotels_in_Krakow[i]["name"],end=", ")
    elif hotels == "Sopot":
        for j in range(len(hotels_in_Sopot)):
            print(hotels_in_Sopot[j]["name"],end=", ")

def avg_price(hotels):
        sum = 0
        if hotels == "Kraków":
            for i in range(len(Hotels_in_Krakow)):
                sum += int(Hotels_in_Krakow[i]["price"])
            return sum//len(Hotels_in_Krakow)
        elif hotels == "Sopot":
            for j in range(len(hotels_in_Sopot)):
                sum += int(hotels_in_Sopot[j]["price"])
            return sum//len(hotels_in_Sopot)
        
def compare():
    if avg_price("Kraków") > avg_price("Sopot"):
        return "Sopot"
    else:
        return "Kraków"
