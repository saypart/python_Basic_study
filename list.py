nums = [[0,1],1,2]
nums2 = [4,5,7]


nums.append(3)
nums.remove(nums[0])
nums2.insert(2,6)

nums3 = nums+nums2


print(nums[:len(nums)])
print(nums+nums2)
print(nums.count(3))
print(nums.index(2))

nums3.sort(reverse=True)
print(nums3)

