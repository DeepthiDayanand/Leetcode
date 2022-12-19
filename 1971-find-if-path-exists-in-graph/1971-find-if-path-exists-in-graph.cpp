class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        
        queue<int> q;
        q.push(source);
        
        unordered_map<int, unordered_set<int>> neighbours;
        for(auto& edge : edges){
            neighbours[edge[0]].insert(edge[1]);
            neighbours[edge[1]].insert(edge[0]);
        }

        unordered_set<int> visited;   
        while(!q.empty()){

            int node = q.front();
            q.pop();

            visited.insert(node);

            if(node == destination) 
                return true;

            for(auto& neighbour : neighbours[node]){
                if(neighbour != node && visited.find(neighbour) == visited.end())
                    q.push(neighbour);
            }
        }
        return false;
    }
};