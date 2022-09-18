"""
XOR operatio can remove all the duplicates
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        for i in range(len(nums)+1):
            res ^= i
        return res

"""
prevSolution --->> sum approach
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        original = (len(nums) * (len(nums)+1))//2
        sum_num =  sum(nums)
        return original - sum_num
"""
        
"""
prevSolution -->>>>>
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return i+1
"""
