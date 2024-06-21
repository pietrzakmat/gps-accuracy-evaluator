#! /usr/bin/python3
import os
import sys
import numpy as np
from matplotlib import pyplot as plt
import data_utils

skiprows = 25

file_str1 = "data/union_0705/fix1.pos"
file_str2 = "data/union_0705/fix2.pos"

data1 = data_utils.load(file_str1, skiprows)
data2 = data_utils.load(file_str2, skiprows)

data_utils.plot_positions(data1, data2)
data_utils.plot_trajectory(data1, data2)
data_utils.plot_two_trajectories_diff(data1, data2)

plt.show()