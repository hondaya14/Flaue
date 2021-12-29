import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from function import laue


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
    ax = fig.add_subplot(projection='3d')

    ax.set_title('Fcalc')

    print(f'x min:{min(x)}, max:{max(x)}')
    print(f'y min:{min(y)}, max:{max(y)}')
    print(f'z min:{min(z)}, max:{max(z)}')

    ax.set_xlabel("a", size=15, color="black")
    ax.set_ylabel("b", size=15, color="black")
    ax.set_zlabel("z", size=15, color="black")

    ax.scatter(x, z, value, c=value, cmap="gray")
    plt.show()


def plot_laue_function(scat_vec):
    fig = plt.figure()
    ax = Axes3D(fig)

    x, y, z, fcalc = [], [], [], []
    for i in range(-10, 10, 1):
        for j in range(-10, 10, 1):
            for k in range(-10, 10, 1):
                x.append(i)
                y.append(j)
                z.append(k)
                fcalc.append(laue(scat_vec))

    ax.set_xlabel("a", size=15, color="black")
    ax.set_ylabel("b", size=15, color="black")
    ax.set_zlabel("c", size=15, color="black")

    # p = np.linspace(-10, 10, 50)
    # plt.plot(p, [laue(Crystal.Na.value, Crystal.Nb.value, Crystal.Nc.value, scat_vec, k, k, k) for k in p])
    # plt.show()

    ax.scatter(x, y, z, c=fcalc, cmap="coolwarm")
    plt.show()
