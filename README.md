Python3 Study
===

一年没写py了,手都生疏了 /(ㄒoㄒ)/~~

### Install && 虚拟环境
- `apt-get install python3 python3-pip`
- 换ali源
- 安装 Pipenv `pip3 install --user pipenv` 
####  virtualenv 虚拟环境
- `pip3 install virtualenv`
- `virtualenv -p pythonFile 虚拟环境名称`
> 算了还是用docker来处理吧
```
docker push dollarkiller/python3alpine
docker run -d -v $(PWD):/data python3alpine
```

### 基本数据类型:
- `type(data)` 查看data数据的类型
- str
  - 多行字符串
    - `'''三引号'''`
  - 原始字符串 
    - `print(r'c:\npr\npp')` 开头加上r
  - 字符串基本操作
    - 合并 `"hello" + "world"`
    - 切片  `"hello"[0]` `"hello"[2开头:3结尾]` 前闭后开 `"hello"[-1]`
    - 替换
- list 列表
  - `type([1,2,3,45])`
  - `len([1,2,3,4])`
  - `10 in [1,2,3,4]`
  - `10 not in [1,2,3,4]`
  - `min([1,2,3,4])`
  - `max([1,2,3,4])`
  - 添加
    - b.append(num)
- tuple 元组 不可变
  - `(1,2,3,12,1)`
- set 集合 {}
  - 无序 不重复
  - `{1,2,3,5,1,25}`
  - in not in
  - `{1,2,3,4,5,6} - {3,4}` 差集
  - `{1,2,3,4,5,6} & {3,4}` 交集
  - `{1,2,3,4} | {1,2,7}` 并集
- dict {:} 字典
  - `{1:12,2:15}` key值唯一 存储无序

### 变量与运算符
- 值类型 与 引用类型
- int str tuple 不可变 值类型  #  list set dict 可变 引用类型
- `id(str)` 查看str在内存中的id
- 成员运算符
  - `in` `not in`
- 身份运输符
  - `is` `is not` 比较内存地址
- 转换类型
  - int(a) double(a) str(a)

### 分支, 循环, 条件 , 枚举
- 流程控制 分支
  - if else for while switch
  - if
    ```
    if mood :
        print('go to left')
    else:
        print('哈哈')
    ```

### 包 模块 函数 变量作用域
- while 递归
  ```
  counter = 1

  while counter <= 10:
      counter += 1
      print(counter)
  else :
      print('+++++++++++')

  ```
- for 遍历循环  `for key in param` `for key,value in param`
  ```
  expression_list = [1,2,3,4,5,6]

  for target_list in expression_list :
      print(target_list)
  ```

  ```
  for i in range(10) : # range(0,10) 前闭后开
    print(i)
  ```



### 工程的组织结构: 包,模块,类
`包>模块>类>函数,变量`
- 让普通的文件夹变成一个包,文件夹下必须包含一个`__init__.py` 文件
  - `__init__` 
- 导入
  - 导入整个文件 import .. as 别名 
  - from ... import 指定函数名,, `from ... import *` 不推荐 * 
  - `__all__ = ['a','c']` * 导入 对外暴露的 
- `__init__.py`
  - 导入 会 默认 执行 __init__ 里面的内容
  - `__all__ = []` * 默认到出的 模块

#### 包与模块常见错误
- 包和模块是不会被重复导入的
- 避免循环导入

#### 模块内置变量
- `__name__`  namespace 主name 为 main
- `__package__`  pageage name
- `__file__` 文件地址包含文件名称
- `__doc__` doc文档
- 导入模块会执行模块内的内容
- 入口文件和普通模块内置变量的区别
- `__name__` 经典应用
  ```
  if __name__ == '__main__':
      pass
  ```
- 顶级包是 main的位置
- 相对导入不能在main里面用

### 函数
- 内置函数
  - round(val,保留小数点几位) 会自动4>5入
- 特性
  - 功能性
  - 隐藏细节
  - 复用性
