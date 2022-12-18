class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        stack<int> s;
        vector<int> waittime(temp.size());
        
        for(int i = 0; i < temp.size(); i++) {
            while(!s.empty() && temp[i] > temp[s.top()]) 
                waittime[s.top()] = i - s.top(), s.pop();
            s.push(i);
        }
        return waittime; 
    }
};

