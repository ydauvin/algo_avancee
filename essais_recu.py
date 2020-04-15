
PROC triangulation(ent nbCordesTracees, ent i) EST

  co On ne trace pas de corde issue du sommet i fco
  co ENCORE POSSIBLE fco
  SI i<NBSOMMETS - 3 ALORS
     triangulation(nbCordesTracees, i+1 )
  FSI

  co On trace l'une des cordes issue de Si fco
  POUR chaque corde j issue du sommet i FAIRE
     co SATISFAISANT fco
     SI valideCorde(i, j, nbCordesTracees) ALORS
        longueurCourante=longueurCourante + longueurCorde(i,j)
        SI longueurCourante < longueurOptimale ALORS
           co ENREGISTRER fco
           EnregistrerCorde(i,j)
           co SOLTROUVEE fco
           SI nbCordesTracees = NBSOMMETS - 3 ALORS
              longueurOptimale = longueurCourante
              EnregistrerLeTrace
           SINON
              co ENCORE POSSIBLE fco
              SI i<NBSOMMETS - 3 ALORS
                 triangulation(nbCordesTracees+1, i+1)
              FSI
           FSI
        FSI
        co DEFAIRE fco
        longueurCourante=longueurCourante - longueurCorde(i,j)
     FSI
  FAIT

  FIN