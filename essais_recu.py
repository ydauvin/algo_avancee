from random import randint

from polygone import *


def main():
    essais_successifs()
    print(tabcorde)

def essais_successifs():
    i=0
    while (nbCorde()<nbSommets-3):
        essais_successifs_etape(i)
        i+=1
        if(i==nbSommets):
            i=0
        print(i)

def essais_successifs_etape(i):
    k=randint(0,nbSommets-1)
    if(valideCorde(i,k)):
        ajoutCorde(i, k)

if __name__ == '__main__':
    main()
