"""
URL: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/?envType=daily-question&envId=2025-02-25
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.



Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16


Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100
"""

class Solution():
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        odds = 0
        evens = 1
        curr_sum = 0
        result = 0
        for num in arr:
            curr_sum += num
            if curr_sum % 2 == 0:
                result +=  odds
                evens += 1
            else:
                result += evens
                odds += 1
        return result



def main():
    arr1 = [1,3,5]
    arr2 = [2,4,6]
    arr3 = [1,2,3,4,5,6,7]
    sol_obj = Solution()
    result1 = sol_obj.numOfSubarrays(arr1)
    result2 = sol_obj.numOfSubarrays(arr2)
    result3 = sol_obj.numOfSubarrays(arr3)
    print(result1)
    print(result2)
    print(result3)


if __name__ == '__main__':
    main()

