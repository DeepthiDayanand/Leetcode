class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        row = [1] * n
        
        for i in range(m - 1):
            newRow = [1] * n
            #(n - 2 because n - 1 is wholly 1s, till the last element thats -1, moving in reverse order)
            for j in range(n - 2, -1, -1): 
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]