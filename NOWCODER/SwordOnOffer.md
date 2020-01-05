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
* program ：[step.py](step.py)
* 题解：
    * 在python中使用递归会卡时间，java，c++可以过
    * 最终使用了动态规划完成了题目