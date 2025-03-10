# widows

## ipconfig命令

1. `ipconfig`可以快速查看网卡的IP地址、子网掩码、默认网关等信息

2. **显示帮助文档**：输入`ipconfig /?`可以显示`ipconfig`的帮助文档，里面有详细的参数说明和使用示例

   | 参数         | 功能                             |
   | ------------ | -------------------------------- |
   | /all         | 显示本机TCP/IP配置的所有详细信息 |
   | /release     | DHCP客户端手动释放IP地址         |
   | /renew       | DHCP客户端手动向服务器刷新请求   |
   | /flushdns    | 清楚本地DNS缓存内容              |
   | /displaydns  | 显示本地DNS内容                  |
   | /registerdns | DNS客户端手动向服务器进行注册    |

## nslookup命令

`nslookup www.baidu.com`,查询百度地址

**nslookup**：查询DNS以获得域名或IP地址的映射关系以及其他DNS记录信息。可以帮助快速诊断网络连接问题，比如当无法访问某个网站时，可以使用`nslookup`来检查域名是否正确解析到了预期的IP地址

**常见资源记录类型：**SOA（起始授权结构）、A（主机或主机记录，是DNS名称到IP地址的映射，用于正向解析）、NS（名称服务器）、CNAME（别名）、MX（邮件交换器）

## netstat命令

| 参数          | 功能                                             |
| ------------- | ------------------------------------------------ |
| **- a (all)** | **显示所有选项，默认不显示LISTEN相关**           |
| - t (tcp)     | 仅显示tcp相关选项                                |
| - u (udp)     | 仅显示udp相关选项                                |
| **- n**       | **拒绝显示别名，能显示数字的全部转化成数字**     |
| - l           | 仅列出有在Listen（监听）的服务状态               |
| - p           | 显示建立相关链接的程序名                         |
| **- r**       | **显示路由信息，如路由表**                       |
| **- e**       | **显示扩展信息，如uid等**                        |
| **- s**       | **按各个协议进行统计**                           |
| - c           | 每隔一个固定时间，执行该netstat命令              |
| - v           | 显示正在进行的工作                               |
| - p           | 显示指定协议信息                                 |
| - b           | 显示子啊创建每个连接或侦听端口时涉及的可执行程序 |
| - f           | 显示外部地址的完全限定域名（FQDN）               |
| **- o**       | **显示拥有的与每个连接关联的进程ID**             |
| - x           | 显示networkDirect连接、侦听器和共享端点          |

```shell
nmap 端口扫描
netstat -nupl  (UDP类型的端口)
netstat -ntpl  (TCP类型的端口)
netstat -anp 显示系统端口使用情况
#### 端口分类 ####
1、公认端口：1~1023，通常用于一些系统内置或知名程序的预留使用，如SSH服务的22端口，HTTPS服务的443端口
非特殊需要，不要占用这个范围的端口
2、注册端口：1024~49151，通常可以随意使用，用于松散的绑定一些程序\服务，3306mysql，8080tomcat
3、动态端口：49152~65535，通常不会固定绑定程序，而是当程序对外进行网络链接时，用于临时使用。
```

1. `netstat -ntlp`  //查看当前所有tcp端口
2. `netstat -ntulp |grep 80`  //查看所有80端口使用情况
3. `netstat -an | grep 3306 ` //查看所有3306端口使用情况
4. `netstat -lanp`  //查看一台服务器上面哪些服务及端口
5. `ps -ef |grep mysqld`  //查看一个服务有几个端口。比如要查看mysqld(端口号)
6. `netstat -pnt |grep :3306 |wc`   //查看某一端口的连接数量,比如3306端口

CLOSED：初始（无连接）状态。

LISTENING：侦听状态，等待远程机器的连接请求。

ESTABLISHED （建立）：完成TCP三次握手后，主动连接端进入ESTABLISHED状态。此时，TCP连接已经建立，可以进行通信。

## tasklist命令

`tasklist`：显示当前运行的所有进程列表，可以查看程序名称、会话名、会话编号、内存使用情况等信息。

**获取系统进程的详细信息**：

- `tasklist /V`：显示所有运行的任务及其详细信息。
- `tasklist /M`：显示每个任务的完整命令行。
- `tasklist /SVC`：显示每个进程中的服务

