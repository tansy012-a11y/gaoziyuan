# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:17:55 2026

@author: Administrator
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None  # 头节点初始为空

    # 在尾部添加节点
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    # =====================删除指定值的节点 =====================
    def delete_by_value(self, target):
        # 情况1：链表为空
        if not self.head:
            return
        
        # 情况2：要删除的是头节点
        if self.head.val == target:
            self.head = self.head.next
            return
        
        # 情况3：找前驱节点
        cur = self.head
        while cur.next and cur.next.val != target:
            cur = cur.next
        
        # 找到则删除
        if cur.next:
            cur.next = cur.next.next

    # 打印链表
    def print_list(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        print(" -> ".join(res) + " -> None")



if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print("原链表：")
    ll.print_list()

    ll.delete_by_value(3)
    print("\n删除值为 3 后：")
    ll.print_list()

    ll.delete_by_value(1)
    print("\n删除头节点 1 后：")
    ll.print_list()
