from random import randint
from polygone import *
C = []

def main():
    initVecteur()
    tabcorde=essais_successifs()
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
    longueurCourante=0
    tab=[]
    nbCorde=len(C)
    i=0
    while(i<nbCorde):
        tab=essais_successifs_etape(i,longueurCourante, tab)
        new=longueurCorde(tab)
        act=longueurCorde(tabcordetmp)
        if(new<act and len(tab)==nbSommets-3):
            tabcordetmp=tab
        tab=[]
        i+=1
    return tabcordetmp

def initVecteur():
    for i in range(0,nbSommets):
        for j in range(i+1,(nbSommets+i)):
            #  print("j =",j%nbSommets)
            if(voisins(i,j)!=True):
                a=i
                b=j%nbSommets
                if a > b:
                    tmp = b
                    b = a
                    a = tmp
                if(present((a,b,longueur(a,b)),C)==False):
                    C.append((a,b,longueur(a,b)))

def essais_successifs_etape(i, longueurCourante,tab):
    print("je suis dans etape")
    if valideCorde(C[i][0], C[i][1],tab) :
        longueurCourante = longueurCourante + C[i][2]
        tab.append((C[i][0], C[i][1]))
        j=(i+1)%len(C)
        essais_successifs_etape(j, longueurCourante,tab)
    return tab

def present(k,tab):
    for i in tab:
        if i==k:
            return True
    return False

def longueurCorde(tab):
    l=0
    for i in tab:
        l+=longueur(i[0],i[1])
    return l


if __name__ == '__main__':
    main()
