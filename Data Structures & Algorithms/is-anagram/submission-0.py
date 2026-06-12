class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_chars = sorted(list(s))
        second_chars = sorted(list(t))
        return first_chars == second_chars
