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
            intensity.set_intensity_coord(','.join(contents[1:4]))
            intensity.background = float(contents[4].split(':')[1])
            intensity.ratio = float(contents[5].split(':')[1])
            intensity.i_b = float(contents[6].split(':')[1])
            intensity.set_back_contents_list(''.join(contents[7:]))
            intensities.append(intensity)
        return intensities
