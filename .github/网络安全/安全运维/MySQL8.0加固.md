## MySQL安装

## MySQL8.0版本在CentOS系统安装

> 注意：安装操作需要root权限



### 一、安装



1. 配置yum仓库

   ```shell
   # 更新密钥
   rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022
   
   # 安装Mysql8.x版本 yum库
   rpm -Uvh https://dev.mysql.com/get/mysql80-community-release-el7-2.noarch.rpm
   ```

2. 使用yum安装MySQL

   ```shell
   # yum安装Mysql
   yum -y install mysql-community-server
   # 如果遇到下载特别慢,尝试清理缓存
   yum clean all
   ```

3. 安装完成后，启动MySQL并配置开机自启动

   ```shell
   systemctl start mysqld        # 启动
   systemctl enable mysqld        # 开机自启
   ```

   > MySQL安装完成后，会自动配置为名称叫做：`mysqld`的服务，可以被systemctl所管理

4. 检查MySQL的运行状态

   ```shell
   systemctl status mysqld
   ```

   

### 二、配置

主要修改root密码和允许root远程登录



1. 获取MySQL的初始密码

   ```shell
   # 通过grep命令，在/var/log/mysqld.log文件中，过滤temporary password关键字，得到初始密码
   grep 'temporary password' /var/log/mysqld.log
   ```

2. 登录MySQL数据库系统

   ```shell
   # 执行
   mysql -uroot -p
   # 解释
   # -u，登陆的用户，MySQL数据库的管理员用户同Linux一样，是root
   # -p，表示使用密码登陆
   
   # 执行完毕后输入刚刚得到的初始密码，即可进入MySQL数据库
   ```

3. 修改root密码

   ```sql
   ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '密码';    -- 密码需要符合：大于8位，有大写字母，有特殊符号，不能是连续的简单语句如123，abc
   ```

4. 



在不影响业务正常运行的情况下，及时更新软件，打补丁。

https://www.oracle.com/security-alerts/



查看数据库版本：

```sql
select version();
```