## arp命令

**arp**：显示或修改地址解析协议(ARP)缓存，ARP用于将IP地址转换为物理地址。

对于Windows系统：

- **打开命令提示符**：首先需要以管理员身份运行命令提示符。
- **查看ARP缓存**：使用`arp -a`命令来显示当前的ARP缓存内容，它会列出IP地址及其关联的MAC地址。
- **删除整个ARP缓存**：可以使用`netsh interface IP delete arpcache`命令来清除所有ARP缓存条目。或者，更简单的方法是使用`arp -d`命令。
- **删除特定条目**：如果只想删除特定的ARP缓存条目，而不是整个表，可以使用`arp -d <ip-address>`命令，将`<ip-address>`替换为想要删除的特定IP地址。

对于Linux系统：

- **查看ARP缓存**：可以使用`arp`或`arp -n`命令来查看ARP缓存。
- **删除整个ARP缓存**：在Linux中，可以使用`ip neigh flush all`命令来清除所有的邻居（ARP）缓存条目。
- **删除特定条目**：要删除特定的条目，可以使用`ip neigh flush dev <interface>`命令，其中`<interface>`是网络接口的名称，例如`eth0`。

**ping**：用于测试网络连接是否通畅，通过发送ICMP请求到指定的网络主机。

**tracert**：跟踪数据包在网络中的传输路径，显示数据从源到目标主机的完整路由。

## 运行窗口

**regedit**:打开注册表

**control**：打开控制面板

**msconfig**:打开系统配置工具

**dxdiag** #打开DirectX诊断工具

**compmgmt.msc**：打开计算机管理

**services.msc**：打开服务窗口，可以查看和管理Windows操作系统中所有的服务。

**mstsc /admin /v:ip地址:端口号**：强制远程登录

## 其他

**C:\Windows\Prefetch**：访问阅读信息

**C:\Windows\System32\LogFiles**：系统日志

**mrt**:恶意软件杀毒工具

**%temp%**：日常缓存垃圾清理

**cleanmgr**：清理磁盘垃圾

**systeminfo**：查看系统配置信息

**chkdsk**：磁盘检查，修复文件系统错误

**sfc /scannow**:自动修复已损坏文件

**cleanmgr**：磁盘清理

**MSG**：给局域网电脑发送文本弹窗

`msg /server：对方IP * “文本内容”`

**sfc /scannow** ：诊断并修复widows系统文件

## win10激活

1. 首先，按下win+R打开"运行",输入 regedit 后回车，打开注册表。
2. 然后再注册表下输入地址HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform\ ，在该目录下找到SkipRearm，双击打开后，将数值0改为1，确认保存后重新启动电脑即可
3. slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX
   slmgr /skms kms.03k.org
   slmgr /ato

注：Windows PowerShell (管理员)

参考网址：https://blog.csdn.net/qq_37700257/article/details/126284196

## win11激活

```
slmgr -ipk W269N-WFGWX-YVC9B-4J6C9-T83GX

slmgr -skms kms.0t.net.cn

slmgr -ato

家庭版：
TX9XD-98N7V-6WMQ6-BX7FG-H8Q99
3KHY7-WNT83-DGQKR-F7HPR-844BM
7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH
PVMJN-6DFY6-9CCP6-7BKTT-D3WVR

专业版：
W269N-WFGWX-YVC9B-4J6C9-T83GX
MH37W-N47XK-V7XM9-C7227-GCQG9

教育版：
NW6C2-QMPVW-D7KKK-3GKT6-VCFB2
2WH4N-8QGBV-H22JP-CT43Q-MDWWJ
NPPR9-FWDCX-D2C8J-H872K-2YT43
DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4
```

## win-server-2016激活

slmgr /ipk CB7KF-BWN84-R7R2Y-793K2-8XDDG

slmgr /skms kms.03k.org

slmgr /ato

参考网址：

https://www.cnblogs.com/daodaoxun/p/14842672.html

## Win-server-2019激活

slmgr /ipk WMDGN-G9PQG-XVVXX-R3X43-63DFG

slmgr /skms kms.03k.org

slmgr /ato

参考网址：

https://www.haixinst.com/thread-89-1-1.html
