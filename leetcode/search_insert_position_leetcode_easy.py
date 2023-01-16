# https://leetcode.com/problems/search-insert-position/description/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def getPosition(nums, target):
            if target in nums:
                return nums.index(target) # returns 1st occurence of target using index()
            else:
                # modify nums list
                # sort nums list and find target using index()
                nums.append(target)
                return sorted(nums).index(target)
        
        # call the getPosition
        return getPosition(nums, target)









