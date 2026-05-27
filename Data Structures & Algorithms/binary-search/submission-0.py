class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # implement binary search

        l, r = 0, len(nums) - 1
        

        while l <= r:

            # (l + r) // 2 can lead to overflow
            mid = l + ((r - l) // 2)

            if nums[mid] < target:
                # search left array
                l = mid + 1

            elif nums[mid] > target:
                # search the right array
                r = mid - 1
            
            else:
                return mid

        return -1