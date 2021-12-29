from intensity import Intensity, BackContents


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
            intensity.background = float(contents[1].split(':')[1])
            intensity.ratio = float(contents[2].split(':')[1])
            intensity.i_b = float(contents[3].split(':')[1])
            intensity.set_back_contents_list(''.join(contents[4:]))
            intensities.append(intensity)
        return intensities
