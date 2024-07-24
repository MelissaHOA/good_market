import copy
import typing

from commun import *
from produit import *


@dataclasses.dataclass
class ProduitKg(Produit):
    poids_g: int

    def prix(self) -> Euro:
        return self.prix_quantite(self.poids_g)

    def prix_quantite(self, qte: int | float) -> Euro:
        return Euro.new_float((self.prix_unite.centimes() * (qte / 1000.0)) / 100.0)

    def prendre_quantite(self, qte: int | float) -> QuantiteRes | typing.Self:
        g = int(qte)
        if g > self.poids_g:
            return QuantiteRes.PAS_ASSEZ
        self.poids_g -= g
        prd = copy.copy(self)
        prd.poids_g = int(qte)
        return prd

    def demander_quantite(self) -> float | int:
        w = 0
        stop = False
        while not stop:
            data = input(f"Quantité de {self.nom} (kg ou g) :")
            data = data.replace(" ", "")
            data = data.lower()
            stop = True
            print(data)
            try:
                if data.endswith("kg"):
                    print(data)
                    data = data[0:len(data) - 2]
                    w = int(float(data) * 1000)
                elif data.endswith("g"):
                    data = data[0:len(data) - 1]
                    w = int(float(data))
                else:
                    data = data[0:len(data) - 1]
                    w = int(float(data))
            except ValueError:
                stop = False
        return w


#q = ProduitKg("X", Euro.new(5), TypeProduit.AUCUN, 19.5)
#qte = q.demander_quantite()
#print(q.prendre_quantite(qte))
#print(q.prix_quantite(qte))
