'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Input: nums = [2,20,4,10,3,4,5]

Output: 4
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest_strk=0

        for num in nums:
            if num-1 not in num_set:
                current_num=num
                current_strk=1


                while current_num+1 in num_set:
                    current_num+=1
                    current_strk+=1

                
                longest_strk=max(longest_strk,current_strk)
        return longest_strk