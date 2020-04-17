from main import *
from polygone import *

def main():
    glouton()
    print(tabcorde)

def corde_exterieur():
    tablong = {}
    i = 0
    while (len(tablong) != nbSommets):
        a=i
        b=(i + 2) % nbSommets
        if (a > b):  # permutation pour avoir j>i
            tmp = b
            b = a
            a = tmp
        tablong[a,b]=longueur(a, b)
        i += 1
    return tablong

def glouton():
    tab = corde_exterieur()
    print(tab)
    while (len(tabcorde)!=nbSommets-3):
        print("Corde tracé",tabcorde)
        glouton_etape(tab)
        last = tabcorde[-1]
        i = last[0]
        if tab.get((last[0],last[1]))!=None:
            del tab[(last[0],last[1])]
        if tab.get((last[1],last[0]))!=None:
            del tab[(last[1],last[0])]
        retirerMax = max(last[0],last[1])
        retirerMin = min(last[0], last[1])
        if valideCorde(retirerMax, retirerMax - 3, tabcorde):
            tab[retirerMax, (retirerMax - 3)%nbSommets] = longueur(retirerMax, (retirerMax - 3)%nbSommets)
        if valideCorde(retirerMin, retirerMin + 3, tabcorde):
            tab[retirerMin, retirerMin + 3] = longueur(retirerMin, retirerMin + 3)

def glouton_etape(tab):
    tab = valideCordeGlouton(tab)
    print("Corde possible",tab)
    min=-1
    for k in tab.values():
        if min==-1 or k<min:
            min=k
    i=find_key(tab,min)[0]
    j=find_key(tab,min)[1]
    ajoutCorde(i,j)

def valideCordeGlouton(tab):
    tabtmp=tab.copy()
    for i in tab.keys():
        if valideCorde(i[0],i[1],tabcorde)==False:
            del tabtmp[(i[0],i[1])]
    return tabtmp

def find_key(tab,v):
    for k, val in tab.items():
        if v == val:
            return k
    return None


if __name__ == '__main__':
    main()
