# -*- coding: utf-8 -*-

class Node:
    def __init__(self,data,pnext=None):
        self.data=data
        self._next=pnext

    def __repr__(self):
        return str(self.data)

class LinkTable:
    def __init__(self):
        self.head=None
        self.length=0
    def is_empty(self):
        return (self.length==0)

    #增加一个节点(在链表尾添加): append()
    def append(self,dataOrNode):
        item=None
        if isinstance(dataOrNode,Node):
            item=dataOrNode
        else:
            item=Node(dataOrNode)
        if not self.head:
            self.head=item
            self.length+=1
        else:
            node=self.head
            while node._next:
                node=node._next
            node._next=item
            self.length+=1

        #删除一个节点: delete()
    def delete(self,index):
        if self.is_empty():
            print("this chain table is empty.")
            return
        if index<0 or index>=self.length:
            pring('error: out of index')
            return
        if index==0:
            self.head=self.head._next
            self.length-=1
            return
        j=0
        node=self.head
        prev=self.head
        while node._next and j<index:
            prev=node
            node=node._next
            j+=1
        if j==index:
            prev.next=node._next
            self.length-=1

    #修改一个节点: update()
    def update(self,index,data):
        if self.is_empty() or index<0 or index>=self.length:
            print('error: out of index')
            return
        j=0
        node=self.head
        while node._next and j<index:
            node=node._next
            j+=1
        if j==index:
            node.data=data
    #查找一个节点: getItem()
    def getItem(self,index):
        if self.is_empty() or index<0 or index>=self.length:
            print('error: out of index')
            return
        j=0
        node=self.head
        while node._next and j<index:
            node=node._next
            j+=1
        return node.data

    #查找一个节点的索引: getIndex()
    def getIndex(self,data):
        if self.is_empty():
            print("this chain table is empty")
            return
        j=0
        node=self.head
        while node:
            if node.data==data:
                return j
            node=node._next
            j+=1
        if j==self.length:
            print("%s not found" % str(data))
            return

    #插入一个节点: insert()
    def insert(self,index,dataOrNode):
        if self.is_empty():
            print("this chain tabale is empty")
            return
        if index<0 or index>=self.length:
            pring('error: out of index')
            return
        item=None
        if isinstance(dataOrNode,Node):
            item=dataOrNode
        else:
            item=Node(dataOrNode)
        if index==0:
            item._next=self.head
            self.head=item
            self.length+=1
            return
        j=0
        node=self.head
        prev=self.head
        while node._next and j<index:
            prev = node
            node = node._next
            j+=1
        if j==index:
            item._next =node
            prev._next=item
            self.length+=1

    def clear():
        self.head=None
        self.length=0
