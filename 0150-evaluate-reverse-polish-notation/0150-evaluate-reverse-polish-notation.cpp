class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        long a, b;
        
        for(auto t: tokens) {
            if (t == "+" or t == "-" or t == "*" or t == "/") {
                b = s.top(); s.pop();
                a = s.top(); s.pop();
                if(t == "+") 
                    s.push(a + b);
                else if(t == "-")
                    s.push(a - b);
                else if(t == "*")
                    s.push(a*b);
                else
                    s.push(a/b);
            }
            else s.push(stoi(t));
        }
        return s.top();
    }
};

