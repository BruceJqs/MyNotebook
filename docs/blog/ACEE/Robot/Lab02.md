# Lab02-SCARA 机械臂运动仿真

## 环境配置

首先从官网下载 Coppeliasim 并安装，并建立 Conda 环境：

![](../../../assets/Pasted%20image%2020251008132139.png)

配置 Coppeliasim 默认解释器为 python 路径：

![](../../../assets/Pasted%20image%2020251008132243.png)

测试成功：

![](../../../assets/Pasted%20image%2020251008132446.png)
***
## 导入零件

### 格式转换

将所有 SLDPRT 零件另存为 SLT 格式：

![](../../../assets/Pasted%20image%2020251008132549.png)
***
### 基座

新建场景，导入基座：

![](../../../assets/Pasted%20image%2020251008133618.png)

编辑参考系为自身参考系并旋转调整坐标后：

![](../../../assets/Pasted%20image%2020251008134152.png)
***
### 大臂

同理，放入调整旋转坐标之后如下：

![](../../../assets/Pasted%20image%2020251008134859.png)

加入关节连接两个零件后：

![](../../../assets/Pasted%20image%2020251008135447.png)
***
### 小臂

同理，导入调整加入关节后：

![](../../../assets/Pasted%20image%2020251008140121.png)
***
### 抓手

导入装配完成如下图所示：

![](../../../assets/Pasted%20image%2020251008142127.png)
***
## 脚本

编写脚本如下：

```python
import math

def sysCall_init():
    sim = require('sim')  

    self.joint1 = sim.getObject("/joint1")  
    self.joint2 = sim.getObject("/joint2")  
    self.joint3 = sim.getObject("/joint3")  
    self.joint4 = sim.getObject("/joint4")  

    self.graph = sim.getObject("/graph")  
    self.dummy = sim.getObject("/dummy")  
 
    self.position_x = sim.addGraphStream(self.graph, "x position", "m", 0, [1, 0, 0])
    self.position_y = sim.addGraphStream(self.graph, "y position", "m", 0, [0, 1, 0])
    self.position_z = sim.addGraphStream(self.graph, "z position", "m", 0, [0, 0, 1])

    self.curve = sim.addGraphCurve(self.graph, "x/y/z position", 3, [self.position_x, self.position_y, self.position_z], [0, 0, 0], "m by m by m")

def sysCall_actuation():
    t = sim.getSimulationTime() 
    if t > 0 and t <= 1: 
        sim.setJointTargetPosition(self.joint1, 0)  
        sim.setJointTargetPosition(self.joint2, 0) 
        sim.setJointTargetPosition(self.joint3, 0) 
        sim.setJointTargetPosition(self.joint4, 0) 
    elif t >= 2 and t <= 8:
        sim.setJointTargetPosition(self.joint1, (t - 2) * math.pi / 3)  
    elif t >= 9 and t <= 10:
        sim.setJointTargetPosition(self.joint2, - math.pi / 2)  
    elif t >= 11 and t <= 17:
        sim.setJointTargetPosition(self.joint1, (t - 11) * math.pi / 3)   
    elif t >= 18 and t <= 19:
        sim.setJointTargetPosition(self.joint3, 0.1)  
    elif t >= 20 and t <= 26:
        sim.setJointTargetPosition(self.joint1, (t - 20) * math.pi / 3)  
    elif t >= 27 and t <= 28:
        sim.setJointTargetPosition(self.joint2, 0)  
    elif t >= 29 and t <= 35:
        sim.setJointTargetPosition(self.joint1, (t - 29) * math.pi / 3)  
    elif t >= 36: 
        sim.setJointTargetPosition(self.joint1, 0)  
        sim.setJointTargetPosition(self.joint2, 0) 
        sim.setJointTargetPosition(self.joint3, 0) 
        sim.setJointTargetPosition(self.joint4, 0) 


def sysCall_sensing():
    pos = sim.getObjectPosition(self.dummy)  
    sim.setGraphStreamValue(self.graph, self.position_x, pos[0])  
    sim.setGraphStreamValue(self.graph, self.position_y, pos[1])  
    sim.setGraphStreamValue(self.graph, self.position_z, pos[2]) 

def sysCall_cleanup(): 
    pass
```

运行即可得到运动轨迹和运动状况