- 定义以及运行特点
```
def funcname (parameter_list) :
    pass
```
- 让函数返回多个结果
  ```
  def mmf() :
    a = 'skill'
    b = 45
    return a,b

  a,b = mmf() # 序列解包
  print(a)
  ```
  返回的是元组
- 序列解包 与 链式赋值
  ```
  a = 1
  b = 2
  c = 3
  # or
  a,b,c = 1,2,3

  d = 1,2,3
  a,d,c = d
  ```
- 必须参数与关联参数
  - 必须参数
    ```
    def add(x,y) :
    ```
  - 关联参数
    ```
    def add(x,y):
    add(y=,x=)
    ```
- 可变参数
    ```
    def add(a ,*param):
        pass
    add(1,2,3,5,6,,)
    # param为元组
    ```
- 关键字可变参数
    ```
    def city_temp(**) :
        pass
    city_temp(bj='123',xm='sds',sh='sds')
    ```
- 变量作用域
  - 函数内部可以调用函数外部的变量 当函数内部局部变量和全局变量重名时,会调用函数内部变量
  - Python 没有块级作用域概念
- global 关键字
  ```
  def demo() :
    global c 
    c = 2
  demo()
  print(c)
  ```

### 面向对象
- 类 最基本的作用: 封装
  ```
  class Student() :
    c = 2 # class 变量

    def print_file(self) :
        print('hello' + str(self.c))
        self.pr()

    def pr(self) :
        print('123')

  student = Student()
  student.print_file()
  ```
- 构造函数
  - `def __init__(self)`
  - 当实例化时,就会被调用
    ```
    class Student() :
      name = ''
      age = 0
      
      def __init__(self,name,age) :
          self.name = name
          self.age = age

      def do_homework(self) :
          print(self.name + 'do homeworld')

    student = Student('dollarkiller',16)

    student.do_homework()
    ```
  - 实例方法
    ```
    def do_homework(self) :
        print(self.name + 'do homeworld')
    ```
    - 实例方法访问类变量
        ```
        def add(self) :
            self.__class__.sum
        ```
  - 类方法
      ```
      @classmethod  #装饰器
      def plus_sum(cls) :
          pass
      ```
  - 静态方法
      ```
      @staticmethod
      def add(x,y):
          pass
      ```
  - 成员可见性
    - 私有 方法前 加 __
  - 继承
    ```
    class Student(Human) : # student继承Human
    ```
    - super 调用父类
      - `super(Student子类,self).__init__(name,age)` 这个init就不用传self1了
  - 小重点
    ```
    class Test() :
        sums = 12

        def __init__(self,age) :
            self.sums = age
            self.__class__.sums += 16
            print(self.__class__.sums)
            print(self.sums)

    test = Test(15)
    test1 = Test(15)
    输出:
    28
    15
    44
    15
    ```
### 正则表达式 与 JSON
- 初窥  
    ```
    import re
    a = 'C|C++|JAVA|C#|PHP|PYTHON|JS|TS'
    re.findall('正则',a)
    ```
