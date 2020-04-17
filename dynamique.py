from orca.punctuation_settings import infinity
from polygone import *

T=[]
for i in range (0,n) :
    for t in range (0,n) :
        T[i][t]=0


def main():


def longueurcorde(i,j) :
    return C[i][j]

def Triag():

    for i in (n,0):
        for t in (4, n + 1):
            longueuropt = infinity
            kmin=0
            ok=False
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
                    ok=ok1&ok2
            if(ok):
                T[i][t]=T[i][t]+C[i,i+kmin]
                T[i][t] = T[i][t] + T[i][kmin+1]
                T[i][t] = T[i][t] + C[i+kmin,t-1]
                T[i][t] = T[i][t] + T[i+kmin][t-kmin]



#
#def T(i,t):
    longueuropt=-1
#
    #  for k in (1,t-1) :
    #
    #           longueurCourante=longueurcorde(i,i+k)+longueurcorde(i+k,i+t-1)+T(i,k+1)+T(i+k,t-k)
    #
    #           #on regarde si la longueur qu'on vient de calculer est plus petite que la longueur optimale actuelle.
    #           if longueurCourante< longueuropt or longueuropt==-1 :
    #               longueuropt=longueurCourante
    #return longueuropt

#def Triangulation_dynamique():
    #   Tmin=-1
    #
    #for t in (4,n+1):
    #   for i in (0,n):
    #       T=T(i,t)
    #       if T<Tmin or Tmin==-1 :
    #           Tmin=T

    #return Tmin

# doit toujours etre a la fin
if __name__ == '__main__':
    main()
