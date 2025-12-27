class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            find = target - num
            if find in num_dict:
                return [i,num_dict[find]]
            num_dict[num] = i
