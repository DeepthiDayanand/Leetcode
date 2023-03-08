class Solution {
    private boolean canEat(int[] piles, int speed, int h) {
        int time = 0;
        for(int pile : piles){
            time += (pile - 1) / speed + 1;
            if(time > h)
                return false;
        }
        return true;
    }
    
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = Arrays.stream(piles).max().getAsInt();
        
        while(left < right) {
            int mid = (left + right)/2;
            if (canEat(piles, mid, h))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
}