result = 0

part_2 = True

with open("2407_input") as file:
    for line in file.readlines():
        raw_test_value, raw_numbers = line.strip().split(":")
        
        test_value = int(raw_test_value)
        numbers = list(map(int, raw_numbers.strip().split(" ")))
        
        possible_test_values = [numbers[0]]
        
        for number in numbers[1:]:
            new_possible_test_values = []
            
            for possible_test_value in possible_test_values:
                new_possible_test_values.append(possible_test_value + number)
                new_possible_test_values.append(possible_test_value * number)
                
                if part_2:
                    new_possible_test_values.append(int(str(possible_test_value) + str(number)))
                
            
            possible_test_values = [value for value in new_possible_test_values if value <= test_value]
            
        if any([value == test_value for value in possible_test_values]):
            result += test_value
            
            
print("Solution")
print(result)