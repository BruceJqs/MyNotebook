---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 05 : Advanced SQL

## Accessing SQL from Programming Languages

数据库程序员必须能够掌握通用编程语言，至少有两个原因：

- 并非所有查询都可以用 SQL 表示，因为 SQL 不能提供通用语言的全部表达能力
- 非声明性操作（比如打印报告、与用户交互或将查询结果发送到图形用户界面）不能在 SQL 中完成

有两种方法可以从通用编程语言访问数据库：

- API（应用程序接口）——通用程序可以使用函数集合连接到数据库服务器并与之通信，程序可以在**运行时**（Runtime）用字符串**构造** SQL 查询，**提交**查询，并且将检索到的结果放到程序变量中（一次仅存一个元组）。动态 SQL 有以下标准：
	- **JDBC**：Java 用于连接数据库的 API
	- **ODBC**：原来为 C 写的用于连接数据库的 API，现在也适用于 C++、C#、Ruby、Go、PHP、VB 等
- 嵌入式 SQL——提供程序与数据库服务器交互的方法
	- SQL 语句在编译时转换为函数调用
	- 在运行时，这些函数调用使用提供动态 SQL 工具的 API 连接到数据库
***
### JDBC

- JDBC 是一个 Java API，用于与支持 SQL 的数据库系统进行通信
- JDBC 支持用于查询和更新数据以及检索查询结果的各种功能
- JDBC 还支持元数据检索，例如查询数据库中存在的关系以及关系属性的名称和类型
***
#### Model

JDBC一般与数据库通信的模型如下：

1. 打开连接
2. 创建 “Statement” 对象
3. 使用 Statement 对象执行查询以发送查询并获取结果
4. 用于处理错误的异常机制

> 在下面的程序中，必须在开头处导入 `java.sql.*`，里面包含了 JDBC 提供的功能接口定义

```java title="JDBC Example"
public static void JDBCexample(String dbid, String userid, String passwd)
{
	 try {
		Connection conn = DriverManager.getConnection(
			"jdbc:oracle:thin:@db.yale.edu:2000:univdb", userid, passwd);
		Statement stmt = conn.createStatement();
		… Do Actual Work ….
		stmt.close(); 
		conn.close(); 
	}

	catch (SQLException sqle) {
		System.out.println("SQLException : " + sqle); 
	}
}
```

!!! note ""

	=== "Database Connection"
	
		在 Java 程序中访问数据库的第一步是建立与数据库的**连接**，连接好后才能执行 SQL 语句。具体来说，需要使用 `DriverManager` 类的 `getConnection()` 方法，它接收以下参数：
		
		- 数据库服务器相关信息，包括 URL/ 机器名、协议、端口号、数据库名
			- JDBC 并没有规定协议，协议取决于数据库实现
			- JDBC 支持多种协议，比如 `jdbc:oracle:thin` 是 Oracle 支持的协议，而 `jdbc:mysql` 是 MySQL 支持的协议等
		- 数据库用户名
		- 密码
		- 返回一个 `Connection` 对象，用于与数据库通信
	
	=== "SQL Statements"
	
		建立连接后，就要将 SQL 语句发送到数据库系统，然后在里面执行语句，在 Java 中通过 `Statement` 类的实例来做到这一点。`Statement` 对象并非 SQL 语句本身，而是一种让 Java 程序调用和**传送** SQL 语句到数据库相关的方法的对象
		
		而执行语句需要调用 `executeQuery()` 或 `executeUpdate()` 方法，它们分别对应**查询语句**和**非查询语句**（更新、插入、删除、创建等）的执行，并且后者会返回一个表示被插入 / 更新 / 删除的元组数（如果是创建语句的话则返回 0）
	
	=== "Exceptions"
	
		- 执行任何的 SQL 语句都有可能抛出异常，所以编程时需要记得用 `try {...} catch {...}` 语句块捕获异常
		- 异常可以分为 `SQLException`（与 SQL 相关的异常）和 `Exception`（一般的异常，与 Java 相关，比如空指针、数组越界等）
		- 如果可以的话，最好编写一个完整的异常处理函数，以应对各种异常
	
	=== "Resource Management"
	
		- 建立连接、创建语句以及其他 JDBC 对象都会占用系统资源，所以需要确保程序能够关闭上述这些资源，以免产生资源池耗尽导致的故障
		- 一种方法是显式调用关闭语句（比如 `conn.close()`、`stmt.close()` 分别关闭连接和语句），但一旦遇到异常，提前退出的话，这些关闭语句就来不及被调用，那么问题还是没解决
		- 更可靠的做法是使用 **try-with-resources 构造块**，就是在 `try` 关键字和语句块之间加上**圆括号**，里面包含连接、语句对象等资源，这样的话当离开 `try` 语句块时，这些资源会被自动关闭
