import sys
from lib.utils import read_data
from lib.reciprocal import calc_reciprocal_lattice_vector
from lib.plot import *
from lib.function import *
from scipy.optimize import leastsq


def main(intensity_file_path):
    intensities = read_data(intensity_file_path)
    reciprocal_lattice_vector = calc_reciprocal_lattice_vector()

    # 強度とその周辺値で強度補正
    for intensity in intensities:
        center = intensity.calculation_center(reciprocal_lattice_vector)
        fcalc, coord = intensity.pickup_back()
        print(f'center ... {center}')
        fcalc.append(intensity.intensity)
        coord.append(intensity.intensity_coord)

        fcalc, coord = np.array(fcalc), np.array(coord)
        # print(len(fcalc), len(coord), len(center))

        fitting_param = np.array([max(fcalc), 0.0001])
        print(f'fit prm(init) ... {fitting_param}')
        result = leastsq(objective_function, fitting_param, args=(coord, center, fcalc))
        print(f'fit prm(fin) ... {result[0]}')

        after_calc = gaussian(result[0], coord, center)

        print(f'Fcalc\t\tFcalc(fitting)')
        for i in range(7):
            print(f'{str(fcalc[i]).rjust(8)}\t{round(after_calc[i], 6)}')
        print(f'--------------------------------------------------------')

    # draw_gaussian_2dim(result, coord, fcalc, center)


if __name__ == "__main__":
    main(sys.argv[1])
