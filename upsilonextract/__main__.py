# Author:     Christopher Wells
# License:    MIT License
from __future__ import print_function
import upsilonextract as up
import numpy as np

import argparse
import sys

program_description = "UPSILoN Extract is a Python script for extracting information from (time, magnitude, error) light curve data. It was created from the functionality built into the UPSILoN periodic variable star classifier (Kim & Bailer-Jones 2015)."

def main():
    parser = argparse.ArgumentParser(description=program_description)
    parser.add_argument('prefix', type=str, help='part of the path of the data files in front of the id number')
    parser.add_argument('suffix', type=str, help='part of the path of the data files after the id number')
    parser.add_argument('padding', type=int, help='number of digits to pad the id numbers to')
    parser.add_argument('start', type=int, help='id number of first file to process')
    parser.add_argument('end', type=int, help='id number of last file to process')

    args = parser.parse_args()

    process_input_files(args.prefix, args.suffix, args.padding, args.start, args.end)
    
def process_input_files(prefix, suffix, padding, start, end):
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
