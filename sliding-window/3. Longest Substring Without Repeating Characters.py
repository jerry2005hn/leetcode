class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        listChars = []
        res = 0
        for char in s:
            if char not in listChars:
                listChars.append(char)
                if res < len(listChars):
                    res = len(listChars)
            else:
                remove = listChars.index(char)
                listChars.append(char)
                listChars = listChars[remove+1:]
        return res