# m and n can be used as two pointers
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        if n==0:
            return nums1
        elif m==0:
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1
        
        for i in range(last, -1, -1):
            # print(m,n)
            if m>0 and n>0:
                if nums1[m-1] <= nums2[n-1]:
                    nums1[i] = nums2[n-1]
                    n -=1
                else:
                    nums1[i] = nums1[m-1]
                    m -=1
                continue
            print(m,n)
            
            if m == 0:
                nums1[i] = nums2[n-1]
                n -= 1
            elif n == 0:
                nums1[i] = nums1[m-1]
                m -= 1




# prev Solution -->> this is not quite optimal cause at the last we are sorting again..which takes nlog(n) 
# where the problem can be solved with O(n)

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         # """
#         # Do not return anything, modify nums1 in-place instead.
#         # """
#         left_pointer = 0
#         for i in range(m,m+n):
#             nums1[i] = nums2[left_pointer]
#             left_pointer +=1
#         nums1.sort()

