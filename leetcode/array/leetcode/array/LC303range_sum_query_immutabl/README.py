# LC303区域和检索

## 题目链接[LeetCode](https://leetcode.cn/problems/range-sum-query-immutable/)

##题目描述
给定一个整数数组`nums`，处理以下类型的多个查询:
计算索引`left`和`right`（包含`left`和`right`）之间的`nums`元素的**和**，其中`left`<=`right`
实现`NumArray`类：
`NumArray(int[] nums)`使用数组`nums`初始化对象
`int sumRange(int i, int j)`返回数组`nums`中索引`left`和`right`之间的元素的**总和** ，包含`left`和`right`两点（也就是`nums[left] + nums[left + 1] + ... + nums[right]`)
 
## 示例
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

##解题思路
 - 前缀和方法

##代码实现
见`LC303_ange_sum_query_immutable/solution.py`

##知识总结
 - range(len())是结合range()函数和len()函数的常用写法，核心为生成彝族与某个序列（如列表、数组）长度一致的连续整数。
    - len(序列类对象#列表/字符串/元组)包含的元素个数，结果是一个整数。
    - range(start,stop,step)生成从start开始到stop结束的连续整数。
 - sum+=nums[i]表示把列表中索引`i`对应的元素加到total中。
 - **在类里，凡是要在多个方法之间共享的变量，都要用self.来保存**，否则就是方法里的"临时变量"，方法一结束就没有了。
 - 区间和公式**pre[right+1]-pre[left]**
 - 前缀和方法需先建一个**长度多1**的数组pre。
          nums:  -2     0     3    -5     2    -1
          索引:   0     1     2     3     4     5
          pre:    0    -2    -2     1    -4    -2    -3
          索引:   0     1     2     3     4     5     6 
          #前缀和总是到n-1个数的和，故区间和公式中为pre[right+1]


### 元组(Tuple)是一种**有序**、**不可复制**的基础数据结构，支持储存多类型数据，常用于**保护不变数据**、**函数返回多值**等情况。
#### 元组的创建方式
##### 基础括号创建：用()包裹元素，元素间用逗号分割，支持多类型混合储存。
    e.g.t1=(10,"python",3.14,True)   #多元素元组:整数，字符串，浮点数，布尔值)
        print(type(t1))              #type函数验证类型:输出<class 'tuple')
##### 省略括号创建:无需写()，直接用逗号分隔元素，本质一样(适合简洁场景，如函数返回多值)。
    e.g.t2=20,"java",2.71,False      #打印时自动补全括号，输出(20,"java",2.71,False)
##### 单元素元组(**关键细节**):单元素元组**必须在元素后加逗号**，否则括号会被识别为[运算优先级符号],而非元组标识。
    e.g.t3_wrong=(5)                       
        print(type(t3_wrong))        #输出<class 'int'>
    e.g.t3_right=(5,)
        print(type(t3_right))        #输出<class 'tuple')
##### tuple()函数转换创建:通过tuple()函数，可将列表、字符串等[可迭代对象]转换为元组。
    e.g.list1=[1,2,3]
        t4=tuple(list1)
        print(t4)                     #输出(1,2,3)
    e.g.str1="hello"
        t5=tuple(str1)
        print(t5)                     #输出('h','e','l','l','o')
#### 元组的核心操作
#####可执行的读取类操作
 - 通过索引访问元素:支持正向索引#从0开始，负向索引#从-1开始(表示最后一个元素—)
 - 切片截取元素:用[start,stop,step]截取元组部分元素，结果仍为元组，不修改原元组
 - 统计与查找元素:
    - count(元素)：统计指定元素在元组中出现的次数。
    - index(元素):查找指定元素的首次出现索引，不存在会报ValueError。
#### 不可执行的修改类操作(会报错):元素创建后的增、删、改全禁止，尝试修改会触发TypeError。
#### 特殊情况:元素包含可变元素
     e.g.t=(10,[20,30],40)
         t[1][2]=200
         print(t)                      #输出(10,[200,30],40)
### 元组vs列表
     | 对比维度   | 元组（Tuple）                     | 列表（List）         |
     |-----------|----------------------------------|----------------------|
     | 可修改性   |  不可修改                         |  可修改            |
     | 语法符号   | `()`(单元素需加逗号)              | `[]`                 |
     | 内存占用   | 小(结构简单)                      | 大（需预留修改空间） |
     | 字典键资格 |  可作为键                         |  不可作为键        |
     | 适用场景   | 固定数据                          | 动态数据             |
     #dict_right={(_,_):"__"}  ✔
      dict_wrong={[_,_]:"_,_"} ❌ #TypeError报错
###元组的实际场景
 - 存储不可变的[固定组合数据]：如坐标(x,y)、日期(年,月,日)、个人信息(姓名,年龄,性别），确保数据不会被意外修改。
 - 函数返回多个值(自动打包成元组)：python不能直接返回多个值，但会把多个返回值[打包成元组]，调用时可直接[解构]获取，无需手动拆包。
   e.g.def get_person_info():
           name = "Alice"
           age = 25
           height = 165
           return name, age, height       #等价于 return (name, age, height)
    e.g.name, age, height = get_person_info()
        print(name, age, height)  # 输出：Alice 25 165
 - 保护数据不被修改(替代列表的[只读模式])
