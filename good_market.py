#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Le programme a pour but de permettre aux clients de faire leurs achats
# en choisissant les fruits et légumes souhaités et leur quantité.
from typing import List

from produit import Produit

produits : List[Produit] = []

print(produits)

pr = input("Nom du produit")

matchs = []

for pr in produits:
    pass