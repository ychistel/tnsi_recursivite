Exercices
=========

Exercice 1
---------

On donne la fonction suivante:

.. figure:: ../img/ordre.png
   :alt: image
   :align: center
   :width: 420

#. Expliquer pourquoi la fonction ``ordre(n)`` est récursive.
#. Que renvoie l’appel ``ordre(4)`` ?
#. Que se passe-t-il si on change la dernière instruction par ``return str(n)+ordre(n-1)`` ?

.. _exercice-1:

Exercice 2
---------

On donne la fonction suivante:

.. figure:: ../img/compte.png
   :alt: image
   :align: center
   :width: 420

#. Expliquer pourquoi la fonction ``compte(n)`` est récursive.
#. Que renvoie l’appel ``compte(5)`` ?
#. Que se passe-t-il si on change la dernière instruction par ``return 1+compte(n-2)`` ?

.. _exercice-2:

Exercice 3
----------

On donne le script suivant et la table de caractères ASCII:


.. |image| image:: ../img/alphabet.png
           :class: width-40
.. |image1| image:: ../img/tableASCII.png
            :class: width-60

|image| |image1|

On rappelle que la fonction Python ``chr(n)`` prend en argument un nombre entier ``n`` en écriture décimale et renvoie le caractère ASCII associé.

#. Quelle est la valeur renvoyée par la commande ``chr(65)`` ?
#. Quel est l’affichage à l’issu du script ?
#. Écrire la fonction récursive ``affiche_recursif`` renvoyant le même résultat que le script ci-dessus.

.. _exercice-3:

Exercice 4
----------

Lorsqu’on effectue une remise de 10% sur un prix, cela revient à multiplier ce prix par la valeur :math:`1-10/100`.

On veut calculer des baisses successives de 10% sur une valeur, le nombre de remises étant défini à l’avance.

#. Calculer trois remises successives de 10% sur un prix de 100 €.
#. Montrer en détaillant le calcul qu’un algorithme récursif peut s’appliquer.
#. Écrire un script itératif qui calcule :math:`n` remises successives de 10% sur un prix. On utilisera les variables ``prix`` et ``n``. La variable ``prix`` contiendra la valeur finale.
#. Vérifier votre script avec un prix de 100 pour :math:`n=3` remises.
#. Écrire la fonction récursive ``remise_successive`` qui calcule :math:`n` remise de 10% sur un prix défini à l’avance.

.. _exercice-4:

Exercice 5
----------

En mathématiques, pour trouver le plus grand commun diviseur de 2 nombres entiers, on applique l’algorithme d’Euclide, donné ci-dessous en python:

.. image:: ../img/ex-pgcd.png
   :alt: image
   :align: center
   :width: 420

#. S’agit-il d’une fonction récursive ? Pourquoi ?
#. a. Que calcule l’opération :math:`a\%b` dans la dernière ligne de la fonction ?
   b. Quelle est la valeur de :math:`12\%7` ?
   c. Que se passe-t-il si :math:`a` est strictement inférieur à :math:`b` ?

#. Quelle est la signification des instructions aux lignes 2 et 3 de la fonction ?
#. Donner les différentes phases d’exécution de l’appel ``pgcd(28,42)``.

.. _exercice-5:

Exercice 6
----------

#. Calculer :

   a. :math:`1 \times 2`
   b. :math:`1 \times 2 \times 3`
   c. :math:`1 \times 2 \times 3 \times 4`
   d. :math:`1 \times 2 \times 3 \times 4 \times 5`

#. Les produits précédents sont des **factorielles** que l'on va noter ``factorielle(n)`` où ``n`` est un nombre entier.

   a. Quelle relation peut-on écrire entre ``factorielle(3)`` et ``factorielle(2)`` ?
   b. Quelle relation peut-on écrire entre ``factorielle(4)`` et ``factorielle(3)`` ?
   #. Pour tout nombre entier :math:`n`, écrire une relation entre ``factorielle(n)`` et ``factorielle(n-1)``.

#. Écrire la fonction récursive ``factorielle(n)`` qui prend en paramètre un nombre entier :math:`n` et renvoie la valeur de sa factorielle. On admet que ``factorielle(1)`` renvoie la valeur 1.

.. _exercice-6:

Exercice 
---------

#. Expliquer quel est le résultat renvoyé par le code suivant:

   .. figure:: ../img/ex-mystere.jpg
      :alt: image
      :align: center

#. Écrire une fonction binaire qui prend en paramètres un entier relatif :math:`r` et un entier naturel :math:`n` strictement positif, et qui renvoie la représentation en machine de :math:`r` sur :math:`n` bits.
    La méthode utilisée est celle du complément à :math:`2`.

   Déterminer l’écriture binaire sur :math:`n` bits d’un nombre négatif
   :math:`r` revient à déterminer l’écriture binaire du nombre positif
   :math:`r+2^{n}`.

   Exemple de l’écriture binaire du nombre :math:`-35` sur 7 bits :
   :math:`-35+2^{7}=93=1011101_{2}`.

.. _exercice-8:

Exercice 
---------

#. Dans un idle (pyzo, thonny, python) saisir le programme ci-dessous et
   le tester:

   .. container:: center

      .. image:: ../img/pgm-dessin-spirale.jpg
         :alt: image

#. En donner une version récursive.

.. _exercice-9:

Exercice 
---------

La fonction **fibonacci(n)**, qui doit son nom au mathématicien Leonardo
Fibonacci, est définie récursivement, pout tout entier :math:`n`, de la
manière suivante:

.. math::

   \begin{aligned}
   \text{fibonnacci}(n)=\left\lbrace \begin{array}{ll}
   0 & \text{si~} n=0,\\
   1 & \text{si~} n=1,\\
   \text{fibonnacci}(n-2) + \text{fibonnacci}(n-1) & \text{si~} n>1.\\
   \end{array}
   \right.
   \end{aligned}

#. Calculer fibonacci(5).

#. Écrire en python cette fonction fibonacci.

