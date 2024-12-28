'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

'''

# Approach 1: using sorting

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
    
    # T.C = O(nlogn)
    # SC = O(n)

# Approach 2: using Heap
    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Best Solution: using Heap 
            freq=Counter(nums)
            return[item for item,count in heapq.nlargest(k,freq.items(),key=lambda x:x[1])]
        
        Time Complexity: O(N + K log N)

# Counter(nums): O(N) to count frequencies
# heapq.nlargest(k): O(N log k) to build and maintain heap of size k
# List comprehension: O(k) to create final list
# Where N is the length of nums

# Space Complexity: O(N)

# Counter dictionary: O(N) for storing frequencies
# Heap: O(k) for maintaining k largest elements
# Output list: O(k)
# Total is O(N) since N ≥ k