# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
# 
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

import re
import numpy as np

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
                
                # check if v1 and v2 are linearly independent
                if np.linalg.matrix_rank(np.array([v1, v2])) < 2:
                    # if the vectors are linear dependent, the goal must also be linear dependent
                    if np.linalg.matrix_rank(np.array([v1, v_goal])) < 2:
                        # the goal may be reachable
                        raise NotImplementedError()
                    else:
                        # the goal is not reachable
                        continue
                else:
                    # the vectors are linear independent
                    # Calculate the linear combination of v1 and v2 that reaches v_goal
                    A = np.linalg.solve(np.array([v1, v2]).T, v_goal)
                    
                    print(A)
                    # Check if the solution is valid (non-negative integers)
                    if np.all(A >= 0) and np.all(np.modf(A)[0] == 0):
                        total += 3 * A[0] + A[1]

                continue
            
                A = (x2 / y2) * Y - X

                print(A)

                A /= y1 - x1

                print(A)
                
                
                continue
                
                # step size that can be achieved by using either button exclusively
                leap = x1 * x2
                
                if x2 < 3 * x1:
                    # its cheaper to use button A
                    
                    # take as many big leaps as possible.
                    # Leave a margin of 2 leaps to allow for all possible combinations of buttons.
                    steps = (X - 2 * leap) // leap
                    
                    # take x2 steps with button A for one big leap
                    button_presses = steps * x2
                    cost = 3 * button_presses
                    
                    print(cost)

                    print(Y)
                    
                    X -= button_presses * x1
                    Y -= button_presses * y1
                    
                    print(button_presses * y1)
                    
                    print(X, Y)
                else:
                    # its cheaper to use button B
                    ...
                
                # print(x1, y1)
                # print(x2, y2)
                # print(X, Y)
                
                A = np.arange(101)
                
                B = (X - A * x1) / x2
                
                print(B)
                
                Y_ = A * y1 + B * y2
                
                mask_valid = Y_ == Y
                # mask_valid &= B <= 100
                mask_valid &= B >= 0
                mask_valid &= np.modf(B)[0] == 0
                
                print(mask_valid)
                
                if any(mask_valid):
                    A = A[mask_valid]
                    B = B[mask_valid]
                    cost = 3 * A + B
                
                    total += cost.min()
                    
                
            case _:
                pass
        
print(total)