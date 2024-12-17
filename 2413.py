# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
# 
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

import re
import numpy as np
from mpmath import mp

mp.dps = 50

def find_coefficients(v1, v2, goal):
    # Create the coefficient matrix
    A = np.array([v1, v2], dtype=object).T
    
    # Convert to mpmath matrices
    A_mp = mp.matrix(A.tolist())
    goal_mp = mp.matrix(goal.tolist())
    
    # Solve the system of linear equations
    try:
        solution = mp.lu_solve(A_mp, goal_mp)
        return np.array(solution, dtype=float)
    except ValueError:
        # The system of equations has no solution
        return None

total = 0

with open("2413_input") as file:
    for ii, line in enumerate(file.readlines()):
        
        match ii % 4:
            case 0:
                # Button A: X+94, Y+34
                # extract X and Y
                
                x1, y1 = re.search(r"X([+-]?\d+), Y([+-]?\d+)", line).groups()
                x1, y1 = int(x1), int(y1)
            case 1:
                x2, y2 = re.search(r"X([+-]?\d+), Y([+-]?\d+)", line).groups()
                x2, y2 = int(x2), int(y2)
            case 2:
                X, Y = re.search(r"X=([+-]?\d+), Y=([+-]?\d+)", line).groups()
                X, Y = int(X), int(Y)
                
                # added for part 2
                X += 10000000000000
                Y += 10000000000000

                v1 = np.array([x1, y1])
                v2 = np.array([x2, y2])
                
                v_goal = np.array([X, Y])
                v_goal_length = np.linalg.norm(v_goal)
                
                A = np.array([v1, v2]).T
                
                coefficients = find_coefficients(v1, v2, v_goal)

                if coefficients is not None:
                    a, b = coefficients
                    # Check if the solution is valid (non-negative integers)
                    if np.all(coefficients >= 0) and np.all(np.modf(coefficients)[0] == 0):
                        total += 3 * a + b
            case _:
                pass
        
print(int(total))