
import math
from polygone import figure

n = 7
# tabcorde= [(0,2),(0,3),(3,5)]
tabcorde = []

C=[(1,3,8),(2,4,6)]
longueur = 0


def main():
    figure()


def test():
    # affiche tout les cordes qui peuvent etre tracées
    for y in range(0, int(n / 2) + 1):
        for p in range(0, n):
            if validecorde(y, p):
                print("i :", y, "| j :", p)

def triangulation(nbCordeTracee, i) :

    if (validecorde2(C[i][0],C[i][1])):
        longueur= longueur+C[2]
        if








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
