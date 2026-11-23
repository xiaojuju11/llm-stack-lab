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
# 删除数据(DELETE)
DELETE删除数据
`DELETE FROM  表名 WHERE 条件`
注意：
在DELETE语句中，如果没有给定删除条件则会删除表中的所有数据。
示例：
删除 emp3 表中 emp_id 为 1 的雇员信息。
delete from emp3 where emp_id = 1;
- TRUNCATE清空表
`TRUNCATE TABLE  表名`
示例：
删除 emp3 表中的所有数据。
truncate table emp3;
- 清空表时DELETE与 TRUNCATE 区别
1. truncate 是整体删除(速度较快)， delete 是逐条删除(速度较慢)；
2. truncate 不写服务器 log，delete 写服务器 log，也就是 truncate 效率比 delete 高的原因；
3. truncate 是会重置自增值，相当于自增列会被置为初始值，又重新从 1 开始记录，而 不是接着原来的值。而 delete 删除以后， 自增值仍然会继续累加。
# MySQL查询数据
- SELECT语句的功能：
SELECT 语句从数据库中返回信息。使用一个 SELECT 语句，可以做下面的事：
1. 列选择：能够使用 SELECT 语句的列选择功能选择表中的列，这些列是想要用查询返回的。当查询时，能够返回列中的数据。
2. 行选择：能够使用 SELECT 语句的行选择功能选择表中的行，这些行是想要用查询返回的。能够使用不同的标准限制看见的行。
3. 连接：能够使用 SELECT 语句的连接功能来集合数据，这些数据被存储在不同的表中，在它们之间可以创建连接，查询出我们所关心的数据。
- SELECT基本语法：
基本 SELECT 语句：
在最简单的形式中，SELECT 语句必须包含下面的内容：
1. 一个 SELECT 子句，指定被显示的列
2. 一个 FROM 子句，指定表，该表包含 SELECT 子句中的字段列表
在语法中：
语句	含义
SELECT	 是一个或多个字段的列表
*	     选择所有的列
DISTINCT	禁止重复
column | expression	选择指定的字段或表达式
alias	给所选择的列不同的标题
FROM table	指定包含列的表
# 查询中的行选择
用 WHERE 子句限制从查询返回的行。一个 WHERE 子句包含一个必须满足的条件，WHERE 子句紧跟着 FROM 子句。如果条件是 true，返回满足条件的行。
在语法中：
WHERE 限制查询满足条件的行
condition 由列名、表达式、常数和比较操作组成
`SELECT * |  投影列 FROM  表名 WHERE  选择条件`
示例：
查询 departments 表中部门 ID 为 90 的部门名称与工作地点 ID。
select department_name,location_id from departments where department_id =4;
# 逻辑条件
逻辑条件组合两个比较条件的结果来产生一个基于这些条件的单个的结果，或者逆转一个单个条件的结果。当所有条件的结果为真时，返回行。
- SQL 的三个逻辑运算符是：
1. AND
2. OR
3. NOT
可以在 WHERE 子句中用 AND 和 OR 运算符使用多个条件。
示例一：
查询 employees 表中雇员薪水是 8000 的并且名字中含有e 的雇员名字与薪水。+
select last_name,salary from employees where salary = 8000 and last_name like '%e%';
示例二：
查询 employees 表中雇员薪水是 8000 的或者名字中含有e 的雇员名字与薪水。
select last_name,salary from employees where salary = 8000 or last_name like '%e%';
示例三：
查询 employees 表中雇员名字中不包含 u 的雇员的名字。
select last_name from employees where last_name not like '%u%';
# 使用 ORDER BY 排序
在一个不明确的查询结果中排序返回的行。ORDER BY 子句用于排序。如果使用了 ORDER BY 子句，它必须位于 SQL 语句的最后。

- SELECT 语句的执行顺序如下：
1. FROM 子句
2. WHERE 子句
3. SELECT 子句
4. ORDER BY 子句
示例一：
查询 employees 表中的所有雇员，显示他们的ID、名字与薪水，并按薪水升序排序。
select employee_id,last_name,salary from employees order by salary;
select employee_id,last_name,salary from employees order by salary asc;
示例二：
查询 employees 表中的所有雇员，显示他们的ID与名字，并按雇员名字降序排序。
select employee_id,last_name from employees order by last_name desc;
- 使用别名排序
示例：
显示雇员ID，名字。计算雇员的年薪，年薪列别名为annsal，并对该列进行升序排序，
select employee_id,last_name ,12*salary annsal from employees order by annsal;
- 多列排序
示例：
以升叙排序显示 DEPARTMENT_ID 列，同时以降序排序显示 SALARY 列。
select department_id,salary from employees order by department_id asc ,salary desc;

