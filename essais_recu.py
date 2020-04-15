
def triangulation(nbCordesTracees, i):

    #On ne trace pas de corde issue du sommet i fco
    # ENCORE POSSIBLE fco
    if i<NBSOMMETS - 3 :
        triangulation(nbCordesTracees, i+1 )

    # On trace l'une des cordes issue de Si fco
    POUR chaque corde j issue du sommet i FAIRE
    #SATISFAISANT fco
    if valideCorde(i, j, nbCordesTracees) :
        longueurCourante=longueurCourante + longueurCorde(i,j)
        if longueurCourante < longueurOptimale :
            # ENREGISTRER fco
            EnregistrerCorde(i,j)
            # SOLTROUVEE fco
            if nbCordesTracees = NBSOMMETS - 3 :
                longueurOptimale = longueurCourante
                EnregistrerLeTrace
            else:
                # ENCORE POSSIBLE fco
                if i<NBSOMMETS - 3 :
                    triangulation(nbCordesTracees+1, i+1)
        # DEFAIRE fco
        longueurCourante=longueurCourante - longueurCorde(i,j)