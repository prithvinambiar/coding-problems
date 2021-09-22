"""Solution for Leetcode problem - Delete and Earn.

Problem -
You are given an integer array nums. You want to maximize the number of points you get by
performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every
element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some
number of times.

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Solution -
We can clearly see a recursive solution for this. For every element on the array, you have
two option
1. Add the points of the current element
2. Ignore the points of the current element

Once the decision is made, recursively call the same function for the next valid element in
the array.

Time complexity - O(2^N)
Space complexity - O(2^N)

Using memoization (dynamic programming), the solution for the sub-problems can be cached.
Time complexity - O(N LogN)
Space complexity - O(N)
"""

from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Sort the array.
        nums.sort()
        # Maintain a cache to keep track of the solution of sub-problems.
        self.cache = {}
        return self._helper(nums, 0)
    
    def _helper(self, nums: List[int], current_index: int):
        # Boundary condition.
        if not current_index < len(nums):
            return 0
        
        current_val = nums[current_index]
        # Return the solution if already computed (memoization).
        if current_val in self.cache:
            return self.cache[current_val]
        
        # Optimization 1 - ignore the same number in the array.
        counter = 1
        while current_index + 1 < len(nums) and nums[current_index+1] == current_val:
            counter += 1
            index += 1

        # Next index if we choose to select current value.
        # We must ignore array elements with current_val + 1 value.
        next_index = current_index + 1
        while (next_index < len(nums) and nums[next_index] == current_val + 1):
            next_index += 1
        
        first_option = (current_val * counter) + self._helper(nums, next_index)
        second_option = self._helper(nums, current_index+1)
        self.cache[current_val] = max(first_option, second_option)
        return self.cache[current_val]
