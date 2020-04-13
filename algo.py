#-*- coding: utf-8 -*-
import math
n = 7
#tabcorde= [(0,2),(0,3),(3,5)]
tabcorde=[]
#polygone=[]
polygone=[(0,10),(0,20),(8,26),(15,26),(27,21),(22,12),(10,0)]

def main():
    #figure()
    #print("7 : ",nbtri(7))
    #print(longueur(0,2))
    glouton()
    #print(tabcorde)
    #print(validecorde(1,6))
    #test()
    #essais_successifs()
    print(tabcorde)

def figure():
    n=int(input("Nombre de sommet de la figure : "))
    for i in range(0,n):
        x=int(input("x = "))
        y=int(input("y = "))
        polygone.append((x,y))
    print(polygone)

def test():
    #affiche tout les cordes qui peuvent etre tracées
    for y in range(0,int(n/2)+1):
        for p in range(0,n):
            if validecorde(y,p):
                print("i :", y, "| j :", p)

def validecorde(i,j) :
    i=i%n 
    j=j%n
    #pour rester entre 0 et n-1
    l = len(tabcorde)
    if(l>=n-3):
    #verification que toutes les cordes ne sont pas déjà tracées
        return False
    elif i==j :
    #si les points sont identiques
        return False
    if(i>j):
        tmp=j
        j=i
        i=tmp
    #permutation pour avoir j>i

    if(abs(i-j)==1 or ((j+1+i)%n)==0):
    #si a coté (j+1+i) c'est pour quand ca reboucle
        return False
    if(abs(i-j)>1):
        for k in tabcorde :
            if(k[0]==i and k[1]==j):
                return False
            elif (k[0]<i and k[1]>i) and (j<k[0] or j>k[1]):
                return False
            elif (k[0]<j and k[1]>j) and (i<k[0] or i>k[1]):
                return False
    return True

def essais_successifs():
    k=0
    for i in range(0,n):
        while validecorde(i,k)==False:
            k+=1
            if k==n-1 :
                break
        if validecorde(i,k):
            if i<k :
                tabcorde.append((i,k))
            else :
                tmp = k
                k = i
                i = tmp
                tabcorde.append((i,k))
        k=0
        print(tabcorde)

def nbtri(n):
    c=n-2
    return ((math.factorial(2*c))/((math.factorial(c+1))*(math.factorial(c))))

def longueur(i,j):
    a=polygone[i]
    b=polygone[j]
    xa=a[0]
    ya=a[1]
    xb=b[0]
    yb=b[1]
    u=xb-xa
    v=yb-ya
    return math.sqrt((u*u)+(v*v))

def corde_exterieur():
    tablong={}
    l=len(polygone)
    i=0
    while(len(tablong)!=l):
        tablong[longueur(i,(i+2)%l)]=(i,(i+2)%l)
        i+=1
    return tablong

def glouton():
    tablong=corde_exterieur()
    while(len(tabcorde)!=len(polygone)):
        if(tablong=={}):
            break
        i=tablong[min(tablong)][0]
        j=tablong[min(tablong)][1]
        if(validecorde(i,j)):
            tabcorde.append((i,j))
        del tablong[min(tablong)]

#doit toujours etre a la fin
if __name__ == '__main__':
     main()