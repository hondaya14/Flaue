import numpy as np


class Intensity:
    def __init__(self):
        self.h, self.k, self.l = 0, 0, 0
        self.intensity = 0
        self.intensity_coord = []
        self.background = 0
        self.ratio = 0
        self.i_b = 0
        self.back_contents_list = []  # 近傍6方向ボクセルの値 BackContentsのリスト

    # 強度値の座標の理論値
    def calculation_center(self, rlv):
        return self.h * rlv[0] + self.k * rlv[1] + self.l * rlv[2]

    def calc_coord(self, rlv):
        vector = self.h * rlv[0] + self.k * rlv[1] + self.l * rlv[2]
        return np.sqrt(np.power(vector[0], 2) + np.power(vector[1], 2) + np.power(vector[2], 2))

    def set_intensity_coord(self, string):
        list_contents = string.split(':')[1].replace('[', '').replace(']', '').split(',')
        self.intensity_coord = list(map(float, list_contents))

    def set_back_contents_list(self, string):
        back_contents_list = []
        for c in string.split(':')[1].split(']'):
            back_contents_str_list = c.replace('[', '').split()
            if len(back_contents_str_list) == 4:
                x, y, z, value = map(float, back_contents_str_list)
                back_contents = BackContents(x, y, z, value)
                back_contents_list.append(back_contents)
        self.back_contents_list = back_contents_list

    def pickup_back(self):
        value_list, coord_list = [], []
        for bc in self.back_contents_list:
            value, coord = bc.pick_up_value_coord()
            value_list.append(value)
            coord_list.append(coord)
        value_list.append(self.intensity)
        coord_list.append(self.intensity_coord)
        return np.array(value_list), np.array(coord_list)


class BackContents:
    def __init__(self, x, y, z, value):
        self.x = x
        self.y = y
        self.z = z
        self.value = value

    def pick_up_value_coord(self):
        return self.value, [self.x, self.y, self.z]
