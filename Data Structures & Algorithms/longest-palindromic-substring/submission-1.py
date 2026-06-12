class Solution:
   

    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        res = ''
        for i in range(len(s)):
        # Case 1: center is at i (e.g., 'aba')
            p1 = expand(i, i)
            p2 = expand(i, i + 1)
            for candidate in [p1, p2]:
                if len(candidate) > len(res):
                    res = candidate
        return res

