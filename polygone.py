import math

nbSommets = 7
polygone = [(0, 10), (0, 20), (8, 26), (15, 26), (27, 21), (22, 12), (10, 0)]

#nbSommets = 0
#polygone = []
tabcorde = []
C = []


def main():
    figure()
    print("le nombre de sommet est :", nbSommets)
    print("le polygone est :", polygone)


def initVecteur():
    for i in range(0, nbSommets):
        for j in range(i + 1, (nbSommets + i)):
            if not voisins(i, j):
                # si i et j ne sont pas adjacents
                a = i
                b = j % nbSommets
                if a > b :
                # permutation pour avoir b<a
                    tmp = b
                    b = a
                    a = tmp
                if not present((a, b, longueur(a, b)), C):
                # si la corde n'est pas déjà ajouté
                    C.append((a, b, longueur(a, b)))


def present(k, tab):
# parcours de tab pour savoir si k est dedans
    for i in tab:
        if i == k:
            return True
    return False


def figure():
    # création du polygone
    nbSommets = int(input("Nombre de sommet de la figure : "))
    for i in range(0, nbSommets):
        print("x" + str(i) + " = ", end='')
        x = int(input())
        print("y" + str(i) + " = ", end='')
        y = int(input())
        polygone.append((x, y))


def longueur(i, j):
    # calcul de la longueur entre les points i et j
    i = i % nbSommets
    j = j % nbSommets
    a = polygone[i]
    b = polygone[j]
    xa = a[0]
    ya = a[1]
    xb = b[0]
    yb = b[1]
    u = xb - xa
    v = yb - ya
    return math.sqrt((u * u) + (v * v))


def valideCorde(i, j, tabcorde):
    nbCorde = len(tabcorde)
    if i == j:
        return False

    # permutation pour avoir j>i
    if i > j:
        tmp = j
        j = i
        i = tmp

    # si i et j sont des sommets adjacents, on retourne Faux
    if voisins(i, j):
        return False

    # On parcoure le tableau des cordes déjà tracées
    for k in range(0, nbCorde):
        (a, b) = tabcorde[k]

        # si a >b, on permute les valeurs de a et b.
        if a > b:
            tmp = b
            b = a
            a = tmp

        # On vérifie si la corde est déjà tracée. Si elle l'est déjà, on retourne Faux
        if ((i, j) == (a, b)) or ((i, j) == (b, a)):
            return False
        # on vérifie que la corde (i,j) ne coupe pas les cordes déjà tracées. Si oui, on retourne Faux
        if (a < i < b < j) or (i < a < j < b):
            return False
    return True


def validecorde(i, j):
    return valideCorde(i, j, tabcorde)


def ajoutCorde(i, j):
    if (i > j):
        tmp = j
        j = i
        i = tmp
    tabcorde.append((i, j))


def voisins(i, j):
    i = i % nbSommets
    j = j % nbSommets
    if i > j:
        tmp = j
        j = i
        i = tmp
    if j == i + 1:
    # les points sont adjacentq
        return True
    elif i == 0 and j == nbSommets - 1:
    # cas du rebouclage
        return True
    else:
        return False


if __name__ == '__main__':
    main()
