class Solution:
	def binary_search(self, x):
		a = [1,2,3,4,8,5,6]
		a.sort()
		n = len(a)
		#x = int('desired number')
		left_index, right_index = 0, n-1
		while(left_index <= right_index):
			mid = (left_index + right_index) //2
			if a[mid] == x:
				return mid, True
			if a[mid] < x:
				left_index = mid + 1
			else:
				right_index = mid - 1
		return None
