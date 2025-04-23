class Solution:
    def twoSum(self, numbers, target: int):
        l, r = 0, len(numbers) - 1
        while l < r:
            res = numbers[l] + numbers[r]
            if res > target:
                r -= 1
            elif res < target:
                l += 1
            else:
                return [l + 1,r + 1]
            
ans = Solution()
print(ans.twoSum([2,7,11,15], target = 9))