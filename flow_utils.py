import numpy
from flow_conf import FLOW_CALC_DURATION
def flow(data:numpy.ndarray)->list:
    times = data["times"] - data["times"][0]
    flow = []
    start_index, end_index = 0, 0
    start_time = 0.
    while end_index < len(times):
        if times[end_index] < start_time + FLOW_CALC_DURATION:
            end_index += 1
        else:
            flow.append(times[start_index:end_index].sum())
            start_index = end_index
            start_time = times[end_index]
            end_index += 1
    return flow

def compare_hist(a:numpy.ndarray,b:numpy.ndarray)->float:
    return float(numpy.sum((a-b)**2))
