class Solution(object):
    def searchInsert(self, nums, target):
        count =0
        for i in range(len(nums)):
            count+=1
            if nums[i] == target:
                return count-1

            elif i < len(nums) - 1 and (target > nums[i] and target < nums[i+1]): 
                return i+1
                    
            elif i == len(nums) - 1 and target > nums[i]:
                return len(nums)
            

        return 0
