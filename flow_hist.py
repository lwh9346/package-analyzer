import numpy as np
import os
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd

classes = os.listdir("data")
for class_d in classes:
    data = {"Name": [], "Max": [], "Min": [], "Median": [], "Mean": [], "Var": []}
    data_files = os.listdir(f"data/{class_d}")
    try:
        os.makedirs(f"hist_flow/{class_d}")
    except Exception:
        pass
    for data_filename in data_files:
        
        data_file = np.load(f"data/{class_d}/{data_filename}")
        img_file = data_filename.removesuffix(".npz")+".png"
        
        times = data_file["times"] - data_file["times"][0]
        flow = []
        start_index, end_index = 0, 0
        start_time = 0.
        while end_index < len(times):
            if times[end_index] < start_time + 0.5:
                end_index += 1
            else:
                flow.append(times[start_index:end_index].sum())
                start_index = end_index
                start_time = times[end_index]
                end_index += 1
                
        plt.cla()
        plt.hist(flow,bins=50, range=(0, 5e4))
        plt.savefig(f"hist_flow/{class_d}/{img_file}")
        flow = np.array(flow)
        data["Name"].append(data_filename)
        data["Max"].append(np.max(flow))
        data["Min"].append(np.min(flow))
        data["Median"].append(np.median(flow))
        data["Mean"].append(np.mean(flow))
        data["Var"].append(np.var(flow))
    df = pd.DataFrame(data)
    df.to_csv(f"hist_flow/{class_d}/info.csv")
        