***
#### Update

```java title="Update to Database"
try {
	stmt.executeUpdate(
		"insert into instructor values(’77987’, ’Kim’, ’Physics’, 98000)");  
}

catch (SQLException sqle)  
{
	System.out.println("Could not insert tuple. " + sqle);  
}
```
***
#### Query

```java title="Execute Query and Fetch and Print Results"
ResultSet rset = stmt.executeQuery(  
						"select dept_name, avg (salary)  
						from instructor  
						group by dept_name");  
while (rset.next()) {
	System.out.println(rset.getString("dept_name") + " " + rset.getFloat(2));  
}
```

- 使用 `executeQuery()` 方法执行查询后，检索得到的元组会放在一个 `ResultSet` 对象上，但一次只能取其中的一个元组。
- 具体来说，该对象调用 `next()` 方法获取下一个元组（如果还有的话），返回值是一个布尔值，表明是否成功获取元组。
- 另外，该对象提供了一些以 `get` 开头的方法来获取元组中具体属性的值，它们接收单个参数，可以是属性名（字符串），也可以是属性的位置（整数值从 1 开始）。常见的 `get` 方法有：
    - `getString()`：可以检索任意 SQL 基本数据类型
    - `getFloat()`：仅限于获取浮点数

```java title="Getting Result Fields"
rset.getString(“dept_name”)
rset.getString(1)
```

> 如果 dept_name 是 select result 的第一个参数，上面这两行语句是等价的

对于 Null 值，可以使用 `wasNull()` 方法来检查是否获取到了 Null 值：

```java title="Dealing With Null Values"
int a = rset.getInt(“a”);
if (rset.wasNull()) 
	Systems.out.println(“Got null value”);
```
***
#### Prepared Statement

我们不必预先编写一条完整的 SQL 语句，而先创建一条**预备语句**（Prepared Statements），其中语句中出现的值用 `?` 替代（占位符），之后再将具体的值插入到对应的位置上。数据库系统会编译好这种预备语句。在执行这种语句的时候，数据库系统复用先前编译好的预备语句，然后将具体值应用到到语句中，构成一条完整的语句。

- `Connection` 类的 `prepareStatement()` 方法用于设置预备语句，该方法返回的是一个 `PreparedStatement` 类的对象，该对象同样具有 `executeQuery()` 和 `executeUpdate()` 方法
- 在 `prepareStatement()` 语句内的 SQL 语句具体值必须用 `?` 替代，之后可以用 `set` 开头的方法来设置具体值（比如 `setInt()`、`setString()`）。这类方法接收两个参数，第 1 个参数指明设置的是第几个 `?`（从 1 开始），第 2 个参数是具体值

```java title="Prepared Statement Example"
PreparedStatement pStmt = conn.prepareStatement(
    "INSERT INTO instructor VALUES(?, ?, ?, ?)"
);
pStmt.setString(1, "88877");
pStmt.setString(2, "Perry");
pStmt.setString(3, "Finance");
pStmt.setInt(4, 125000);
pStmt.executeUpdate();
pStmt.setString(1, "88878");
pStmt.executeUpdate();
```

