from flow_conf import HIST_BINS, HIST_UPPER_RANGE
from flow_utils import flow
from utils import DataFiles
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib
matplotlib.use('agg')

classes = os.listdir("data")
for class_name in classes:
    statistic_data = {"Name": [], "Max": [],
                      "Min": [], "Median": [], "Mean": [], "Var": []}
    data_filenames = os.listdir(f"data/{class_name}")
    try:
        os.makedirs(f"hist_flow/{class_name}")
    except Exception:
        pass
    try:
        os.makedirs(f"norm_hist_data_flow/{class_name}")
    except Exception:
        pass
    for data_filename in data_filenames:
        data = np.load(f"data/{class_name}/{data_filename}")
        data_basename = data_filename.removesuffix(".npz")
        times = data["times"] - data["times"][0]
        flow_ = flow(data)
        # 绘制直方图
        plt.cla()
        plt.hist(flow_, bins=HIST_BINS, range=(0, HIST_UPPER_RANGE))
        plt.savefig(f"hist_flow/{class_name}/{data_basename}.png")
        # 保存归一化后的直方图
        hist = np.histogram(flow_, bins=HIST_BINS, range=(0, HIST_UPPER_RANGE))
        hist = hist[0]/np.sum(hist[0])
        np.save(f"norm_hist_data_flow/{class_name}/{data_basename}.npy", hist)
        # 保存统计信息
        flow_ = np.array(flow_)
        statistic_data["Name"].append(data_filename)
        statistic_data["Max"].append(np.max(flow_))
        statistic_data["Min"].append(np.min(flow_))
        statistic_data["Median"].append(np.median(flow_))
        statistic_data["Mean"].append(np.mean(flow_))
        statistic_data["Var"].append(np.var(flow_))
    df = pd.DataFrame(statistic_data)
    df.to_csv(f"hist_flow/{class_name}/info.csv", encoding="GBK")
