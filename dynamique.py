from main import *
from polygone import *
T=[]
for i in range (0,n) :
    for t in range (0,n) :
        T[i][t]=0
def longueurcorde(i,j) :
    return C[i][j]


def T(i,t):
    longueuropt=-1

    for k in (1,t-1) :

                longueurCourante=longueurcorde(i,i+k)+longueurcorde(i+k,i+t-1)+T(i,k+1)+T(i+k,t-k)

                #on regarde si la longueur qu'on vient de calculer est plus petite que la longueur optimale actuelle.
                if longueurCourante< longueuropt or longueuropt==-1 :
                    longueuropt=longueurCourante
    return longueuropt

def Triangulation_dynamique():
    Tmin=-1

    for t in (4,n+1):
        for i in (0,n):
            T=T(i,t)
            if T<Tmin or Tmin==-1 :
                Tmin=T

    return Tmin
