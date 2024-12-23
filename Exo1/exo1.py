file_path = "C:\\Users\\AbdelBadi\\Desktop\\Avent_Calendar\\Avent_Calendar\\Exo1\\1.txt"
data = open(file_path, "r")

gauche = []
droite = []

for elem in data :
    l = elem[:-1].split(" ")
    gauche.append(int(l[0]))
    droite.append(int(l[-1]))

gauche.sort()
droite.sort()

total = 0

for i in range(len(gauche)) :
    total = total + abs(gauche[i] - droite[i])

print(total)

#############################################################