"""
url : https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/?envType=daily-question&envId=2024-11-22

You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that
column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is either 0 or 1.
"""
from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        counter = {}
        for x in range(m):
            row_string = ''
            flag = 0
            for y in range(n):
                if y == 0 and matrix[x][y] == 1:
                    flag = 1
                if flag == 0:
                    row_string = row_string + str(matrix[x][y])
                else:
                    row_string = row_string + str(1 - matrix[x][y])
            if row_string in counter:
                counter[row_string] += 1
            else:
                counter[row_string] = 1
        return max(counter.values())


def main():
    input_matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
    sol_obj = Solution()
    result = sol_obj.maxEqualRowsAfterFlips(input_matrix)
    print(result)


if __name__ == '__main__':
    main()
