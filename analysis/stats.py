"""
Fonctions statistiques from scratch.
Reference : Joel Grus, "Data Science From Scratch", chapitre 5.

IMPORTANT : N'importez pas numpy, pandas ou statistics pour ces fonctions.
Implementez-les avec du Python pur (listes, boucles, math).
"""

import math


def mean(xs: list[float]) -> float:
    return sum(xs) / len(xs)


def median(xs: list[float]) -> float:
    sorted_xs = sorted(xs)
    n = len(sorted_xs)
    mid = n // 2
    if n % 2 == 1:
        return sorted_xs[mid]
    return (sorted_xs[mid - 1] + sorted_xs[mid]) / 2


def variance(xs: list[float]) -> float:
    """Retourne la variance d'une liste de nombres."""
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez variance() - voir Grus ch.5")


def standard_deviation(xs: list[float]) -> float:
    """Retourne l'ecart-type d'une liste de nombres."""
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez standard_deviation() - voir Grus ch.5")


def covariance(xs: list[float], ys: list[float]) -> float:
    """Retourne la covariance entre deux series."""
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez covariance() - voir Grus ch.5")


def correlation(xs: list[float], ys: list[float]) -> float:
    """
    Retourne le coefficient de correlation de Pearson entre deux series.
    Retourne 0 si l'une des series a un ecart-type nul.
    """
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez correlation() - voir Grus ch.5")
