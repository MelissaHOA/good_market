import copy
import dataclasses
import typing

from produit import *
from commun import *


@dataclasses.dataclass
class Produit_Piece(Produit):
    stock: int
    """ Stock disponible en nombre de pièces"""

    def prix(self) -> Euro:
        return self.prix_quantite(self.stock)

    def prix_quantite(self, qte: int | float) -> Euro:
        if not isinstance(qte,int):
            raise ValueError("La quantité saisi doit être un nombre entier")
        return Euro(self.prix_unite.centimes() * int(qte))

    def prendre_quantite(self, qte: int | float) -> QuantiteRes | typing.Self:
        if not isinstance(qte,int):
            raise ValueError("La quantité saisi doit être un nombre entier")
        if qte > self.stock:
            return QuantiteRes.PAS_ASSEZ
        self.stock -= int(qte)
        produit = copy.copy(self)
        produit.stock = int(qte)
        return produit

    def demander_quantite(self) -> int:
        qte_saisi = input(f"Saisir la quantité de {self.nom} : ").strip()
        return int(qte_saisi)
