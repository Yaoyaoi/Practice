# 剑指offer67题题解（牛客网）

## 二维数组中的查找
* 考点： 数组
* program ：[findd2array.py](findd2array.py)
* 题解
    * 使用c++一个个比都可以过得样子
    * python版本：
        * 用target比较每一行的最后一列的元素
        * 选择第一个比target大的行数
        * 对该行和该行以后的所有行用二分查找查找target

## 跳台阶
* 考点： 递归
* program ：[jumpfloor.py](jumpfloor.py)
* 题解：
    * 在python中使用递归会卡时间，java，c++可以过
    * 最终使用了动态规划完成了题目

## 从尾到头打印链表
* 考点：链表
* program ：[printlistfromtailtohead.py](printlistfromtailtohead.py)
* 题解：
    * 三种方法
        1. 将链表中的元素储存在列表中然后翻转列表
        2. 使用栈
        3. 递归

## 反转链表
* 考点： 代码的鲁棒性
* program ：[reverseList.py](reverseList.py)
* 题解：
    * 两种方法：
        1. 使用栈
        2. 用两个指针分别指向前一个节点和后一个节点，然后按顺序交换值：
            ```python
            prep = None
            nextp = None
            while pHead:
                nextp = pHead.next
                pHead.next = prep
                prep = pHead
                pHead = nextp
            ```

## 变态跳台阶
* 考点：贪心
* program ： [hentaijumpfloor.py ](hentaijumpfloor.py )
* 题解：
        