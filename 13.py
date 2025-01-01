'''
You are given an integer array heights where heights[i] represents the height of the 
ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store

Input: height = [1,7,2,5,4,7,3,6]

Output: 36

'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
            
        return res