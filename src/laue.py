import sys
from lib.utils import read_data, read_fobs
from lib.reciprocal import calc_reciprocal_lattice_vector
from lib.plot import *
from lib.function import *
from scipy.optimize import leastsq

from src.lib.estimate_result import EstimateResult
from src.lib.r_factor import calculate_r_factor


def main(intensity_file_path):
    intensities = read_data(intensity_file_path)
    reciprocal_lattice_vector = calc_reciprocal_lattice_vector()

    estimate_results = []
    # 強度とその周辺値で強度補正
    index = 0
    for intensity in intensities:
        estimate_result = EstimateResult()
        estimate_result.index = index
        estimate_result.intensity = intensity
        center = intensity.calculation_center(reciprocal_lattice_vector)
        estimate_result.center = center

        fcalc, coord = intensity.pickup_back()

        estimate_result.fcalc_list = fcalc
        estimate_result.coord_list = coord

        fitting_param = np.array([max(fcalc), 0.0001])
        result = leastsq(objective_function, fitting_param, args=(coord, center, fcalc))

        estimate_result.fitting_param = [fitting_param, result[0]]

        estimate_result.fcalc_fit_list = gaussian(result[0], coord, center)

        estimate_results.append(estimate_result)
        index += 1

    # show_index = 4
    # estimate_results[show_index].print_result()
    # draw_result(estimate_results[show_index])

    fobs_data = read_fobs('/Users/honda/Repositories/lab/Flaue/test_data/Fobs.hkl')
    r_factor = calculate_r_factor(estimate_results, fobs_data)
    print(r_factor)


if __name__ == "__main__":
    main(sys.argv[1])
