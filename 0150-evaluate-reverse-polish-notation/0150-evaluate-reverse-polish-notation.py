class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {"+" : add, "-" : sub, "*" : mul, "/" : truediv}
        s = []
        
        for t in tokens:
            if t in operators:
                b, a = s.pop(), s.pop()
                t = operators[t](a, b)
            s.append(int(t))
            
        return s[-1]
