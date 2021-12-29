import numpy as np
from src.config.constants import Crystal, UnitCell


def laue(scat_vec):
    #
    # sin^2(π Na K a) ・sin^2(π Nb K b) ・sin^2(π Nc K b)
    #  sin^2(π K a)      sin^2(π K b)      sin^2(π K b)
    #
    # x, y, z = K・a, K・b, K・c

    x = UnitCell.lv_a
    y = UnitCell.lv_b
    z = UnitCell.lv_c
    return np.square(np.sin(np.pi * Crystal.Na * x)) / np.square(np.sin(np.pi * x)) * \
           np.square(np.sin(np.pi * Crystal.Nb * y)) / np.square(np.sin(np.pi * y)) * \
           np.square(np.sin(np.pi * Crystal.Nc * z)) / np.square(np.sin(np.pi * z))

    # return np.square(np.sin(np.pi * na * x)) / np.square(np.sin(np.pi * x)) * \
    #        np.square(np.sin(np.pi * nb * y)) / np.square(np.sin(np.pi * y)) * \
    #        np.square(np.sin(np.pi * nc * z)) / np.square(np.sin(np.pi * z))
