class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        alien_dictionary = {}
        
        for i, val in enumerate(order):
            alien_dictionary[val] = i
            
        for x in range(len(words) - 1):
            for y in range(len(words[x])):
                if y >= len(words[x+1]):
                    return False
                if words[x][y] != words[x+1][y]:
                    if alien_dictionary[words[x][y]] > alien_dictionary[words[x+1][y]]:
                        return False
                    break
        return True