# LC704 二分查找

## 题目链接
[LeetCode - 二分查找](https://leetcode.cn/problems/binary-search/description/)

## 题目描述
给定一个 n个**升序排列的整数数组** `nums` 和一个目标值 `target`，在数组中查找 `target`，如果存在返回其索引，否则返回 `-1`。

## 示例
输入：nums = [-1,0,3,5,9,12], target = 9  
输出：4

## 解题思路
- 通过二分查找法，初始化左右指针，找到中间元素并判断目标值与之比较
- 时间复杂度 O(log n)，空间复杂度 O(1)

## 代码实现
见 `LC704_binary_search.py`
