class Solution:
    def isValid(self, s: str) -> bool:
        # append , pop
        stack = []
        match = { '(': ')', '[': ']', '{':  '}'}
        
        
        for brace in s:
            if brace in match:
                stack.append(brace)
            else:
                if not stack or match[stack.pop()] != brace:
                    return False
        return not stack 
