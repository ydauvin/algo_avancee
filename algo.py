#-*- coding: utf-8 -*-
import math
#import numpy
#from scipy import *
n = 7
tabcorde= [(0,2),(0,3)]


def main():
    print(validecorde(7, 3))

def validecorde(i,j) :
    l = len(tabcorde)
    if(l>=n-3):
        return False
    if(i>j):
        tmp=j
        j=i
        i=tmp
    if(abs(i-j)>1):
        for k in tabcorde :
            if(k[0]==i and k[1]==j):
                return False
            elif (k[0]<i and k[1]>i) and (j<k[0] or j>k[1]):
                return False
            elif (k[0]<j and k[1]>j) and (i<k[0] or i>k[1]):
                return False
    return True




#doit toujours etre a la fin
if __name__ == '__main__':
    main()