import os
import os.path
import matplotlib.pyplot as plt
from utils import DataFiles

for class_name, data_basename, data in DataFiles():
    if not os.path.exists(f"time_gap_hist/{class_name}"):
        os.makedirs(f"time_gap_hist/{class_name}")
    plt.cla()
    time_gap = data["times"][1:]-data["times"][:-1]
    plt.hist(time_gap, bins=8, range=(.001, .005))
    plt.savefig(f"time_gap_hist/{class_name}/{data_basename}.png")
