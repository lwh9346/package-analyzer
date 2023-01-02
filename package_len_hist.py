import os
import os.path
import matplotlib.pyplot as plt
from utils import DataFiles

for class_name, data_basename, data in DataFiles():
    if not os.path.exists(f"len_hist/{class_name}"):
        os.makedirs(f"len_hist/{class_name}")
    plt.cla()
    plt.hist(data["lens"], bins=8, range=(0, 2000))
    plt.savefig(f"len_hist/{class_name}/{data_basename}.png")
