class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        
        for i in range (numRows - 1):
            temp = [0] + res[-1] + [0] #append zeroes on either side of the prev row
            row = [] 
            
            for j in range(len(res[-1]) + 1): #length of the previous row + 1
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res
    
    
#time complexity O(n^2) could be optimized using math to O(n) maybe