- 在上面的例子中执行了两条插入语句，其中第二条插入语句用 SQL 语法表示为：

```sql
INSERT INTO instructor VALUES("88878", "Perry", "Finance", 125000);
```

!!! warning "Warning"

	- 在获取用户输入并将其添加到查询时，请始终使用预备语句
	
	切勿通过连接作为输入获取的字符串来创建查询，例如：`insert into instructor values(’ " + ID + " ’, ’ " + name + " ’, " + " ’ " + dept name + " ’, " + salary + ");`
	
	这时候，如果 name 字段为 `D’Souza`，那么查询就会变成：`insert into instructor values(’ 88879 ’, ’ D’Souza ’, ’ Finance ’, 125000);`，这会导致 SQL 语法错误
	
	- 事实上，这就是著名的 SQL 注入攻击，攻击者可以通过输入恶意字符串来执行任意 SQL 语句，比如删除表、插入数据等
***
#### SQL Injection

假如在 Java 程序中执行这样一条 SQL 语句：

```java
"SELECT * FROM instructor WHERE name = '" + name + "'"
```

其中 `name` 是字符串变量

!!! example "Example"

	如果 `name = "X' OR 'Y' = 'Y"`，那么最终的语句就会变成：
	
	```java
	"SELECT * FROM instructor WHERE name = '" + "X' OR 'Y' = 'Y" + "'"
	```
	
	整理得：
	
	```java
	"SELECT * FROM instructor WHERE name = 'X' OR 'Y' = 'Y'
	```
	
	由于 `WHERE` 子句恒为 `true`，因此查询语句就能被执行，表里的全部内容都能被查到
	
	如果使用预备语句及其 `set` 方法时，上述问题就不会发生了，因为所有输入的引号都会被转化为转义字符，不会破坏原字符串的结构。
***
#### Metadata Features

通常，Java 程序会在运行时，从数据库系统中获取数据声明

用于存储执行查询语句的结果的 `ResultSet` 接口有一个方法 `getMetaData()`，它返回一个 `ResultSetMetaData` 类对象，里面包含结果集的**元数据**（Metadata）。而这个 `ResultSetMetaData` 对象也有一些寻找元数据信息的方法，比如结果的列数、具体列的名称和类型等等，这样我们就能获取数据声明（即模式，Schema）了

!!! example "Example"

	执行 Query 获取 ResultSet（重命名为 rs）之后：
	
	```java title="ResultSet Metadata"
	ResultSetMetaData rsmd = rs.getMetaData();
	for (int i = 1; i <= rsmd.getColumnCount(); i++) {
	    System.out.println(rsmd.getColumnName(i));
	    System.out.println(rsmd.getColumnTypeName(i));
	}
	```
	
	- `getColumnCount()` 方法返回元数（Arity）（即列数）
	- `getColumnName()` 和 `getColumnTypeName()` 分别获取列名和数据类型名，它们都接收单个表示列位置的整型参数（从 1 开始）

`Connection` 接口有一个方法 `getMetaData()`，它返回一个 `DatabaseMetaData` 对象。而 `DatabaseMetaData` 接口则提供了寻找数据库元数据的途径，提供了更为丰富的方法，比如返回产品名、版本号等等

!!! example "Example"

	```java title="Database Metadata"
	DatabaseMetaData dbmd = conn.getMetaData();
	ResultSet rs = dbmd.getColumns(null, "univdb", "department", "%");
	
	while (rs.next()) {
	    System.out.println(rs.getString("COLUMN_NAME"), rs.getString("TYPE_NAME"));
	}
	```
	
	- `getColumns()` 方法接收四个参数
	    - 目录名：`null` 表示忽略该值
	    - 模式名
	    - 表名
	    - 列名：这里的 `%` 表示获取所有列

`DatabaseMetaData` 还有其他方法：

