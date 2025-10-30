# Web-23｜第二十三章 幻境迷心·皇陨星沉(大结局)

## 碎碎念

终于来到小说大结局了吗...

题目难度是指数级上升啊，Java 反序列化
***
## Writeup

查看源码，可以看到：

![](../../../../assets/Pasted%20image%2020251030155650.png)

这部分代码调用了 `readObject()`，这是 Java 反序列化的入口函数，反序列化时 Java 会自动调用 `hashCode()` 函数，而在这个源码中已经重写了这个函数：

```java
public int hashCode() {  
    this.wagTail(this.object, this.methodName, this.paramTypes, this.args);  
    return Objects.hash(new Object[]{this.id});  
}
```

它调用了 `wagTail()` 函数：

```java
default Object wagTail(Object input, String methodName, Class[] paramTypes, Object[] args) {  
    try {  
        Class cls = input.getClass();  
        Method method = cls.getMethod(methodName, paramTypes);  
        return method.invoke(input, args);  
    } catch (Exception e) {  
        e.printStackTrace();  
        return null;  
    }  
}
```

可以看到它会通过反射调用 `input` 对象的 `methodName` 方法，并传入 `args` 参数，我们就可以利用这个来执行反弹 shell 命令

![](../../../../assets/Pasted%20image%2020251030192136.png)