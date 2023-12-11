countries = [{
    "name":"Poland",
    "population":"39M",
},
{
    "name":"Germany",
    "population":"78M",
},
{
    "name":"Ukraine",
    "population":"20M",
},
{
    "name":"Hungary",
    "population":"100M",
},
{
    "name":"Turkey",
    "population":"2000M",
}
]
i=0
print("COUNTRY\tPOPULATION")
while i < len(countries):
    x,y = countries[i].items()
    print(f'{x[1]}\t{y[1]}')
    i+=1