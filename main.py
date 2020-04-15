import math

from polygone import figure

def main():
    figure()


def test():
    # affiche tout les cordes qui peuvent etre tracées
    for y in range(0, int(n / 2) + 1):
        for p in range(0, n):
            if valideCorde(y, p):
                print("i :", y, "| j :", p)

# doit toujours etre a la fin
if __name__ == '__main__':
    main()
