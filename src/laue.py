import sys

import matplotlib.pyplot as plt
import numpy as np

from lib.utils import read_data, read_fobs
from lib.reciprocal import calc_reciprocal_lattice_vector
from lib.plot import *
from lib.function import *
from scipy.optimize import leastsq

from src.lib.estimate_result import EstimateResult
from src.lib.r_factor import calculate_r_factor


def main(intensity_file_path):
    fobs_data = read_fobs('/Users/honda/Repositories/lab/Flaue/test_data/Fobs.hkl')
    intensities = read_data(intensity_file_path)
    reciprocal_lattice_vector = calc_reciprocal_lattice_vector()

    estimate_results = []
    d = []
    fest_list = []
    fobs_list = []
    fcalc_list = []

    del_index = []
    # 強度とその周辺値で強度補正
    index = 0
    for intensity in intensities:
        estimate_result = EstimateResult()
        estimate_result.index = index
        estimate_result.fobs = fobs_data[index][4]
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

        estimate_result.err = sum(objective_function(estimate_result.fitting_param[1],
                                                     estimate_result.coord_list, estimate_result.center,
                                                     estimate_result.fcalc_list))

        d.append(estimate_result.intensity.calc_coord(reciprocal_lattice_vector))
        fest_list.append(estimate_result.fest())
        fobs_list.append(estimate_result.fobs)
        fcalc_list.append(estimate_result.intensity.intensity)

        estimate_results.append(estimate_result)
        index += 1

    # show_index = 96
    # estimate_results[show_index].print_result()
    # draw_result(estimate_results[show_index])

    # distance_fcalc_fobs(d, fest_fcalc)

    # diff = 0
    # for i in del_index:
    #     i -= diff
    #     del estimate_results[i]
    #     del fest_fobs[i]
    #     del d[i]
    #     del fobs_data[i]
    #     diff += 1

    r_factor_est, scale_est = calculate_r_factor(estimate_results, fobs_data, True)
    r_factor_calc, scale_calc = calculate_r_factor(estimate_results, fobs_data, False)
    print(f'R factor(est) = {r_factor_est}')
    print(f'scale : {scale_est}')
    print(f'R factor(calc) = {r_factor_calc}')
    print(f'scale : {scale_calc}')

    fest, fobs, fcalc = np.array(fest_list), np.array(fobs_list), np.array(fcalc_list)

    # draw_distance_fcalc_fobs(d, (fcalc - fobs).tolist(), 'Fcalc - Fobs')
    # draw_scatter_compare(d, (fcalc - fobs).tolist(), (fest - fobs).tolist(), 'reciprocal space distance', 'Fcalc-Fobs & Fest-Fobs')
    fobs_sum = sum(fobs)
    fest *= scale_est
    fcalc *= scale_calc
    # draw_scatter_compare(d, fobs, fest, 'reciprocal space distance', 'Fobs(h, k, l) & Fest(h, k, l)')
    # draw_scatter_compare3(d, fcalc, fest, fobs, 'reciprocal space distance', 'Fcalc(h, k, l) & Fest(h, k, l) & Fobs')
    r_est = (np.abs(fobs-fest)/fobs).tolist()
    r_calc = (np.abs(fobs-fcalc)/fobs).tolist()
    print(np.abs(fobs-fest) < fobs)
    print(fobs)
    draw_scatter_compare(d, r_calc, r_est, 'reciprocal space distance', 'Rcalc(h, k, l) & Rest(h, k, l)')
    # draw_scatter(d, r_calc, 'reciprocal space distance', 'Rcalc ( h, k, l)')
    # draw_distance_fcalc_fobs(d, (np.abs(fobs-fcalc)/fobs-np.abs(fobs-fest)/fobs).tolist(), '')
    # draw_distance_fcalc_fobs(d, (np.abs(fobs - fcalc) / fobs - np.abs(fobs - fest) / fobs).tolist(), '')


    good_num = (np.abs(fobs - fcalc) / fobs - np.abs(fobs - fest) / fobs) > 0
    d_r = (np.abs(fobs - fest) / fobs_sum) - (np.abs(fobs - fcalc) / fobs_sum)
    bad_num = (np.abs(fobs - fcalc) / fobs - np.abs(fobs - fest) / fobs) < 0
    print(f'{sum(good_num)}/509')
    print(f'{sum(bad_num)}/509')

    d_left = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3]
    d_num = [0, 0, 0, 0, 0, 0, 0]
    height = [0, 0, 0, 0, 0, 0, 0]
    for di, gi in zip(d, good_num):
        if 0 <= di < 0.2:
            d_num[0] += 1
            height[0] += gi
        elif 0.2 <= di < 0.4:
            d_num[1] += 1
            height[1] += gi
        elif 0.4 <= di < 0.6:
            d_num[2] += 1
            height[2] += gi
        elif 0.6 <= di < 0.8:
            d_num[3] += 1
            height[3] += gi
        elif 0.8 <= di < 1.0:
            d_num[4] += 1
            height[4] += gi
        elif 1.0 <= di < 1.2:
            d_num[5] += 1
            height[5] += gi
        elif 1.2 <= di:
            d_num[6] += 1
            height[6] += gi

    height = [0, 0, 0, 0, 0, 0, 0]
    for di, dr in zip(d, d_r):
        if 0 <= di < 0.2:
            height[0] += dr
        elif 0.2 <= di < 0.4:
            height[1] += dr
        elif 0.4 <= di < 0.6:
            height[2] += dr
        elif 0.6 <= di < 0.8:
            height[3] += dr
        elif 0.8 <= di < 1.0:
            height[4] += dr
        elif 1.0 <= di < 1.2:
            height[5] += dr
        elif 1.2 <= di:
            height[6] += dr

    print(d_num)
    print(height)
    print(sum(height))
    # plt.bar(d_left, height, width=0.2, color="#FF5B70", edgecolor="#CC4959")
    # plt.show()

    # percentages = []
    # for i in range(7):
    #     percentages.append(height[i]/d_num[i]*100)
    #
    # plt.bar(d_left, percentages, width=0.2, color="#FF5B70", edgecolor="#CC4959")
    # plt.show()

    # draw_distance_fcalc_fobs(d, good_num, 'Fcalc - Fobs')
    # draw_distance_fcalc_fobs(d, (fcalc-fest).tolist())


if __name__ == "__main__":
    main(sys.argv[1])
