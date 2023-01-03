'''计算一些基础的统计量 例如所有数据的均值、方差等， 并绘制水平箱线图'''
import os
import numpy as np
from utils import DataFiles
from flow_utils import flow

import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt

def box_plot(box_data, title, labels, vert=False):
    fig_path = os.path.join('boxplots', f'{title}-boxplot-log10.png')
    color_list = ['lightgreen', 'orange', 'deepskyblue']
    # 水平箱线图
    plt.figure(figsize=(20, 8))
    plt.title(title, fontsize=20)
    f = plt.boxplot(box_data, labels=labels, vert=vert, showmeans=True, patch_artist=True, showfliers=True)
    plt.tick_params(labelsize=16)
    for box, c in zip(f["boxes"], color_list): # 对箱线图设置颜色
        box.set(color=c, linewidth=2)
        box.set(facecolor=c)
    # plt.show()

    plt.savefig(fig_path)


def log(x, base):
    return np.log(x) / np.log(base)


try:
    os.makedirs('boxplots')
except:
    pass

data_files = DataFiles() # 因为没有用game和standby两类数据，直接本地把那个两个文件夹移出去了
box_data = {}
for class_name in data_files.classes:
    box_data[class_name] = {"lens": [], "timegap": [], "flow": []}

# 计算三类统计量
for class_name, data_basename, data in DataFiles(): 
    box_data[class_name]["lens"] += data["lens"].tolist()
    box_data[class_name]["timegap"] += (data["times"][1:]-data["times"][:-1]).tolist()
    box_data[class_name]["flow"] += flow(data)

# 转换为ndarray数组
for class_name in box_data.keys(): 
    box_data[class_name]["lens"] = np.reshape(np.array(box_data[class_name]["lens"], dtype=np.float32), (-1))
    box_data[class_name]["timegap"] = np.reshape(np.array(box_data[class_name]["timegap"], dtype=np.float32), (-1))
    box_data[class_name]["flow"] = np.reshape(np.array(box_data[class_name]["flow"], dtype=np.float32).reshape(-1), (-1))

# 绘制箱线图
for statistic in ["lens", "timegap", "flow"]:
    data = []
    labels = []
    for class_name, v in box_data.items():
        labels.append(class_name)
        # data.append(v[statistic])
        data.append(log(v[statistic]+1, 10)) # 以10为底取对数

    box_plot(data, statistic, labels)