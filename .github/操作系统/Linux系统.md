# LIinux

WSL：Windows Subsystem for Linux，是用于Windows系统之上的Linux子系统。

作用：可以在Windows系统中获得Linux系统环境，并完全直连计算机硬件，无需通过虚拟机虚拟硬件。

## WSL部署：

1.打开控制面板→程序→启动或关闭 Windows 功能

2.勾选 “适用于 Linux 的 Windows 子系统” 和 “虚拟机平台”

3.立即重新启动电脑

4.按win键或者点击左下角的windows图标打开微软的应用商店，下载Ubuntu

5.安装完成，创建用户名和密码

## 服务器部署

1、使用UltraISO制作liunx，系统U盘

2、安装过程出错选择回车会出现如下所示

ERR: starting timeout script

3、出现以上错误后，回车输入`cd dev`，然后回车，输入`ls`查看一下自己的U盘是哪一个标识符，此时可以拔插下U盘，多使用几次ls命令，看一看区别。我就是这样发现自己的U盘是的标识符是sdc4（一般U盘默认都是sd开头加数字。）在输入`reboot`命令重启设备。

4、把光标移动到第三个 键入`e`
将：
`vmlinuz initrd=initrd.img inst.stage2=hd:LABEL=CentOS\x207\x20x86_64.check quiet`
改为
`vmlinuz initrd=initrd.img inst.stage2=hd:/dev/sde4 quiet`
然后
`Ctrl+X` 就可以出现安装界面了

5、命令行安装

## centos7环境配置

```shell
1、配置阿里仓库源
[root@192 ~]# curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo

2、检测yum仓库源
[root@192 yum.repos.d]# yum repolist all |grep enable
base/7/x86_64               CentOS-7 - Base - mirrors.aliyun.com enabled: 10,072
extras/7/x86_64             CentOS-7 - Extras - mirrors.aliyun.c enabled:    512
updates/7/x86_64            CentOS-7 - Updates - mirrors.aliyun. enabled:  3,875
```

```shell
3、修改网卡配置文件
/etc/sysconfig/network-scripts/ifcfg-ens33

TYPE=Ethernet                               网卡类型:以太网
PROXY_METHOD=none                           代理方式:关闭状态
BROWSER_ONLY=no                             只是浏览器(yes|no)
BOOTPROTO=static                            设置网卡获得ip地址的方式(static|dhcp|none|bootp)
DEFROUTE=yes                                设置为默认路由(yes|no)
IPV4_FAILURE_FATAL=no                       是否开启IPV4致命错误检测(yes|no)
IPV6INIT=yes                                IPV6是否自动初始化
IPV6_AUTOCONF=yes                           IPV6是否自动配置
IPV6_DEFROUTE=yes                           IPV6是否可以为默认路由
IPV6_FAILURE_FATAL=no                       是不开启IPV6致命错误检测
IPV6_ADDR_GEN_MODE=stable-privacy           IPV6地址生成模型
NAME=eth0                                   网卡物理设备名称
UUID=6e89ea13-f919-4096-ad67-cfc24a79a7e7   UUID识别码
DEVICE=eth0                                 网卡设备名称
ONBOOT=no                                   开机自启(yes|no)
IPADDR=192.168.103.203                      IP地址
NETNASK=255.255.255.0                       子网掩码,也可使用掩码长度表示(PREFIX=24)
GATEWAY=192.168.103.1                       网关
DNS1=114.114.114.114                        首选DNS
DNS2=8.8.8.8                                备用DNS

4、执行：systemctl restart network 重启网卡，执行ifconfig即可看到ip地址固定为xxxx
```

参考连接：

https://blog.csdn.net/gsl371/article/details/79631447?spm=1001.2101.3001.6650.17&utm_medium=distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-17-79631447-blog-121128204.235121128204.235

## Linux基础知识

