class Solution {
    public int minJumps(int[] arr) {
        int steps=0;
        int  n=arr.length;
        HashMap<Integer,List<Integer>> graph = new HashMap<>();
        
        for(int i=0;i<arr.length;i++) {
            if(!graph.containsKey(arr[i])) {
                List<Integer> temp = new ArrayList<>();
                temp.add(i);
                graph.put(arr[i],temp);
            }
            
            else {
                List<Integer> temp = graph.get(arr[i]);
                temp.add(i);
                graph.put(arr[i],temp);
            }
        }
        
        boolean vis[] = new boolean[n];
        vis[0] = true;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        
        while(!queue.isEmpty()) {
            int size = queue.size();
            
            for(int i=0;i<size;i++) {
                int curridx=queue.poll();
                
                if(curridx == n-1)
                    return steps;
                
                List<Integer> jumptoindexes = graph.get(arr[curridx]);
                jumptoindexes.add(curridx + 1);
                jumptoindexes.add(curridx - 1);
                
                for(int q:jumptoindexes) {
                    if(q >= 0 && q < n && !vis[q]){
                        vis[q]=true;
                        queue.add(q);
                    }
                }
                jumptoindexes.clear();
            }
            steps++;
        }
        return -1;
    }
}