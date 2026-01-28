from typing import  List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        max = len(nums) -1
        min = 0
        while(True):
            middle = (max - min + 1) // 2 
            print(f"{min=} {max=} {middle=}")
            if nums[middle]  == target:
                return middle
            if max - min == 0:
                return min

            if nums[middle] < target:
                min = middle
            else:
                max = middle
            
            i += 1
        return -1

s = Solution()
r = s.searchInsert([1,2,3,4,6],5)
print(r)
