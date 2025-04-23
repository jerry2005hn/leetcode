class Solution:
    def maxArea(self, height) -> int:
        res = 1
        l, r = 0, len(height) - 1
        while l < r:
            cur = (r - l) * min(height[l], height[r])
            res = max(res, cur)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

ans = Solution()
print(ans.maxArea(height = [1,8,6,2,5,4,8,3,7]))