![image-20231212115131345](http://cdn.jsdelivr.net/gh/flamesusr/picgo/img/202502202220983.png)

***\*01 禁止数据库用户的密码为空并设置密码有效期\****

执行如下执行SQL语句检查密码是否为空：

```sql
select user,host from mysql.user where length(authentication_string) = 0;
```

查看所有用户信息

```sql
select user,host,authentication_string,password_lifetime,account_locked from mysql.user;
```

![](http://cdn.jsdelivr.net/gh/flamesusr/picgo/img/202502202220450.png) 

 

若存在空密码的数据库用户，则执行如下命令设置数据库用户密码，且密码必须满足密码策略的要求：

```sql
set password for 'user'@'host' = password('yourpassword');
'user' 替换为要设置密码的用户名，'host' 替换为用户所在的主机地址，'yourpassword' 替换为所需的密码。这将为指定的用户设置新密码。
例：set password for 'test'@'192.168.56.1' = password('testtest');
```

***\*另外还要注意：\****

1. 禁用或限制匿名、默认账户、测试账户的访问权限；（禁用账户）
2. 应重命名或删除默认账户，修改默认账户的默认口令；
3. 应及时删除或停用多余的、过期的账户，避免共享账户的存在；
4. 删除了默认数据库TEST。（旧版本会有默认的测试数据库）

***\*禁用数据库用户的语句\****

```sql
ALTER USER 'user'@'host' ACCOUNT LOCK;
'user' 替换为要锁定的用户名，'host' 替换为用户所在的主机地址。这将锁定指定用户的账户，使其无法登录到数据库。
```

***\*查看密码有效期（全局变量）\****

```sql
show global variables like 'default_password_lifetime';
```

![image-20231211111526168](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502202221398.png)

配置密码有效期全局变量，编辑mysql配置文件，添加下面内容。

```sql
default_password_lifetime = 180
```

或者通过命令进行修改。

```sql
SET GLOBAL default_password_lifetime = 180;
```

配置某个用户的密码有效期，使用ALTER USER命令为每个具体的用户账户单独设置特定的值，它会自动覆盖密码过期的全局策略。要注意ALTER USER语句的INTERVAL的单位是“天”。 

```sql
ALTER USER 'root'@'localhost' PASSWORD EXPIRE INTERVAL 180 DAY;
将特定用户的密码过期间隔设置为180天的示例。该命令会将 'root'@'localhost' 用户的密码过期间隔设置为180天。这意味着该用户的密码将在180天后过期，需要重新设置密码。
```

```sql
flush privileges；  
更新配置
```

登录到 MySQL 服务器并运行以下命令：

```sql
SET PERSIST default_password_lifetime = 90;
```

该命令将设置 `default_password_lifetime` 参数的值为 90，同时使用 PERSIST 关键字指示 MySQL 在重启后保留该更改。

如果您想要验证参数的值是否已经成功更改，请执行以下命令：

1. ```sql
   SELECT @@default_password_lifetime;
   ```

   该命令将返回 `default_password_lifetime` 参数的当前值。

请注意，如果您使用 `SET PERSIST` 命令更改任何 MySQL 系统变量的值，则 MySQL 可能会在配置文件中自动创建一个新的参数条目。因此，当您再次编辑 MySQL 配置文件时，请务必查看是否存在类似于以下条目的内容：

```ini
[mysqld]
default_password_lifetime=90
```



***\*02 检查数据库用户的密码是否为弱口令\****

有些人为了方便，可能会把数据库用户的密码设置为弱口令，现在的数据库会以mysql5加密算法加密口令，可以去MD5解密的平台输入密文，看能否得出明文。

https://www.cmd5.com/

https://www.somd5.com/

![](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502211831315.png) 

 

如果是弱口令，则要求更改其数据库用户的口令。

关于MySQL密码你应该知道的那些事 - cenalulu

MySQL：密码加密方式 - xuejianbest

***\*03  密码复杂度配置\****

密码不能与用户名一致，密码长度8位以上（包含8位）、至少有一个数字、一个大写字母、一个小写字母、一个特殊字符。

```ini
plugin-load = "validate_password.so"
validate-password = FORCE_PLUS_PERMANENT
validate_password_length = 8 
validate_password_policy = 1 
validate_password_mixed_case_count = 1 
validate_password_number_count = 1 
validate_password_special_char_count = 1 
```

`validate-password = FORCE_PLUS_PERMANENT`
 值为`FORCE_PLUS_PERMANENT`
表示强制启用该插件，并且不能被卸载。

执行以下命令来查看当前的密码验证设置：

```sql
SHOW VARIABLES LIKE 'validate_password%';
```

这将显示与密码验证相关的变量及其当前值。

根据您的需求，选择适当的选项修改密码验证设置。以下是一些常用的选项：

- `validate_password_policy`：设置密码策略的级别。可选值包括：
  - `0` 或 `LOW`：较低的密码复杂性要求。
  - `1` 或 `MEDIUM`：中等的密码复杂性要求。
  - `2` 或 `STRONG`：较高的密码复杂性要求。
- `validate_password_length`：设置密码最小长度。
- `validate_password_number_count`：设置密码中所需的数字个数。
- `validate_password_special_char_count`：设置密码中所需的特殊字符个数。
- `validate_password_dictionary_file`：指定自定义密码字典文件的路径。

使用 `SET GLOBAL` 命令来修改相应的变量值。例如，要将密码策略设置为中等级别（MEDIUM），可以执行以下命令：

```sql
SET GLOBAL validate_password_policy=1; 
SET GLOBAL validate_password_length=8;
SET GLOBAL validate_password_number_count=1;
SET GLOBAL validate_password_special_char_count=1;
```

注意：使用 `SET GLOBAL` 命令会立即生效，但不会在重启后保持设置。如果想要在重启后保持设置，需要在 MySQL 配置文件中进行相应的更改。

如果您对密码验证设置进行了更改并且想要立即使其生效，可以执行以下命令来刷新权限：

```sql
FLUSH PRIVILEGES;
```

效果：密码不能与用户名一致，密码长度8位以上（包含8位）、至少有一个数字、一个大写字母、一个小写字母、一个特殊字符。

```sql
show variables like '%validate_password%';
```

![image-20231211113900933](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502211831313.png)  

安装和卸载插件

`validate_password`插件相关参数的介绍

MySql5.6使用`validate password` 插件加强密码强度的安装及使用方法 - wangmm0218

如果` validate_password `没有被激活，您可以通过以下步骤启用它：

​	a. 编辑 MySQL 配置文件 (my.cnf 或者 my.ini)。您可以在文件中找到 [mysqld] 段落。

​	b. 在 [mysqld] 段落中添加以下行（如果已经存在，请确保将其修改为正确的值）：

```ini
plugin-load = validate_password.so
validate-password=FORCE_PLUS_PERMANENT
```

​	c. 保存并关闭配置文件。

重新启动 MySQL 服务器，以使配置更改生效。

登录到 MySQL 服务器，并执行以下命令来验证 validate_password 插件是否已启用：

```sql
SHOW VARIABLES LIKE 'validate_password%';
```

您应该能够看到 validate_password 插件的相关变量的值。



***\*04 登录失败和连接超时设置和操作超时策略\****

mysql有个连接超时的插件，相当于登录失败锁定策略，可根据业务需要进行最低配置。

1.插件安装

```cobol
install plugin CONNECTION_CONTROL soname 'connection_control.so';
install plugin CONNECTION_CONTROL_FAILED_LOGIN_ATTEMPTS soname 'connection_control.so';
```

2.查看是否安装成功

```sql
show variables like 'connection_control%';
```

2.修改my.cnf文件,增加如下两行

```cobol
connection-control-failed-connections-threshold=5   #登陆失败次数限制
connection-control-min-connection-delay=300000    #限制重试时间，此处为毫秒，注意按需求换算，此处为5分钟
```

3.重新登录数据库，查看是否生效

```sql
show variables like '%connection_control%';
```

![image-20231212115031078](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502211832867.png)

```
connection_control_failed_connections_threshold
```

失败尝试的次数，默认为3，表示当连接失败3次后启用连接控制0表示不开启

```
connection_control_max_connection_delay
```

响应延迟的最大时间

```sql
connection_control_min_connection_delay
```

响应延迟的最小时间，默认1000微秒，1秒

然后是超时时间设置。

查看和设置 连接超时相关的两个参数interactive_timeout和wait_timeout，其值应当至多为30分钟。

```sql
show global variables like 'interactive_timeout';
show global variables like 'wait_timeout'; 

set global interactive_timeout=1800;
set global wait_timeout=1800;
```

interactive_timeout：交互式连接超时时间(mysql工具、mysqldump等)
wait_timeout：非交互式连接超时时间、默认的连接mysql api程序、jdbc连接数据库等

简单来说，通过mysql客户端连接数据库是交互式连接，通过jdbc连接数据库是非交互式连接。

 

连接控制插件安装

MySQL安全插件：Connection-Control Plugins 的利与弊 - leonpenn

MySQL 插件之 连接控制插件(Connection-Control) - ZhenXing_Yu

MySQL连接超时相关的两个参数interactive_timeout和wait_timeout的区别和解释 - young5201314

MySQL参数max_connect_errors分析释疑 - 潇湘隐者

MySQL状态变量Aborted_connects与Aborted_clients浅析 -海东潮



### 三、操作超时策略

登录到 MySQL 服务器。

```sql
show global variables like '%wait_timeout';
```

运行以下命令来修改 `wait_timeout` 参数的值：

```sql
SET GLOBAL wait_timeout = 300;
```

这将将 `wait_timeout` 参数的值设置为 300 秒（即 5 分钟）。请注意，这只会在当前 MySQL 会话中生效。

如果您希望在 MySQL 服务器重新启动后仍然保留更改，您需要编辑 MySQL 配置文件。通常情况下，MySQL 配置文件名为 `my.cnf` 或 `my.ini`，具体取决于您的操作系统和 MySQL 版本。

打开 MySQL 配置文件，并找到 `[mysqld]` 部分。

在 `[mysqld]` 部分中，添加或修改以下行：

```ini
wait_timeout = 300
```

将 `wait_timeout` 参数设置为所需的值（例如 300）。保存并关闭配置文件。重新启动 MySQL 服务器，以使更改生效。

请注意，修改 `wait_timeout` 参数可能会影响 MySQL 服务器的性能和稳定性，

![image-20231212141459977](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502211832167.png)

***\*05 启用SSL\****

查看是否启用SSL（如果启用了SSL需要进行配置才能正常远程连接管理）。

```sql
 show variables like '%ssl';
```

![image-20231211171059517](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502211832988.png)

说明：如果数据库禁止远程管理（`select user,host from mysql.user;`），则已经符合安全要求，此情况下已无需启用SSL。

MySQL SSL配置（mysql5.7和mysql5.6) - Yuki_xiong

MYSQL SSL配置与使用 - 德莱華

***\*06 远程管理限制\****

其实最好还是应当禁止远程登录至少要禁止root直接远程登录管理数据库。

```sql
select user,host from mysql.user where user='root';
```

![image-20231211171147420](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502211832016.png)

看访问地址是否仅为 127.0.0.1 或 localhost 或 ::1

其它用户如需远程连接，应做访问范围限制。

执行

```sql
select user,host from mysql.user where host = '%';
```

若host字段为：% （允许任何IP连接），则说明不合规。

 

***\*远程连接管理配置方法：\****

**创建新用户**： 使用 `CREATE USER` 命令创建一个新用户，并指定其允许访问的主机和密码。例如：

```sql
CREATE USER 'newuser'@'<ip>' IDENTIFIED BY '<password> ';
```

**授予权限**： 使用 `GRANT` 命令为该用户授予相应的权限。例如，如果你希望用户拥有对特定数据库的所有权限，你可以这样做：

```sql
GRANT ALL PRIVILEGES ON <databases-name>.* TO 'newuser'@'<ip>';
```

如果你只想授予部分权限，可以相应地调整命令。

**刷新权限**： 在完成上述步骤后，通过执行以下命令来刷新权限：

```sql
FLUSH PRIVILEGES;
```

创建用户newuser

以上步骤将会创建一个新用户，并授予其访问数据库的权限。请确保用强密码保护用户，并根据需要限制用户的访问范围。

<databases-name> 指定单个数据库名 也可以用 *（即所有数据库名）

user 指定一个数据库用户名

<ip> 指定一个IP、一个网段（包括B段、C段 192.168.1.%）、%（所有IP）

<password> 指定远程连接时使用的密码，与本地密码可不同（但需符合密码复杂度要求）

\# 举例，给数据库用户root分配*数据库，只允许%网段远程连接并设置口令为Admin@123。

```sql
CREATE USER 'root'@'%' IDENTIFIED BY 'Admin@123';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
FLUSH PRIVILEGES;
```

```sql
select user,host from mysql.user where host = '%';
```

效果如下

 ![image-20231211173617703](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502211832794.png)

 

 

最后可以在mysql.user表中看到账号的情况，也是从这里删除。

```sql
select user,host from mysql.user where account_locked='N' and host!='localhost';
drop user 'user'@'host';
```

***\*知识补充-drop和delete的区别\****

·drop
drop user XXX;

删除已存在的用户，默认删除的是'XXX'@'%'这个用户，如果还有其他的用户(其它主机名),如'XXX'@'localhost'等，不会一起被删除。如果要删除'XXX'@'localhost'，使用drop删除时需要加上host即drop user 'XXX'@'localhost'。

· delete
delete from user where user='XXX' and host='localhost';

其中XXX为用户名，localhost为主机名(即需指定主机名)。

· drop和delete的区别
drop不仅会将user表中的数据删除，还会删除其他权限表的内容。

而delete只删除user表中的内容，所以使用delete删除用户后需要执行FLUSH PRIVILEGES;刷新权限，否则下次使用create语句创建用户时会报错。

***\*07 会话连接数配置\****

配置同样是在mysql配置文件中添加相关参数（max_connections = 100）。

```sql
show variables like "%connections";
```

![image-20231212101949498](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502211832350.png)

max_connections是对整个服务器的用户做出限制，
max_user_connections是对每个用户的限制，
为0表示不限制。

```shell
root@NF:~$ grep max_connections etc/mysql/mysql.conf.d/mysqld.cnf
max_connections     = 100
```

MySQL参数最大连接数max_connections - paul_hch

***\*08 启用日志审计\****

mysql默认启用日志审计，记录的内容也符合相关安全要求，此项默认符合。

查看日志启用情况

查看变量，看相关日志是否启用

```sql
show variables like 'log%';
```

或看mysql的配置文件，看相关日志的配置情况（根据业务需要启用相关日志和设置日志保存路径。）

\# * Logging and Replication
\#
\# Both location gets rotated by the cronjob.
\# Be aware that this log type is a performance killer.
\# As of 5.1 you can enable the log at runtime!
\#通用日志，将所有到达MySQL Server的SQL语句记录下来

```ini
general_log_file=/var/log/mysql/mysql.log
general_log=1
log_timestamps=SYSTEM
```

MySQL 正在使用 `/var/log/mysql/mysql.log` 文件记录通用查询日志。 `general_log` 参数设置为 `1` 表示启用通用查询日志功能， `log_timestamps` 参数设置为 `SYSTEM` 表示在日志中使用系统时间戳。

![image-20231212142512611](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502211833213.png)

\# Error log - should be very few entries.
\#错误日志,文件内容不会很多

```
log_error = var/log/mysql/error.log
```

\#
\# Here you can see queries with especially long duration
\#慢查询日志，记录SQL执行语句（执行时间超过2秒才会记录）

```
slow_query_log      = 1
slow_query_log_file   = var/log/mysql/mysql-slow.log
long_query_time = 2
log-queries-not-using-indexes
```

\#
\# The following can be used as easy to replay backup logs or for replication.
\# note: if you are setting up a replication slave, see README.Debian about
\#    other settings you may need to change.
\#二进制日志

```
server-id=1
log_bin=/var/log/mysql/mysql-bin.log
expire_logs_days=10
max_binlog_size=100M
#binlog_do_db=include_database_name
#binlog_ignore_db=include_database_name
```

```
server-id = 1 设置了 MySQL 服务器的唯一标识符，用于在主从复制场景中区分不同的服务器。
expire_logs_days = 10 设置了二进制日志文件过期时间，即文件会在指定天数后被自动删除。
max_binlog_size = 100M 指定了每个二进制日志文件的最大大小。
binlog_do_db 和 binlog_ignore_db 用于选择性地指定要记录或忽略的数据库。
```

来看一下日志内容，日志默认是分天存储的，一天一个文件并压缩保存。

· 相关日志（主要是查询日志和错误日志）应留存6个月以上。

· 日志记录的日期和时间应当是正确的，服务器需开启了NTP服务进行时间校对。

\#Linux 检查NTP服务时间同步情况
ntpq -p -n
ntpstat

查看系统时间

```sql
select now();
date 查看系统时间
```

`SELECT NOW()` 不是数据表中存储的数据，而是 MySQL 中用于获取当前日期和时间的函数。因此，您无法直接修改 `SELECT NOW()` 的结果。

如果您想更改 MySQL 服务器的系统日期或时间，您可以使用以下命令：

```sql
SET GLOBAL time_zone = '+8:00';
```

这将把 MySQL 服务器的时区设置为北京时间（GMT+8）。您可以将 `+8:00` 更改为您所在时区的 UTC 偏移量。

请注意，修改时间区设置可能会影响 MySQL 服务器的其他操作，例如 TIMESTAMP 数据类型的行为，因此在进行更改之前，请确保您已了解相关的安全性和性能规则。

![image-20231212142649242](https://raw.githubusercontent.com/flamesusr/picgo/main/img/202502211833719.png)

***\*09 禁止.mysql_history文件记录信息\****

.mysql_history文件会记录MySQL操作历史（即数据库查询语句），包含敏感信息。为了避免敏感信息泄露，需要禁止使用。
检查所有.mysql_history文件是否链接到dev/null，若没连接到，则以root用户执行如下命令：

```shell
find  -name ".mysql_history" | xargs
rm <your_path>/.mysql_history 
ln -s dev/null <your_path>/.mysql_history
```

***\*10 禁止mysql对系统文件进行读写操作\****

`local_infile`变量表示能否使用`load data local infile`命令。该变量默认为ON。该变量为OFF时，禁用客户端使用	`load data local infile`命令。避免通过数据库查询语句造成的任意文件读写漏洞。

执行如下SQL语句：

`show variables like 'local_infile';`

若返回结果不为OFF，则在/etc/my.cnf配置文件中修改

```ini
[mysqld] 
local_infile = 0
```

***\*11 用户权限合理分配\****

执行下面语句，查看各账户和权限分配情况。请根据业务需求进行合理的权限分配，应遵循三权分立原则（分为系统管理员、安全管理员、安全审计员等，并检查系统各用户所属的权限组。如：系统管理员不能进行业务操作、审计操作审计员不能进行业务操作、系统管理操作安全员不能进行添加账号操作等）

```sql
select user,host,account_locked from mysql.user;
show grants for 'user'@'host';
select * from mysql.user where user='user' and host='host' \G;
```

· 不能存在特权用户

· 不存在越权访问情况（绕过访问控制策略）

· mysql 数据库应当只允许root用户进行访问和管理



***\*others\****

***\*1.其它建议\****

· 最小权限原则

1.对于数据库，可以一个数据库用户分配一个数据库

2.对于mysql进程，不得以root用户运行，默认是采用了mysql用户运行。

· 更改默认开放端口3306

· 站库分离

***\*2.一些常见语句记录\****

```sql
SET GLOBAL default_password_lifetime = 180;
#设置全局变量及赋值。
INSTALL PLUGIN validate_password SONAME 'validate_password.so';
#安装插件，这里是安装配置密码复杂度策略的插件。
```

***\*3.关于更改数据库用户密码\****

```sql
update user set password=password('123') where user='root' and host='localhost';
# mysql 5.7以下

update mysql.user set authentication_string=PASSWORD('newpassword') where user='username' and host='localhost';
# mysql 5.7以上

alter user 'root'@'localhost' identified by 'newpassword';
# mysql 8.0以上
```

其实就是要注意密码的列名是什么，版本不一样，列名不同，可使`select * from mysql.user \G;`查看密码的列名。（\G 即把列数据逐行显示）

***\*4.实验环境\****

 
