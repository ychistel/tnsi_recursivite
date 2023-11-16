.. TNSI

Activité
========

On cherche à calculer la somme des premiers nombres entiers naturels sans utiliser la formule mathématique. On étendra
cette somme à des nombres entiers issus d'une suite.

Programmation itérative
-----------------------

#. Écrire une fonction ``somme_f`` qui calcule la somme des ``n`` premiers nombres entiers positifs. La fonction prend
   en paramètre le nombre ``n`` et renvoie un nombre entier égal à la somme :math:`1+2+3+...+n`.

   Cette fonction utilise une boucle bornée ``for``.

#. Écrire une fonction ``somme_w`` qui calcule la somme des ``n`` premiers nombres entiers positifs. La fonction prend
   en paramètre le nombre ``n`` et renvoie un nombre entier égal à la somme :math:`1+2+3+...+n`.

   Cette fonction utilise une boucle conditionnelle ``while``.

#. Vérifier dans les deux cas que la somme des 100 premiers nombres entiers vaut 5050.

Programmation récursive
-----------------------

Il est possible de calculer cette somme sans utiliser de boucle. On donne le code de la fonction ``somme_r`` qui a pour
paramètre le nombre ``n``.

.. literalinclude:: ../python/activite.py
   :lines: 36,47-50

#. Que renvoie l'appel ``somme_r(1)`` lorsque ``n=1`` ?
#. Que renvoie l'appel ``somme_r(2)`` lorsque ``n=2`` ?
#. Décrire l'enchainement d'appels des fonctions pour ``n=3``.
#. Ecrire le code de la fonction puis vérifier que la somme des 100 premiers nombres entiers est 5050.
#. Modifier votre code pour calculer la somme des nombres pairs jusqu'à la valeur ``n``.

   a) Vérifier que la somme des nombres pairs lorsque ``n=100`` est égale à 2550.
   b) Vérifier que la somme des nombres pairs lorsque ``n=101`` est aussi égale à 2550.
      Dans le cas contraire corriger votre code.
      
#. On cherche à calculer la somme des nombres entiers en partant d'un nombre :math:`n` donné telle que tous les termes
   de la somme sont :
   
   - des nombres positifs inférieurs ou égaux à :math:`n`
   - deux nombres consécutifs ont pour différence 3.

   Par exemple:

   - la somme à calculer pour :math:`n=10` est :math:`10+7+4+1`
   - la somme à calculer pour :math:`n=8` est :math:`8+5+2`.

   Créer la fonction récursive ``somme_suite`` qui a pour paramètre un nombre ``n`` et qui renvoie la somme demandée.
