# using binary search
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original = list(nums)
        nums.sort()
        start = l = 1 
        end = r = len(nums) - 1
        
        for i in range(end+1):
            # print(i)
            l = start
            while(l<=r):
                mid = (l + r) // 2
                res = nums[i] + nums[mid]
                # print(nums[l],nums[r],nums[mid],res)
                
                if res == target:
                    first_index = original.index(nums[i])
                    second_index = original.index(nums[mid])
                    if first_index != second_index:
                        return [first_index, second_index]
                    else:
                        first_index = original.index(nums[i])
                        second_index = original.index(nums[i], first_index+1)
                        return [first_index, second_index]
                
                elif res < target:
                    l = mid + 1
                else:
                    r = mid - 1
            start +=1
            r = end

"""
prev approach --> O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
"""
