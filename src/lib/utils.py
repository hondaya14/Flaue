import numpy as np

from intensity import Intensity, BackContents
import sys


def read_data(path):
    intensities = []
    with open(file=path, mode='r') as intf:
        intensity_list = intf.readlines()
        for line in intensity_list:
            intensity = Intensity()
            intensity.h, intensity.k, intensity.l, *contents = line.split()
            intensity.h, intensity.k, intensity.l = int(intensity.h), int(intensity.k), int(intensity.l)
            contents = ' '.join(contents)
            contents = contents.split(',')
            intensity.intensity = float(contents[0].split(':')[1])
            intensity.set_intensity_coord(','.join(contents[1:4]))
            intensity.background = float(contents[4].split(':')[1])
            intensity.ratio = float(contents[5].split(':')[1])
            intensity.i_b = float(contents[6].split(':')[1])
            intensity.set_back_contents_list(''.join(contents[7:]))
            intensities.append(intensity)
        return intensities


# return gt
def read_fobs(path):
    fobs_data = []
    with open(file=path, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            h, k, l, *values = line.split()
            h, k, l = map(int, [h, k, l])
            fcalc_crys_squared, fobs_squared, f_sigma_squared = map(float, values[:-1])
            if fobs_squared > 2 * f_sigma_squared:
                fobs_data.append([h, k, l, np.sqrt(fcalc_crys_squared), np.sqrt(fobs_squared), f_sigma_squared, int(f'{h}{k}{l}')])
    # fobs_data.sort(key=lambda x: x[-1])
    return fobs_data


if __name__ == '__main__':
    read_fobs(sys.argv[1])
