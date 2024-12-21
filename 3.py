
'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #approach 1: using 2 for loops
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return []
        #Approach 2:using Hashmap
        prevMap={}
        for i, n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[n]=i 