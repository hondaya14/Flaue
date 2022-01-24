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
        pass

    fitting_param = np.array([10.0, 0.0001])
    intensity = intensities[0]

    center = calculation_center(intensity, reciprocal_lattice_vector)
    fcalc, coord = pickup_back(intensity)
    print(f'center ... {center}')
    fcalc.append(intensity.intensity)
    coord.append(center)

    fcalc, coord = np.array(fcalc), np.array(coord)
    # print(len(fcalc), len(coord), len(center))
    result = leastsq(objective_function, fitting_param, args=(coord, center, fcalc))
    print(f'result ... {result}')

    after_calc = gaussian(result[0], coord, center)

    for i in range(7):
        print(f'{fcalc[i]} {after_calc[i]}')

    draw_gaussian_2dim(result, coord, fcalc, center)


if __name__ == "__main__":
    main(sys.argv[1])
