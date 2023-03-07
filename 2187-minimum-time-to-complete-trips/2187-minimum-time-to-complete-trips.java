class Solution {
    
    public boolean possible(int[] time, long givenTime, int totalTrips) {
        long actualTrips = 0;
        for (int t: time)
            actualTrips += givenTime/t;
        return actualTrips >= totalTrips;
    }
    public long minimumTime(int[] time, int totalTrips) {
        int maxTime = 0;
        for (int t: time)
            maxTime = Math.max(maxTime, t);
        
        long left = 1, right = (long) maxTime* totalTrips;
        
        while (left < right) {
            long mid = (left + right)/2;
            if (possible (time, mid, totalTrips))
                right = mid;
            else 
                left = mid + 1;
        }
        return left;
    }
}