- `getTables()`：列出数据库中的所有表。前三个参数和 `getColumns()` 一致，最后一个参数用于限制符合条件的表，如果设为 `null` 则返回所有表（包括系统内部的表）
- `getPrimaryKeys()`：获取主键
- `getCrossReference()`：获取外键参照
***
#### Transaction Control

- 默认情况下，每个 SQL 语句都被视为自动提交的单独事务，这对于具有多个更新的事务来说是个比较麻烦的事情
- 我们可以在 Connection 中关闭自动提交
	- conn.setAutoCommit(false); 
- 然后，我们必须显式提交或回滚事务
	- conn.commit(); 
	- 或 conn.rollback();
- conn.setAutoCommit(true) 表示开启自动提交
***
### SQLJ

> JDBC 有时过于动态，编译器无法很好地捕获错误

在 Java 中，也提供了嵌入式的 SQL 语句，这种语句称为 SQLJ

!!! example "Example"

	```java title="SQLJ Example"
	#sql iterator deptInfoIter ( String dept name, int avgSal);
	deptInfoIter iter = null;
	#sql iter = { select dept_name, avg(salary) as avgSal from instructor group by dept name };
	while (iter.next()) {
		String deptName = iter.dept_name();
		int avgSal = iter.avgSal();
		System.out.println(deptName + " " + avgSal);
		
	}  
	iter.close();
	```
***
### ODBC

- 开放数据库连接（Open Database Connectivity，ODBC）标准
	- 应用程序与数据库服务器通信的标准
	- 当客户端程序发起 ODBC API 的调用时，库代码便与服务器通信，执行需要执行的动作，并返回结果
- 应用于 GUI、电子表格等应用程序
- ODBC 最初为 Basic 和 C 定义，可用于多种语言
- 每个支持 ODBC 的数据库系统都提供了一个必须与客户端程序链接的“驱动程序”库

![](../../../assets/Pasted%20image%2020250317110348.png)

- 当客户端程序进行 ODBC API 调用时，库中的代码将与服务器通信以执行请求的作并获取结果
- ODBC 程序首先分配一个 SQL 环境，然后分配一个数据库连接处理器
- 使用 SQLConnect() 打开数据库连接
	- SQLConnect 的参数：
		- 连接处理器
		- 要连接的服务器
		- 用户标识符
		- 密码
	- 还必须指定参数的类型：SQL_NTS，表示前一个参数是以 null 结尾的字符串
***
#### Model

```c title="ODBC Model"
int ODBCexample() {
    RETCODE error;
    HENV env;     /* environment */
    HDBC conn;     /* database connection */

    SQLAllocEnv(&env);
    SQLAllocConnect(env, &conn);
    SQLConnect(conn, "db.yale.edu", SQL_NTS, "avi", SQL_NTS, "avipassswd", SQL_NTS);
    {… Do actual work …}
    
    SQLDisconnect(conn);
    SQLFreeConnect(conn);
    SQLFreeEnv(env);
}
```

- 程序使用 SQLExecDirect 向数据库发送 SQL 命令
- 使用 SQLFetch() 获取结果元组
- SQLBindCol() 将 C 语言变量绑定到查询结果的属性
	- 当获取 Tuples 时，其 attribute 值会自动存储在相应的 C 变量中
	- SQLBindCol() 的参数：
		- ODBC stmt 变量，查询结果中的属性位置
		- 从 SQL 到 C 的类型转换
		- 变量的地址
		- 对于字符数组等可变长度类型，
			- 变量的最大长度
			- 用于在获取元组时存储实际长度的位置
			- 注： Length 字段返回负值表示该字段为 null 值
***
#### Actual Work

```c title="Actual Work"
char deptname[80];
float salary;
int lenOut1, lenOut2;
HSTMT stmt;

char * sqlquery = "SELECT dept_name, SUM(salary)"
				  "FROM instructor"
				  "GROUP BY dept_name";
SQLAllocStmt(conn, &stmt);
error = SQLExecDirect(stmt, sqlquery, SQL_NTS);
if (error == SQL_SUCCESS) {
	SQLBindCol(stmt, 1, SQL_C_CHAR, deptname, 80, &lenOut1);
	SQLBindCol(stmt, 2, SQL_C_FLOAT, &salary, 0, &lenOut2);
	while (SQLFetch(stmt) == SQL_SUCCESS) {
		printf(" %s %g\n", deptname, salary);
	}
}
SQLFreeStmt(stmt, SQL_DROP);
```
***
#### ODBC Prepared Statements

