infinity=9999999999999999999
from polygone import *

n=nbSommets
T = []
tab = []
for k in range(0,n):
    for i in range(0, n):
        tab.append([])
    T.append(tab)
    tab=[]

def main():

    Triangulation_dynamique()
    print(T)

def longueurcorde(i,j) :
    return longueur(i,j)

def longueur_Tab(T) :
    if(T==[]) :
        return 0
    lenT=len(T)
    l=0
    for i in(0,lenT):
        a=T[i][0]
        b=T[i][1]
        l=l+longueurcorde(a,b)
    return l

def Triangulation_dynamique():
    # On boucle en commençant par n-1 puisque on remplit le tableau en ayant besoin des tableaux d'indice de sommets supérieurs
    for i in (n-1,0):
        # On fait varier t de 4 à n puisque il n'existe pas de triangulation pour t<=3.
        for t in (3, n):

            # on prend une longueur optimale initiale très grande (infini si on est en python)
            longueuropt = infinity
            # kmin sert à stocker le k que l'on veut déterminer
            kmin=0
            # ces deux booléens nous servent à déterminer si on a tracé la corde 1 ou la corde 2 ou les deux (dans les cas particuliers, on ne trace qu'une seule corde, d'où ces vérifications)
            okCorde1=False
            okCorde2=False

            for k in (1,t-1):
                ok1 = False
                ok2 = False
                longueurCourante=0

                #  on a un cas particulier si k=1, en effet la première équation de corde n'est pas possible donc on retire ce cas

                if k>1 :
                    # on ajoute à la longueur courante la longueur de la corde
                    longueurCourante = longueur(i,(i + k)%n)  + longueur_Tab(T[i][(k + 1)%n])
                    ok1=True
                # on a un cas particulier si k vaut t-2, en effet la deuxième équation de corde n'est pas possible donc on retire ce cas
                if k<n-2 and validecorde((i+k)%n,(i+t-1)%n):
                    longueurCourante = longueur((i + k)%n,( i + t - 1)%n) + longueur_Tab(T[(i+k)%n][(t - k)%n])
                    ok2=True
                # on regarde si la longueur qu'on vient de calculer est plus petite que la longueur optimale actuelle.
                if longueurCourante < longueuropt:
                    # Dans ce cas, on conserve cette valeure de longueur et cette valeur de k dans respectivement longueuropt et kmin et on associe aux booléens okCorde1 et okCorde2 les valeurs de ok1 et ok2
                    longueuropt = longueurCourante
                    kmin=k
                    okCorde1=ok1
                    okCorde2=ok2
            # si la corde1 est valide on met à jour notre tableau
            if(okCorde1):
                tab=[T[i%n][t%n]]
                tab.append([i%n,(i+kmin)%n])
                tab.extend([T[i%n][(kmin+1)%n]])
                T[i%n][t%n]=tab
            # Si la corde 2 est valide, on met à jour notre tableau
            if (okCorde2):
                tab=[T[i%n][t%n]]
                tab.append([(i+kmin)%n,(t-1)%n])
                tab.extend([T[(i+kmin)%n][(t-kmin)%n]])
                T[i%n][t%n] =tab


# doit toujours etre a la fin

if __name__ == '__main__':
    main()
