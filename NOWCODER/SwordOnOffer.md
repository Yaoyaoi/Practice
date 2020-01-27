# 剑指offer67题题解（牛客网）

## 二维数组中的查找
* 考点： 数组
* program: [findd2array.py](findd2array.py)
* 题解
    * 使用c++一个个比都可以过得样子
    * python版本：
        * 用target比较每一行的最后一列的元素
        * 选择第一个比target大的行数
        * 对该行和该行以后的所有行用二分查找查找target

## 跳台阶
* 考点： 递归
* program: [jumpfloor.py](jumpfloor.py)
* 题解：
    * 在python中使用递归会卡时间，java，c++可以过
    * 最终使用了动态规划完成了题目

## 斐波那契数列
* 递归
* program: [jumpfloor.py](jumpfloor.py)
* 题解：同跳台阶

## 矩形覆盖
考点：递归
* program：[jumpfloor.py](jumpfloor.py)
* 题解：同跳台阶

## 从尾到头打印链表
* 考点：链表
* program: [printlistfromtailtohead.py](printlistfromtailtohead.py)
* 题解：
    * 三种方法
        1. 将链表中的元素储存在列表中然后翻转列表
        2. 使用栈
        3. 递归

## 反转链表
* 考点： 代码的鲁棒性
* program: [reverseList.py](reverseList.py)
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
* program: [hentaijumpfloor.py ](hentaijumpfloor.py )
* 题解：
    * $f(n) = 2^{n-1}$

## 重建二叉树
* 考点：树
* program: [reConstructBinaryTree.py](reConstructBinaryTree.py)
* 题解：
    * 树的基本知识 使用了递归的方法
    * 代码中还实现了对树的后序遍历

## 两个栈实现队列
* 考点：队列 栈
* program: [queueOfTwoStacks.py](queueOfTwoStacks.py)
* 题解：
    * 存：
        1. 每一次将栈2中的数字取出存进栈1
        2. 将存入的数字存进栈2
        3. 将栈1的数字取出存进栈1
    * 取：
        * 从栈2中取数字

## 翻转数组的最小数字
* 考点：查找
* program: [rotateArray.py](rotateArray.py)
* 题解：
    * 类似于二分查找
        * 如果是递增序列 i移到mid+1
        * 如果是递减序列 j移到mid
        * 如果是相等的 无法判断，缩小检测范围 i++

## 替换空格
* 考点：字符串
* program: [replaceSpace.py](replaceSpace.py)
* 题解: 
    * 利用python自己的函数 string.replace(' ','%20')
    * 遍历一遍 

## 数值的整数次方
* 考点：数学
* program: [power.py](power.py)
* 题解：
    * 如果直接乘的话会卡时间（python，C++）
    * 可以考虑先计算 base 的 2n 次幂 （令2n < exponent）
    * 位运算

## 合并两个排序的链表
* 考点：链表
* program: [mergelist.py](mergelist.py)
* 题解：两种方法：
    * 用归并排序的方法写
    * 递归

## 调整数组顺序使奇数位于偶数前面
* 考点：数组
* program: [reOrderArray.py](reOrderArray.py)
* 题解：
    * 另外开两个数组，遍历原数组，将奇数偶数分别储存在两个数组中，最后再将偶数数组放在技术数组后面
    * 冒泡排序的方法，将偶数后移
    * 如果不需要保证奇数与奇数间顺序不变，偶数与偶数间顺序不变可以用快排的方法来实现

## 链表中倒数第k个结点
* 考点：链表
* program: [findKthToTail.py](findKthToTail.py)
* 题解:
    * 方法1.遍历一遍得到链表的长度，再遍历一遍取第length-k节点
    * 方法2.用栈储存节点，在依次弹出，取第k个节点
    * 方法3.快慢指针，快指针起始在第k+1个元素，慢指针在第一个元素，两个指针同时后移，当快指针为none时，慢指针指向倒数第k个元素

## 二进制中1的个数
* 考点：进制转换 补码原码反码
* program: [numberof1.py](numberof1.py)
* 题解：
    * 方法1. 一个一个数
    * 方法2. 移动1 而不是移动数字
    * 方法3 最佳解法：
        > 链接：https://www.nowcoder.com/questionTerminal/8ee967e43c2c4ec193b040ea7fbb10b8?f=discussion
        来源：牛客网
        如果一个整数不为0，那么这个整数至少有一位是1。如果我们把这个整数减1，那么原来处在整数最右边的1就会变为0，原来在1后面的所有的0都会变成1(如果最右边的1后面还有0的话)。其余所有位将不会受到影响。
        举个例子：一个二进制数1100，从右边数起第三位是处于最右边的一个1。减去1后，第三位变成0，它后面的两位0变成了1，而前面的1保持不变，因此得到的结果是1011.我们发现减1的结果是把最右边的一个1开始的所有位都取反了。这个时候如果我们再把原来的整数和减去1之后的结果做与运算，从原来整数最右边一个1那一位开始所有位都会变成0。如1100&1011=1000.也就是说，把一个整数减去1，再和原整数做与运算，会把该整数最右边一个1变成0.那么一个整数的二进制有多少个1，就可以进行多少次这样的操作。

## 树的子结构
* 考点：二叉树
* program: [subtree.py](subtree.py)
* 题解：
    * 使用了递归，对二叉树进行前序遍历。如果treeA的节点等于 treeB的根节点，怎检测是否等于treeB
    如果 treeA的节点不等于treeB的根节点则分别检测左子树和右子树是否包含treeB

## 二叉树的镜像
* 考点：树
* program: [mirrorTree.py](mirrorTree.py)
* 题解:
    * 交换树的左子树和右子树，对左子树和右子树递归调用该方法

## 顺时针打印矩阵
* 考点：数组
* program: [printMatrix.py](printMatrix.py)
* 题解：
    * 方法一：定义四个边界变量up，down，left，right，循环收缩矩阵的边界
    * 方法二：将第一行读入数组中 并移除第一行，顺时针旋转矩阵，重复上述步骤直到数组为空
    * 方法三：标记数组

## 包含min函数的栈
* 考点：栈
* program:[minStack.py](minStack.py)
* 题解：
    * 方法一： 增加一个数组，以从小到大的方式排序栈中的数字。push时插入排序；pop时去掉该数字的第一个匹配项；min函数返回该数组第一个值 空间复杂度o(n)
    * 方法二： 辅助栈，记录曾经的最小值，pop时比较两个栈的栈顶元素，如果相等，两个栈都要pop(better) 空间复杂度 <= o(n)
    * 方法三： 压缩还原法，栈中储存当前值和最小值的差值， 用额外的变量min记录当前最小值 空间复杂度o(1)