- 预备语句
	- SQL 语句在数据库中已经编译好
	- 可以有占位符：例如 `insert into account values(?,?,?)`
	- 使用占位符的实际值重复执行
- 使用 SQLPrepare() 准备预备语句
	- `SQLPrepare(stmt, <SQL String>);`
- 绑定参数
	- `SQLBindParameter(stmt, <parameter#>, … type information and value omitted for simplicity..)`
- 执行语句
	- `retcode = SQLExecute(stmt);`
***
#### More ODBC Features

- 元数据功能：
	- 查找数据库中的所有关系，并在数据库中查找查询结果或关系的列的名称和类型
- 默认情况下，每个 SQL 语句都被视为自动提交的单独事务
	- 可以关闭连接上的自动提交
		- SQLSetConnectOption(conn, SQL_AUTOCOMMIT, 0)
	- 事务必须由 SQLTransact(conn, SQL_COMMIT) 或 SQLTransact(conn, SQL_ROLLBACK)
***
### Embedded SQL

- SQL 标准定义了 SQL 在各种编程语言（如 C、C++、Java、Fortran 和 PL/1）中的嵌入
- 嵌入 SQL 查询的语言称为主机语言，主机语言中允许的 SQL 结构包括嵌入式 SQL
- 这些语言的基本形式遵循在操作系统 R 将 SQL 嵌入到 PL/1 中的形式
- EXEC SQL 语句在主机语言中用于标识对预处理器的嵌入式 SQL 请求：
	- `EXEC SQL <嵌入式 SQL 语句>;`
	- 这样的语句因语言而异
- 在某些语言（如 COBOL）中，分号被 END-EXEC 替换
- 在 Java 中，嵌入使用 `#SQL { .... };` ；在 C 中，使用 `EXEC SQL <embedded SQL statement>;`
- 在执行任何 SQL 语句之前，程序必须首先连接到数据库
- 这是通过以下方式完成的： 
	- 使用密码的 EXEC-SQL 连接到服务器用户用户名;
	- 此处，server 标识要建立连接的服务器
***
#### Variables

- 主机语言的变量可以在嵌入式 SQL 语句中使用
	- 它们前面有冒号以区别于SQL变量（例如 `:credit_amount`）
- 如上所述使用的主机变量必须在 DECLARE 部分中声明，如下面所示。但是，用于声明变量的语法遵循通常的主机语言语法

```sql title="Embedded SQL Example"
EXEC SQL BEGIN DECLARE SECTION;
	int account_number;
	float credit_amount;
EXEC SQL END DECLARE SECTION;
```
****
#### Query

- 要编写嵌入式 SQL 查询，我们使用 `declare c cursor for <SQL query>` 语句，其中变量 c 用于标识查询

!!! example "Example"

	- 在主机语言中，查找完成超过主机语言中变量 credit_amount 中存储的学分的学生的 ID 和姓名
	- 在 SQL 中指定查询，如下所示：
	
	```sql
	EXEC SQL
	declare c cursor for
	select ID, name
	from student
	where tot_cred > :credit_amount;
	```
***
#### Open and Fetch

open 语句如下所示：

```sql
EXEC SQL OPEN c;
```

此语句使数据库系统执行查询并将结果保存在临时关系中，查询在执行 open 语句时使用主机语言变量 credit-amount 的值

fetch 语句导致将查询结果中一个元组的值放在主机语言变量上：

```sql
EXEC SQL FETCH c INTO :si, :sn;
```

重复调用 fetch 可以获取查询结果中的连续元组
***
#### Close

