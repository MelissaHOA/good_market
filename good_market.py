#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Le programme a pour but de permettre aux clients de faire leurs achats
# en choisissant les fruits et légumes souhaités et leur quantité.
from typing import List

from commun import *
from produit import Produit


from produit_kg import *

from produit_piece import *

produits : List[Produit] = [
    ProduitKg("Carrotte",Euro.new(5),TypeProduit.LEGUME),
    ProduitKg("Pomme", Euro.new(9), TypeProduit.FRUIT)

]


panier : List[Produit] = []



while True:
    print(produits)

    print("Panier : ",*panier)

    pr = input("Nom du produit").strip()

    pr = pr + "."

    matchs = []

    if input("Continuer ? : ").lower().strip().startswith("n"):
        break

    for x in produits:
        if (x.nom.lower()+".").startswith(pr):
            matchs.append(x)

    if len(matchs) == 1:
        x = matchs[0]
        qte = x.demander_quantite();
        ret = x.prendre_quantite(qte)
        if ret is Produit:
            panier.append(ret)
        else:
            print(ret)
            continue;