infinity=9999999999999999999

from essais_successifs import *
from polygone import *

n=nbSommets
T = []
tab = []
for k in range(0,n):
    for i in range(0, n):
        tab.append(0)
    T.append(tab)
    tab=[]

def main():
    print(T)
    initVecteur()
    Triangulation_dynamique()
    print(T)

def longueurcorde(i,j) :
    return C[i][j][3]

def longueur_Tab(T) :
    lenT=len(T)
    l=0
    for i in(0,lenT):
        l=l+longueurcorde(T[i])



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
                    longueurCourante = longueurcorde(i, i + k%n)  + longueur_Tab(T[i][k + 1%n])
                    ok1=True
                if k<n-2 :# and valideCorde(i+k%n,i+t-1%n):
                    longueurCourante = longueurcorde(i + k %n, i + t - 1%n) + longueur_Tab(T[i+k%n][t - k%n])
                    ok2=True
                # on regarde si la longueur qu'on vient de calculer est plus petite que la longueur optimale actuelle.
                if longueurCourante < longueuropt:
                    longueuropt = longueurCourante
                    kmin=k
                    okCorde1=ok1
                    okCorde2=ok2
            if(okCorde1):
                tab=T[i][t]
                tab.append(C[i][i+kmin])
                tab.append(T[i][kmin+1])
                T[i][t]=tab
            if (okCorde2):
                tab=T[i][t]
                tab.append(C[i+kmin][t-1])
                tab.append(T[i+kmin][t-kmin])
                T[i][t] =tab


# doit toujours etre a la fin

if __name__ == '__main__':
    main()
