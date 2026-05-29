class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force

        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        # return []

        # two pointer approach

        # since array is sorted incrementing left pointer increases sum, decrememting right reduces sum

        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r = r-1
            elif curSum < target:
                l = l+1
            else:
                return [l+1, r+1]
        
        return []