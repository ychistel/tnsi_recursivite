Les tours de Hanoï
==================

Dans le jeu des tours de Hanpoï, :math:`n` disques sont empilés par taille décroissante sur un premier poteau. Le but du jeu est de déplacer ces disques vers un second poteau en les plaçcant dans le même ordre, c'est à dire par taille décroissante. On dispose pour cela d'un troisième poteau. 

Les règles du jeu sont les suivantes:

-  on ne déplace qu'un disque à la fois,
-  on ne peut déplacer qu'un disque situé en haut d'une pile,
-  on ne peut pas déposer un disque sur un disque de plus petite taille.

On donne ci-dessous la disposition des disques en début et fin de partie.

.. figure:: ../img/hanoi_debut_partie.svg
   :align: center
   :width: 420

   Début de partie des tours de hanoï avec 4 disques

   .. figure:: ../img/hanoi_fin_partie.svg
      :align: center
      :width: 420

   Fin de partie des tours de hanoï avec 4 disques

Étude de cas particuliers
-------------------------

#. Proposer une solution du jeu avec 2 disques.
#. Donner une solution du jeu avec 3 disques. On pourra représenter les différentes étapes par des schémas.
#. Dans le cas des trois disques, repérer dans votre schéma les étapes correspondant à la resolution du problème avec 2 disques. 
#. En déduire un algorithme de résolution du jeu avec 3 disque en notant la resolution du jeu à 2 disque par ``hanoi(2, x -> y)`` où ``x`` et ``y`` désignent des poteaux.

Étude du cas général
--------------------

On suppose que l'on sait résoudre le problème avec :math:`n-1` disques. On note cette résolution comme précédemment par ``hanoi(n-1, A -> C)`` lorsqu'on déplace les disques du poteau A vers le poteau C. 

.. figure:: ../img/hanoi_n_disques.svg
   :align: center
   :width: 420

   Jeu des tours de Hanoï avec :math:`n` disques

#. Représenter schématiquement la résolution du jeu avec :math:`n` disques.
#. Écrire un algorithme qui s'appuie sur la résolution du jeu avec :math:`n-1` disques pour résoudre le jeu avec :math:`n` disques.

Programmation en Python
-----------------------

Le programme Python du jeu des tours de Hanoi utilisent les structures de données suivantes:

-  3 piles pour représenter les poteaux A, B et C avec leurs disques,
-  des nombres entiers pour représenter les disques

Au début de la partie, la pile A contient tous les disques, c'est à dire les nombres entiers rangés par ordre croissant (le plus petit est au sommet de la pile). Les pilse B et C sont vides.

À la fin du programme, La pile C contient les disques, c'est à dire les nombres entiers rangés dans l'ordre croissant, le plus petit étant au sommet de la pile. Les piles A et B sont vides.

Le programme à compléter contient des fonctions:

-  la fonction ``dessus(p)`` qui renvoie la valeur du disque au sommet de la pile ``p`` sans le supprimer.
-  la fonction ``transfert(p1,p2)`` qui déplace un disque d'une pile ``p1`` à une autre pile ``p2``.
-  l'import des fonctions pour créer et manipuler des piles.

Ouvrir le notebook de code ``fc4e-2297352`` qui contient le programme puis compléter la fonction ``tout_hanoi`` pour résoudre le jeu.

