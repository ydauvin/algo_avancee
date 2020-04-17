from polygone import *

def main():
    initVecteur()
    tabcorde = essais_successifs()
    print(tabcorde)


def essais_successifs():
    i = 0
    tabcordetmp = []
    # on prend les premières valeurs de C comme solution
    while (len(tabcordetmp) < nbSommets - 3):
        if valideCorde(C[i][0], C[i][1], tabcordetmp):
            tabcordetmp.append((C[i][0], C[i][1]))
        i = (i + 1) % nbSommets

    tab = []
    nbCorde = len(C)
    i = 0
    while (i < nbCorde):
        # on appelle la fonction pour de nouvelle valeur
        tab = essais_successifs_etape(i, tab)
        new = longueurCorde(tab)
        act = longueurCorde(tabcordetmp)

        # si la solution est meilleure, on la garde
        if (new < act and len(tab) == nbSommets - 3):
            tabcordetmp = tab
        tab = []
        i += 1
    return tabcordetmp


def essais_successifs_etape(i, tab):
    if valideCorde(C[i][0], C[i][1], tab):
    # si la corde est valide

        tab.append((C[i][0], C[i][1]))
        j = (i + 1) % len(C)

        essais_successifs_etape(j, tab)
        # appel recursif avec pour l element suivant dans C
    return tab


def present(k, tab):
    # indique si k est present dans tab
    for i in tab:
        if i == k:
            return True
    return False


def longueurCorde(tab):
    # Donne la longueur total des cordes presentes dans tab
    l = 0
    for i in tab:
        l += longueur(i[0], i[1])
    return l


if __name__ == '__main__':
    main()
