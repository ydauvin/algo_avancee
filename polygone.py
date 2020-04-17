import math

#nbSommets = 7
#polygone = [(0, 10), (0, 20), (8, 26), (15, 26), (27, 21), (22, 12), (10, 0)]

nbSommets = 6
polygone = [(0, 0), (0, 20), (7, 3), (6, 8),(2, 9),(1, 7)]
tabcorde = []
C=[]

# polygone=[]
# tabcorde= [(0,2),(0,3),(3,5)]

def main():
    #figure()
    print(longueur(0,2)+longueur(0,3)+longueur(0,4))
    print(longueur(5,1)+longueur(5,2)+longueur(5,3))
    print(longueur(4,0)+longueur(4,1)+longueur(4,2))
    print(longueur(3,5)+longueur(3,0)+longueur(3,1))
    print(longueur(2,0)+longueur(2,5)+longueur(2,4))

    print(longueur(1,5)+longueur(1,4)+longueur(1,3))
    print(longueur(1,5)+longueur(5,3)+longueur(2,4))
    print(longueur(2,0)+longueur(0,3)+longueur(3,5))
    print(longueur(5,1)+longueur(1,4)+longueur(4,2))

    print(longueur(0,2)+longueur(2,5)+longueur(5,3))
    print(longueur(4,0)+longueur(0,3)+longueur(3,1))
    print(longueur(2,0)+longueur(0,4)+longueur(4,2))

    print(longueur(5,1)+longueur(1,3)+longueur(3,5))
    print(longueur(0,4)+longueur(4,1)+longueur(1,3))



def initVecteur():
    for i in range(0,nbSommets):
        for j in range(i+1,(nbSommets+i)):
            #  print("j =",j%nbSommets)
            if(voisins(i,j)!=True):
                a=i
                b=j%nbSommets
                if a > b:
                    tmp = b
                    b = a
                    a = tmp
                if(present((a,b,longueur(a,b)),C)==False):
                    C.append((a,b,longueur(a,b)))

def present(k,tab):
    for i in tab:
        if i==k:
            return True
    return False



def figure():
    nbSommets = int(input("Nombre de sommet de la figure : "))
    for i in range(0, nbSommets):
        print("x" + str(i) + " = ", end='')
        x = int(input())
        print("y" + str(i) + " = ", end='')
        y = int(input())
        polygone.append((x, y))
    print(polygone)


def longueur(i, j):
    i=i%nbSommets
    j=j%nbSommets
    a = polygone[i]
    b = polygone[j]
    xa = a[0]
    ya = a[1]
    xb = b[0]
    yb = b[1]
    u = xb - xa
    v = yb - ya
    return math.sqrt((u * u) + (v * v))


""
def nbtri(n):
    c = n - 2
    return ((math.factorial(2 * c)) / ((math.factorial(c + 1)) * (math.factorial(c))))
""


def valideCorde(i, j,tabcorde):
    nbCorde = len(tabcorde)
    if i == j:
        return False

    # permutation pour avoir j>i
    if i > j:
        tmp = j
        j = i
        i = tmp

    # si i et j sont des sommets adjacents, on retourne Faux
    if voisins(i,j):
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

        # on vérifie que la corde (i,j) ne coupe pas les cordes déjà tracées. SI oui, on retourne Faux
        if (a < i < b < j) or (i < a < j < b):
            return False

    return True


def ajoutCorde(i, j):
    if (i > j):  # permutation pour avoir j>i
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
        return True
    elif i == 0 and j == nbSommets - 1:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
