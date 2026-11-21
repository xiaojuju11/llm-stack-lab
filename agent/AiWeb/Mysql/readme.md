# 数据库基础
1. 查看MySQL中的所有数据库
show databases;
2. 使用DDL语句创建数据库
CREATE DATABASE  数据库名 DEFAULT CHARACTER SET  字符编码;
示例：
create database test default character set utf8;
3. 删除数据库
DROP DATABASE  数据库名称;
drop database test;
4. 选择数据库
USE text;
# 数据库类型
1. 整数类型
MySQL数据类型	含义（有符号）
tinyint(m)	1个字节 范围(-128~127)
smallint(m)	2个字节 范围(-32768~32767)
mediumint(m)	3个字节 范围(-8388608~8388607)
int(m)	4个字节 范围(-2147483648~2147483647)
bigint(m)	8个字节 范围(+-9.22*10的18次方)
数值类型中的长度 m 是`指显示长度，并不表示存储长度`，`只有字段指定 zerofill 时有用`

例如： int(3) ，如果实际值是 2 ，如果列指定了 zerofill ，查询结果就是 002 ，左边用 0 来 填充

2. 浮点类型
MySQL数据类型	含义
float(m,d)	单精度浮点型 8位精度(4字节) m总个数，d小数位
double(m,d)	双精度浮点型 16位精度(8字节) m总个数，d小数位
3. 字符类型
MySQL数据类型	含义
char(n)	固定长度，最多255个字符
tinytext	可变长度，最多255个字符
varchar(n)	可变长度，最多65535个字符
text	可变长度，最多65535个字符
mediumtext	可变长度，最多2的24次方-1个字符
longtext	可变长度，最多2的32次方-1个字符
char和varchar：

`char长度固定`， 即每条数据占用等长字节空间；适合用在身份证号码、手机号码等定长。
`varchar可变长度`，可以设置最大长度；适合用在长度可变的属性。`(比如存储姓名)`
`text不设置长度`， `当不知道属性的最大长度时，适合用text`
按照查询速度： char最快， varchar次之，text最慢。

- 字符串型使用建议：
    - `经常变化的字段用varchar`
    - `知道固定长度的用char`
    - `尽量用varchar`
    - `超过255字符的只能用varchar或者text`
    - `能用varchar的地方不用text`
4. 日期类型
MySQL数据类型	含义
date	日期 YYYY-MM-DD
time	时间 HH:MM:SS
datetime	日期时间 YYYY-MM-DD HH:MM:SS
timestamp	时间戳YYYYMMDD HHMMSS
5. 二进制数据(BLOB)
BLOB和TEXT存储方式不同，TEXT以文本方式存储，英文存储区分大小写，而`Blob是以二进制方式存储，不分大小写。`
BLOB存储的数据只能整体读出。
TEXT可以指定字符集，BLOB不用指定字符集。
# 创建表与删除表
1. 创建表:
`CREATE TABLE 表名(列名 类型,列名 类型......)`
示例：
创建一个 employees 表包含雇员 ID ，雇员名字，雇员薪水。
create table employees(employee_id int,employee_name varchar(10),salary float(8,2));
查看已创建的表。
2. 删除表:
DROP TABLE 表名;
示例:
删除 employees 表。
drop table employees;
# MySQL中的约束
- 约束概述
数据库约束是对表中的数据进行进一步的限制，保证数据的正确性、有效性和完整性。

1. 主键约束(Primary Key) PK
- 不允许为空
- 不允许有重复值出现
- 保证数据的唯一性
主键约束是使用最频繁的约束。在设计数据表时，一般情况下，都会要求表中设置一个主键。 主键是表的一个特殊字段，该字段能唯一标识该表中的每条信息。例如，学生信息表中的学号是唯一的。

2. 外键约束(Foreign Key) FK
- 允许有空值
- 允许有重复
- 值必须是参照表的参照列中所包含的值
- 保证数据的参照完整性
外键约束经常和主键约束一起使用，用来确保数据的一致性。

