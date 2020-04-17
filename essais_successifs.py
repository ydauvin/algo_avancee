from random import randint
from polygone import *

C = []
longueurCourante=0
longueurOptimale=0
def main():
    print(C)
    initVecteur()
    print(C)
   # essais_successifs()
    print(tabcorde)

def essais_successifs():
    i=0
    longueurCourante=0
    tabcordetmp = []
    while(len(tabcordetmp)<nbSommets-3):
        if valideCorde(C[i][0], C[i][1],tabcordetmp):
            longueurCourante = longueurCourante + C[i][2]
            tabcordetmp.append((C[i][0], C[i][1]))
        i=(i+1)%nbSommets
    print(tabcordetmp)
    longueurOptimale=longueurCourante
    longueurCourante=0
    tab=[]
    while(len(tab)<nbSommets-3):
        tab=essais_successifs_etape(i,longueurCourante,longueurOptimale, tab)
        if tab==None :
            tab=[]
        i = (i + 1) % (((nbSommets-3)*(nbSommets)//2)-1)



def essais_successifs_etape(i, longueurCourante, longueurOptimale,tab):
    i = (i) % (((nbSommets - 3) * (nbSommets) // 2) - 1)
    print(i)
    if valideCorde(C[i][0], C[i][1],tab) :
        longueurCourante = longueurCourante + C[i][2]
        if (longueurCourante<longueurOptimale):
            tab.append((C[i][0], C[i][1]))
            if len(tab)==nbSommets-3:
                return tab
            else:
                j=randint(0,nbSommets)
                tab=essais_successifs_etape(i+j, longueurCourante, longueurOptimale,tab)
        else:
            tab=[]
            return tab

if __name__ == '__main__':
    main()
