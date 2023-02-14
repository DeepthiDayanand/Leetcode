class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(max(len(a), len(b))):
            a_bit = int(a[i]) if i < len(a) else 0
            b_bit = int(b[i]) if i < len(b) else 0
            sum = a_bit + b_bit + carry
            result += str(sum % 2)
            carry = sum // 2
        if carry:
            result += str(carry)
        return result[::-1]