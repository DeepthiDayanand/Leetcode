class Solution {
    Integer memo[][];
    
    public int minDistance(String word1, String word2) {
        memo = new Integer[word1.length() + 1][word2.length() + 1];
        return recurMinDistance(word1, word2, word1.length(), word2.length());
    }
    
    int recurMinDistance(String word1, String word2, int wordIndex1, int wordIndex2) {
        
        if(wordIndex1 == 0) {
            return wordIndex2; //add characters of word2; edit distance is the number of characters in word2
        }
        if(wordIndex2 == 0) {
            return wordIndex1; //delete all characters from word1; edit distance is the number of characters in word 1
        }
        if (memo[wordIndex1][wordIndex2] != null) {
            return memo[wordIndex1][wordIndex2];
        }
        
        int minEditDistance = 0;
        if(word1.charAt(wordIndex1 - 1) == word2.charAt(wordIndex2 - 1)){
            minEditDistance = recurMinDistance(word1, word2, wordIndex1 - 1, wordIndex2 - 1);
        }
        else {
            int insertOperation = recurMinDistance(word1, word2, wordIndex1, wordIndex2 - 1);
            int deleteOperation = recurMinDistance(word1, word2, wordIndex1 - 1, wordIndex2);
            int replaceOperation = recurMinDistance(word1, word2, wordIndex1 -1, wordIndex2 - 1);
            
            minEditDistance = Math.min(insertOperation, Math.min(deleteOperation, replaceOperation)) + 1; //+1 is to count the current operation.
        }
        memo[wordIndex1][wordIndex2] = minEditDistance;
        return minEditDistance;
    }
}

