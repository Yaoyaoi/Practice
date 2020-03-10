## 剑指offer67题题解（牛客网）
### 需要复习的题目
* 二叉树的遍历
    * <a href="#tree1">二叉搜索树的后序遍历序列</a>（二叉搜索树的定义
    * <a href="#tree2">二叉树中和为某一值的路径</a>（深度优先遍历
* 字符串
    * <a href="#string1">字符串的排列</a>（字典序全排列
* 数组
    * <a href="#list1">数组中出现次数超过一半的数字</a>
    * <a href="#list2">最小的K个数</a>
* 栈
    * <a href="#stack1">栈的压入、弹出序列</a>
* 链表
    * <a href="#linklist1">复杂链表的复制</a>
* 其他
    * <a href="#other1">孩子们的游戏（最终胜利者）</a>
    * <a href="#other2">丑数</a> 

### 二维数组中的查找
* 考点： 数组
* program: [findd2array.py](findd2array.py)
* 题解
    * 使用c++一个个比都可以过得样子
    * python版本：
        * 用target比较每一行的最后一列的元素
        * 选择第一个比target大的行数
        * 对该行和该行以后的所有行用二分查找查找target

### 跳台阶
* 考点： 递归
* program: [jumpfloor.py](jumpfloor.py)
* 题解：
    * 在python中使用递归会卡时间，java，c++可以过
    * 最终使用了动态规划完成了题目

### 斐波那契数列
* 递归
* program: [jumpfloor.py](jumpfloor.py)
* 题解：同跳台阶

### 矩形覆盖
考点：递归
* program：[jumpfloor.py](jumpfloor.py)
* 题解：同跳台阶

### 从尾到头打印链表
* 考点：链表
* program: [printlistfromtailtohead.py](printlistfromtailtohead.py)
* 题解：
    * 三种方法
        1. 将链表中的元素储存在列表中然后翻转列表
        2. 使用栈
        3. 递归

### 反转链表
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

### 变态跳台阶
* 考点：贪心
* program: [hentaijumpfloor.py ](hentaijumpfloor.py )
* 题解：
    * $f(n) = 2^{n-1}$

### 重建二叉树
* 考点：树
* program: [reConstructBinaryTree.py](reConstructBinaryTree.py)
* 题解：
    * 树的基本知识 使用了递归的方法
    * 代码中还实现了对树的后序遍历

### 两个栈实现队列
* 考点：队列 栈
* program: [queueOfTwoStacks.py](queueOfTwoStacks.py)
* 题解：
    * 存：
        1. 每一次将栈2中的数字取出存进栈1
        2. 将存入的数字存进栈2
        3. 将栈1的数字取出存进栈1
    * 取：
        * 从栈2中取数字

### 翻转数组的最小数字
* 考点：查找
* program: [rotateArray.py](rotateArray.py)
* 题解：
    * 类似于二分查找
        * 如果是递增序列 i移到mid+1
        * 如果是递减序列 j移到mid
        * 如果是相等的 无法判断，缩小检测范围 i++

### 替换空格
* 考点：字符串
* program: [replaceSpace.py](replaceSpace.py)
* 题解: 
    * 利用python自己的函数 string.replace(' ','%20')
    * 遍历一遍 

### 数值的整数次方
* 考点：数学
* program: [power.py](power.py)
* 题解：
    * 如果直接乘的话会卡时间（python，C++）
    * 可以考虑先计算 base 的 2n 次幂 （令2n < exponent）
    * 位运算

### 合并两个排序的链表
* 考点：链表
* program: [mergelist.py](mergelist.py)
* 题解：两种方法：
    * 用归并排序的方法写
    * 递归

### 调整数组顺序使奇数位于偶数前面
* 考点：数组
* program: [reOrderArray.py](reOrderArray.py)
* 题解：
    * 另外开两个数组，遍历原数组，将奇数偶数分别储存在两个数组中，最后再将偶数数组放在技术数组后面
    * 冒泡排序的方法，将偶数后移
    * 如果不需要保证奇数与奇数间顺序不变，偶数与偶数间顺序不变可以用快排的方法来实现

### 链表中倒数第k个结点
* 考点：链表
* program: [findKthToTail.py](findKthToTail.py)
* 题解:
    * 方法1.遍历一遍得到链表的长度，再遍历一遍取第length-k节点
    * 方法2.用栈储存节点，在依次弹出，取第k个节点
    * 方法3.快慢指针，快指针起始在第k+1个元素，慢指针在第一个元素，两个指针同时后移，当快指针为none时，慢指针指向倒数第k个元素

