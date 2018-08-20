# -*- coding: utf-8 -*-
'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
def construct_tree(pre, mid):
    if len(pre) == 0 :
        return None
    root_data = pre[0]
    for i in range(0, len(mid)):
        if mid[i] == root_data:
            break  # 递归构造左子树和右子树
    left = construct_tree(pre[1 : 1 + i], mid[:i])
    right = construct_tree(pre[1 + i:], mid[i+1:])
    return TreeNode(root_data, left, right)
