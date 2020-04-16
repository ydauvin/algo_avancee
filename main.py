import math

from polygone import figure

n = 7
# tabcorde= [(0,2),(0,3),(3,5)]
tabcorde = []


def main():
    figure()


def test():
    # affiche tout les cordes qui peuvent etre tracées
    for y in range(0, int(n / 2) + 1):
        for p in range(0, n):
            if validecorde(y, p):
                print("i :", y, "| j :", p)


def validecorde2(i, j):

    l = len(tabcorde)

    # permutation pour avoir j>i
    if (i > j):
        tmp = j
        j = i
        i = tmp

    #si i et j sont des sommets adjacents, on retourne Faux
    if(j==i+1) :
        return False
    #On parcoure le tableau des cordes déjà tracées
    for k in (0,l) :
        (a,b)=tabcorde[k]

        #si a >b, on permute les valeurs de a et b.
        if (a > b):
            tmp = b
            b = a
            a = tmp

        #On vérifie si la corde est déjà tracée. Si elle l'est déjà, on retourne Faux
        if (((i,j)==(a,b))or((i,j)==(b,a))) :
            return False

        #on vérifie que la corde (i,j) ne coupe pas les cordes déjà tracées. SI oui, on retourne Faux
        if((a<i<b<j)or (i<a<j<b)) :
            return False

    return True



def validecorde(i,j) :

    l = len(tabcorde)

    if (l >= n - 3):
        # verification que toutes les cordes ne sont pas déjà tracées
        return False
    elif i == j:
        # si les points sont identiques
        return False
    if (i > j):
        tmp = j
        j = i
        i = tmp
    # permutation pour avoir j>i

    if abs(i - j) == 1 or ((j + 1 + i) % n) == 0:
        # si a coté (j+1+i) c'est pour quand ca reboucle
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


def essais_successifs():
    k = 0
    for i in range(0, n):
        while validecorde(i, k) == False:
            k += 1
            if k == n - 1:
                break
        if validecorde(i, k):
            if i < k:
                tabcorde.append((i, k))
            else:
                tmp = k
                k = i
                i = tmp
                tabcorde.append((i, k))
        k = 0
        print(tabcorde)


# doit toujours etre a la fin
if __name__ == '__main__':
    main()
