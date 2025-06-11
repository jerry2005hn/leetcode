class Solution:
    def threeSum(self, nums):
        nums.sort()
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if target not in count:
                    continue
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res
ans = Solution()
print(ans.threeSum(nums = [-1,0,1,2,-1,-4]))