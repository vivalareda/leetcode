class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)-1
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i] == nums[j] :
                    return True
        return False
