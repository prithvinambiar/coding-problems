"""Solution for Leetcode problem - Jump Game.

Problem -
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Solution -
Keep track of left most index which is valid i.e. a position on the array from which you can
reach the last element.

Now for every element, check if you can reach that element.

Time complexity - O(N)
Space complexity - O(1)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left_most_valid_position = len(nums) - 1
        for current_index in range(left_most_valid_position - 1, -1, -1):
            if current_index + nums[current_index] >= left_most_valid_position:
                left_most_valid_position = current_index
        return left_most_valid_position == 0