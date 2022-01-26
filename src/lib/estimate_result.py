from src.lib.intensity import Intensity


class EstimateResult:
    def __init__(self):
        self.intensity = Intensity()
        self.center = []
        self.fcalc_list = []
        self.coord_list = []
        self.fitting_param = []  # [0]: initial, [1]: finally
        self.fcalc_fit_list = []

    def print_result(self):
        print(f'h: {self.intensity.h}, k: {self.intensity.k}, l: {self.intensity.l}')
        print(f'center ... {self.center}')
        print(f'fit prm (init) ... {self.fitting_param[0]}')
        print(f'fit prm  (fin) ... {self.fitting_param[1]}')
        print(f'\nFcalc(voxel) information')
        print(f'Coordinate\t\t\t\tFcalc')
        for i in range(7):
            print(f'{self.coord_list[i]}\t{self.fcalc_list[i]}')
        print(f'\nFcalc(voxel)\tFcalc(fitting)')
        for i in range(7):
            print(f'{str(self.fcalc_list[i]).rjust(8)}\t{round(self.fcalc_fit_list[i], 6)}')
        print(f'\nFcalc(est) = {self.fitting_param[1][0]}')
        print(f'--------------------------------------------------------')
