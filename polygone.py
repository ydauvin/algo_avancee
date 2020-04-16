import math

nbSommets = 5
polygone = [(0, 10), (0, 20), (8, 26), (15, 26), (27, 21)]#, (22, 12), (10, 0)]
tabcorde = []

# polygone=[]
# tabcorde= [(0,2),(0,3),(3,5)]

def main():
    #figure()
    print(nbtri(5))

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


def valideCorde(i, j):
    i = i % nbSommets  # pour rester entre 0 et n-1
    j = j % nbSommets  # pour rester entre 0 et n-1
    l = nbCorde()
    if (l >= nbSommets - 3): # verification que toutes les cordes ne sont pas déjà tracées
        return False
    elif i == j: # si les points sont identiques
        return False
    if (i > j): # permutation pour avoir j>i
        tmp = j
        j = i
        i = tmp

    if abs(i - j) == 1 or (j==0 and i==nbSommets-1) or (i==0 and j==nbSommets-1): #test si i et j sont voisins
        return False
    if abs(i - j) > 1:
        for k in tabcorde:
            if (k[0] == i and k[1] == j):
                return False
            elif (k[0] < i and k[1] > i) and (j < k[0] or j > k[1]):
                return False
            elif (k[0] < j and k[1] > j) and (i < k[0] or i > k[1]):
                return False
    return True

def ajoutCorde(i,j):
    tabcorde.append((i, j))

def nbCorde():
    return len(tabcorde)

if __name__ == '__main__':
    main()