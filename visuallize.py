import numpy
import os
import matplotlib.pyplot as plt

classes = os.listdir("data")
for class_d  in classes:
    data_files = os.listdir(f"data/{class_d}")
    try:
        os.makedirs(f"hist/{class_d}")
    except Exception:
        pass
    for data_filename in data_files:
        data_file = numpy.load(f"data/{class_d}/{data_filename}")
        img_file = data_filename.removesuffix(".npz")+".png"
        plt.cla()
        plt.hist(data_file["lens"],bins=8,range=(0,2000))
        plt.savefig(f"hist/{class_d}/{img_file}")
