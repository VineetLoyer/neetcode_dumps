'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''

#Solution 1 : Brute force using sorting  
# idea : we sort each string and pair them , since the output is a nested list we will use defaultdict(list)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict=defaultdict(list) #creates a special dict that automatically creates an empty list when we acess new key
        for s in strs:
            sorteds=''.join(sorted(s)) #sorts each string
            ana_dict[sorteds].append(s) # append the original string in list as value, and key is sorted string
        return list(ana_dict.values()) #returns all anagram pairs.
#T.c = O(m*nlogn)
#S.c = O(m*n)

#SOlution 2: using hash table
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# Processing "cat":
# count = [1,0,1,0,...,1,0] (a=1, c=1, t=1)
# ana_dict = {(1,0,1,0,...,1,0): ["cat"]}

# Processing "act":
# count = [1,0,1,0,...,1,0] (same as "cat")
# ana_dict = {(1,0,1,0,...,1,0): ["cat", "act"]}

# Processing "dog":
# count = [0,0,0,1,...,0,0] (different pattern)
# ana_dict = {
#   (1,0,1,0,...,1,0): ["cat", "act"],
#   (0,0,0,1,...,0,0): ["dog"]
# }
# T.C = O(m*n)
# S.c = O(m)