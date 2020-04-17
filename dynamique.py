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
    return longueur(i,j)

def longueur_Tab(T) :
    if(T==0) :
        return 0
    lenT=len(T)
    l=0
    for i in(0,lenT):
        a=T[i][0]
        b=T[i][1]
        l=l+longueurcorde(a,b)
    return l
def Triangulation_dynamique():

    for i in (n-1,0):
        for t in (3, n):
            longueuropt = infinity
            kmin=0
            okCorde1=False
            okCorde2=False

            for k in (1,t-1):
                ok1 = False
                ok2 = False
                longueurCourante=0
                if k>1 :
                    longueurCourante = longueur(i,(i + k)%n)  + longueur_Tab(T[i][(k + 1)%n])
                    ok1=True
                if k<n-2 :# and valideCorde(i+k%n,i+t-1%n):
                    longueurCourante = longueur((i + k)%n,( i + t - 1)%n) + longueur_Tab(T[(i+k)%n][(t - k)%n])
                    ok2=True
                # on regarde si la longueur qu'on vient de calculer est plus petite que la longueur optimale actuelle.
                if longueurCourante < longueuropt:
                    longueuropt = longueurCourante
                    kmin=k
                    okCorde1=ok1
                    okCorde2=ok2
            if(okCorde1):
                tab=[T[i%n][t%n]]
                tab.append([i%n,(i+kmin)%n])
                tab.extend([T[i%n][(kmin+1)%n]])
                T[i%n][t%n]=tab
            if (okCorde2):
                tab=[T[i%n][t%n]]
                tab.append([(i+kmin)%n,(t-1)%n])
                tab.extend([T[(i+kmin)%n][(t-kmin)%n]])
                T[i%n][t%n] =tab


# doit toujours etre a la fin

if __name__ == '__main__':
    main()