- 元字符 与 普通 字符
  - `[ca]` c or a `r = re.findall('a[cf]c',s)`
  - `[^ca]` 除了 c a 之外的
  - `[a-d]` a ~ b 之间的
  - 概括字符集
    - '\d' 数字
    - '\D' 非数字
    - '\w' 匹配字母或数字或下划线或汉字 等价于 '[^A-Za-z0-9_]'
    - '\s' 匹配任意的空白符
    - `.` 匹配换行付之外的所有
  - 数量词
    -  `r = re.findall('[a-z]{3}',a)` 匹配三长度 {min,max}
    -  `*` 匹配0次或者无限次
    -  `+` 匹配一次或者无限次
    -  `?` 匹配0次或者一次
  - 贪婪和非贪婪
    -   `r = re.findall('[a-z]{3,6}?',a)` 默认贪婪,加?非贪婪
  -   边界匹配
      -  ^ 匹配字符串的开始
      - $ 匹配字符串的结束
  - 组
    - `r = re.findall('(Python){3}',a)`
  - 匹配模式参数
    - `r - re.findall('',,模式|模式|模式)`
    - `re.I` 忽略大小写
    - `re.S` 包括换行符
  - re.sub 正则替换
    - `re.sub(正则,替换成的,原字符串,count,匹配模式)`
    - count替换的个数,不填全部替换 0 全部替换 1 替换一个 
    - 代码实例: test3>t8
  - 把函数当做参数传递
    ```
    import re

    s = 'AB5AS4DG4R8DGRT5GH4F8H48SF5SDF4SD89J5YUK9UIL98'

    def conver(value) :
        bbs = value.group()
        if int(bbs) >= 6:
            return '\n'
        

    r = re.sub('\d',conver,s)

    print(r)
    ```
    - search 与 match 函数 (不常用)
      - re.match 从开始匹配 if not return none
      - re.search 返回match对象
      - 处理 match对象
        - `r = re.search('\d',s)`
        - 获取匹配内容
          - `r.group()`
        - 获取匹配内容位置
          - `r.span()`
    - group 分组
    - JSON
      - 反序列化  `json.loads(json)` 转化为 字典
        ```
        import json

        json_str = '{"name":"dollarkiller","age":18}'

        student = json.loads(json_str)

        print(student)

        print(type(student))
        ```
      - 序列化 `json.dumps(student)`

### Python 高级语法 与 用法
- 枚举
    ```
    from enum import Enum

    class VIP(Enum) :
        YELLOW = 1
        GREEN = 2
        BLACK = 3
        RED = 4

    print(VIP.YELLOW) # 这个是不会返回值的
    ```
    - 获取枚举的值 `print(VIP.YELLOW.value)`
    - 获取标签的名字 `print(VIP.YELLOW.name)`
- Python 高级用法
  - 函数式编程
    - 闭包  函数+环境变量   闭包的环境变量会记忆上一次的状态
      ```
        def curve_pre() :
            a = 25
            def cureve(x) :
                return a*x*x
            return cureve

        f = curve_pre()
        c = f(15)
        print(c)
      ```

### 函数式编程
- lambda 表达式
  - 匿名函数
    ```
    def add(x,y) :
    return x + y

    f = lambda x,y:x+y
    print(f(15,75))
    ```
  - 三元表达式
    - `条件判断为true的结果 if 条件判断 else 为假的结果`   

### 装饰器 AOP
- 不改变原有函数 new func  (开闭原则)
```
import time

def decorator(func) :
    def wrapper(*args) :
        print(time.time())
        func(*args)
    return wrapper

@decorator
def f1(fun_name) :
    print('This is a function ' + fun_name)

@decorator
def f2(func_name,funcname2) :
    print('This is a function ' + func_name + funcname2)


f1('dollarkiller')

f2('dollarsda','asdasdsad')
```


### 小技巧 与 规范
- print(x,end='|') end 结尾
- class name 大写开头 大驼峰
- 变量 小写_链接
- 方法和函数的区别
  - 方法: 设计层面 类
  - 函数: 程序运行,过程式的称谓 模块 
  - 模块下的 变量:称为数据成员
- 去str空格 str.strip()

### 原生爬虫
- 目的
  - 找到数据对应网页
  - 分析页面结构找到数据所在位置
- 操作
  - 模拟HTTP请求 抓取网页
  - 正则匹配
    - 数据分析
      - video-info  
        - video-title
        - video-nickname
        - vudei-number
- 技巧
  - htmls = str(htmls,encoding='utf-8')


### 完结了 在 讲下 pipenv
- `pip3 install pipenv` 安装
- `pipenv install`  部署
- `pipenv shell` 进入
- `pipenv install flask` install package
- `exit` 退出虚拟环境
- `pipenv uninstall flask` uninstall package
- `pipenv graph` 依赖环境
- Docker 天下无敌