| /     | 根目录                                                       |
| ----- | ------------------------------------------------------------ |
| /bin  | 存放必要的命令                                               |
| /boot | 存放内核以及启动所需的文件                                   |
| /dev  | 存放设备文件                                                 |
| /etc  | 存放系统配置文件                                             |
| /home | 普通用户的宿主目录，用户数据存放在其主目录中lib 存放必要 的运行库 |
| /mnt  | 存放临时的映射文件系统，通常用来挂载使用                     |
| /proc | 存放存储进程和系统信息                                       |
| /root | 超级用户的主目录                                             |
| /sbin | 存放系统管理程序                                             |
| /tmp  | 存放临时文件                                                 |
| /usr  | 存放应用程序，命令程序文件、程序库、手册和其它文档           |
| /var  | 系统默认日志存放目录录                                       |

## Linux基础命令

ls命令：列出目录下的内容

- `-a` ：显示所有文件和目录，包括隐藏的（以`.`开头的）。
- `-l` ：以列表方式显示信息。
- `-h` ：以易读的方式显示文件大小（例如K，M，G）。
- `-t` ：按修改时间排序。
- `-r` ：反向排序。

！命令前缀----自动执行上一次匹配前缀的命令

ctrl+c-----强制停止

ctrl+d----退出者登出，或者退出某些特定程序专属页面

ctrl+r----历史命令搜索（键盘左右键得到命令，不执行）

ctrl+a---跳到命令开头

ctrl+e----跳到命令结尾

ctrl+键盘左键----向左跳一个单词

ctrl+键盘右键----向右跳一个单词

ctrl+l-----清屏（clear一样效果）

history----历史搜索

halt-------立即关机   

reboot---重启

shutdown----关机

cd命令：切换路径

cat命令：查看文件内容

more命令：查看文件内容（支持翻页）

pwd命令：显示当前所在位置的绝对路径

```shell
绝对路径
[root@localhost sysconfig]# cd /usr/bin/
相对路径
[root@localhost sysconfig]# cd ../../usr/bin/

cd /etc/
cd ..（切换到上一级目录）
cd - 切换到上一次目录所在的位置
cd ~ 切换到家目录
```

mkdir命令：创建文件夹

- `-p` ：创建不存在的父目录，适用于创建连续多层级的目录。

touch命令：创建文件

- 语法：touch 自定义文件名称

cp命令：复制

- `-r` ：复制文件夹使用，表示递归。

mv命令：移动文件或文件夹

- 语法：mv 被移动的文件 要移动去的地方

rm命令：删除文件|文件夹

- `-r` ：强制删除（不会弹出提示确认信息）
- `-rf /`：等同于在widows上执行C盘格式化

which命令：查看所使用的一系列命令的程序文件存放在哪里

- 语法：which 要查找的命令

echo命令：输出指定内容

- 语法：echo  输出的内容

find命令：按文件名查找

```shell
find 起始路径 -size  +/- n（k，M，G）
+、- 表示大于和小于
n表示大小数字
kMG表示大小单位，k(小写字母)表示kb，M表示MB，G表示GB
```

grep命令：从文件中通过文件关键字过滤文件行

- `-n`：表示在结果中显示匹配的行的行号。

| \|   | 管道符（将左边命令的结果，作为右边命令的输入）               |
| ---- | ------------------------------------------------------------ |
| >    | 重定向符（将左侧命令的结果，覆盖写入到符号右侧指定的文件中） |
| >>   | 重定向符（将左侧命令的结果，追加写入到符号右侧指定的文件中） |
| $    | 用于脚本参数、变量替换和命令替换中                           |

wc命令：数量统计

- `-c`：统计字节bytes数量 
- `-m`：统计字符chars数量
- `-l`：统计行数line
- `-w`：统计单词数量words

tail命令：查看文件尾部命令，并可以持续跟踪

```shell
tail -num -f Linux路径

-f：持续跟踪
-num：启动的时候查看尾部多少行，默认10
Linux路径，表示被查看的文件
```

systemctl命令：