### 二进制中1的个数
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

### 树的子结构
* 考点：二叉树
* program: [subtree.py](subtree.py)
* 题解：
    * 使用了递归，对二叉树进行前序遍历。如果treeA的节点等于 treeB的根节点，怎检测是否等于treeB
    如果 treeA的节点不等于treeB的根节点则分别检测左子树和右子树是否包含treeB

### 二叉树的镜像
* 考点：树
* program: [mirrorTree.py](mirrorTree.py)
* 题解:
    * 交换树的左子树和右子树，对左子树和右子树递归调用该方法

### 顺时针打印矩阵
* 考点：数组
* program: [printMatrix.py](printMatrix.py)
* 题解：
    * 方法一：定义四个边界变量up，down，left，right，循环收缩矩阵的边界
    * 方法二：将第一行读入数组中 并移除第一行，顺时针旋转矩阵，重复上述步骤直到数组为空
    * 方法三：标记数组

### 包含min函数的栈
* 考点：栈
* program:[minStack.py](minStack.py)
* 题解：
    * 方法一： 增加一个数组，以从小到大的方式排序栈中的数字。push时插入排序；pop时去掉该数字的第一个匹配项；min函数返回该数组第一个值 空间复杂度o(n)
    * 方法二： 辅助栈，记录曾经的最小值，pop时比较两个栈的栈顶元素，如果相等，两个栈都要pop(better) 空间复杂度 <= o(n)
    * 方法三： 压缩还原法，栈中储存当前值和最小值的差值， 用额外的变量min记录当前最小值 空间复杂度o(1)

### <a id="stack1">栈的压入、弹出序列</a>
* 考点：栈
* program:[popOrder.py](popOrder.py)
* 题解：
    * 新建一个栈，依次将数组pushV压入栈中，每次压入时，访问数组popV，当栈顶元素等于数组popV中的元素时，就将其出栈，并访问数组popV的下一个元素。当循环结束时，判断栈是否为空，若为空则返回true.


### 从上往下打印二叉树
* 考点：队列，树
* program:[printTree.py](printTree.py)
* 题解：
    * 方法一：× 用队列来储存树的每一层，下一层的节点则是该层的节点的子节点。
    * 方法二： 
        1. 将根节点加入队列
        2. 弹出队列的首节点 并把该节点的左子节点和右子节点先后加入队列，将该节点储存在列表中
        3. 重复2直到队列为空

### <a id="tree1">二叉搜索树的后序遍历序列</a>
* 考点：举例让抽象具体化
* 知识点：栈，树（二叉搜索树）
* program:[VerifySquenceOfBST.py](VerifySquenceOfBST.py)
* 题解：
    * 递归分割法

### <a id="tree2">二叉树中和为某一值的路径</a>
* 考点：举例让抽象具体化
* 知识点：二叉树
* program:[findPath.py](findPath.py)
* 题解：
    * 方法一：寻找当前节点node,和为a的路径 = 寻找子节点和为a-node.val的路径。递归地去寻找路径，最后排序
    * 方法二：递归地遍历所有的路径，记录和为a的路径，最后排序 (用递归与非递归两种方法实现遍历树的路径)
             ps: 递归实现时树的路径保存在栈中 ; 递归实现时可以全局保存，或作为参数传进函数中

### <a id="linklist1">复杂链表的复制</a>
* 考点：分解让复杂问题简单
* 知识点：链表
* program:[cloneList.py](cloneList.py)
* 题解：
    * 最佳方法：
        1. 复制每一个节点并插入到原来的节点后面
        2. 复制每个节点的random 到复制的节点中
        3. 分裂成两个链表
    * 方法二：（写起来比最佳方法简单，但是改变了原链表，失去了‘复制’的本意，但可以过题
        1. 复制链表，复制后的节点的random指向原节点的random（原链表中的节点），并使原链表的random指向复制的节点，
        2. 使复制的节点的random = random.random(即指向新链表中的对应节点)

### 二叉搜索树与双向链表
* 考点：分解让复杂问题简单
* 知识点：链表，二叉树
* program:[convertTree2List.py](convertTree2List.py)
* 题解：
    * 方法一：中序遍历二叉树并将节点储存在数组中，遍历数组改变指针
    * 方法二：中序遍历二叉树，递归函数传入父节点作为before/after,返回以该节点为根节点的树的最小节点和最大节点；
            如果该节点有左子树，则该节点的前一个节点为左子树的最大节点；该树的最小节点为左子树的最小节点
            如果该节点有右子树，则该节点的后一个节点为右子树的最小节点；该树的最右节点为右子树的最大节点
    * 方法三：
