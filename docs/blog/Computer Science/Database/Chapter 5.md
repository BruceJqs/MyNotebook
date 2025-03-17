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
	
	如果使用预备语句及其 `set` 方法时
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
