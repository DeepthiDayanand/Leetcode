class Solution {
    public int strStr(String haystack, String needle) {
        
        int haystackLength = haystack.length();
        int needleLength = needle.length();
        
        if(haystackLength < needleLength)
            return -1;
        for(int i = 0; i <= haystack.length() - needle.length(); i++) {
            int j = 0;
            while(j < needle.length() && haystack.charAt(i+j)==needle.charAt(j))
                j++;
            if(j==needle.length()){
                return i;
            }
        }
        return -1;
    }
}

