class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sto={}
        for i in range(len(nums)):
            if nums[i] in sto:
                return True
        
            sto[nums[i]]=1
        return False

        