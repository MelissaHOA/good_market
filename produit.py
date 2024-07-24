import dataclasses
import typing
from abc import *

from commun import *


@dataclasses.dataclass
class Produit:
    nom: str
    prix_unite: Euro
    """Prix par unité de produit (kg, pièce, ...)"""
    type_produit: TypeProduit
    """Type du produit (par exemple Légume)"""

    @abstractmethod
    def prix_quantite(self, qte: int | float) -> Euro:
        """
        Renvoie le prix pour une quantitée
        :param qte:  Quantitée
        :return: Prix en euros
        """
        ...
    @abstractmethod
    def prendre_quantite(self, qte: int | float) -> QuantiteRes | typing.Self:
        """
        Prend la quantité de produit à acheter

        :param qte: Quantitée à prendre soit en entier ou flottant (retourne INVALIDE si le produit n'accepte pas les flottants)
        :return: True si la quantité est valide
        """
        ...


    @abstractmethod
    def demander_quantite(self) -> float | int:
        """
        Demande la quantité au client (input)
        :return: la quantité entrée
        """
        ...
