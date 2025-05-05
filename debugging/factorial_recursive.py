#!/usr/bin/python3
import sys

def factorial(n):

    """
    Calcule la factorielle d'un entier en utilisant la récursion.

    Paramètres :
    n (int) : un entier non négatif pour lequel on souhaite calculer la factorielle.

    Retours :
    int : la factorielle de n (n!), c'est-à-dire le produit de tous les entiers de 1 à n.
    """
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)