>        链接：https://www.nowcoder.com/questionTerminal/947f6eb80d944a84850b0538bf0ec3a5?f=discussion&toCommentId=5255549
>        1. 明确Convert函数的功能。
>            输入：输入一个二叉搜索树的根节点。
>            过程：将其转化为一个有序的双向链表。
>            输出：返回该链表的头节点。
>        2. 明确成员变量pLast的功能。
>            pLast用于记录当前链表的末尾节点。
>        3. 明确递归过程。
>            递归的过程就相当于按照中序遍历，将整个树分解成了无数的小树，然后将他们分别转化成了一小段一小段的双向链表。再利用pLast记录总的链表的末尾，然后将这些小段链表一个接一个地加到末尾。

### <a id="string1">字符串的排列</a>
* 考点：分解让复杂问题简单
* 知识点：字符串 动态规划 递归 全排列算法
* program: [permutation.py](permutation.py)
* 题解：
    * 方法一： 递归法：分别将每个位置交换到最前面位，之后全排列剩下的位。（相同的字符不交换）(由于不是字典序，没有AC) 
    * 方法二：字典序法：
>       https://www.cnblogs.com/pmars/archive/2013/12/04/3458289.html
> 设P是[1,n]的一个全排列。
> P=P1P2…Pn=P1P2…Pj-1PjPj+1…Pk-1PkPk+1…Pn
> find: j=max{i|Pi<Pi+1} k=max{i|Pi>Pj}
>1，  对换Pj，Pk，
>2，  将Pj+1…Pk-1PjPk+1…Pn翻转
> P’= P1P2…Pj-1PkPn…Pk+1PjPk-1…Pj+1即P的下一个

### <a id="list1">数组中出现次数超过一半的数字</a>
* 考点：时间效率
* 知识点： 数组 数组中任意第K大的数字 
* program: [moreThanhalfnum.py](moreThanhalfnum.py)
* 题解：
    * 方法一： o(nlogn) 排序法： 将数组排序，符合条件的值只可能是数组最中间的值，计算该值出现的次数，判断是否符合条件
    * 方法二：o(n) ‘打擂’法：如果一个数在数组中超过了半数说明它比其他数出现的次数的和还多
        * 记录两个值 host（擂主，和count（受擂成功次数
        * 如果当前值 == host count += 1 ，else，count-=1
        * 如果count == 0，换擂主 host = 当前值，count = 1
        * 遍历一遍数组，如果一个数超过了半数，它一定是擂主
        * 再遍历一遍数组计算host出现的次数，如果大于数组长度的一半则满足条件

### <a id="list2">最小的K个数</a>
* 考点：时间效率
* 知识点：数组  partition（快排） 堆
* program: [GetKLeastNumbers.py](GetKLeastNumbers.py)     [GetLeastKNumbers.java](GetLeastKNumbers.java)
* 题解：
    * 方法一：o(nlogk) 用数组前k个元素建立k个节点最大堆。后面的元素如果比堆顶大，则将对顶设为该元素，对顶siftdown   （最后的数组没排序）
    * 方法二：最好情况o(n) 最坏情况o($n^2$) 利用patition的思想

### 矩阵中的路径
* 考点：回溯法
* 知识点：回溯法
* program: [findPath.py](findPath.py)
* 题解： 用一个额外的数组标记是否有走过该格子，对于等于字符串首字母的字符 ，递归的确定周围四格有没有下一个字符。

