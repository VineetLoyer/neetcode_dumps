'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
   
        triplets = []

        for i in range(len(nums) - 2):
            # Skip the same element to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find the two numbers which sum to -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Move the left pointer to the right, skipping over duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to the left, skipping over duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return triplets