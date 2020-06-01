/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* invertTree(struct TreeNode* root){
    if(root==NULL){
        return;
    }
    else{
        struct Treenode* temp;
        invertTree(root->left);
        invertTree(root->right);
        temp=root->left;
        root->left=root->right;
        root->right=temp;
    }
   return root;
}
