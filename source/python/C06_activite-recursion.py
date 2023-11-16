# coding: utf-8
#
# Chapitre 6 - Activité 1 - Les tours de Hanoi (page 116)
#

def hanoi(n, p_source, p_arrivee, p_auxiliaire):
    """
    Affiche la solution de Hanoi lorsque
    - on veut déplacer n disques
    - ces disques sont sur la pile p_source
    - on veut les amener sur la pile p_arrivee
    - on peut utiliser la pile p_auxiliaire
    --------------
    On représente les mouvements par des paires (pile d'origine, pile de destination)
    """
    if n > 0:
        # On déplace les n-1 plus petits disques:
        hanoi(n - 1, p_source, p_auxiliaire, p_arrivee)
        # On déplace le disque n sur la pile d'arrivée:
        print((p_source, p_arrivee))
        # A compléter


# Test:
print(hanoi(2, "x", "y", "z"))
# doit afficher dans l'ordre :
# ('x', 'z')
# ('x', 'y')
# ('z', 'y')


def hanoi_liste(n, p_source, p_arrivee, p_auxiliaire):
    """
    Renvoie sous forme de liste la solution de Hanoi lorsque
    - on veut déplacer n disques
    - ces disques sont sur la pile p_source
    - on veut les amener sur la pile p_arrivee
    - on peut utiliser la pile p_auxiliaire
    --------------
    On représente les mouvements par des paires (pile d'origine, pile de destination)
    """
    if n > 0:
        pass  # A compléter
    else:
        return []


# Test:
print(hanoi_liste(2, "x", "y", "z") == [("x", "z"), ("x", "y"), ("z", "y")])
print(
    hanoi_liste(4, 0, 2, 1)
    == [
        (0, 1),
        (0, 2),
        (1, 2),
        (0, 1),
        (2, 0),
        (2, 1),
        (0, 1),
        (0, 2),
        (1, 2),
        (1, 0),
        (2, 0),
        (1, 2),
        (0, 1),
        (0, 2),
        (1, 2),
    ]
)
