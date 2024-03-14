# -*- coding: utf-8 -*-
"""
Bibliothèque permettant la trauction d'un message d'une base 10 à base 20.

Voici le dictionnaire de la base 20 utilisé : "0123456789§µ£?%&éçà|".
Par exemple, 11 (base10) -> µ (base20); 20 (base10) -> | (base20);
15 (base10) -> & (base20)
"""


def traduction(message):
    """
    Convertit les éléments d'une liste d'une base à l'autre.

    La conversion de chaque élément se fait d'un entier 
    de base 10 vers un entier de base 20, selon le dictionnaire de la
    base 20 fournie en documentation
    
    Parameters
    ----------
    message : list
        contient des entiers en base 10.

    Returns
    -------
    res : list
        contient les entiers traduit en base 20 sous forme
        de chaine de caractère.

    >>> traduction([4, 0, 16])
    ['4', '0', 'g']
    >>> traduction([5, 1, 4])
    ['5', '1', '4']
    >>> traduction([11, 16])
    ['b', 'g']
    """
    base20='0123456789abcdefghij'
    res = []
    for i in message:
        res.append(base20[i])
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()   
    