file_path = "C:\\Users\\AbdelBadi\\Desktop\\Avent_Calendar\\Avent_Calendar\\Exo5\\5.txt"
fichier = open(file_path, "r")

ordre = True
somme = 0
ordList = []

for ligne in fichier:
    ligne = ligne[:-1]
    if ligne == "":
        ordre = False
    elif ordre:
        ordList.append((int(ligne[0:2]), int(ligne[3:5])))
    else:
        feuilles = [int(x) for x in ligne.split(",")]
        test = True
        for premier, second in ordList :
            if premier in feuilles and second in feuilles:
                if feuilles.index(premier) > feuilles.index(second):
                    test = False
                
        if test:
            somme += feuilles[len(feuilles) // 2]

print(somme)
    