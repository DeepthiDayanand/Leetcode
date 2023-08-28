class Solution:
    def reverseWords(self, s: str) -> str:
        
        string = s.split()[::-1]
        return(' '.join(string))
        
        
        
        
        
        
#         words = s.split(' ')
#         string = []
        
#         for word in words:
#             string.insert(0, word)
        
#         return " ".join(string)


        