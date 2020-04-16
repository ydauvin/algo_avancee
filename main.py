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
