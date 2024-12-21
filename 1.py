'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false
Input: nums = [1, 2, 3, 3]

Output: true

'''
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # approach 1: (Worst case) (2 for loops = O(n*n) operation)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

        #approach 2: Using Hashset (if num in hashset (fetch) only needs O(1) operation)
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False