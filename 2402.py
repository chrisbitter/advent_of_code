import numpy as np
from copy import deepcopy

result_1 = 0
result_2 = 0

def is_safe(report):
    report = np.array(report)
    diffs = report[1:] - report[:-1]
    signs = np.sign(diffs)
    
    # print(diffs)
    # print(signs)

    if all(signs) and len(set(signs)) == 1:
        if all(0 <= np.abs(diffs)) and all(np.abs(diffs) < 4):
            return True

    return False

with open("02_input") as file:
    for line in file.readlines():
        report = list(map(int, line.split(" ")))

        if is_safe(report):
            result_1 += 1
            result_2 += 1
        else:
            for idx in range(len(report)):
                sub_report = deepcopy(report)
                del sub_report[idx:idx+1]
                
                if is_safe(sub_report):
                    result_2 += 1
                    break
            

print("Solution 1")
print(result_1)

print("Solution 2")
print(result_2)
