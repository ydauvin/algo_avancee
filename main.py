
import math
from polygone import figure, valideCorde

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
            if valideCorde(y, p):
                print("i :", y, "| j :", p)

def triangulation(nbCordeTracee, i) :
    longueur = 0
    if (valideCorde(C[i][0],C[i][1])):
        longueur = longueur+C[2]


# doit toujours etre a la fin
if __name__ == '__main__':
    main()
