n=7
polygone=[(0,10),(0,20),(8,26),(15,26),(27,21),(22,12),(10,0)]
#polygone=[]

def figure():
    n=int(input("Nombre de sommet de la figure : "))
    for i in range(0,n):
        x=int(input("x = "))
        y=int(input("y = "))
        polygone.append((x,y))
    print(polygone)

def nbtri(n):
    c = n - 2
    return ((math.factorial(2 * c)) / ((math.factorial(c + 1)) * (math.factorial(c))))