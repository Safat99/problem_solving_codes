frst_array = [4,9,5]
scnd_array = [9,4,9,8,4]
output = []
## output >>> [4,9]

frst_array.sort()
scnd_array.sort()
l = len(frst_array)
r = len(scnd_array)

##for 2nd array

for i in range(l):
    l_index, r_index = 0, r-1
    while(l_index<=r_index):
        mid = (l_index + r_index) // 2
        # print(scnd_array[mid])
        if frst_array[i] == scnd_array[mid]:
            output.append(frst_array[i])
            break
        if frst_array[i] < scnd_array[mid]:
            r_index = mid - 1
        else:
            l_index = mid + 1

print("the final output: ", output)