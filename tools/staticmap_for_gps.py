from staticmap import StaticMap, Line
import os
import sys

sys.path.append('..')
import tools

def map_for_gps():

    dm = tools.data_manager.DataManager()
    # Download and extract sensor data
    dm.setup_data_files('sensor_data')
    # load gps
    dm.load_gps()

    range_tuple = dm.data_dict["gps_range"]

    m = StaticMap(1000, 1000, 80)

    start = [range_tuple[1][0], range_tuple[0][0]]
    end = [range_tuple[1][1], range_tuple[0][1]]

    coordinates = [start, end]
    line_outline = Line(coordinates, 'white', 6)
    line = Line(coordinates, '#D2322D', 4)

    m.add_line(line_outline)
    m.add_line(line)

    image = m.render()
    # Put image in the corresponding data directory
    os.chdir(dm.data_dir)
    image.save('umich.png')


if __name__ == '__main__':
    map_for_gps()