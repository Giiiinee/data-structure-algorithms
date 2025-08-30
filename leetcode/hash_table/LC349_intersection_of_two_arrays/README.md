# LC349两个数组
## 题目链接
[LeetCode](https://leetcode.cn/problems/intersection-of-two-arrays/)
## 题目描述
给定两个数组`nums1`和`nums2`，返回它们的**交集**。输出结果中的每个元素一定是**唯一**的。我们可以**不考虑输出结果的顺序**。
## 示例
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
## 解题思路
 - 哈希集合
 - 集合法
## 代码实现
见`LC349_intersection_of_two_arrays/solution.py`
## 知识总结
 - `table[num]`的作用是统计数组`nums1`中各元素出现的情况。
 - `dict.get(key,default)`是字典的方法，作用:根据`key`(这里是`num`)去字典里查找对应的值。如果`num`不在`table`中,返回指定的默认值(`default`)。如果`num`已经在`table`中存在,就返回它当前的"出现次数"。
 - `add`是集合`set`的内置方法,专门用于向集合中添加元素。如果添加的元素已经存在于集合中,集合不会有任何变化(**因为集合不允许重复元素**)。
 - `del table[num]`:删掉重复添加交集的元素，确保最终的交集结果中每个元素只出现一次。
 - 集合`add`确实能去重,但`del table[num]`是为了减少"判断元素是否存在"的次数,提升效率。
