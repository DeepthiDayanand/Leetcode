class Solution {
    
    private void countingSort(int[] arr) {
        
        HashMap<Integer, Integer> frequency = new HashMap<>();
        int min = arr[0];
        int max = arr[0];
        
        for(int i = 0; i < arr.length; i++) {
            min = Math.min(min, arr[i]);
            max = Math.max(max, arr[i]);
            frequency.put(arr[i], frequency.getOrDefault(arr[i], 0) + 1);
        }
        
        int index = 0;
        
        for(int val = min; val <= max; val++) {
            while(frequency.getOrDefault(val, 0) > 0) {
                arr[index] = val;
                index += 1;
                frequency.put(val, frequency.get(val) - 1);
            }
        }
    }
    
    
    public int[] sortArray(int[] nums) {
        countingSort(nums);
        return nums;
    }
}