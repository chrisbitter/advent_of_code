import re

result_1 = 0
result_2 = 0
do = True

with open('2403_input', 'r') as file:
    for line in file:
        matches = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)', line)
        for match in matches:
            if match.group(0).startswith("mul("):
                # print(match.groups(0)[1])
                num1, num2 = int(match.group(1)), int(match.group(2))
                product = num1 * num2
                result_1 += product
                
                if do:
                    result_2 += product
                    
            else:
                print(match)
                print(match.group(0) == "do()")
                do = match.group(0) == "do()"

print("Solution 1")
print(result_1)

print("Solution 2")
print(result_2)