SQL 通信区域 （SQL Communication Area, SQLCA）中名为 SQLSTATE 的变量设置为“02000”，以指示没有更多数据

我们可以用 close 语句会导致数据库系统删除保存查询结果的临时关系：

```sql
EXEC SQL CLOSE c;
```
***
#### Update

- 嵌入式 SQL 表达式也可以用于数据库修改（更新、插入和删除）
- 可以通过声明游标用于更新 cursor 获取的元组

```sql
EXEC SQL
declare c cursor for
select * from instructor 
where dept_name = 'Music'  
for update
```

- 然后，我们通过在 cursor 上执行 fetch 操作来迭代元组，在获取每个元组之后，我们执行以下代码：

```sql
update instructor
set salary = salary + 1000
where current of c
```
***
## Procedural Constructs in SQL

### Procedural Extensions and Stored Procedures

- SQL 提供模块语言
	- 允许在 SQL 中定义过程，使用 if-then-else 语句、for 和 while 循环等
- 存储过程
	- 可以在数据库中存储过程
	- 然后使用 call 语句执行它们
	- 允许外部应用程序在不知道内部详细信息的情况下对数据库进行操作
***
### Functions and Procedures

- 函数和过程允许将 “业务逻辑（Business Logic）” 存储在数据库中，并根据 SQL 语句执行
- 这些可以由 SQL 的过程组件或外部编程语言（如 Java、C 或 C++）定义
- 我们在这里介绍的语法由 SQL 标准定义
	- 大多数数据库都实现此语法的非标准版本
***
#### SQL Functions

!!! example "Example"

	- 定义一个函数，该函数在给定部门名称的情况下，返回该部门中的老师人数总数
	
	```sql
	// Declaration
	create function dept_count(dept_name varchar(20))
		return integer
		begin
		declare d_count interger;
			select count(*) into d_count
			from instructor
			where instructor.dept_name = dept_name;
		return d_count;
		end
	
	// Invocation
	select dept_name, budget
	from department
	where dept_count(dept_name) > 12;
	```

此外，SQL 标准还支持将表作为返回结果的函数，这样的函数称为**表函数**（Table Functions），也可以看作是带参数的实体化视图。具体的函数定义和调用如下所示：

!!! example "Example"

	SQL 还可以将表格作为返回值，这样的比如返回给定客户拥有的所有账户：
	
	```sql
	// Declaration
	create function instructor_of(dept_name varchar(20))
	    returns table(
	        ID varchar(5),
	        name varchar(20),
	        dept_name varchar(20),
	        salary numeric(8, 2)
	    )
	    return table(
	        select ID, name, dept_name, salary
	        from instructor
	        where instructor.dept_name = instructor_of.dept_name
	    );
	
	// Invocation
	select *
	from table(instructor_of('Finance'));
	```
	
	- 在函数定义内使用参数时，如果参数名有重名的情况，那么需要加上`函数名.`前缀（这里就是在第 11 行改为 `instructor_of.`）
***
#### SQL Procedures

- 在上面的例子中，dept_count 函数还可以改写为 procedure：

!!! example "Example"

	```sql
	// Declaration
	create procedure dept_count_proc(
	    in dept_name varchar(20),
	    out d_count integer
	)
	begin
		select count(*) into d_count
		from instructor
		where instructor.dept_name = dept_count_proc.dept_name
	end
	```
	
	- 关键字 `in` 和 `out` 分别表示接收进来的参数和存放返回结果的参数（其实就是返回值）
	- 我们可以使用 call 语句从 SQL 过程或嵌入式 SQL 调用过程
	
	```sql
	// Invocation
	declare d_count integer;
	call dept_count_proc('Physics', d_count);
	```

SQL 允许多个参数不同的函数或过程**同名**，因为 SQL 会同时根据函数 / 过程名以及参数来识别函数 / 过程
***
### Procedural Constructs

- 大多数数据库系统都实现了以下标准语法的变体
	- 所以用户必须阅读系统手册，了解哪些功能适用于用户的系统
