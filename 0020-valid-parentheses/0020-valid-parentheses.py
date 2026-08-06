class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p= {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            if ch in p:      
                if not stack or stack[-1] != p[ch]:
                    return False
                stack.pop()
            else:              
                stack.append(ch)

        return len(stack) == 0
        