class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s : dict[int , int] = {}
        for i , num in enumerate(nums):
            diff = target - num
            if diff in s:
                return [s[diff] , i]
            s[num]=i

        return []


        