import matplotlib.pyplot as plt
from function import gaussian, gaussian_1dim, gaussian_2dim
import numpy as np


def plot_all(intensities, reciprocal_lattice_vector):
    x, y, z, value = [], [], [], []
    for intensity in intensities:
        h, k, l, intensity_value = intensity.h, intensity.k, intensity.l, intensity.intensity
        reciprocal_coord = h * reciprocal_lattice_vector[0] + \
                           k * reciprocal_lattice_vector[1] + \
                           l * reciprocal_lattice_vector[2]

        x.append(reciprocal_coord[0])
        y.append(reciprocal_coord[1])
        z.append(reciprocal_coord[2])
        value.append(intensity_value)

        for bc in intensity.back_contents_list:
            x.append(bc.x)
            y.append(bc.y)
            z.append(bc.z)
            value.append(bc.value)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.set_title('Fcalc')

    # print(f'x min:{min(x)}, max:{max(x)}')
    # print(f'y min:{min(y)}, max:{max(y)}')
    # print(f'z min:{min(z)}, max:{max(z)}')

    ax.set_xlabel("a", size=15, color="black")
    ax.set_ylabel("b", size=15, color="black")
    ax.set_zlabel("z", size=15, color="black")

    ax.scatter(x, z, value, c=value, cmap="gray")
    plt.show()


def f_calc_plot(intensities, reciprocal_lattice_vector):
    x = []
    y = []
    z = []
    value = []
    for intensity in intensities:
        h, k, l, intensity_value = intensity.h, intensity.k, intensity.l, intensity.intensity
        reciprocal_coord = h * reciprocal_lattice_vector[0] + \
                           k * reciprocal_lattice_vector[1] + \
                           l * reciprocal_lattice_vector[2]
        x.append(reciprocal_coord[0])
        y.append(reciprocal_coord[1])
        z.append(reciprocal_coord[2])
        value.append(intensity_value)

    fig = plt.figure()
    # plt.rcParams['axes.facecolor'] = 'black'

    ax = fig.add_subplot(projection='3d')
    # ax.tick_params(labelbottom=False,
    #                labelleft=False,
    #                labelright=False,
    #                labeltop=False)
    # ax.tick_params(bottom=False,
    #                left=False,
    #                right=False,
    #                top=False)
    # ax.axis("off")

    ax.set_title('Fcalc')

    print(f'x min:{min(x)}, max:{max(x)}')
    print(f'y min:{min(y)}, max:{max(y)}')
    print(f'z min:{min(z)}, max:{max(z)}')
    print(f'max: {max(value)}')

    ax.set_xlabel("a", size=15, color="black")
    ax.set_ylabel("b", size=15, color="black")
    ax.set_zlabel("z", size=15, color="black")

    ax.scatter(x, y, z, c=value, cmap="gray")
    plt.show()


def draw_laue(scat_vec, fcalc, params):
    a, b, c, d, e = params[0]
    x = []
    for sv in scat_vec:
        x.append(sv[0])
    y = np.array(f_fit(scat_vec, d, e) * laue(scat_vec, a, b, c))
    # y = np.multiply(fcalc, d)

    print(len(x), len(y))
    plt.scatter(x, y)
    plt.show()


def draw_laue_r(scat_vec, fcalc, params):
    a, b, c, d, e = params[0]
    fig, ax = plt.subplots()
    # x 軸のラベルを設定する。
    ax.set_xlabel("r")

    # y 軸のラベルを設定する。
    ax.set_ylabel("fcalc")
    x = []
    for sv in scat_vec:
        x.append(np.sqrt(sv[0] * sv[0] + sv[1] * sv[1] + sv[2] * sv[2]))
    y = fcalc
    # y = np.array(f_fit(scat_vec, d, e) * laue(scat_vec, a, b, c))

    print(len(x), len(y))
    plt.scatter(x, y)
    plt.show()


def draw_fcalc(scat_vec, fcalc):
    x = []
    for sv in scat_vec:
        x.append(sv[0])
    y = fcalc
    plt.scatter(x, y)

    plt.show()


def draw_gauss(d, e):
    x = np.array([i/100 for i in range(-150, 151)])
    result = gaussian(x, d, e)
    plt.plot(x, result)
    plt.show()


def draw_gaussian_1dim(result, coord_list, fcalc_list, center):
    x = np.array([i / 100 for i in range(-150, 151)])
    y = gaussian_1dim(result[0], x, center)

    coord_x_list = [c[0] for c in coord_list]
    plt.plot(x, y)
    plt.scatter(coord_x_list, fcalc_list)
    plt.show()


def draw_gaussian_2dim(result, coord_list, fcalc_list, center):
    print(coord_list)
    # Figureと3DAxeS
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    # 軸ラベルを設定
    ax.set_xlabel("x", size=16)
    ax.set_ylabel("y", size=16)
    ax.set_zlabel("fcalc", size=16)

    # (x,y)データを作成
    x = np.array([i / 1000 for i in range(-50, 51)])
    y = np.array([i / 1000 for i in range(80, 131)])

    # 格子点を作成
    X, Y = np.meshgrid(x, y)

    # 高度の計算式
    Z = gaussian_2dim(result[0], X, Y, center)

    # 曲面を描画
    ax.plot_surface(X, Y, Z, color=(0.4, 0.4, 0.9, 0.8))

    # 底面に等高線を描画
    # ax.contour(X, Y, Z, colors="black", offset=-1)

    cx = [c[0] for c in coord_list]
    cy = [c[1] for c in coord_list]

    ax.scatter(cx, cy, fcalc_list, color='black')

    plt.show()
