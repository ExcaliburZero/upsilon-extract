# Author:     Christopher Wells
# License:    MIT License
from __future__ import print_function
import upsilonextract as up
import numpy as np
import sys

def main():
    if len(sys.argv) != 6:
        sys.exit("Invalid Arguments.")

    prefix = sys.argv[1]
    suffix = sys.argv[2]
    padding = sys.argv[3]
    start = int(sys.argv[4])
    end = int(sys.argv[5])
    
    for x in range(start, end + 1):
        number = ("%0" + str(padding) + "d") % (x,)
        file_path = prefix + number + suffix
        (date, mag, err) = parse_file(file_path)
        e_features = up.ExtractFeatures(date, mag, err)
        e_features.run()
        features = e_features.get_features()
    
        print(number, end="")

        features_string = ""
        num_features = len(features)
        i = 0
        for key in features:
            if i < num_features:
                features_string += "\t"
            i += 1

            features_string += str(features[key])

        print(features_string)
        print_stderr(number)


def parse_file(file_path):
    contents = open(file_path).read().split("\n")[0:-1]
    return get_file_parts(contents)

def parse_input():
    return get_file_parts(get_stdin())

def get_file_parts(file_contents):
    parts_list = [line.lstrip().split(' ') for line in file_contents]
    times = np.array([float(line[0]) for line in parts_list])
    magnitudes = np.array([float(line[1]) for line in parts_list])
    errors = np.array([float(line[2]) for line in parts_list])
    return (times, magnitudes, errors)

def get_stdin():
    return sys.stdin.read().split("\n")[0:-1]

def print_stderr(message):
    print(message, file=sys.stderr)

if __name__ == '__main__':
    main()
