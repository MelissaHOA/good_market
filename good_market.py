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

from liste_produits import produits



historique = []

while True:

    nom = input("Nom : ")
    prenom = input("Prénom : ")

    if nom == "":
        break

    panier: List[Produit] = []

    while True:
        print("Produits :")

        for i in produits:
            print("",i)

        print("Panier : ", panier)

        pr = input("Nom du produit :").strip().lower()

        matchs = []


        # Trouver produit
        for x in produits:
            if (x.nom.lower()).startswith(pr):
                matchs.append(x)

        if len(matchs) == 1 and pr != "":
            x = matchs[0]
            qte = x.demander_quantite();
            ret = x.prendre_quantite(qte)
            if not isinstance(ret, QuantiteRes):
                print("Prix : ", x.prix_quantite(qte))
                panier.append(ret)
            else:
                print("Error", ret)
                continue

        if input("Continuer ? : ").lower().strip().startswith("n"):
            break

    print(nom,prenom)

    print("Panier :", panier)

    sm = Euro.new(0)

    for x in panier:
        sm += x.prix()

    print("Total :", sm)

    historique.append((nom,prenom,panier,sm))




print("Clients",historique)