3. 唯一性约束(Unique)
- 相同值只能出现一次
- 允许为多个列添加唯一性约束
- 保证数据的唯一性
唯一约束与主键约束有一个相似的地方，就是它们都能够确保列的唯一性。与主键约束不同的是，唯一约束在一个表中可以有多个，并且设置唯一约束的列是允许有空值的。

4. 非空约束(Not Null)
- 列中不能有空值
- 允许重复值
- 允许为多个列添加非空约束
- 保证数据没有空值
非空约束用来约束表中的字段不能为空。

5. 检查约束(Check)
- 用户自己定义约束条件
- 保证数据满足自定义的条件约束
- MySQL 目前不支持检查约束
检查约束也叫用户自定义约束，是用来检查数据表中，字段值是否有效的一个手段，但目前 MySQL 数据库不支持检查约束。
`补充：MySQL8.0 之后版本已经支持 Check 约束`
# 添加主键约束(Primary Key)
1. 单一主键
使用一个列作为主键列，当该列的值有重复时，则违反唯一约束。
2. 联合主键
使用多个列作为主键列，当多个列的值都相同时，则违反唯一约束。

- 修改表添加主键约束
    1. 使用DDL语句添加主键约束
    `ALTER TABLE  表名 ADD PRIMARY KEY(列名)`
    示例：
    将 emp 表中的 employee_id 修改为主键。
    alter table emp add primary key(employee_id);
    2. 主键自增长
    MySQL 中的自动增长类型要求：
    - 1. 一个表中只能有一个列为自动增长。
    - 2. 自动增长的列的类型必须是`整数类型`。
    - 3. 自动增长只能添加到具备`主键约束与唯一性约束`的列上。 
    - 4. 删除主键约束或唯一性约束，如果该列拥有自动增长能力，则需要先去掉自动增长然 后在删除约束。
    `alter table 表名 modify 主键 类型 auto_increment`
    示例：
    将 emp 表中的 employee_id 主键修改为自增。
    alter table emp modify employee_id int auto_increment;
# 创建表时添加约束
查询表中的约束信息：
`SHOW KEYS FROM  表名`
示例：
创建 depts 表包含 department_id 该列为主键且自动增长，department_name 列不 允许重复，location_id 列不允含有空值。
- create table depts(department_id int primary key auto_increment,department_name varchar(30) unique,location_id int not null);
# 添加数据(INSERT)
1. 选择插入
`INSERT INTO  表名(列名 1 ，列名 2 ，列名 3.....) VALUES(值 1 ，值 2 ，值 3......)`
示例：
向 departments 表中添加一条数据，部门名称为 market ，工作地点 ID 为 1。
insert into departments(department_name,location_id) values("market", 1);
2. 完全插入
`INSERT INTO  表名 VALUES(值 1 ，值 2 ，值 3......)`
注意：
`如果主键是自动增长，需要使用 default 或者 null 或者 0 占位。`
示例一：
向 departments 表中添加一条数据，部门名称为 development ，工作地点 ID 为 2 。使用 default 占位。
insert into departments values(default,"development",2);
示例二：
向 departments 表中添加一条数据，部门名称为human ，工作地点 ID 为 3 。使用 null 占 位。
insert into departments values(null,"human",3);
示例三：
向 departments 表中添加一条数据，部门名称为 teaching ，工作地点 ID 为 4 。使用 0 占 位。
insert into departments values(0,"teaching",4);
# 更新数据(UPDATE)
`UPDATE 表名 SET  列名=值，列名=值 WHERE 条件`
注意：
更新语句中一定要给定更新条件，否则表中的所有数据都会被更新。
示例：
更新 emp3 表中的 id 为 1 的数据，添加 address 为 BeiJing。
update emp3 set address = "BeiJing" where emp_id = 1;