from random import randint

from polygone import *


def main():
    essais_successifs()
    print(tabcorde)

def essais_successifs():
    for i in range(0,nbSommets):
        essais_successifs_etape(i)
        print(i)

def essais_successifs_etape(i):
    k=randint(0,nbSommets-1)
    if(valideCorde(i,k)):
        ajoutCorde(i, k)

if __name__ == '__main__':
    main()
