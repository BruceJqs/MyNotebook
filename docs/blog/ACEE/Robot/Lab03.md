# Lab03-ZJU-I 型机械臂 URDF 生成

## 装配机械臂

装配机械臂并调整固定位置如下图：

![](../../../assets/Pasted%20image%2020251008200331.png)
***
## 导出 URDF

使用插件，导出 URDF 并修改路径：

![](../../../assets/Pasted%20image%2020251008200807.png)

![](../../../assets/Pasted%20image%2020251008200832.png)
***
## Coppeliasim 仿真

新建场景，导入 URDF：

![](../../../assets/Pasted%20image%2020251008201113.png)

设置所有的零件为静态：

![](../../../assets/Pasted%20image%2020251008201149.png)

将所有关节设置限位：

![](../../../assets/Pasted%20image%2020251008201339.png)

编写脚本如下：

```python
def sysCall_init():
    sim = require('sim')
    self.joint1 = sim.getObject("/joint1")
    self.joint2 = sim.getObject("/joint2")
    self.joint3 = sim.getObject("/joint3")
    self.joint4 = sim.getObject("/joint4")
    self.joint5 = sim.getObject("/joint5")
    self.joint6 = sim.getObject("/joint6")

def sysCall_actuation():
    time = sim.getSimulationTime()
    sim.setJointTargetPosition(self.joint1, time * 0.5)
    sim.setJointTargetPosition(self.joint2, time * 0.1)
    sim.setJointTargetPosition(self.joint3, time * 0.2)
    sim.setJointTargetPosition(self.joint4, time * 0.3)
    sim.setJointTargetPosition(self.joint5, time * 0.4)
    sim.setJointTargetPosition(self.joint6, time * 0.6)
    pass

def sysCall_sensing():
    pass

def sysCall_cleanup():
    pass
```

运行即可开始运动：

![](../../../assets/Pasted%20image%2020251008201434.png)