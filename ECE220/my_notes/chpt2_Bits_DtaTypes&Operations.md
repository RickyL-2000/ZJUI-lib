# Chpt2 Bits, Data Types and Operations

1. Signed magnitude 符号位表示法
2. 1's Complement 反码
3. 2's Complement 补码

算术逻辑单元 Arithmetic and Logic Unit, ALU

 #NOTE1: 如果已知一个非零整数A的码字，可以很方便地求得其相应负数-A的码字，换算口诀是：**取反加一**

LC-3将采用16-bit的补码方式，数值范围从-32768到+32767之间的所有整数。*我们说LC-3的精度(precision)是15位，范围(range)是$2^15$。

 #NOTE2：计算两个二进制数相减时，可以算出减数的取反加一，再**加**到被减数上。
 #NOTE3: 一个二进制数乘以n倍，就向左移动n位。

**符号扩展** (Sign-Extension) 应用于两个长度不同的的二进制数相加的场合。

**屏蔽字位** (bit mask) 利用屏蔽字单独筛选一个bit列中的某几位bit。using AND or OR.

 #NOTE: 可以用XOR判断两个数是否相同

**位矢量** 表示多个独立单元的状态。可用屏蔽字调节。

## floating

1. 符号：1 bit，代表符号
2. 数值范围：8 bit，代表范围（指数）
3. 数值精度：23 bit，代表精度（尾数部分，fraction，不包括整数部分）

 #NOTE：

 1. 浮点表示法中，小数点左边只有一个1，而这个1就不必被表示出来了。
 2. IEEE的浮点的基数为2.
 3. 实际的指数值等于该无符号整数-127。range = [1, 254]
 4. 如果指数字段内容是00000000，表示指数值是-126，而且尾数中小数点左边默认数字变成0。