### 剪绳子
* 考点：贪心，动态规划
* 知识点：贪心，动态规划
* program: [cutRope.py](cutRope.py)
* 题解：
    1. 方法一： 动态规划 时间o($n^2$) 空间o(n)
        1. 按顺序计算并存储从0到number每一个数的m值。
        2. 对于长度为n 的绳子来说，f(n) = max(max(f(i),i)+ max(f(n-i),n-i)) i~(1,n//2)
    2. 方法二： 贪心 
        1. 将n分为最多可能的长度为3的小段。
        2. 如果剩下长度1 则最后4m 分成2*2m的小段

### 滑动窗口的最大值
* 考点：栈和队列
* 知识点： 数组 队列
* program: [maxInWindows.py](maxInWindows.py)
* 题解：双端队列：循环访问数组： 队列首为最大值的下标，如果队最大值过期则从前面推出，每次在插入当前值之前将比当前值小的值都从后面推出队列。

### 连续子数组的最大和
* 考点：时间效率
* 知识点：动态规划
* program: [FindGreatestSumofSubArray.py](FindGreatestSumofSubArray.py)
* 题解：动态规划，循环访问数组， 到当前值的连续序列最大值 等于 前一个值的连续最大值加上当前值。

### <a id="other1">孩子们的游戏(最终胜利者)</a>
* 考点：抽象建模能力
* 知识点：链表，数学
* program: [Remain.py](Remain.py)
* 题解：
    * 方法一：循环链表模拟
    * 方法二：数学公式法
    链接：https://www.nowcoder.com/questionTerminal/f78a359491e64a50bce2d89cff857eb6?f=discussion
来源：牛客网
使用动态规划。我们注意到，输入的序列在删除一个元素后，序列的长度会改变，如果索引
在被删除的元素位置开始计算，那么每删除一个元素，序列的长度减一而索引会完全改变。
如果能找到改变前的索引和新索引的对应关系，那么该问题就容易解决了。
我们定义一个函数f(n, m)，表示每次在n个数字0,1,2,3,…,n-1中每次删除第m个数字后剩下
的数字。那么第一个被删除的数字的索引是(m-1)%n。删除该索引元素后，剩下的n-1个数字
为0,1,2,…,k-1,k+1,…,n-1。下次删除数字是重k+1位置开始，于是可以把序列看
作k+1,..,n-1,0,1,…,k-1。该序列最后剩下的序列也是f的函数。但该函数和第一个函数
不同，存在映射关系，使用f'来表示，于是有：f(n, m)=f'(n-1, m)。接下来需要找到映射关系。
k+1 --> 0
k+2 --> 1
     .
     .
n-1 --> n-k-2
0   --> n-k-1
     .
     .
k-1 --> n-2
所以可以得到：right = left-k-1，则p(x) = (x-k-1)%n，而逆映射是p'(x) = (x+k+1)%n
即0~n-1序列中最后剩下的数字等于（0~n-2序列中最后剩下的数字+k）%n，很明显当n=1时，
只有一个数，那么剩下的数字就是0.问题转化为动态规划问题

### <a id="other2">丑数</a>)
* 考点：时间空间效率的平衡
* 知识点：穷举
* program: [UglyNumber.py](UglyNumber.py)


### 整数中1的个数
* 考点：时间效率
* 知识点：查找 数学
* program: [NumberOf1Between1AndN.py](NumberOf1Between1AndN.py)
* 题解：数学归纳法


### 把数组排成最小的数
* 考点：时间效率
* 知识点：数组
* program: [MinNumber.py](MinNumber.py)
* 题解：如果 str1 + str2 > str2 + str1 则 str1 > str2

### 第一个只出现一次的字符位置
* 考点：时间空间效率的平衡
* 知识点： 哈希表 字符串
* program: [FirstNotRepeatingChar.py](FirstNotRepeatingChar.py)
* 题解：先在hash表中统计各字母出现次数，第二次扫描直接访问hash表获得次数


### 数组中的逆序对
* 考点: 时间空间效率的平衡
* 知识点： 数组 排序
* program: [InversePairs.py](InversePairs.py)
* 题解：
    * 方法一： 冒泡排序($o(n^2)$) 每交换一次就有一个逆序对
    * 方法二： 归并排序（$o(nlogn)$）


### 两个链表的第一个公共结点
* 考点：时间空间效率的平衡
* 知识点：链表
* program: [FirstCommonNode.py](FirstCommonNode.py)[FirstCommonNode.java](FirstCommonNode.java)
* 题解：
    * 方法一： 
        1. 遍历链表2 记录节点数count1 记录最后一个节点pLast1
        2. 遍历并翻转链表2 记录节点数count2 记录最后一个节点pLast2
        3. 遍历链表1 记录节点数count2 记录最后一个节点pLast3
        4. 如果pLast1 == pLast3，则两条链表没有公共节点 
        5. 否则 两条链的公共节点数量为 length = (count1 + count2 - count3 + 1)/2
        6. 以pLast2为起始节点 翻转链表并记录第length个节点，该节点为一个公共节点
    * 方法二:
        1. 假定 List1长度: a+n  List2 长度:b+n, 且a小于b那么 p1 会先到链表尾部, 这时p2 走到 a+n位置,将p1换成List2头部
        2. 接着p2 再走b+n-(n+a) =b-a 步到链表尾部,这时p1也走到List2的b-a位置，还差a步就到可能的第一个公共节点。
        3. 将p2 换成 List1头部，p2走a步也到可能的第一个公共节点。如果恰好p1==p2,那么p1就是第一个公共节点。  或者p1和p2一起走n步到达列表尾部，二者没有公共节点，退出循环。 同理a>=b.
        时间复杂度O(n+a+b)