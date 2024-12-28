'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # output=[]
        # for i in range(n):
        #     prd=1
        #     for j in range(n):
        #         if i!=j:
        #             prd*=nums[j]
        #     output.append(prd)
        # return output
        n=len(nums)
        output=[1]*n
        prefix_prd=1
        for i in range(n):
            output[i]=prefix_prd
            prefix_prd*=nums[i]
        
        suffix_prd=1
        for i in range(n-1,-1,-1):
            output[i]*=suffix_prd
            suffix_prd*=nums[i]
        
        return output