# -*- coding: utf-8 -*-
#遍历二叉树A，定位B的根节点在A中的可能位置——> 定位后，验证B是不是A当前位置的子结构。
#输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False

        result = False
        if pRoot1.val == pRoot2.val:
            result = self.isSubtree(pRoot1, pRoot2)
        if result == False:
            result = self.HasSubtree(pRoot1.left, pRoot2) | self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def isSubtree(self, root1, root2):
        if root2 == None:
            return True
        if root1 == None:
            return False
        if root1.val == root2.val:
            return self.isSubtree(root1.left, root2.left) & self.isSubtree(root1.right, root2.right)
        return False