/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pathDiff(TreeNode* root, int max_value, int min_value) {
        if(root == NULL)
            return max_value - min_value;
            
        max_value = max(max_value, root->val);
        min_value = min(min_value, root->val);
        
        int left = pathDiff(root->left, max_value, min_value);
        int right = pathDiff(root->right, max_value, min_value);
        
        return max(left, right);
    }
    
    int maxAncestorDiff(TreeNode* root) {
        return pathDiff(root, root->val, root->val);
    }
};

