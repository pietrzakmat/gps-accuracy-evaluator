import numpy as np
from matplotlib import pyplot as plt
import time
import datetime
import pandas as pd
import colorama
from colorama import Fore
from colored import fg
import pyproj
geodesic = pyproj.Geod(ellps='WGS84')
# from sklearn.metrics import mean_squared_error
import heading

# Globally measured parameters in meters
# measured_distance is a distance between centers of receivers measured manually by hand.
# It is a sort of ground truth.
# measured_elevation is a heigh from ground measured manually by hand
measured_distance = 0.15 # [m]
measured_elevation = 1.5 # [m]

def load(fname, skipped_rows, quality=1):
    print("Loading: " + fname)
    # pd.set_option('display.max_rows', None)
    df = pd.read_csv(fname, skiprows=skipped_rows, sep="\s+", usecols=[*range(1, 6)], header=None)
    df.columns = ["Time", "East", "North", "Up", "Q"]

    df = df[df.Q == quality]
    # print(df)
    del df["Q"]

    return df

def sync_times_and_merge(data1, data2):
    return pd.merge(data1, data2, how="inner", on="Time")

def plot_two_trajectories_diff(data1, data2):
    sync_data = sync_times_and_merge(data1, data2)
    sync_data = sync_data.assign(East_diff=sync_data["East_x"] - sync_data["East_y"])
    sync_data = sync_data.assign(North_diff=sync_data["North_x"] - sync_data["North_y"])
    sync_data = sync_data.assign(EN_diff=np.sqrt(sync_data["East_diff"]**2 + sync_data["North_diff"]**2)) 
    sync_data = sync_data.assign(Heading=sync_data.apply(lambda x: heading.get_heading_from_diff(x["East_diff"], x["North_diff"]), axis=1)) 
    # print(sync_data)

    plt.figure('ENU trajectory difference')
    plt.scatter(sync_data["East_diff"], sync_data["North_diff"], linestyle="-", s=0.1, c="green", label="Rx1-Rx2")
    plt.plot(sync_data["East_diff"], sync_data["North_diff"], linewidth=0.1, c="green")

    compute_stats(sync_data)

    plt.legend()
    plt.grid()
    # plt.show()

def get_stats_of(df, col_name):
    mean = df[col_name].mean()
    min = df[col_name].min()
    max = df[col_name].max()
    std = df[col_name].std()
    e1 = abs(mean - min)
    e2 = abs(mean - max)
    max_error = e1
    if e2 > max_error:
        max_error = e2
    
    return mean, std, max_error


def compute_stats(df):
    
    pd.options.display.float_format = '{:.3f}'.format
    # print(sync_data["EN_diff"].describe())
    mean_length = df["EN_diff"].mean()

    df = df.assign(EN_diff_to_mean=df["EN_diff"] - mean_length)
    mean, std, max_error = get_stats_of(df, "EN_diff_to_mean")

    df = df.assign(EN_diff_to_measured=df["EN_diff"] - measured_distance)
    m_mean, m_std, m_max_error = get_stats_of(df, "EN_diff_to_measured")

    # print(df)
    print("\nSummary:")
    print(fg("green") + "Measured length: " + str(float(f'{measured_distance:.3f}')) + " [m]")
    print(fg("green") + "Avg length: " + str(float(f'{mean_length:.3f}')) + " [m]")

    print(fg("blue") +"\nStatistics to mean:")
    print(fg("green") + "Mean: " + str(float(f'{mean:.3f}')) + " [m]")
    print(fg("red") + "Std Dev: " + str(float(f'{std:.3f}')) + " [m]")
    print(fg("red") + "Max error: " + str(float(f'{max_error:.3f}')) + " [m]")
    print(fg("blue") + "\nStatistics to measured:")
    print(fg("green") + "Mean: " + str(float(f'{m_mean:.3f}')) + " [m]")
    print(fg("red") + "Std Dev: " + str(float(f'{m_std:.3f}')) + " [m]")
    print(fg("red")+ "Max error: " + str(float(f'{m_max_error:.3f}')) + " [m]")

    print(fg("white")+ "Describe EN_diff_to_mean:")
    print(df["EN_diff_to_mean"].describe())
    print("Describe EN_diff_to_measured:")
    print(df["EN_diff_to_measured"].describe())

def plot_trajectory(data1, data2=None, sync=True):
    
    plt.figure('ENU trajectory')
    if sync and data2 is not None:
        sync_data = sync_times_and_merge(data1, data2)
        # print(sync_data)
        plt.scatter(sync_data["East_x"], sync_data["North_x"], s=0.1, c="blue", label="Rx1")
        plt.scatter(sync_data["East_y"], sync_data["North_y"], s=0.1, c="red", label="Rx2")
    else:
        plt.scatter(data1["East"], data1["North"], s=0.1, c="blue", label="Rx1")
        if data2 is not None:
            plt.scatter(data2["East"], data2["North"], s=0.1, c="red", label="Rx2")

    plt.legend()
    plt.grid()
    # plt.show()

def plot_positions(data1, data2 = None, sync=True):

    fig, axs = plt.subplots(3)
    fig.canvas.manager.set_window_title('Positions') 

    if sync and data2 is not None:
        sync_data = sync_times_and_merge(data1, data2)
        # print(sync_data["Up_x"])
        axs[0].plot(sync_data["East_x"], c="blue", label="Rx1")
        axs[0].plot(sync_data["East_y"], c="orange", label="Rx2") 

        axs[1].plot(sync_data["North_x"], c="blue", label="Rx1")
        axs[1].plot(sync_data["North_y"], c="orange", label="Rx2") 
          
        axs[2].plot(sync_data["Up_x"], c="blue", label="Rx1")
        axs[2].plot(sync_data["Up_y"], c="orange", label="Rx2") 
    else:
        axs[0].plot(data1["East"], c="blue", label="Rx1")
        if data2 is not None:        
            axs[0].plot(data2["East"], c="orange", label="Rx2") 

        axs[1].plot(data1["North"], c="blue", label="Rx1")
        if data2 is not None:        
            axs[1].plot(data2["North"], c="orange", label="Rx2") 
          
        axs[2].plot(data1["Up"], c="blue", label="Rx1")
        if data2 is not None:        
            axs[2].plot(data2["Up"], c="orange", label="Rx2") 
        
    
    axs[0].set(xlabel='Time', ylabel='E-W (m)')
    axs[1].set(xlabel='Time', ylabel='N-S (m)')
    axs[2].set(xlabel='Time', ylabel='U-D (m)') 

    for ax in axs: 
        ax.grid(True)
        ax.legend() 

    # plt.show()