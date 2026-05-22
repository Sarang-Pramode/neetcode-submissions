class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # hashmap = {}

        # for index,value in enumerate(nums):
        #     if value in hashmap.keys():
        #         return True
        #     else:
        #         hashmap[value] = index
        # return False 

        # set implementation

        return len(set(nums)) < len(nums)