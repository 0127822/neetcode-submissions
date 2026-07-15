class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # s : dict[int , int] = {}
        # for i , num in enumerate(nums):
        #     diff = target - num
        #     if diff in s:
        #         return [s[diff] , i]
        #     s[num]=i

        # return []

        diffs : dict[int , int] = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in diffs:
                return [diffs[diff],i]
            diffs[nums[i]] = i

        return []


        