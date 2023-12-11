import json
movie = {
    "title":"Interstellar",
    "year":"2014",
    "actors":{"leading":"Matthew McConaughey","supporting":"Anna Hathaway"},
    "oscar": True,
    "ratings":"92/100"
}

f = open("favourite.json","w")
f.write(json.dumps(movie, indent=1))
f.close