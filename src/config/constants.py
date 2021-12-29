
from enum import Enum


class Crystal(Enum):
    # Crystal Size
    Na = 9
    Nb = 6
    Nc = 5


class UnitCell(Enum):
    # lattice vector
    lv_a = [7.1178, 0, 0]
    lv_b = [0, 9.6265, 0]
    lv_c = [-1.39567, 0, 11.81314]

