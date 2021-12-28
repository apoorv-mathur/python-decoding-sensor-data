import os
import glob
import csv
def load_sensor_data():
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
#   load_sensor_data = load_data.query("def load_sensor_data(): ??")
#   load_sensor_data = load_data.defines("load_sensor_data")
    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file, delimiter=',')
            for row in data_reader:
                sensor_data.append(row)
    return sensor_data
