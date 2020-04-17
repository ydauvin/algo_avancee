from orca.punctuation_settings import infinity
from polygone import *
from essais_recu import *

nbSommets = 7
polygone = [(0, 10), (0, 20), (8, 26), (15, 26), (27, 21), (22, 12), (10, 0)]
tabcorde = []

n=nbSommets

T=[]
for i in range (0,n) :
    for t in range (0,n) :
        T[i][t]=0

def longueurcorde(i,j) :
    return C[i][j]

def Triangulation_dynamique():

    for i in (n,0):
        for t in (4, n + 1):
            longueuropt = infinity
            kmin=0
            okCorde1=False
            okCorde2=False

            for k in (1,t-1):
                ok1 = False
                ok2 = False
                longueurCourante=0
                if k>1 :
                    longueurCourante = longueurcorde(i, i + k%n)  + longueur(T(i, k + 1%n))
                    ok1=True
                if k<n-2 and valideCorde(i+k%n,i+t-1%n):
                    longueurCourante = longueurcorde(i + k %n, i + t - 1%n) + longueur(T(i + k%n, t - k%n))
                    ok2=True
                # on regarde si la longueur qu'on vient de calculer est plus petite que la longueur optimale actuelle.
                if longueurCourante < longueuropt:
                    longueuropt = longueurCourante
                    kmin=k
                    okCorde1=ok1
                    okCorde2=ok2
            if(okCorde1):
                T[i][t]=T[i][t]+C[i,i+kmin]
                T[i][t] = T[i][t] + T[i][kmin+1]

            if (okCorde2):
                T[i][t] = T[i][t] + C[i+kmin,t-1]
                T[i][t] = T[i][t] + T[i+kmin][t-kmin]
# doit toujours etre a la fin

if __name__ == '__main__':
    main()
