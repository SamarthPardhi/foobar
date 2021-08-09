# Gearing Up for Destruction
# ==========================

# As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

# The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

# Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

# For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

# The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution({4, 17, 50})
# Output:
#     -1,-1

# Input:
# Solution.solution({4, 30, 50})
# Output:
#     12,1

# -- Python cases --
# Input:
# solution.solution([4, 30, 50])
# Output:
#     12,1

# Input:
# solution.solution([4, 17, 50])
# Output:
#     -1,-1


def solution(pegs):
    #Your code here
    import numpy
    inv_row=[]
    cons_col=[]
    numo=0
    for i in range(len(pegs)-1):
        cons_col.append(abs(pegs[i+1]-pegs[i]))
        if i%2==0:
            inv_row.append(2)
        else:
            inv_row.append(-2)
        numo+=(cons_col[i]*inv_row[i])
    if len(pegs)%2==0:
        deno=3
    else:
        deno=1
    if numo/deno<1:
        return [-1,-1]
    else:
        if numo%3==0 and deno==3:
            numo=numo/3
            deno=1
        gear_matrix=[]
        pegs_col=[]
        n=len(pegs)
        for i in range(n-1):
            pegs_col.append(abs(pegs[i+1]-pegs[i]))
            s=i*'0'+'11'+(n-2-i)*'0'
            row=[int(ch) for ch in s]
            gear_matrix.append(row)
        gear_matrix.append([1]+[0]*(n-2)+[-2])
        pegs_col.append(0)
        
        import numpy as np
        inv_gear_matrix=np.linalg.inv(gear_matrix)
        
        gears_radius=[]
        for i in inv_gear_matrix:
            gears_radius.append(sum(i*pegs_col))
        
        for i in gears_radius:
            if i<1:
                return [-1,-1]
        return [numo,deno]

    # gear_matrix=[]
    # pegs_col=[]
    # n=len(pegs)
    # for i in range(n-1):
    #     pegs_col.append(abs(pegs[i+1]-pegs[i]))
    #     s=i*'0'+'11'+(n-2-i)*'0'
    #     row=[int(ch) for ch in s]
    #     gear_matrix.append(row)
    # gear_matrix.append([1]+[0]*(n-2)+[-2])
    # pegs_col.append(0)

    # import numpy as np
    # inv_gear_matrix=np.linalg.inv(gear_matrix)
    
    # gears_radius=[]
    # for i in inv_gear_matrix:
    #     gears_radius.append(sum(i*pegs_col))
    # return gears_radius
    

print(solution([4,30,50]))
print(solution([4,17,50]))
print(solution([8,30]))

