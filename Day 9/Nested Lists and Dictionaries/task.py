#NESTED LISTS

VistedPlace = {
    "Hetauda":["Buspark","Samari","ViewTower","Thanabharang"],
    "Kathmandu": ["Balkhu","Kalimati","Thamel"]
}

print(VistedPlace["Hetauda"][2])


Nested_alpha=["a","b",["c","d"]]
print(Nested_alpha[2][1])

#Dictionary in a Dictionary

travel_places={
    "Hetauda": {
     "Num_times_visted":4,
        "Place_visted":["Samari","ViewTower","Smarak"]
    },

    "Pokhara":{
     "Num_times_visted":2,
        "Place_visited":["LakeSide","Peace Gumba","Sarangkot"]
    }
}

print(travel_places["Pokhara"]["Place_visited"][2])