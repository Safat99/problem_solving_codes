class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = 0
        if len(nums) == 1:
            return 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                d +=1
            else:
                nums[i-d] = nums[i]
        
        print(nums)
        return len(nums) - d

## shamim's solution 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        id = 1
        prev_elem = nums[0]
        n = len(nums)
        if n == 1:
            return 1
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[id] = prev_elem = nums[i]
                id += 1
        
        return id


