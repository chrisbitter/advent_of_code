import itertools
import numpy as np

rules = []
manuals = []

with open("2405_input") as file:
    for line in file.readlines():
        if "|" in line:
            rules.append(list(map(int, line.strip().split("|"))))
        elif "," in line:
            manuals.append(list(map(int, line.strip().split(","))))

pages = list(set(itertools.chain.from_iterable(rules)))

result_1 = 0
result_2 = 0

for manual in manuals:
    relevant_rules = [rule for rule in rules if all([page in manual for page in rule])]
    
    if all([manual.index(vl) < manual.index(vr) for vl, vr in relevant_rules]):
        result_1 += int(manual[len(manual) // 2])
    else:
        sorted_manual = [0] * len(manual)
        
        for page in manual:
            ll = sum([page == rule[0] for rule in relevant_rules])
            rr = sum([page == rule[1] for rule in relevant_rules])
            
            # print(ll, rr)
            
            sorted_manual[rr] = page
        
        result_2 += int(sorted_manual[len(sorted_manual) // 2])


print("Solution 1")
print(result_1)

print("Solution 2")
print(result_2)