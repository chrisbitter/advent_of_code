import numpy as np

list_a = []
list_b = []

with open("01_input") as file:
    for line in file.readlines():
        _ = line.split(" ")
        list_a.append(int(_[0]))
        list_b.append(int(_[-1]))
        
list_a = np.sort(list_a)
list_b = np.sort(list_b)

print(list_a[:3])
print(list_b[:3])

result_1 = np.abs(list_a - list_b).sum()

print("Solution 1")
print(result_1)

similarity = 0

for value in list_a:
    similarity += value * np.sum(list_b == value)
    
print("Solution 2")
print(similarity)