- 复合语句： begin ... end 
	- 我们可以在 begin 和 end 之间包含多个 SQL 语句
	- 局部变量可以在复合语句中声明
- 循环语句：
	
	```sql
	// While Statements
	while boolean expression do
	    sequence of statements;
	end while
	
	// Repeat Statements
	repeat
	    sequence of statements;
	until boolean expression
	end repeat
	
	// For Statements
	declare n integer default 0;
	for r as
	    select budget from department
	    where dept_name = 'Music'
	do 
	    set n = n - r.budget
	end for
	```
	
	- 循环体内使用 `leave` 关键字可提前退出循环，而 `iterate` 则忽略当前元组，处理下一个元组。它们类似编程语言的 `break` 和 `continue` 语句
- 条件分支语句：

	```sql
	if boolean expression
    then statement or compound statement
	else boolean expression
	    then statement or compound statement
	else statement or compound statement
	end if
	```
***
### External Language Functions / Procedures

上述介绍的构造块鲜有数据库支持，因此程序员转而使用外部的编程语言：先用其他编程语言（比如 Java、C++ 等）定义函数后，再用 SQL 语句导入外部的过程或函数，比如：

```sql
create procedure dept_count_proc(
    in dept_name varchar(20),
    out count integer
) 
language C
external name '/usr/avi/bin/dept_count_proc';

create function dept_count(
    dept_name varchar(20)
)
return integer
language C
external name '/usr/avi/bin/dept_count';
```

- 外部语言功能/过程的好处：许多操作更高效，表现力更强
- 缺点：
	- 实现功能的代码可能需要加载到数据库系统中，并在数据库系统的地址空间中执行，可能会有：
		- 数据库结构意外损坏的风险
		- 安全风险，允许用户访问未经授权的数据
	- 还有其他选择，它们可以提供良好的安全性，但代价是性能可能会变差
	- 当效率比安全性更重要时，更偏向在数据库系统空间中直接执行

对于外部语言造成的风险，数据库系统提供了一些安全机制，比如：

- 使用沙盒技术
	- 即使用像 Java 这样的安全语言，它不能用于访问/损坏数据库代码的其他部分
- 或者，在单独的进程中运行外部语言函数/过程，而不访问数据库进程的内存
	- 通过进程间通信传输参数和结果
- 两者都有性能开销
- 许多数据库系统同时支持上述方法以及在数据库系统地址空间中直接执行
***
## Triggers

**触发器**（Trigger）是一种系统自动执行的语句，作为对数据库修改的“副作用”。要想定义一个触发器，需要：

- 指定触发器何时执行——这点可以分解为检查触发器的**事件**（Event）
	- 可以是插入、删除或更新
	- 更新时的触发器可以限制为特定属性
		- e.g. `after update of takes on grade`
	- 可以引用更新之前和之后的属性值
		- `referencing old row as`：可以用于删除和更新
		- `referencing new row as`：可以用于插入和更新
- 执行触发器需满足的**条件**（Condition）
- 指定触发器需要执行的**动作**（Actions）

要设计触发机制，我们必须：

- 指定要执行触发器的条件
- 指定触发器执行时要执行的操作

