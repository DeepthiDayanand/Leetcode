class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
            
                #store topLeft value
                topLeft = matrix[top][left + i]
                
                #move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                #move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                #move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                #move topLeft to top right
                matrix[top + i][right] = topLeft
            
            right -= 1
            left += 1
