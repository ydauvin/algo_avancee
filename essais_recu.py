from random import randint
from polygone import *


def main():
    initVecteur()
    essais_successifs()
    print(tabcorde)

def essais_successifs():
    for i in range(0,nbSommets):
        essais_successifs_etape(i)

def essais_successifs_etape(i):
    k=randint(0,nbSommets-1)
    while(k==i):
        k = randint(0, nbSommets - 1)
    if(valideCorde(i,k)):
        ajoutCorde(i, k)

def initVecteur():
    C  =[]
    for i in range(0,nbSommets):
        for j in range(i+1,(nbSommets+i)):
            #  print("j =",j%nbSommets)
            if(i+1!=j%nbSommets and j%nbSommets+1!=i and voisins(i,j)!=True):
                a=i
                b=j%nbSommets
                if a > b:
                    tmp = b
                    b = a
                    a = tmp
                if(present((a,b),C)==False):
                    C.append((a,b))
    print(C)

def present(k,tab):
    for i in tab:
        if i==k:
            return True
    return False



if __name__ == '__main__':
    main()
