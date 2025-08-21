# LC707设计链表

## 题目链接
见[LeetCode]`https://leetcode.cn/problems/design-linked-list/`

## 题目描述
你可以选择使用单链表或者双链表，设计并实现自己的链表。
单链表中的节点应该具备两个属性:`val`和`next`。`val`是当前节点的值，`next`是指向下一个节点的指针/引用。
如果是双向链表，则还需要属性`prev`以指示链表中的上一个节点。假设链表中的所有节点下标从`0`开始。
实现`MyLinkedList`类：

`MyLinkedList()`初始化`MyLinkedList`对象。
`int get(int index)`获取链表中下标为`index`的节点的值。如果下标无效，则返回`-1`。
`void addAtHead(int val)`将一个值为`val`的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
`void addAtTail(int val)`将一个值为`val`的节点追加到链表中作为链表的最后一个元素。
`void addAtIndex(int index, int val)`将一个值为`val`的节点插入到链表中下标为`index`的节点之前。如果`index`等于链表的长度，那么该节点会被追加到链表的末尾。如果`index`比长度更大，该节点将**不会插入**到链表中。
`void deleteAtIndex(int index)`如果下标有效，则删除链表中下标为`index`的节点。

## 示例
输入
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
输出
[null, null, null, null, 2, null, 3]

## 解题思路
 - 链表节点定义(定义ListNode)
    - `val=0`给节点的值`val`提供一个默认值。如果传入了具体值就会被赋值，如果没传入值，默认使用0，避免因缺少参数报错，让代码更灵活。
    - `next=None`给节点后继指针`next`提供默认值。如果传入后继节点，`next`指向传入的节点，如果没传入，`next`会默认是`None`，表示当前节点是"链尾"，后续暂时没有节点，符合链表初始化或单个节点的逻辑。
 - 关键操作
    - `get(index)`:从头节点开始遍历`index`步，如果越界返回`-1`。
    - `addAtHead(val)`:等价于`addAtHead(0,val)`。
    - `addAtTail(val)`:等价于`addAtTail(size,val)`。
    - `addAtIndex(index,val)`:如果`index`>`size`，不插入；如果`index`<=`0`，插入到头部；否则，找到前驱节点，在其后插入。
    - `deleteAtIndex(index)`:如果`index`越界，忽略；如果找到前驱节点，调整`next`指针跳过目标节点。
 - 技巧
    - 使用虚拟头节点简化插入/删除逻辑。
    - 用size来快速判断索引是否有效。

## 知识总结
 - 单链表：每个节点仅包含**1个指针**：next(指向下一个节点)。
    - 存在一个头指针(或虚拟头节点)，用于定位链表起点；无尾指针(需遍历到最后一个节点才能定位尾部，其`next`为`none`。
    - 每个节点仅存1个指针。
    - 仅需维护`next`指针，插入/删除时只需修改1个方向的指针，代码逻辑更简单。
 - 双链表：每个节点包含**2个指针**。
    - 通常同时维护"头指针"(dummyHead)和"尾指针"(dummyTail或直接用tail)，可直接定位链表两端；尾部节点的next为None，头部节点的prev为None。
    - 每个节点需存2个指针。
    - 需同时维护`next`和`prev`两个指针，插入/删除时需同步修改"前驱节点的`next`"和"后驱节点的`prev`"，代码逻辑更复杂。
 - `pred`和`prev`都指"前驱节点"(即当前节点的前一个节点)，区别为`pred`是临时变量，仅在特定操作(如添加/删除节点)中作为“桥梁”使用;`prev`更多见于双向链表的节点定义中，作为节点的固定属性(如`self.prev`)，用于永久保存前驱节点的引用。
