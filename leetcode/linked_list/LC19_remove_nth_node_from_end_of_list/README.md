# LC19删除链表的倒数第n个结点
## 题目链接
[LeetCode](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)
## 题目描述
给你一个链表，删除链表的倒数第`n`个结点，并且返回链表的头结点。
## 示例
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
## 解题思路
 - 快慢指针:让`fast`**先走`n+1`**步，保证`fast`和`slow`相差`n+1`,之后一起走,当`fast`停在`None`时,`slow`刚好停在**待删节点的前一个**。
 - 复杂度:时间复杂度O(n),空间复杂度O(1)。
## 代码实现
见`LC19_/remove_nth_node_from_end_of_list/solution.py`
## 知识总结
 - `ListNode(val,head)`意味着`dummy_head`指向原来的`head`,链表连接起来才是完整的,`ListNode(val,None)`、`ListNode(val)`、`ListNode()`意味着创建的"孤立"的节点,还没有和链表连接。
