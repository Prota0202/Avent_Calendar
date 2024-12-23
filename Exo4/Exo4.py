file_path = "C:\\Users\\AbdelBadi\\Desktop\\Avent_Calendar\\Avent_Calendar\\Exo4\\4.txt"
fichier = open(file_path, "r")

grille = []

for ligne in fichier:
    if ligne.strip():
        grille.append(ligne.strip())
    
cpt_xmas = 0

for i in range(len(grille)):
    for j in range(len(grille[0])):
        if grille[i][j] == 'X':
            for decH in [-1, 0, 1] :
                for decV in [-1, 0, 1] :
                    if 0 <= i+(3*decV) < len(grille) and 0 <= j+(3*decH) < len(grille[0]):
                        if grille[i+(1*decV)][j+(1*decH)] == 'M' and \
                            grille[i+(2*decV)][j+(2*decH)] == 'A' and \
                            grille[i+(3*decV)][j+(3*decH)] == 'S':
                            cpt_xmas += 1
                            
print(cpt_xmas)