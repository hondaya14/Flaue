import sys
from lib.utils import read_data
from lib.reciprocal import calc_reciprocal_lattice_vector
from lib.plot import *


def main(intensity_file_path):
    intensities = read_data(intensity_file_path)
    reciprocal_lattice_vector = calc_reciprocal_lattice_vector()

    # plot_all(intensities, reciprocal_lattice_vector)
    # f_calc_plot(intensities, reciprocal_lattice_vector)
    # plot_laue_function(reciprocal_lattice_vector)


if __name__ == "__main__":
    main(sys.argv[1])
