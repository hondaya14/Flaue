import numpy as np


# calculation gt
# flag: Fest or Fcalc
def calculate_r_factor(estimate_result, fobs_data, flag):
    hkl_gt_list = []
    # R variable
    sum_f_obs_gt, sum_f_calc_gt, sum_fo_fc_diff_gt = 0, 0, 0
    sum_f_obs_x_f_calc_gt = 0
    sum_f_calc_power_gt = 0

    est_data = []
    for er in estimate_result:
        if flag:
            # fest
            est_data.append([er.intensity.h, er.intensity.k, er.intensity.l, er.fest(),
                             int(f'{er.intensity.h}{er.intensity.k}{er.intensity.l}')])

        else:
            # fcalc
            est_data.append([er.intensity.h, er.intensity.k, er.intensity.l, er.intensity.intensity,
                             int(f'{er.intensity.h}{er.intensity.k}{er.intensity.l}')])
    # est_data.sort(key=lambda x: x[-1])

    for ed, fd in zip(est_data, fobs_data):
        assert ed[0:3] == fd[0:3], f'{ed[0:3]} {fd[0:3]}'
        h, k, l = ed[0:3]
        f_calc_clisalis_value, f_obs_value, f_sigma_squared = fd[3], fd[4], fd[5]
        f_calc_value = ed[3]
        f_obs_value = 0 if f_obs_value < 0 else f_obs_value

        hkl_gt_list.append([h, k, l, f_obs_value, f_calc_value])
        sum_f_obs_gt += abs(f_obs_value)
        sum_f_calc_gt += abs(f_calc_value)
        sum_f_obs_x_f_calc_gt += abs(f_obs_value) * abs(f_calc_value)
        sum_f_calc_power_gt += f_calc_value * f_calc_value

    s_gt = 0.001
    min_r_gt = 1
    s = 0
    for i in range(10001):
        sum_fo_fc_diff_gt = 0
        for hgl in hkl_gt_list:
            h, k, l, fobs, fcalc = hgl[0], hgl[1], hgl[2], hgl[3], hgl[4]
            sum_fo_fc_diff_gt += abs(fobs - s * fcalc)
        r_factor_gt = sum_fo_fc_diff_gt / sum_f_obs_gt
        min_r_gt = min(r_factor_gt, min_r_gt)
        if min_r_gt == r_factor_gt:
            s_gt = s
        s += 0.001
    return round(min_r_gt, 4), s_gt
