
class Intensity:
    def __init__(self):
        self.h, self.k, self.l = 0, 0, 0
        self.intensity = 0
        self.background = 0
        self.ratio = 0
        self.i_b = 0
        self.back_contents_list = []

    def set_back_contents_list(self, string):
        back_contents_list = []
        for c in string.split(':')[1].split(']'):
            back_contents_str_list = c.replace('[', '').split()
            if len(back_contents_str_list) == 4:
                x, y, z, value = map(float, back_contents_str_list)
                back_contents = BackContents(x, y, z, value)
                back_contents_list.append(back_contents)
        self.back_contents_list = back_contents_list


class BackContents:
    def __init__(self, x, y, z, value):
        self.x = x
        self.y = y
        self.z = z
        self.value = value
