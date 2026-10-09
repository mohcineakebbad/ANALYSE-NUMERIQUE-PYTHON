# Algèbre linéaire — Matrices et systèmes linéaires

## Description

Ce projet consiste à utiliser Python et la bibliothèque NumPy pour manipuler des matrices, étudier leur inversibilité et résoudre des systèmes d'équations linéaires.

## Objectifs

- Créer et manipuler des matrices avec NumPy.
- Calculer les dimensions et la transposée d'une matrice.
- Accéder aux lignes, colonnes et coefficients d'une matrice.
- Effectuer des opérations matricielles.
- Calculer le déterminant d'une matrice.
- Vérifier si une matrice est inversible.
- Calculer l'inverse d'une matrice.
- Résoudre un système linéaire \(AX=b\).
- Vérifier la solution obtenue.
- Calculer le résidu et sa norme.
- Étudier le cas d'une matrice singulière.
- Créer une fonction réutilisable pour analyser un système linéaire.

## Technologies utilisées

- Python
- NumPy

## Contenu du projet

### A — Prise en main des matrices

Manipulation d'une matrice `A` et d'un vecteur `b` :

- dimensions
- transposée
- lignes et colonnes
- coefficients
- addition de matrices
- multiplication par un scalaire
- produit matriciel

### B — Déterminant et inversibilité

Calcul du déterminant de `A` et vérification de son inversibilité.

Lorsque la matrice est inversible, son inverse est calculé avec :

```python
np.linalg.inv(A)
