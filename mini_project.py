import math, random
#1

# def charger_villes(chemin):
#     with open(chemin, "r") as cities:
#         content = cities.readlines()

#         for line in content:
#             print(tuple(line))

#         print(content)
#         print(len(content))  
# charger_villes("villes.txt")

#2

def distance(ville_a, ville_b):
    # print(f"Calcul de la distance entre {ville_a[0]} et {ville_b[0]}")
    distance = math.sqrt((ville_a[1] - ville_b[1])**2 + (ville_a[2] - ville_b[2])**2 )
    # print(distance)
    return distance

distance(("Nantes", 47.2181, -1.5528), ("Montpellier", 43.6119, 3.8772))

#3 

list_of_cities = []
with open("villes.txt", "r", encoding="utf-8") as cities:
    content = cities.readlines()

    for line in content:
        parts = line.strip().rsplit(" ", 2)
        print(parts)
        nom = parts[0]
        lat = float(parts[1])
        long = float(parts[2])
        list_of_cities.append((nom, lat, long))

print(list_of_cities)

roadmap = []

def itineraire_greedy(villes):
    start_of_road = villes[0]
    print(start_of_road)

    for city in villes:
        print(city[0])
        print(start_of_road)
        roadmap.append((city[0], distance(start_of_road, city)))
        print(sorted(roadmap, key=lambda x:x[1]))

#4
    total_distance = 0
    
    for distances in roadmap:
        total_distance += distances[1]

    print(total_distance)
    
itineraire_greedy(list_of_cities)

#5


# À chaque étape, notre robot regarde juste le bonbon (la ville) le plus proche et saute dessus. Il ne réfléchit pas du tout à la suite ! 
# C'est comme manger tout le chocolat d'un coup et se retrouver coincé à la fin avec les légumes super loin. Ce n'est pas le chemin le plus malin.

# - Le grand saut de la fin : Au début, il s'amuse à côté, mais à la fin, il se rend compte qu'il a oublié une ville tout au bout de la Terre. 
#   Il est obligé de faire un giga-bond géant qui gâche tout le score !