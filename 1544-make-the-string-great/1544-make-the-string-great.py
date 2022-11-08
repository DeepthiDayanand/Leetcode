class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for curr_char in (s):
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
                
            else:
                stack.append(curr_char)
                
        return "".join(stack)