!!! example "Example"

	=== "Example 01"
	
		对于一个表格 `account_log(account, amount, datetime)`
		
		```sql
		create trigger account_trigger after update of account on balance
		referencing new row as nrow
		referencing old row as orow
		for each row 
		when nrow.balance - orow.balance >= 200000 or
			orow.balance - nrow.balance >= 50000
		begin
			insert into account_log values (nrow.account - number, 
									nrow.balance-orow.balance, current_time())
		end
		```
	
	=== "Example 02"
	
		- `time_slot_id` 不是主键，因此我们无法创建从 section 到 timeslot 的外键约束，在删除操作中不会引起其他影响。但我们可以设计一个触发器，用来检查当前课程的 time_slot_id 是否在表内，在 section 和 timeslot 上使用触发器来实施完整性约束
		
		```sql
		create trigger timeslot_check1 after insert on section
		referencing new row as nrow
		for each row
		when (nrow.time_slot_id not in (
		    select time_slot_id
		    from time_slot /* time_slot_id not present in time_slot */
		))
		begin
		    rollback
		end;
		```
		
		- `for each row` 子句能够显式迭代每一个被插入的行记录
		- `referencing new row as` 子句创建一个**过渡变量**（Transition Variable），用于临时存储被插入的行记录
		- `when` 语句指明了触发器的触发条件
	
	=== "Example 03"
	
		- `time_slot_id` 不是主键，所以当 time_slot_id 已经被删完了，但依然有课程在引用，就要 rollback
		
		```sql
		create trigger timeslot_check2 after delete on timeslot
		referencing old row as orow
		for each row
		when (orow.time_slot_id not in (
		        select time_slot_id
		        from time_slot
		    ) 
		    and orow.time_slot_id in (
		        select time_slot_id
		        from section
		    )
		)
		begin
			rollback
		end;
		```

- 触发器可以在事件之前激活，这可以用作额外的约束

!!! example "Example"

	=== "Example 01"
	
		例如我们将空白的部分设置为 Null：
		
		```sql
		create trigger setnull_trigger before update of takes  
		referencing new row as nrow  
		for each row  
		when (nrow.grade = ‘ ‘)
		begin atomic  
			set nrow.grade = null;  
		end;
		```
	
	=== "Example 02"
	
		我们使用触发器来保持 `credits_earned` 的值，如果本来挂科，或者没有成绩，更新后不再挂科而且有成绩，就把学分加上去。
		
		```sql
		create trigger credits_earned after update of takes on grade  
		referencing new row as nrow  
		referencing old row as orow  
		for each row
		when nrow.grade <> ’F’ and nrow.grade is not null  
		    and (orow.grade = ’F’ or orow.grade is null)  
		begin atomic  
			update student
			set tot_cred= tot_cred +  
				(select credits
				from course
				where course.course_id= nrow.course_id)
			where student.id = nrow.id;  
		end;
		```

很多数据库系统还支持其他触发事件，比如用户登录数据库、系统关机、修改系统设置等。

在上述例子中，可以看到触发器既可以在事件**发生前**执行，也可以在事件**发生后**执行。一般来说，前者作为一个额外的约束限制，不仅阻止非法行为引起的错误，还要采取补救措施，使语句变得合法。

除了将触发器的动作一行行地应用到表中的每个行记录上，也可以将触发器一次性作用于满足 SQL 的所有行记录上，只要：

- 将 `for each row` 改为 `for each statement`
- 并且使用 `referencing old table as` 和 `referencing new table as` 来创建过渡表

我们还可以决定启用或禁用触发器，相关语法为：`alter trigger trigger_name disable`

- 有些数据库采用另一种语法：`disable trigger trigger_name`。

此外，还可以删除触发器：`drop trigger trigger_name`。

与函数 / 过程的语法类似，由于很多数据库系统在 SQL 相关标准建立前就广泛使用触发器了，因此几乎每个数据库系统都有自己的触发器语法，它们是互不兼容的
***
### When not to Use Triggers

实际上，很多看似能够用触发器解决的问题， SQL 标准早已为我们提供了更方便的方法来解决这些问题，所以在以下场景中，没有必要使用触发器：

- 维护实体化视图：现在很多数据库系统都支持自动维护了，因此无需使用触发器手动维护
- 维护数据库的拷贝：理由同上
- 从备份拷贝上加载数据，或备份地点上复制数据库更新

编写触发器的时候需小心，因为在运行时，一个触发器的错误可能会触发下一个触发器，最严重的情况下会出现无限的连锁反应。解决方案有：

- 某些数据库系统规定了最大的触发器链长度，超过限制就会报错
- 另外的数据库系统则会根据触发器是否尝试引用更新后导致自身首先被触发的关系来判断是否产生错误









