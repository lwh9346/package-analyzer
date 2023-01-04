import utils
import flow_utils
print("开始交叉验证")
print("已知样本:B未知样本:A")
correct = {"browsing":0,"streaming":0,"video":0}
wrong = {"browsing":0,"streaming":0,"video":0}
for c,b,d in utils.DataFiles("hist_A"):
    best_match = (1.,)
    for cc,bb,dd in utils.DataFiles("hist_B"):
        ul = flow_utils.compare_hist(d,dd)
        if ul<best_match[0]:
            best_match = (ul,cc,bb)
    if best_match[1]==c:
        correct[c]+=1
    else:
        wrong[c]+=1
print("correct")
print(correct)
print("wrong")
print(wrong)
print("已知样本:A未知样本:B")
correct = {"browsing":0,"streaming":0,"video":0}
wrong = {"browsing":0,"streaming":0,"video":0}
for c,b,d in utils.DataFiles("hist_B"):
    best_match = (1.,)
    for cc,bb,dd in utils.DataFiles("hist_A"):
        ul = flow_utils.compare_hist(d,dd)
        if ul<best_match[0]:
            best_match = (ul,cc,bb)
    if best_match[1]==c:
        correct[c]+=1
    else:
        wrong[c]+=1
print("correct")
print(correct)
print("wrong")
print(wrong)