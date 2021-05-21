# PROJETNAN
PYTHON 3

# EXERCICE 1

liste=("Maxime","Martine","Christopher","Calors","Michael","Eric")
trois_premiers=liste[0:3]
trois_derniers=liste[3:6]
millieu=liste[1:5]
premier_dernier=liste[0:6:4]


# EXERCICE 2

liste=[1,2,3,4,5]
liste.append(6)
if 6 in liste:
    print("le nombre 6 est dans la liste.")
else:
    print("le nombre 6 ne se trouve pas dans la liste")
    
    # EXERCICE 3

langages=[["Python","C++"],"Java"]
nombres=[1,[4,[2,3]],5,[6],[[7]]]
python=langages[0][0]
deux=nombres[1][1][0]
sept=nombres[4][0][0]
