from commun import *
from produit import *
from produit_piece import *
from produit_kg import *

produits: [Produit] = [
    ProduitKg("Clementine",Euro.new(2,90),TypeProduit.FRUIT,6000),
    ProduitKg("Datte",Euro.new(7),TypeProduit.FRUIT,3000),
    ProduitKg("Grenade",Euro.new(3,50),TypeProduit.FRUIT,3000),
    ProduitKg("Kaki",Euro.new(4,50),TypeProduit.FRUIT,3000),
    ProduitKg("Kiwi",Euro.new(3,50),TypeProduit.FRUIT,5000),
    ProduitKg("Mandarine",Euro.new(2,80),TypeProduit.FRUIT,6000),
    ProduitKg("Orange",Euro.new(1,50),TypeProduit.FRUIT,8000),
    ProduitKg("Poire",Euro.new(2,50),TypeProduit.FRUIT,5000),
    ProduitKg("Poire",Euro.new(2,50),TypeProduit.FRUIT,5000),
    ProduitKg("Pomme",Euro.new(1,50),TypeProduit.FRUIT,8000),
    ProduitKg("Carotte",Euro.new(1,30),TypeProduit.LEGUME,7000),
    ProduitKg("Choux de Bruxelles",Euro.new(4),TypeProduit.LEGUME,4000),
    ProduitKg("Endive",Euro.new(2,50),TypeProduit.LEGUME,5000),
    ProduitKg("Epinard",Euro.new(2,60),TypeProduit.LEGUME,4000),
    ProduitKg("Poireau",Euro.new(1,20),TypeProduit.LEGUME,5000),
    ProduitKg("Salsifis",Euro.new(2,50),TypeProduit.LEGUME,3000),
    Produit_Piece("Pamplemousse",Euro.new(2),TypeProduit.FRUIT,8),
    Produit_Piece("Chou vert",Euro.new(2,50),TypeProduit.LEGUME,12),
    Produit_Piece("Courge butternut",Euro.new(2,50),TypeProduit.LEGUME,6),
    Produit_Piece("Potiron",Euro.new(2,50),TypeProduit.LEGUME,6),
    Produit_Piece("Radis noir",Euro.new(5),TypeProduit.LEGUME,10)
]