# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:39:56 2021

@author: leosh
"""

def biggestPlus(matrix):
    def get_left_up():
        dp_left = [[-1 for _ in row] for row in matrix]
        dp_up = [[ -1 for _ in row ] for row in matrix ]

        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val == '1':
                    #####FOR DP_LEFT
                    if x != 0:
                        dp_left[y][x] = dp_left[y][x-1] + 1
                    else:
                        dp_left[y][x] = 0

                    #####FOR DP_UP
                    if y != 0:
                        dp_up[y][x] = dp_up[y-1][x] + 1
                    else:
                        dp_up[y][x] = 0

        return dp_left, dp_up

    def get_right_down():
        dp_right = [[-1 for _ in row] for row in matrix]
        dp_down = [[-1 for _ in row] for row in matrix]

        for y in range(len(matrix)-1,-1,-1):
            row = matrix[y]
            for x in range(len(row) - 1, -1, -1):
                val = matrix[y][x]
                if val == '1':
                    #####FOR DP_RIGHT
                    if x < len(row)-1:
                        dp_right[y][x] = dp_right[y][x + 1] + 1
                    else:
                        dp_right[y][x] = 0

                    #####FOR DP_DOWN
                    if y < len(matrix)-1:
                        dp_down[y][x] = dp_down[y + 1][x] + 1
                    else:
                        dp_down[y][x] = 0

        return dp_right, dp_down

    def getBiggestPlus(dp_left,dp_up,dp_right,dp_down):
        #####GET MIN OF 4 MATRICES
        result = 0

        for y, row in enumerate(dp_left):
            for x, val in enumerate(row):
                minimum = min(dp_left[y][x],dp_down[y][x],dp_right[y][x],dp_up[y][x])
                result = max(result,minimum)         #####ANSWER IS THE MAX

        return result

    dp_left, dp_up = get_left_up()
    dp_right, dp_down = get_right_down()
    return getBiggestPlus(dp_left,dp_up,dp_right,dp_down)

matrix =   ["0110010",
            "1010101",
            "1111111",
            "0010000",
            "0000000"]
print(biggestPlus(matrix))