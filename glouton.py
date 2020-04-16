from main import *
from polygone import *

def main():
    glouton()
    print(tabcorde)

def corde_exterieur():
    tablong = {}
    i = 0
    while (len(tablong) != nbSommets):
        tablong[i,(i + 2) % nbSommets]=longueur(i, (i + 2) % nbSommets)
        i += 1
    return tablong

def glouton():
    tab = corde_exterieur()
    while (len(tabcorde)!=nbSommets-3):
        glouton_etape(tab)
        last = tabcorde[-1]
        i = last[0]
        del tab[(last[0],last[1])]
        retirerMax = max(last[0],last[1])
        retirerMin = min(last[0], last[1])
        if valideCorde(retirerMax, retirerMax - 3):
            tab[retirerMax, (retirerMax - 3)%nbSommets] = longueur(retirerMax, (retirerMax - 3)%nbSommets)
        if valideCorde(retirerMin, retirerMin + 3):
            tab[retirerMin, retirerMin + 3] = longueur(retirerMin, retirerMin + 3)
        tab=valideCordeGlouton(tab)

def glouton_etape(tab):
    print(tab)
    min=-1
    for i in tab.values():
        if min==-1 or i<min:
            min=i
    i=find_key(tab,min)[0]
    j=find_key(tab,min)[1]
    ajoutCorde(i,j)

def valideCordeGlouton(tab):
    tabtmp=tab.copy()
    for i in tab.keys():
        if valideCorde(i[0],i[1])==False:
            del tabtmp[(i[0],i[1])]
    print("   tab",tab)
    print("tabtmp",tabtmp)
    return tabtmp

def find_key(tab,v):
    for k, val in tab.items():
        if v == val:
            return k
    return None


if __name__ == '__main__':
    main()
