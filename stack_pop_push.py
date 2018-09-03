# -*- coding: utf-8 -*-
#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
stack1,stack2=[],[]
def push(node):
    stack1.append(node)
def pop(node):
    if len(stack2)!=0:
        return stack2.pop()
    elif len(self.stack1)!=0:
        while len(stack1):
            stack2.append(stack1.pop())
        return stack2.pop()
