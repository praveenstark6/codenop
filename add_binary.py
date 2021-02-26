class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i = len(a)-1
        j = len(b)-1
        while carry or i >= 0 or j >= 0:
            total = carry 
            if i>=0: total += int(a[i])
            if j>=0: total += int(b[j])
            i -= 1
            j -= 1
            result.append(str(total%2))
            carry = total//2
        return "".join(result[::-1])
            
            
   
