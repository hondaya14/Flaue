import numpy as np
from src.config.constants import Crystal, UnitCell


def gaussian_1dim(fp, x, center):
    return fp[0] * np.exp(-(np.power(x-center[0], 2)) / fp[1])


def gaussian_2dim(fp, x, y, center):
    return fp[0] * np.exp(-(np.power(x-center[0], 2) +
                            np.power(y-center[1], 2)) / fp[1])


def gaussian(fp, coord_list, center):
    results = []
    for coord in coord_list:
        result = fp[0] * np.exp(-(np.power(coord[0]-center[0], 2) +
                                  np.power(coord[1]-center[1], 2) +
                                  np.power(coord[2]-center[2], 2)) / fp[1])
        results.append(result)
    return np.array(results)


def objective_function(fitting_params, coord, center, fcalc):
    err = fcalc - gaussian(fitting_params, coord, center)
    return err


#
# sin^2(π Na K a) ・sin^2(π Nb K b) ・sin^2(π Nc K b)
#  sin^2(π K a)      sin^2(π K b)      sin^2(π K b)
#
# x, y, z = K・a, K・b, K・c
#
# sin^2(π Na x) ・sin^2(π Nb y) ・sin^2(π Nc z)
#  sin^2(π x)      sin^2(π y)      sin^2(π z)
#
# lim x->0: Na, lim y->0: Nb, lim z->0: Nc
# lim x,y->0: NaNb, lim y,z->0: NbNc, lim z,x->0: NcNa
# lim x,y,z->0: NaNbNc
#
# def laue(scat_vec, a, b, c):
#     x = np.dot(np.array(scat_vec), np.array(UnitCell.lv_a.value))  # K・a
#     y = np.dot(np.array(scat_vec), np.array(UnitCell.lv_b.value))  # K・b
#     z = np.dot(np.array(scat_vec), np.array(UnitCell.lv_c.value))  # K・c
#
#     result = []
#     len_x = len(x)
#     for i in range(len_x):
#         x[i] = round(x[i], 5)
#         y[i] = round(y[i], 5)
#         y[i] = round(z[i], 5)
#         peak_x_flag = x[i] % 1 == 0
#         peak_y_flag = y[i] % 1 == 0
#         peak_z_flag = z[i] % 1 == 0
#         if peak_x_flag and peak_y_flag and peak_z_flag:
#             result.append(np.power(Crystal.Na.value * a * Crystal.Nb.value * b * Crystal.Nc.value * c, 2))
#         elif peak_x_flag and peak_y_flag:
#             result.append(np.power(Crystal.Na.value * a * Crystal.Nb.value * b, 2))
#         elif peak_y_flag and peak_z_flag:
#             result.append(np.power(Crystal.Nb.value * b * Crystal.Nc.value * c, 2))
#         elif peak_z_flag and peak_x_flag:
#             result.append(np.power(Crystal.Nc.value * c * Crystal.Na.value * a, 2))
#         elif peak_x_flag:
#             result.append(np.power(Crystal.Na.value * a, 2))
#         elif peak_y_flag:
#             result.append(np.power(Crystal.Nb.value * b, 2))
#         elif peak_z_flag:
#             result.append(np.power(Crystal.Nc.value * c, 2))
#         else:
#             result.append(
#                 np.square(np.sin(np.pi * Crystal.Na.value * a * x[i])) / np.square(np.sin(np.pi * x[i])) * \
#                 np.square(np.sin(np.pi * Crystal.Nb.value * b * y[i])) / np.square(np.sin(np.pi * y[i])) * \
#                 np.square(np.sin(np.pi * Crystal.Nc.value * c * z[i])) / np.square(np.sin(np.pi * z[i]))
#             )
#
#     return np.array(result)
#
#
# def gauss(d, e, x):
#     return d * np.exp(-np.power(x, 2) / e)
#
#
# def f_fit(scat_vec, d, e):
#     result = []
#     for sv in scat_vec:
#         r = np.sqrt(sv[0] * sv[0] + sv[1] * sv[1] + sv[2] * sv[2])
#         result.append(gauss(d, e, r))
#     return np.array(result)
#
#
# # 目的関数
# def objective_function(fitting_param, scat_vec, fcalc):
#     a, b, c, d, e = fitting_param
#     err = fcalc - f_fit(scat_vec, d, e) * laue(scat_vec, a, b, c)
#     print(sum(err))
#     return err
#
#
# def laue_1dim(x):
#     # x = np.dot(np.array(scat_vec), np.array(UnitCell.lv_a.value))  # K・a
#     result = []
#     for xe in x:
#         if xe % 1 == 0:
#             result.append(np.power(Crystal.Na.value, 2))
#         else:
#             result.append(np.square(np.sin(np.pi * Crystal.Na.value * xe)) / np.square(np.sin(np.pi * xe)))
#     return result
