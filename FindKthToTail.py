# -*- coding: utf-8 -*-
#输入一个链表，输出该链表中倒数第k个结点。
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return head
        if k<=0:
            return ListNode(0).next
        pnode=head
       stack1=[]
    pnode=head
    stack1.append(pnode)
    while pnode.next:
        pnode=pnode.next
        stack1.append(pnode)
    if k<=len(stack1):
        return stack1[-k]
    else:
        return ListNode(0).next