class Solution {
public:
    int climbStairs(int n) {
        int step1 = 0, step2 = 1, ans = 0, steps = 0;
        
        for(steps = 0; steps < n; steps++) {
            ans = step1 + step2;
            step1 = step2;
            step2 = ans;
        }
        return ans;
    }
};


// class Solution {
// public:
//     int climbStairs(int n) {
//         int first = 0, second = 1, result = 0, steps = 0;
//         while(steps < n) {
//             result = first + second;
//             first = second;
//             second = result;
//             steps++;
//         }
//         return result;
//     }
// };