- 语法：systemctl 【start（启动）、stop （关闭）、status (查看状态）、enable （开启开机自启）、disable （关闭开机自启）】

**系统内置服务**

NetworkManager，主网络服务
network，副网络服务
firewalld，防火墙服务
sshd，ssh服务（XShell远程登录Linux使用的就是这个服务）



ln命令：创建软连接 【在系统中创建软连接，可以将文件、文件夹连接到其他位置】

- 语法：ln 【-s】被连接的文件或文件夹、要连接驱动目的地				//`-s`选项，创建软连接


ps命令：查看系统进程信息

```shell
语法：
-e     显示所有进程
-f     显示所有字段（UID，PPIP，C，STIME字段）
-a     显示一个终端的所有进程
-u     显示当前用户进程和内存使用情况
-x     显示没有控制终端的进程
–sort     按照列名排序

常用操作
ps -ef：查看所有进程
ps -aux：查看所有进程
ps -ef | grep tomcat：查看指定进程
ps -ef | grep tail----即可准确的找到tail命令的信息
```

**从左到右分别是：**

| UID： | 进程所属的用户ID                              |
| ----- | --------------------------------------------- |
| PID   | 进程的进程号ID                                |
| PPID  | 进程的父ID（启动此进程的其它进程）            |
| C     | 此进程的CPU占用率（百分比）                   |
| STIME | 进程的启动时间                                |
| TTY   | 启动此进程的终端序号，如显示?，表示非终端启动 |
| TIME  | 进程占用CPU的时间                             |
| CMD   | **进程对应的名称或启动路径或启动命令**        |

kill命令：关闭进程

- 语法：kill【-9】进程ID

- 选项：-9，表示强制关闭进程。不使用此选项会向进程发送信号要求其关闭，但是否关闭看进程自身的处理机制。

top命令查看cup、内存使用情况

- killall

killall 通过程序的名字，直接杀死所有进程

用法：killall + 正在运行的程序名

![img](https://cdn.nlark.com/yuque/0/2020/png/2196144/1603604426750-30f6e6fd-3531-471b-ae88-3bc18339a944.png)

### 为普通用户配置sudo认证

sudo命令：为普通命令授权，临时以root身份执行

su命令：切换用户

- 语法：su【-】【用户名】

1、切换到root用户，执行visudo命令，会自动通过vim编辑器打开：/etc/sudoers

2、在文件的最后添加：用户名 ALL=(ALL) <u>NOPASSWD:ALL</u>(表示使用sudo命令，无需输入密码)

3、最后通过 wq！保存

4、sudo 执行的命令，均以root运行

### root权限命令

#### 创建用户组

getent group-----查看用户组

groupadd 用户组名 ----创建用户组名

groupdel 用户组名-----创建用户组名

getent passwd---查看用户

#### 创建用户

useradd【-g	-d】用户名

- ​	`-g`：指定用户的组，不指定-g，会创建同名组自动加入，指定-g需要组以及存在，如已存在同名组，必须使用-g


- ​	`-d`：指定用户HOME路径，不指定，home目录默认在：/home/用户名


#### 删除用户

userdel【-r】用户名

- ​	`-r`：删除用户的home目录，不使用-r，删除用户时，home目录保留

#### id【用户名】----查看用户所属组

usermod-aG 用户组 用户名，将指定用户加入指定用户组

- `-a -G`：仅和 —G一快使用，将用户追加到附属组群，注意关键字“-a：追加”
- `-g`：修改用户所属群组

#### getent查看系统

getent passwd---查看系统全部用户信息

getent group----查看系统全部组信息

### rwx代表的意义

| r表示读权限 read     | 针对文件可以查看文件内容<br/>针对文件夹，可以查看文件夹内容，如ls命令 |
| -------------------- | ------------------------------------------------------------ |
| w表示写权限 write    | 针对文件表示可以修改此文件<br/>针对文件夹，可以在文件夹内：创建、删除、改名等操作 |
| x表示执行权限 excute | 针对文件表示可以将文件作为程序执行<br/>针对文件夹，表示可以更改工作目录到此文件夹，即cd进入 |

chmod命令：修改文件、文件夹的权限信息

语法：chmod【-R】权限 文件或文件夹

- `-R`对文件夹内的全部内容应用同样的操作

**权限可以用3位数字来代表，第一位数字表示用户权限，第二位表示用户组权限，第三位表示其它用户权限。**
**数字的细节如下：r记为4，w记为2，x记为1，可以有：**
**0：无任何权限，	即 ---**
**1：仅有x权限，	即 --x**
**2：仅有w权限	即 -w-**
**3：有w和x权限	即 -wx**
**4：仅有r权限	即 r--**
**5：有r和x权限	即 r-x**
**6：有r和w权限	即 rw-**
**7：有全部权限	即 rwx**
**所以751表示： rwx(7) r-x(5) --x(1)**

### 压缩格式

1、tar压缩、解压命令

```sh
语法：tar【-c	-v	-x	-f	-z	-c】参数1	参数二	...	参数N

-c，创建压缩文件，用于压缩模式
-v，显示压缩、解压过程，用于查看进度
-x，解压模式
-f，要创建的文件，或要解压的文件，-f选项必须在所有选项中位置处于最后一个
-z，gzip模式，不使用-z就是普通的tarball格式，建议在开头位置
-C，选择解压的目的地，用于解压模式，单独使用

#### 压缩 #### 
tar -cvf test.tar 1.txt 2.txt 3.txt----将1.txt 2.txt 3.txt 压缩到test.tar文件内
tar -zcvf test.tar.gz 1.txt -----将1.txt 压缩到test.tar.gz文件内，使用gzip模式

#### 解压 #### 
tar -xvf test.tar----解压test.tar,将文件解压至当前目录
tar -xzvf test.tar.gz -C /home/admin-----解压test.tar.gz，将文件解压至指定目录（/home/admin）
```

2、zip压缩、解压文件命令

```shell
语法：zip 文件名.zip 文件参数1 文件参数2
-r，被压缩的包含文件夹的时候，需要使用-r选项，和rm、cp等命令的-r效果一致

#### 压缩 #### 
zip test.zip a.txt b.txt c.txt-------将a.txt b.txt c.txt 压缩到test.zip文件内
zip -r test.zip test test2 a.txt-------将test、test2两个文件夹和a.txt文件，压缩到test.zip文件内

#### unzip解压文件命令 #### 
语法:unzip【-d】参数
-d，指定要解压去的位置，同tar的-C选项
参数，被解压的zip压缩包文件

#### 解压 #### 
unzip test.zip，将test.zip解压到当前目录
unzip test.zip -d /home/admin，将test.zip解压到指定文件夹内（/home/admin）
```

## vi/vim编辑器

在命令模式内，按键盘 i ，进入输入模式

输入完成后，按esc回退会命令模式

在命令模式内，按 : ，进入底线命令模式

### 1、编辑模式

| 快捷键  | 功能描述               |
| ------- | ---------------------- |
| shift+4 | 光标移动到行尾         |
| shift+6 | 光标移动到行首         |
| gg      | 光标移动到文档首行     |
| gm      | 光标移动到当前行中间处 |
| G       | 光标移动到文档尾行     |
| yy      | 复制当前行             |
| p       | 粘贴复制内容           |
| /       | 进入搜索模式           |

### 2、底线命令模式

|    命令     |           功能描述            |
| :---------: | :---------------------------: |
|     :wq     |      保存并退出 Vim 编辑      |
|    :wq!     |   保存并强制退出 Vim 编辑器   |
|     :q      |    不保存就退出 Vim 编辑器    |
|     :q!     | 不保存，且强制退出 Vim 编辑器 |
|     :w      |   保存但是不退出 Vim 编辑器   |
|     :w!     |         强制保存文本          |
| :w filename |     另存到 filename 文件      |
|     x！     |  保存文本，并退出 Vim 编辑器  |
|     ZZ      |      直接退出 Vim 编辑器      |
|      v      | 可视模式方向键选择（d—删除）  |
|  ：set nu   |           显示行号            |

## 查看命令帮助手册

man（manual， 手册）-----查看命令的详细手册

例：man ls，就是查看ls命令的详细手册
		man cd，就是查看cd命令的详细手册

--help ----查看命令的帮助

## 软件安装命令

**CentOS系统安装软件**

yum命令：安装命令

- 语法：yum【-y】【install（安装）、remove（卸载）、search（搜索）】

wget命令：下载文件的工具

- 语法：wget【-b】url

  选项：-b----后台下载，将日志写入到当前工作目录的wget-log文件

  参数：url（下载连接）

cturl命令：下载文件、获取信息【发送http网络请求】

- 语法：curl【-0】url

- 选项：-0，用于下载文件，当url是下载链接时，可以使用此选项保存文件

- 参数：url，要发起请求的网络地址

**Ubuntu系统安装软件**

apt命令：

语法：apt【-y】【install（安装）、remove（卸载）、search（搜索）】