# 函数介绍
函数是 SQL 的一个非常强有力的特性，函数能够用于下面的目的：
- 执行数据计算
- 修改单个数据项
- 操纵输出进行行分组
- 格式化显示的日期和数字
- 转换列数据类型
SQL 函数有输入参数，并且总有一个返回值。

- 函数分类
1. 单行函数
单行函数仅对单个行进行运算，并且每行返回一个结果。
    - 常见的函数类型：
    - 字符
    - 数字
    - 日期
    - 转换
2. 多行函数 
多行函数能够操纵成组的行，每个行组给出一个结果，这些函数也被称为组函数。
# 字符函数
1. 大小写处理函数
函数	描述	实例
LOWER(s)|LCASE(s)	将字符串 s 转换为小写	将字符串 OLDLU转换为小写：SELECT LOWER("OLDLU"); -- oldlu
UPPER(s)|UCASE(s)	将字符串s转换为大写	将字符串 oldlu转换为大写：SELECT UPPER("oldlu"); -- OLDLU
示例：
显示雇员 Davies 的雇员号、姓名和部门号，将姓名转换为大写。
select employee_id,UPPER(last_name),department_id from employees where last_name = 'davies';
2. 字符处理函数
函数	描述	实例
LENGTH(s)	返回字符串 s 的长度	返回字符串oldlu的字符数SELECT LENGTH("oldlu"); --5;
CONCAT(s1,s2...sn)	字符串 s1,s2 等多个字符串合并为一个字符串	合并多个字符串SELECT CONCAT("sxt ", "teacher ", "oldlu"); --sxt teacher oldlu;
LPAD(s1,len,s2)	在字符串 s1 的开始处填充字符串 s2，使字符串长度达到 len	将字符串 x 填充到 oldlu字符串的开始处：SELECT LPAD('oldlu',8,'x'); -- xxxoldlu
LTRIM(s)	去掉字符串 s 开始处的空格	去掉字符串 oldlu开始处的空格：SELECT LTRIM(" oldlu") ;-- oldlu
REPLACE(s,s1,s2)	将字符串 s2 替代字符串 s 中的字符串 s1	将字符串 oldlu 中的字符 o 替换为字符 O：SELECT REPLACE('oldlu','o','O'); --Oldlu
REVERSE(s)	将字符串s的顺序反过来	将字符串 abc 的顺序反过来：SELECT REVERSE('abc'); -- cba
RPAD(s1,len,s2)	在字符串 s1 的结尾处添加字符串 s2，使字符串的长度达到 len	将字符串 xx填充到 oldlu字符串的结尾处：SELECT RPAD('oldlu',8,'x'); -- oldluxxx
RTRIM(s)	去掉字符串 s 结尾处的空格	去掉字符串 oldlu 的末尾空格：SELECT RTRIM("oldlu "); -- oldlu
SUBSTR(s, start, length)	从字符串 s 的 start 位置截取长度为 length 的子字符串	从字符串 OLDLU中的第 2 个位置截取 3个 字符：SELECT SUBSTR("OLDLU", 2, 3); -- LDL
SUBSTRING(s, start, length)	从字符串 s 的 start 位置截取长度为 length 的子字符串	从字符串 OLDLU中的第 2 个位置截取 3个 字符：SELECT SUBSTRING("OLDLU", 2, 3); --LDL
TRIM(s)	去掉字符串 s 开始和结尾处的空格	去掉字符串 oldlu 的首尾空格：SELECT TRIM(' oldlu ');--oldlu
示例：
显示所有工作岗位名称从第 4 个字符位置开始，包含字符串 REP的雇员的ID信息，将雇员的姓和名连接显示在一起，还显示雇员名的的长度，以及名字中字母 a 的位置。
SELECT employee_id, CONCAT(last_name，first_name) NAME, 
job_id, LENGTH(last_name),INSTR(last_name, 'a') "Contains 'a'?" FROM employees WHERE SUBSTR(job_id, 4) = 'REP';
# 数字函数
函数名	描述	实例
ABS(x)	返回 x 的绝对值	返回 -1 的绝对值：SELECT ABS(-1) -- 返回1
ACOS(x)	求 x 的反余弦值(参数是弧度)	SELECT ACOS(0.25);
ASIN(x)	求反正弦值(参数是弧度)	SELECT ASIN(0.25);
ATAN(x)	求反正切值(参数是弧度)	SELECT ATAN(2.5);
ATAN2(n, m)	求反正切值(参数是弧度)	SELECT ATAN2(-0.8, 2);
AVG(expression)	返回一个表达式的平均值，expression 是一个字段	返回 Products 表中Price 字段的平均值：SELECT AVG(Price) AS AveragePrice FROM Products;
CEIL(x)	返回大于或等于 x 的最小整数	SELECT CEIL(1.5) -- 返回2
CEILING(x)	返回大于或等于 x 的最小整数	SELECT CEILING(1.5); -- 返回2
COS(x)	求余弦值(参数是弧度)	SELECT COS(2);
COT(x)	求余切值(参数是弧度)	SELECT COT(6);
COUNT(expression)	返回查询的记录总数，expression 参数是一个字段或者 * 号	返回 Products 表中 products 字段总共有多少条记录：SELECT COUNT(ProductID) AS NumberOfProducts FROM Products;
DEGREES(x)	将弧度转换为角度	SELECT DEGREES(3.1415926535898) -- 180
n DIV m	整除，n 为被除数，m 为除数	计算 10 除于 5：SELECT 10 DIV 5; -- 2
EXP(x)	返回 e 的 x 次方	计算 e 的三次方：SELECT EXP(3) -- 20.085536923188
FLOOR(x)	返回小于或等于 x 的最大整数	小于或等于 1.5 的整数：SELECT FLOOR(1.5) -- 返回1
GREATEST(expr1, expr2, expr3, ...)	返回列表中的最大值	返回以下数字列表中的最大值：SELECT GREATEST(3, 12, 34, 8, 25); -- 34返回以下字符串列表中的最大值：SELECT GREATEST("Google", "Runoob", "Apple"); -- Runoob
LEAST(expr1, expr2, expr3, ...)	返回列表中的最小值	返回以下数字列表中的最小值：SELECT LEAST(3, 12, 34, 8, 25); -- 3返回以下字符串列表中的最小值：SELECT LEAST("Google", "Runoob", "Apple"); -- Apple
LN	返回数字的自然对数，以 e 为底。	返回 2 的自然对数：SELECT LN(2); -- 0.6931471805599453
LOG(x) 或 LOG(base, x)	返回自然对数(以 e 为底的对数)，如果带有 base 参数，则 base 为指定带底数。	SELECT LOG(20.085536923188) -- 3 SELECT LOG(2, 4); -- 2
LOG10(x)	返回以 10 为底的对数	SELECT LOG10(100) -- 2
LOG2(x)	返回以 2 为底的对数	返回以 2 为底 6 的对数：SELECT LOG2(6); -- 2.584962500721156
MAX(expression)	返回字段 expression 中的最大值	返回数据表 Products 中字段 Price 的最大值：SELECT MAX(Price) AS LargestPrice FROM Products;
MIN(expression)	返回字段 expression 中的最小值	返回数据表 Products 中字段 Price 的最小值：SELECT MIN(Price) AS MinPrice FROM Products;
MOD(x,y)	返回 x 除以 y 以后的余数	5 除于 2 的余数：SELECT MOD(5,2) -- 1
PI()	返回圆周率(3.141593）	SELECT PI() --3.141593
POW(x,y)	返回 x 的 y 次方	2 的 3 次方：SELECT POW(2,3) -- 8
POWER(x,y)	返回 x 的 y 次方	2 的 3 次方：SELECT POWER(2,3) -- 8
RADIANS(x)	将角度转换为弧度	180 度转换为弧度：SELECT RADIANS(180) -- 3.1415926535898
RAND()	返回 0 到 1 的随机数	SELECT RAND() --0.93099315644334
ROUND(x)	返回离 x 最近的整数	SELECT ROUND(1.23456) --1
SIGN(x)	返回 x 的符号，x 是负数、0、正数分别返回 -1、0 和 1	SELECT SIGN(-10) -- (-1)
SIN(x)	求正弦值(参数是弧度)	SELECT SIN(RADIANS(30)) -- 0.5
SQRT(x)	返回x的平方根	25 的平方根：SELECT SQRT(25) -- 5
SUM(expression)	返回指定字段的总和	计算 OrderDetails 表中字段 Quantity 的总和：SELECT SUM(Quantity) AS TotalItemsOrdered FROM OrderDetails;
TAN(x)	求正切值(参数是弧度)	SELECT TAN(1.75); -- -5.52037992250933
TRUNCATE(x,y)	返回数值 x 保留到小数点后 y 位的值（与 ROUND 最大的区别是不会进行四舍五入）	SELECT TRUNCATE(1.23456,3) -- 1.234
1. ROUND(column|expression, n) 函数
ROUND 函数四舍五入列、表达式或者 n 位小数的值。如果第二个参数是 0 或者缺少，值被四舍五入为整数。如果第二个参数是 2值被四舍五入为两位小数。如果第二个参数是–2，值被四舍五入到小数点左边两位。
SELECT ROUND(45.923,2), ROUND(45.923,0),ROUND(45.923,-1);
45.92   46  46
2. TRUNCATE(column|expression,n) 函数
TRUNCATE函数的作用类似于 ROUND 函数。如果第二个参数是 0 或者缺少，值被截断为整数。如果第二个参数是 2，值被截断为两位小数。如果第二个参数是–2，值被截断到小数点左边两位。与 ROUND 最大的区别是不会进行四舍五入。
SELECT TRUNCATE(45.923,2);
45.92
3. MOD(m,n) 函数
MOD 函数找出m 除以n的余数。
示例：
所有job_id是SA_REP的雇员的名字，薪水以及薪水被5000除后的余数。
SELECT last_name, salary, MOD(salary, 5000) FROM employees
WHERE job_id = 'SA_REP';
# 日期函数
在MySQL中允许直接使用字符串表示日期，但是要求字符串的日期格式必须为：‘YYYY-MM-DD HH:MI:SS’ 或者‘YYYY/MM/DD HH:MI:SS’;
函数名	描述	实例
CURDATE()	返回当前日期	SELECT CURDATE(); -> 2018-09-19
CURTIME()	返回当前时间	SELECT CURTIME(); -> 19:59:02
CURRENT_DATE()	返回当前日期	SELECT CURRENT_DATE(); -> 2018-09-19
CURRENT_TIME()	返回当前时间	SELECT CURRENT_TIME(); -> 19:59:02
DATE()	从日期或日期时间表达式中提取日期值	SELECT DATE("2017-06-15"); -> 2017-06-15
DATEDIFF(d1,d2)	计算日期 d1->d2 之间相隔的天数	SELECT DATEDIFF('2001-01-01','2001-02-02') -> -32
DAY(d)	返回日期值 d 的日期部分	SELECT DAY("2017-06-15"); -> 15
DAYNAME(d)	返回日期 d 是星期几，如 Monday,Tuesday	SELECT DAYNAME('2011-11-11 11:11:11') ->Friday
DAYOFMONTH(d)	计算日期 d 是本月的第几天	SELECT DAYOFMONTH('2011-11-11 11:11:11') ->11
DAYOFWEEK(d)	日期 d 今天是星期几，1 星期日，2 星期一，以此类推	SELECT DAYOFWEEK('2011-11-11 11:11:11') ->6
DAYOFYEAR(d)	计算日期 d 是本年的第几天	SELECT DAYOFYEAR('2011-11-11 11:11:11') ->315
HOUR(t)	返回 t 中的小时值	SELECT HOUR('1:2:3') -> 1
LAST_DAY(d)	返回给给定日期的那一月份的最后一天	SELECT LAST_DAY("2017-06-20"); -> 2017-06-30
MONTHNAME(d)	返回日期当中的月份名称，如 November	SELECT MONTHNAME('2011-11-11 11:11:11') -> November
MONTH(d)	返回日期d中的月份值，1 到 12	SELECT MONTH('2011-11-11 11:11:11') ->11
NOW()	返回当前日期和时间	SELECT NOW() -> 2018-09-19 20:57:43
SECOND(t)	返回 t 中的秒钟值	SELECT SECOND('1:2:3') -> 3
SYSDATE()	返回当前日期和时间	SELECT SYSDATE() -> 2018-09-19 20:57:43
TIMEDIFF(time1, time2)	计算时间差值	SELECT TIMEDIFF("13:10:11", "13:10:10"); -> 00:00:01
TO_DAYS(d)	计算日期 d 距离 0000 年 1 月 1 日的天数	SELECT TO_DAYS('0001-01-01 01:01:01') -> 366
WEEK(d)	计算日期 d 是本年的第几个星期，范围是 0 到 53	SELECT WEEK('2011-11-11 11:11:11') -> 45
WEEKDAY(d)	日期 d 是星期几，0 表示星期一，1 表示星期二	SELECT WEEKDAY("2017-06-15"); -> 3
WEEKOFYEAR(d)	计算日期 d 是本年的第几个星期，范围是 0 到 53	SELECT WEEKOFYEAR('2011-11-11 11:11:11') -> 45
YEAR(d)	返回年份	SELECT YEAR("2017-06-15"); -> 2017
示例一：
向 employees 表中添加一条数据，雇员ID：300，名字：kevin ，email：kevin@sxt.cn ，入职时间：2049-5-1 8:30:30，工作部门：‘IT_PROG’。
insert into employees(EMPLOYEE_ID,last_name,email,HIRE_DATE,JOB_ID) values(300,'kevin','kevin@sxt.cn','2049-5-1 8:30:30','IT_PROG');
# 通用函数
函数名	描述	实例
IF(expr,v1,v2)	如果表达式 expr 成立，返回结果 v1；否则，返回结果 v2。	SELECT IF(1 > 0,'正确','错误') ->正确
IFNULL(v1,v2)	如果 v1 的值不为 NULL，则返回 v1，否则返回 v2。	SELECT IFNULL(null,'Hello Word') ->Hello Word
ISNULL(expression)	判断表达式是否为 NULL	SELECT ISNULL(NULL); ->1
NULLIF(expr1, expr2)	比较两个参数是否相同，如果参数 expr1 与 expr2 相等 返回 NULL，否则返回 expr1	SELECT NULLIF(25, 25); ->
COALESCE(expr1, expr2, ...., expr_n)	返回参数中的第一个非空表达式（从左向右）	SELECT COALESCE(NULL, NULL, NULL, 'bjsxt.com', NULL, 'google.com'); -> bjsxt.com
CASE expression WHEN condition1 THEN result1 WHEN condition2 THEN result2 ... WHEN conditionN THEN resultN ELSE result END	CASE 表示函数开始，END 表示函数结束。如果 condition1 成立，则返回 result1, 如果 condition2 成立，则返回 result2，当全部不成立则返回 result，而当有一个成立之后，后面的就不执行了。	SELECT CASE 'oldlu' WHEN 'oldlu' THEN 'OLDLU' WHEN 'admin' THEN 'ADMIN' ELSE 'kevin' END;

示例一：
查询部门编号是50或者80的员工信息，包含他们的名字、薪水、佣金。在income列中，如果有佣金则显示‘SAL+COMM’，无佣金则显示'SAL'。
SELECT last_name, salary, commission_pct,     if(ISNULL(commission_pct),
'SAL','SAL+COMM') income 
FROM employees 
WHERE department_id IN (50, 80);
示例二：
计算雇员的年报酬，你需要用 12 乘以月薪，再加上它的佣金 (等于年薪乘以佣金百分比)。
SELECT last_name, salary, IFNULL(commission_pct, 0), (salary*12) +(salary*12*IFNULL(commission_pct, 0)) AN_SAL 
FROM employees;
示例三
查询员工表，显示他们的名字、名字的长度该列名为expr1，姓氏、姓氏的长度该列名为expr2。在result列中，如果名字与姓氏的长度相同则显示空，如果不相同则显示名字长度。
SELECT first_name, LENGTH(first_name) "expr1",
    last_name, LENGTH(last_name) "expr2",    NULLIF(LENGTH(first_name), LENGTH(last_name)) result
FROM employees;
示例四：
查询员工表，显示他们的名字，如果 COMMISSION_PCT 值是非空，显示它。如果COMMISSION_PCT 值是空，则显示 SALARY 。如果 COMMISSION_PCT 和SALARY 值都是空，那么显示 10。在结果中对佣金列升序排序。
SELECT last_name,
COALESCE(commission_pct, salary, 10) comm 
FROM employees 
ORDER BY commission_pct;
示例五：
查询员工表，如果 JOB_ID 是 IT_PROG，薪水增加 10%；如果 JOB_ID 是 ST_CLERK，薪水增加 15%；如果 JOB_ID 是 SA_REP，薪水增加 20%。对于所有其他的工作角色，不增加薪水。
SELECT last_name, job_id, salary, 
    CASE job_id WHEN 'IT_PROG' THEN 1.10*salary 
          WHEN 'ST_CLERK' THEN 1.15*salary 
          WHEN 'SA_REP' THEN 1.20*salary 
    ELSE salary END "REVISED_SALARY"
FROM employees;
 
 