import matplotlib.pyplot as plt
from function import gaussian, gaussian_1dim, gaussian_2dim
import numpy as np


# estimate resultの描画
def draw_result(estimate_result):
    window_title = f'Result[{estimate_result.index}] (h, k, l)=' \
                   f'({estimate_result.intensity.h},{estimate_result.intensity.k},{estimate_result.intensity.l})'
    fig = plt.figure(num=window_title, figsize=(10, 10))
    ax = fig.add_subplot(projection="3d")

    xi, yi = 0, 1  # X, Y, Z = 0, 1, 2
    label = ['x', 'y', 'z']

    # 軸ラベルを設定
    ax.set_xlabel(label[xi], size=16)
    ax.set_ylabel(label[yi], size=16)
    ax.set_zlabel('Fcalc', size=16)

    cx = [c[xi] for c in estimate_result.coord_list]
    cy = [c[yi] for c in estimate_result.coord_list]

    cx_min, cx_max = min(cx), max(cx)
    cy_min, cy_max = min(cy), max(cy)

    rest_x_range = abs(cx_max * 1.4 - cx_max)
    range_cx_r = int(1000 * (cx_max + rest_x_range) // 1)
    range_cx_l = int(1000 * (cx_min - rest_x_range) // 1)

    rest_y_range = abs(cy_max * 1.4 - cy_max)
    range_cy_r = int(1000 * (cy_max + rest_y_range) // 1)
    range_cy_l = int(1000 * (cy_min - rest_y_range) // 1)

    x = np.array([i / 1000 for i in range(range_cx_l, range_cx_r)])
    y = np.array([i / 1000 for i in range(range_cy_l, range_cy_r)])

    # 格子点を作成
    X, Y = np.meshgrid(x, y)

    # 高度の計算式
    Z = gaussian_2dim(estimate_result.fitting_param[1], X, Y, estimate_result.center, xi, yi)

    # 曲面を描画
    ax.plot_surface(X, Y, Z, color=(0.6, 0.6, 0.6, 0.8))

    ax.scatter(cx, cy, estimate_result.fcalc_list, color='red')

    plt.show()


def draw_distance_fcalc_fobs(d, fcalc_fobs, ylabel):
    fig, ax = plt.subplots()
    ax.set_xlabel("reciprocal space distance")
    ax.set_ylabel(ylabel)
    plt.scatter(d, fcalc_fobs)
    plt.axhline(y=0, color='red')
    plt.show()


def draw_scatter(a, b, label_a, label_b):
    fig, ax = plt.subplots()
    ax.set_xlabel(label_a)
    ax.set_ylabel(label_b)
    plt.ylim(0, 2.5)
    plt.scatter(a, b)
    # plt.axhline(y=0, color='red')
    plt.show()


def draw_scatter_compare(a, b, c, label_a, label_b):
    fig, ax = plt.subplots()
    ax.set_xlabel(label_a)
    ax.set_ylabel(label_b)
    # plt.ylim(0, 2.5)
    plt.scatter(a, b, color=(0.2, 0.2, 1.0, 0.75))
    plt.scatter(a, c, color=(1.0, 0.2, 0.2, 0.75))
    plt.show()


def draw_scatter_compare3(a, b, c, d, label_a, label_b):
    fig, ax = plt.subplots()
    ax.set_xlabel(label_a)
    ax.set_ylabel(label_b)
    # plt.ylim(0, 2.5)
    plt.scatter(a, b, color=(0.2, 0.2, 1.0, 0.75))
    plt.scatter(a, c, color=(1.0, 0.2, 0.2, 0.75))
    plt.scatter(a, d, color=(0.2, 1.0, 0.2, 0.75))
    plt.show()

# def plot_all(intensities, reciprocal_lattice_vector):
#     x, y, z, value = [], [], [], []
#     for intensity in intensities:
#         h, k, l, intensity_value = intensity.h, intensity.k, intensity.l, intensity.intensity
#         reciprocal_coord = h * reciprocal_lattice_vector[0] + \
#                            k * reciprocal_lattice_vector[1] + \
#                            l * reciprocal_lattice_vector[2]
#
#         x.append(reciprocal_coord[0])
#         y.append(reciprocal_coord[1])
#         z.append(reciprocal_coord[2])
#         value.append(intensity_value)
#
#         for bc in intensity.back_contents_list:
#             x.append(bc.x)
#             y.append(bc.y)
#             z.append(bc.z)
#             value.append(bc.value)
#
#     fig = plt.figure()
#     ax = fig.add_subplot(projection='3d')
#
#     ax.set_title('Fcalc')
#
#     # print(f'x min:{min(x)}, max:{max(x)}')
#     # print(f'y min:{min(y)}, max:{max(y)}')
#     # print(f'z min:{min(z)}, max:{max(z)}')
#
#     ax.set_xlabel("a", size=15, color="black")
#     ax.set_ylabel("b", size=15, color="black")
#     ax.set_zlabel("z", size=15, color="black")
#
#     ax.scatter(x, z, value, c=value, cmap="gray")
#     plt.show()
#
#
# def f_calc_plot(intensities, reciprocal_lattice_vector):
#     x = []
#     y = []
#     z = []
#     value = []
#     for intensity in intensities:
#         h, k, l, intensity_value = intensity.h, intensity.k, intensity.l, intensity.intensity
#         reciprocal_coord = h * reciprocal_lattice_vector[0] + \
#                            k * reciprocal_lattice_vector[1] + \
#                            l * reciprocal_lattice_vector[2]
#         x.append(reciprocal_coord[0])
#         y.append(reciprocal_coord[1])
#         z.append(reciprocal_coord[2])
#         value.append(intensity_value)
#
#     fig = plt.figure()
#     # plt.rcParams['axes.facecolor'] = 'black'
#
#     ax = fig.add_subplot(projection='3d')
#     # ax.tick_params(labelbottom=False,
#     #                labelleft=False,
#     #                labelright=False,
#     #                labeltop=False)
#     # ax.tick_params(bottom=False,
#     #                left=False,
#     #                right=False,
#     #                top=False)
#     # ax.axis("off")
#
#     ax.set_title('Fcalc')
#
#     print(f'x min:{min(x)}, max:{max(x)}')
#     print(f'y min:{min(y)}, max:{max(y)}')
#     print(f'z min:{min(z)}, max:{max(z)}')
#     print(f'max: {max(value)}')
#
#     ax.set_xlabel("a", size=15, color="black")
#     ax.set_ylabel("b", size=15, color="black")
#     ax.set_zlabel("z", size=15, color="black")
#
#     ax.scatter(x, y, z, c=value, cmap="gray")
#     plt.show()
#
#
# def draw_laue_r(scat_vec, fcalc, params):
#     a, b, c, d, e = params[0]
#     fig, ax = plt.subplots()
#     # x 軸のラベルを設定する。
#     ax.set_xlabel("r")
#
#     # y 軸のラベルを設定する。
#     ax.set_ylabel("fcalc")
#     x = []
#     for sv in scat_vec:
#         x.append(np.sqrt(sv[0] * sv[0] + sv[1] * sv[1] + sv[2] * sv[2]))
#     y = fcalc
#     # y = np.array(f_fit(scat_vec, d, e) * laue(scat_vec, a, b, c))
#
#     print(len(x), len(y))
#     plt.scatter(x, y)
#     plt.show()
#
#
# def draw_fcalc(scat_vec, fcalc):
#     x = []
#     for sv in scat_vec:
#         x.append(sv[0])
#     y = fcalc
#     plt.scatter(x, y)
#
#     plt.show()
#
#
# def draw_gauss(d, e):
#     x = np.array([i/100 for i in range(-150, 151)])
#     result = gaussian(x, d, e)
#     plt.plot(x, result)
#     plt.show()
#
#
# def draw_gaussian_1dim(result, coord_list, fcalc_list, center):
#     x = np.array([i / 100 for i in range(-150, 151)])
#     y = gaussian_1dim(result[0], x, center)
#
#     coord_x_list = [c[0] for c in coord_list]
#     plt.plot(x, y)
#     plt.scatter(coord_x_list, fcalc_list)
#     plt.show()
