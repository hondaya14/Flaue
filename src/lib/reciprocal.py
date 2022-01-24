import numpy as np


# 逆格子ベクトルを計算
def calc_reciprocal_lattice_vector():
    # unit cell parameters
    unit_cell_tv_x = [7.1178, 0, 0]
    unit_cell_tv_y = [0, 9.6265, 0]
    unit_cell_tv_z = [-1.39567, 0, 11.81314]

    # unit cell volume
    unit_cell_volume = np.dot(np.cross(unit_cell_tv_x, unit_cell_tv_y), unit_cell_tv_z)

    reciprocal_lattice_vector_a = np.cross(unit_cell_tv_y, unit_cell_tv_z) / unit_cell_volume
    reciprocal_lattice_vector_b = np.cross(unit_cell_tv_z, unit_cell_tv_x) / unit_cell_volume
    reciprocal_lattice_vector_c = np.cross(unit_cell_tv_x, unit_cell_tv_y) / unit_cell_volume
    return [reciprocal_lattice_vector_a, reciprocal_lattice_vector_b, reciprocal_lattice_vector_c]


# 逆格子ベクトルを計算
def calc_reciprocal_lattice_vector_to_list():
    # unit cell parameters
    unit_cell_tv_x = [7.1178, 0, 0]
    unit_cell_tv_y = [0, 9.6265, 0]
    unit_cell_tv_z = [-1.39567, 0, 11.81314]

    # unit cell volume
    unit_cell_volume = np.dot(np.cross(unit_cell_tv_x, unit_cell_tv_y), unit_cell_tv_z)

    reciprocal_lattice_vector_a = np.cross(unit_cell_tv_y, unit_cell_tv_z) / unit_cell_volume
    reciprocal_lattice_vector_b = np.cross(unit_cell_tv_z, unit_cell_tv_x) / unit_cell_volume
    reciprocal_lattice_vector_c = np.cross(unit_cell_tv_x, unit_cell_tv_y) / unit_cell_volume
    return [reciprocal_lattice_vector_a.tolist(), reciprocal_lattice_vector_b.tolist(), reciprocal_lattice_vector_c.tolist()]


if __name__ == "__main__":
    print(calc_reciprocal_lattice_vector())
