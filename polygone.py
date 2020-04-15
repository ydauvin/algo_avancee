import math

n = 7
polygone = [(0, 10), (0, 20), (8, 26), (15, 26), (27, 21), (22, 12), (10, 0)]


# polygone=[]

def figure():
    n = int(input("Nombre de sommet de la figure : "))
    for i in range(0, n):
        x = int(input("x = "))
        y = int(input("y = "))
        polygone.append((x, y))
    print(polygone)


def longueur(i, j):
    a = polygone[i]
    b = polygone[j]
    xa = a[0]
    ya = a[1]
    xb = b[0]
    yb = b[1]
    u = xb - xa
    v = yb - ya
    return math.sqrt((u * u) + (v * v))


def nbtri(n):
    c = n - 2
    return ((math.factorial(2 * c)) / ((math.factorial(c + 1)) * (math.factorial(c))))
