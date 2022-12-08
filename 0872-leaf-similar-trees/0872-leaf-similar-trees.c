/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

//note: int memcmp(const void *str1, const void *str2, size_t n)) compares the first n bytes of memory area str1 and memory area str2.


void traverse(struct TreeNode*root, int*tree, int*count) {
    if(!root->left && !root->right)
        tree[(*count)++] = root->val;
    else {
        if (root->left)
            traverse(root->left, tree, count);
        if (root->right)
            traverse(root->right, tree, count);
    }
}

bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2){
    
    int i, tree1[100], tree2[100];
    int size1 = 0, size2 = 0;
    
    traverse(root1, tree1, &size1); traverse (root2, tree2, &size2);
    
    return size1==size2 && !memcmp(tree1, tree2, size1*sizeof(int));
    

}