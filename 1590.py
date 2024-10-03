"""
URL: https://leetcode.com/problems/make-sum-divisible-by-p/description/

Question:
Given an array of positive integers nums, remove the smallest subarray
(possibly empty) such that the sum of the remaining elements is divisible by p.
It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove,
    or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

Example 1:
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6.
We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

Example 2:
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9.
The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

Example 3:
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3.
Thus we do not need to remove anything.
"""

class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total_sum = sum(nums)
        remainder_needed = total_sum % p

        # If the total sum is already divisible by p, return 0
        if remainder_needed == 0:
            return 0

        # Initialize variables
        current_sum = 0
        min_length = len(nums)
        remainder_map = {
            0: -1}  # Dictionary to track the most recent index of each remainder

        for i in range(len(nums)):
            # Update prefix sum
            current_sum += nums[i]

            # Compute the current remainder
            current_remainder = current_sum % p

            # Find the target remainder we need to make the sum divisible by p
            target_remainder = (current_remainder - remainder_needed + p) % p

            # Check if the target remainder is in the remainder_map
            if target_remainder in remainder_map:
                subarray_length = i - remainder_map[target_remainder]
                min_length = min(min_length, subarray_length)

            # Update the remainder_map with the current remainder and index
            remainder_map[current_remainder] = i

        # If min_length is not updated, return -1. Otherwise, return min_length
        return min_length if min_length < len(nums) else -1


def main():
    obj = Solution()
    print(obj.minSubarray([3, 1, 4, 2], 6))  # Output: 1
    print(obj.minSubarray([6, 3, 5, 2], 9))  # Output: 2
    print(obj.minSubarray([1, 2, 3], 3))     # Output: 0
    print(obj.minSubarray([8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2], 148))

if __name__ == '__main__':
    main()
