#! /usr/bin/python3
import sys
import numpy as np
from matplotlib import pyplot as plt
import data_utils

skiprows = 25

if len(sys.argv) == 2:
    file_str1 = sys.argv[1]
    data1 = data_utils.load(file_str1, skiprows)
    data_utils.plot_trajectory(data1)
elif len(sys.argv) == 3:
    file_str1 = sys.argv[1]
    file_str2 = sys.argv[2]
    data1 = data_utils.load(file_str1, skiprows)
    data2 = data_utils.load(file_str2, skiprows)
    data_utils.plot_trajectory(data1, data2)