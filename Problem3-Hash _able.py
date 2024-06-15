# Longest Substring Without Repeating Characters
# Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        j = 0
        r = 0
        passed = set()
        for i in range(n):
            while j < n and s[j] not in passed :
                passed.add(s[j])
                j+=1
            r = max(r,j-i)
            passed.remove(s[i])
        return r


        
