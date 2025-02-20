###常用工具

​	python3：https://www.python.org/downloads/
  pyCharm：https://www.jetbrains.com/zh-cn/pycharm/download/?section=windows
  Sublime：https://www.sublimetext.com/download
  Visual Studio Code：https://code.visualstudio.com/Download

### 符号和注释

#### 一、程序中的符号

1. 程序中的所有字符都必须是英文（半角）字符，不能是中午（全角）字符，注意  .' (," 之类的，都必须是英文字符！

2. 输出中午的括号和双引号，导致pyCharm以红线提示错误！
3. 除非就是要输出中文文字，才会在”字符串“中使用中午 

#### 二、注释

1. 并非需要执行的指令，只是为了编程者方便理解程序之用

2. 单行注释： ”#“ 开头

   ```python
   a = b # 让b赋值给a
   ```

   

3. pyCharm中，选中若干行，`Ctrl + /`可将这些行都变成注释/都由注释变非注释

#### 三、变量

1. 变量有名字，可以用来存储数据。其值可变

   ```python
   a = 12
   b = a		# 让b赋值给a
   print(a+b)
   a = "hello"
   print(a)
   
   输出：
   12
   hello
   ```

2. 变量有大小写字母、数字和下划线构成，中间不能有空格，长度不限，不能以数字开头

3. 变量名最好能够体现变量的含义

4. 多单词的变量名，最好第一个单词小写，后面单词首字母大写

5. 变量名是大小写相关的

6. 有些名字python预留了，不可用做变量的名字，使用`help keywords`查看

   ```python
   Here is a list of the Python keywords.  Enter any keyword to get more help.
   
   False               class               from                or
   None                continue            global              pass
   True                def                 if                  raise
   and                 del                 import              return
   as                  elif                in                  try
   assert              else                is                  while
   async               except              lambda              with
   await               finally             nonlocal            yield
   break               for                 not               
   
   如果不小心用了，python会报错
   ```

#### 四、赋值语句

1. 形式：

   **变量 = 表达式**

   将变量的值变得和 ”表达式“ 的值一样

   变量、数、字符串......都是 "表达式"

   程序是顺序执行，从上到下

   ```python
   a = "he"
   print(a)		# >>he
   b = 3+2
   a = b			# b赋值给a
   print(b)		# >>5
   print(a)		# >>5
   b = b + a 		# b的值改为原来b的值加a
   print(b)		# >>10
   a,b = "he",12
   print(a,b)		# >>he 12
   a,b = b,a		# 交换a,b的值
   print(a,b)		# >>12 he
   c,a,b = a,b,a
   print(a,b,c)	# >>he 12 12
   a = b = c = 10
   print(a,b,c)	# 10 10 10
   ```

   程序每行前面不能留空格（例外后面讲）

#### 五、字符串

1. 可以且**必须**用单引号、双引号或三引号括起来

   ```python
   x = "I said:'hello'"
   print(x)			# >>| said:'hello'
   print('I said:"hello"') 	# >>|said: "hello"
   print('''I said: 'he said "hello" '.''')  # >>|said:'he said "hello"'
   print("this \
   is \
   good")		# >>this is good  字符串太长时，可以分行写
   print( hello,word)		# 错！没有用括号括起来
   ```

2. 字符串里面不会包含变量

   ```python
   s = 1.75
   print(s)					# >>1.75
   print("I am s m tall")		# >>I am s m tall
   字符串中的 s 就是个字符，和前面的变量 s 没有关系！！！
   字符串必须用引号括起来，用引号括起来的就是字符串！
   a = 4
   b = 5
   print("a+b")				# >>a+b      不会打出9！！！
   ```

3. 三双引号字符串中可以包含换行符、制表符以及其他特殊字符

   ```python
   para_str = """多行字符串可以使用制表符
   TAB( \t)。
   也可以使用换行符【 \n 】
   """
   print(para_str)
   ```

4. 字符串的下标

   有n个字符的字符串，其中的每个字符都是长度为1的字符串：

   ​			从左到右依次编号为0,1,2.... n-1

   ​			从右到左依次编号为-1,-2..... -n

   **编号就是下标**

   ```python
   a = "ABCD"
   print(a[-1])		# >>D 
   print(a[0])			# >>A
   print(a[2])			# >>C
   ```

5. 用”+“连接字符串

   ```python
   a = "ABCD"
   b = "1234"
   a = a + b 			
   print(a)			# >>ABCD1234
   a = a + a[1]
   print(a)			# >>ABCD1234B
   ```

6. 不可以修改字符串中的字符

   ```python
   a = "ABCD"
   a[2] = 'k'		# 错，字符串中的字符不能修改
   ```

7. 用 in ，not in 判断子串

   ```python
   a = "Hello"
   b = "Python"
   print("el" in a)		`	# >>True
   print("th" not in b)		# >>False
   print("lot" in a)			# >>False
   ```
