#!/usr/bin/python3

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        map = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in map:
                return [map[target - num], i]
            map[num] = i
#        idx1 = 0
#        idx2 = 1
#
#        while (True):
#            if nums[idx1] + nums[idx2] == target:
#                return [idx1, idx2]
#            if idx2+1 < len(nums):
#                idx2 = idx2 + 1
#            else:
#                idx1 = idx1 + 1 
#                idx2 = idx1 + 1 

pino = Solution()

print(pino.twoSum([2,7,11,15],9))
print(pino.twoSum([3,2,4],6))
print(pino.twoSum([3,3],6))
