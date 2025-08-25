# LC24两两交换链表中的节点
## 题目链接
[LeetCode](https://leetcode.cn/problems/swap-nodes-in-pairs/)
## 题目描述
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
## 示例
输入：head = [1,2,3,4]
输出：[2,1,4,3]
## 解题思路
 - 虚拟头节点
 - 指针调整
## 代码实现
见`LC24_swap_nodes_in_pairs/solution.py`
## 知识总结
 - 临时变量`temp`:保持交换节点及后续节点，防止指针调整时丢失节点引用。
 - ListNode类:其本质为链表节点的"构造蓝图",`ListNode`类就是用代码定义了这种"节点构造"。
 - `dummy_head=ListNode()`:从`ListNode`类中建出实例对象`dummy_head`。
 - "类"和"实例"的关系:
    - `ListNode`是一个类("节点的设计图纸")，定义了节点该有什么属性(`val`值、`next`指针),但本身不是一个具体的节点。
    - `ListNode()`是调用这个类的"构造方法",根据"图纸"创建出一个具体的节点实例(比如一个`val=0`、`next=None`的空节点)。
    - `dummy_head=ListNode()`就是把这个"具体的空节点"赋值给变量`dummy_head`,此时`dummy_head`才是一个实际用的"虚拟头节点"。
 - 循环条件:`cur.next`和`cur.next.next`必须同时存在(链表长度为奇偶两种情况)。
 - `cur.next.next`条件必须放在`cur.next`后面,因为如果当`cur.next`为空时,就是对空指针取值了，会报空指针异常。
