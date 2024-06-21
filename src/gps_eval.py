#! /usr/bin/python3
import sys
import numpy as np
from matplotlib import pyplot as plt
import data_utils

if len(sys.argv) == 2:
    file_str1 = sys.argv[1]
    data1 = data_utils.load(file_str1, 25)
elif len(sys.argv) == 3:
    file_str1 = sys.argv[1]
    file_str2 = sys.argv[2]
    data1 = data_utils.load(file_str1, 25)
    data2 = data_utils.load(file_str2, 25)

print("len(data1):" + str(len(data1["East"])))
print("len(data2):" + str(len(data2["East"])))
# data_utils.plot_trajctory(data2)
# data_utils.plot_two_trajctories(data1, data2)
data_utils.plot_positions(data1, data2)

# print(data2["East"])

# east_diff = data_utils.trajectory_diff(data1, data2)

# print(east_diff)