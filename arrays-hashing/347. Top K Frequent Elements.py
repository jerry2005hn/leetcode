from collections import heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
ans = Solution()
print(ans.topKFrequent(nums = [1,1,1,2,2,3], k = 2)) 