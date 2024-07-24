import dataclasses
import math
from enum import Enum

from typing import NewType


@dataclasses.dataclass
class Euro:
    __centimes: int

    def centimes(self) -> int:
        return self.__centimes

    @classmethod
    def new(cls, euros: int, centimes: int = 0) -> 'Euro':
        assert centimes < 100
        return Euro(euros * 100 + centimes)

    def __repr__(self):
        return str(float(self.__centimes) / 100.0)

    def __add__(self, other: 'Euro') -> 'Euro':
        return Euro(self.__centimes + other.__centimes)


class QuantiteRes(Enum):
    """Résultat d'une requête"""
    OK = 1
    INVALIDE = 2
    """Type invalide (float au lieu de int) """
    PAS_ASSEZ = 3
    """Pas assez de stock"""
    VIDE = 4


class TypeProduit(str, Enum):
    AUCUN = ""
    FRUIT = "Fruit"
    LEGUME = "Légume"


