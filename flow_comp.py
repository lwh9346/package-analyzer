from flow_utils import flow, compare_hist, flow_normed_hist
from utils import DataFiles
import numpy as np

data_to_compare = flow_normed_hist(
    flow(np.load("data/game/data5_webgame.npz")))

best_match = (1.,)
for class_name, basename, data in DataFiles(path="norm_hist_data_flow"):
    if basename == "data5_webgame":
        continue
    l = compare_hist(data_to_compare, data)
    if l < best_match[0]:
        best_match = (l, class_name, basename)
assert not len(best_match) < 3
print(f"best match class:{best_match[1]}\nbest match name:{best_match[2]}\nunlikelyhood:{best_match[0]}")
