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
    int max_path = INT_MIN;
    
    int subtree(TreeNode * root) {
        if (root == NULL)
            return 0;
        int leftST = subtree(root->left);
        int rightST = subtree(root->right);
        max_path = max(max_path, leftST + rightST + root->val);
        return max({leftST + root->val, rightST + root->val, 0});
    }
    
    int maxPathSum(TreeNode* root) {
        subtree(root);
        return max_path;
    }
};
