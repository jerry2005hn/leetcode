class Solution:
    def rankTeams(self, votes) -> str:
        d = {}

        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char] = [0] * len(vote) #create ranking array e.g 'A': [0, 0, 0]
                d[char][i] += 1 # if in array, +1 for the position

        voted_names = sorted(d.keys())
        return "".join(sorted(voted_names, key=lambda x: d[x], reverse=True))
        
ans = Solution()
print(ans.rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))