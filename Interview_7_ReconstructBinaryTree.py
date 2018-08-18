# -*- coding:utf-8 -*-
"""重建二叉树"""
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如
输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,
1,5,3,8,6}，则重建二叉树并返回。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==len(tin)==None:
            return None
        return self.subConstructTree(pre,tin)

    def subConstructTree(self,pre,tin):
        root = TreeNode(pre[0])
        root_index_tin = None
        for i in range (len(tin)):
            if tin [i] == root.val:
                root_index_tin=i
        len_left=len(tin[:root_index_tin])
        len_right=len(tin[root_index_tin+1:])
        if len_left>0:
            left_tree_tin=tin[:root_index_tin]
            left_tree_pre=pre[1:len_left+1]
            root.left=self.subConstructTree(left_tree_pre,left_tree_tin)

        if len_right>0:
            right_tree_tin = tin[root_index_tin+1:]
            right_tree_pre = pre[len_left+1:]
            root.right=self.subConstructTree(right_tree_pre,right_tree_tin)

        return root






