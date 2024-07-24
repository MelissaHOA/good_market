#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Le programme a pour but de permettre aux clients de faire leurs achats
# en choisissant les fruits et légumes souhaités et leur quantité.
from typing import List

from commun import *
from produit import Produit

produits : List[Produit] = []


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
        if ret == QuantiteRes.OK:
            panier.append(x)
        else:
            print(ret)
            continue;