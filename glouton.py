from main import *
from polygone import *


def corde_exterieur():
    tablong = {}
    l = len(polygone)
    i = 0
    while (len(tablong) != l):
        tablong[longueur(i, (i + 2) % l)] = (i, (i + 2) % l)
        i += 1
    return tablong


def glouton():
    tablong = corde_exterieur()
    while len(tabcorde) != len(polygone):
        if tablong == {}:
            break
        i = tablong[min(tablong)][0]
        j = tablong[min(tablong)][1]
        if valideCorde(i, j):
            tabcorde.append((i, j))
        del tablong[min(tablong)]
