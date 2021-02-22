from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mag_count = Counter(magazine)
        ransom_count = Counter(ransomNote)
        
        for c in ransom_count:
            if c not in mag_count or mag_count[c] < ransom_count[c]:
                return False
            
        return True
    
