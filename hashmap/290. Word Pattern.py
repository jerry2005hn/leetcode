class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(" ")):
            return False
        p_map = {}
        s_map = {}
        for i in range(len(s.split(" "))):
            if s.split(" ")[i] not in s_map:
                s_map[s.split(" ")[i]] = pattern[i]
            if pattern[i] not in p_map:
                p_map[pattern[i]] = s.split(" ")[i]
            if s_map[s.split(" ")[i]] != pattern[i] or p_map[pattern[i]] != s.split(" ")[i]:
                return False
        return True
ans = Solution()
print(ans.wordPattern("abba", "dog cat cat dog"))
print(ans.wordPattern("aaaa", "dog cat cat dog"))
print(ans.wordPattern("aba", "cat cat cat dog"))
print(ans.wordPattern("aba", "dog cat cat"))