class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        if not s or not l:
            return 0
        return len(l[-1])
