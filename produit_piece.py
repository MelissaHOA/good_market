import dataclasses
from produit import *
from commun import *


@dataclasses.dataclass
class Produit_Piece(Produit):
    stock: int
    """ Stock disponible en nombre de pièces"""


    @abstractmethod
    def prix_quantite(self, qte: int) -> Euro:
        if qte is not int:
            raise ValueError("La quantité saisi doit être un nombre entier")
        return Euro(self.prix_unite.centimes() * qte)


    @abstractmethod
    def prendre_quantite(self, qte: int) -> QuantiteRes:
        if qte is not int:
            raise ValueError("La quantité saisi doit être un nombre entier")
        if qte > self.stock:
            return QuantiteRes.PAS_ASSEZ
        self.stock -= qte
        return QuantiteRes.OK


    @abstractmethod
    def demander_quantite(self) -> int:
        qte_saisi = input(f"Saisir la quantité de {self.nom} : ").strip()
        return int(qte_saisi)





