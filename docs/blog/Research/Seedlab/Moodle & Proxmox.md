# Moodle & Proxmox
## Moodle

### 安装移植

- 需要 Ubuntu 24.04 系统

#### 环境部署

一键部署环境脚本：

```bash
#!/bin/bash

# 获取当前 Linux 发行版信息
OS_INFO=$(cat /etc/os-release)

# 检测是否为 Ubuntu 24.04
if echo "$OS_INFO" | grep -q "Ubuntu" && echo "$OS_INFO" | grep -q "VERSION_ID=\"24.04\""; then
    echo "当前系统是 Ubuntu 24.04，可以继续后续操作。"
else
    echo "当前系统不是 Ubuntu 24.04。"
    echo "当前系统信息如下："
    echo "$OS_INFO"
    echo "请在 Ubuntu 24.04 系统上运行此脚本。"
    exit 1
fi


# 设置变量
DB_ROOT_PASSWORD="seedlabs2025"  # MariaDB root 用户的密码
DB_USER="moodleuser"                   # 创建的数据库用户
DB_USER_PASSWORD="yourPassword1#" # 数据库用户的密码
DB_NAME="moodle"                      # 创建的数据库名称

# 更新系统包
echo "更新系统包..."
sudo apt update
sudo apt upgrade -y

# echo "安装基础依赖..."
# sudo apt install -y software-properties-common apt-transport-https
# 安装 MariaDB
echo "安装 MariaDB..."
sudo apt install -y mariadb-server mariadb-client

# 配置 MariaDB
echo "配置 MariaDB..."
sudo mysql_secure_installation <<EOF

$DB_ROOT_PASSWORD
$DB_ROOT_PASSWORD
y
y
y
y
y
EOF

# 创建数据库和用户
echo "创建数据库和用户..."
sudo mysql -u root -p$DB_ROOT_PASSWORD <<EOF
CREATE DATABASE $DB_NAME DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER '$DB_USER'@'%' IDENTIFIED BY '$DB_USER_PASSWORD';
GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'%';
FLUSH PRIVILEGES;
EOF

# 重启 MariaDB 服务
echo "重启 MariaDB 服务..."
sudo systemctl restart mariadb


echo "MariaDB 安装和配置完成！"

#!/bin/bash

# 设置变量
PHP_VERSION="8.2"  # 默认安装 PHP 8.2，可以根据需要修改

# 更新系统包
echo "更新系统包..."
sudo apt update
sudo apt upgrade -y

# 安装 Apache
echo "安装 Apache..."
sudo apt install -y apache2

# 启动并启用 Apache 服务
sudo systemctl start apache2
sudo systemctl enable apache2

# 安装 PHP
echo "安装 PHP..."
sudo apt install -y php libapache2-mod-php php-mysql php-gd php-xml php-curl php-zip php-intl php-mbstring php-soap php-ldap
# 重启 Apache 服务以加载 PHP 模块
sudo systemctl restart apache2

# 创建一个 PHP 测试文件
echo "创建 PHP 测试文件..."
echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/info.php



# 输出完成信息
echo "Apache 和 PHP 安装完成！"
echo "你可以通过访问 http://<your-server-ip>/info.php 来测试 PHP 是否正常工作。"
```

![](../../../assets/Pasted%20image%2020250705211630.png)

遇到这种情况选第一个或第二个均可
***
#### 站点迁移
 
脚本如下（命名为 restore_or_backup.sh），和备份 zip 放在同一路径下，使用方法：restore_or_backup.sh restore 待还原的 zip 路径 / restore_or_backup.sh backup

```bash
#!/bin/bash

# 检查是否为root用户
if [ "$(id -u)" -ne 0 ]; then
    echo "请使用root用户或通过sudo运行此脚本!"
    exit 1
fi

# 设置变量
MOODLE_DATA="/var/moodledata"         # Moodle数据目录
MOODLE_DIR="/var/www/html/moodle50"     # Moodle安装目录
MOODLE_BACKUP_DIR="/root/backup"		# Moodle备份目录
DB_NAME="moodle"      # 要操作的数据库名


# 检查是否传入参数
if [ $# -eq 0 ]; then
    echo "Usage: $0 [backup|restore]"
    exit 1
fi


backup() {
	echo "正在备份..."
	current_dir="$PWD"  # 保存路径
	current_date=$(date +"%Y-%m-%d")  # 获取当前日期，格式为 YYYY-MM-DD

	if [ -e "${MOODLE_BACKUP_DIR}" ]; then
		echo "${MOODLE_BACKUP_DIR} 已存在"
		exit 1
	else
		echo "创建备份文件夹 ${MOODLE_BACKUP_DIR}"
		mkdir -p ${MOODLE_BACKUP_DIR}
	fi

	echo "备份数据库"
	mysqldump moodle > ${MOODLE_BACKUP_DIR}/moodle.sql

	echo "备份站点数据"
	cd ${MOODLE_DIR}
	zip -qr ${MOODLE_BACKUP_DIR}/moodle50.zip ./*

	echo "备份其他数据"
	cd ${MOODLE_DATA}
	zip -qr ${MOODLE_BACKUP_DIR}/moodledata.zip ./*

	cd ${MOODLE_BACKUP_DIR}
	zip -qr backup${current_date}.zip ./*
	
	# 返回之前保存的路径
	cd "$current_dir"
	mv ${MOODLE_BACKUP_DIR}/backup${current_date}.zip ./
	rm -rf ${MOODLE_BACKUP_DIR}

	echo "备份成功 $current_dir/backup${current_date}.zip"
}


restore() {
    BACKUP_ZIP="$1"

    if [ -z "$BACKUP_ZIP" ]; then
        echo "❌ restore 操作必须指定备份 zip 文件路径"
        echo "Usage: $0 restore /path/to/backup.zip"
        exit 1
    fi

    if [ ! -f "$BACKUP_ZIP" ]; then
        echo "❌ 文件不存在: $BACKUP_ZIP"
        exit 1
    fi
	echo "正在还原..."

	echo "停止apache2 服务"
	systemctl stop apache2

	echo "删除原有 ${MOODLE_DATA} ${MOODLE_DIR} 文件夹的内容"
	rm -rf ${MOODLE_DATA}/* ${MOODLE_DIR}/*
	
	echo "正在解压"
    ZIP_BASENAME=$(basename "$BACKUP_ZIP" .zip)
    TEMP_DIR="/tmp/${ZIP_BASENAME}"
    mkdir -p "$TEMP_DIR"
    echo "📦 解压到临时目录 $TEMP_DIR"
    rm -rf "$TEMP_DIR"
    mkdir -p "$TEMP_DIR"
    unzip -oq "$BACKUP_ZIP" -d "$TEMP_DIR"
	unzip -oq ${TEMP_DIR}/moodledata.zip -d ${MOODLE_DATA}/
	unzip -oq ${TEMP_DIR}/moodle50.zip -d ${MOODLE_DIR}/
	chown -R www-data:www-data ${MOODLE_DATA} ${MOODLE_DIR} 
	chmod -R 755 ${MOODLE_DATA} ${MOODLE_DIR}
	
	# 进入MySQL执行操作
	mysql <<EOF
# 如果数据库存在则删除
DROP DATABASE IF EXISTS $DB_NAME;
# 创建新数据库
CREATE DATABASE $DB_NAME CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use $DB_NAME;
source ${TEMP_DIR}/moodle.sql
# 退出MySQL
EOF
	
	echo "启动apache2 服务"
	systemctl start apache2

	echo "还原成功"
}

echo "========================================================="
echo "提醒："
echo "执行脚本前请设置正确的路径参数，已设置请忽略该提醒"
echo "=========================================================\n"

# 根据参数执行不同操作
case "$1" in
    backup|--backup|-b)
        echo "执行备份操作..."
        backup
        ;;
    restore|--restore|-r)
        echo "执行还原操作..."
        restore $2
        ;;
    *)
        echo "错误：未知参数 '$1'"
        echo "Usage: $0 [backup|restore]"
        exit 1
        ;;
esac

exit 0
```

3. 手动修改 apache2 中的 moodle 站点配置文件（文件位于 /etc/apache2/site-available/moodle.conf），内容如下：

```
<VirtualHost *:80>
	ServerName 你的域名或者服务器ip地址
	DocumentRoot /var/www/html/moodle50
	
	<Directory /var/www/html/moodle50>
	   Options Indexes FollowSymLinks
	   AllowOverride All
	   Require all granted
	</Directory>
	
	ErrorLog ${APACHE_LOG_DIR}/moodle50_error.log
	CustomLog ${APACHE_LOG_DIR}/moodle50_access.log combined
</VirtualHost>
```

随后运行在同目录下运行命令行 `a2ensite moodle.conf`
***
### 虚拟机创建插件移植

1. 插件文件夹 `vmcreator/` 放到 `/var/www/html/moodle50/blocks/` 目录下
2. 运行命令行 `chown -R www-data:www-data vmcreator/`
3. 修改 `vm_create.py` 的配置部分，改 proxmox 内部 IP、API_TOKEN_ID（格式为 用户名!API 名）和 API_TOKEN_SECRET
4. 运行 `pip install filelock --break-system-packages`
5. 刷新 Moodle，得到画面：

![](../../../assets/Pasted%20image%2020250705211408.png)

4. 访问 `http://moodleip/info.php` ，查看配置文件位置：

![](../../../assets/Pasted%20image%2020250705211844.png)

5. 修改其中的 `php.ini` 的 `max_input_vars`：

![](../../../assets/Pasted%20image%2020250705211923.png)

6. `systemctl reload apache2`，刷新 moodle，没有错误提示，进行下一步：

![](../../../assets/Pasted%20image%2020250705212012.png)

7. 点击现在升级 Moodle 数据库：

![](../../../assets/Pasted%20image%2020250705212043.png)

8. 点击继续：

![](../../../assets/Pasted%20image%2020250705212108.png)

9. 随便找个课，编辑模式，点击添加板块，点击虚拟机创建器：

![](../../../assets/Pasted%20image%2020250705212153.png)

10. 测试成功即可

- 如果创建超时，需要把 vm_create.py 当中 clone_data 的 "full" 改成 0：

![](../../../assets/Pasted%20image%2020250705212324.png)
***
### 虚拟机自动销毁脚本

删除脚本：

```python
import warnings
warnings.filterwarnings("ignore")
import requests
import random
import string
import time
import datetime
import sys
import json
from datetime import datetime
print("timelog:",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# ==== 配置 ====
PVE_HOST = "https://10.1.101.152:8006"
API_TOKEN_ID = "root@pam!test"
API_TOKEN_SECRET = "f5f08a6b-bef7-49ff-9a1e-6c77c1bacc1e"
node = "fangkai03"     # 你的节点名


headers = {
    "Authorization": f"PVEAPIToken={API_TOKEN_ID}={API_TOKEN_SECRET}"
}
# 获取 VM 列表
resp = requests.get(f"{PVE_HOST}/api2/json/cluster/resources?type=vm", headers=headers, verify=False)
vms = resp.json()["data"]
for vm in vms:
    print(f"VMID: {vm['vmid']} Name: {vm['name']} Node: {vm['node']}")


resp_acl = requests.get(f"{PVE_HOST}/api2/json/access/acl", headers=headers, verify=False)
acls = resp_acl.json()["data"]
# print(acls)
# 构建 VM 权限表
vm_user_roles = []
for acl in acls:
    if acl["path"].startswith("/vms/"):
        vmid = acl["path"].split("/vms/")[1]
        vm_user_roles.append({
            "vmid": vmid,
            "user": acl["ugid"],
            "role": acl["roleid"]
        })
vm_users={i["user"]:i["vmid"] for i in vm_user_roles}


resp = requests.get(f"{PVE_HOST}/api2/json/access/users", headers=headers, verify=False)
users = resp.json()["data"]
# print(users)
now = int(time.time())
base_url = f"{PVE_HOST}/api2/json"

def force_stop_vm(vmid):
    print("⚠️ 发送强制关闭请求（stop）...")
    url = f"{base_url}/nodes/{node}/qemu/{vmid}/status/stop"
    resp = requests.post(url, headers=headers, verify=False)
    if resp.status_code != 200:
        print(f"❌ 强制关闭失败: {resp.text}")
        sys.exit(1)

def delete_vm(vmid):
    print("删除虚拟机...")
    url = f"{base_url}/nodes/{node}/qemu/{vmid}"
    resp = requests.delete(url, headers=headers, verify=False)
    if resp.status_code != 200:
        print(f"❌ 删除失败: {resp.text}")
        sys.exit(1)
    print("虚拟机删除成功")


def get_vm_status(vmid):
    url = f"{base_url}/nodes/{node}/qemu/{vmid}/status/current"
    resp = requests.get(url, headers=headers, verify=False)
    if resp.status_code != 200:
        print(f"❌ 查询虚拟机状态失败: {resp.text}")
        sys.exit(1)
    return resp.json()["data"]["status"]


for user in users:

    userid = user["userid"]
    if userid in vm_users:
        expire = user["expire"]
        vmid=vm_users[userid]
        if expire == 0:
            status = "永不过期"
        elif expire < now:
            status = f"❌ 已过期（{datetime.fromtimestamp(expire)}）"
            print(f"{vm_users[userid]},{userid}: {status}")
            status = get_vm_status(vmid)
            if status == "running":
                force_stop_vm(vmid)
                time.sleep(5)  # 可选：稍等几秒以确保状态同步
            else:
                print(f"虚拟机当前状态: {status}，无需强制关闭")

            delete_vm(vmid)

        else:
            status = f"✅ 有效至 {datetime.fromtimestamp(expire)}"
            print(f"{vm_users[userid]},{userid}: {status}")



# 遍历用户并删除过期的
for user in users:
    userid = user["userid"]
    expire = user["expire"]

    if expire != 0 and expire < now:
        readable_time = datetime.fromtimestamp(expire).strftime("%Y-%m-%d %H:%M:%S")
        print(f"🗑️ 删除过期用户: {userid}（过期时间：{readable_time}）")
        delete_url = f"{PVE_HOST}/api2/json/access/users/{userid}"
        resp_del = requests.delete(delete_url, headers=headers, verify=False)
        if resp_del.status_code == 200:
            print(f"✅ 已删除 {userid}")
        else:
            print(f"❌ 删除 {userid} 失败: {resp_del.text}")
```

1. 保存脚本在任意位置
2. 命令行 `crontab -e`，添加定时任务 `*/5 * * * * /usr/bin/python3 /home/bcds/del_vm.py >> /home/bcds/del_vm.log 2>&1`（其中 `/home/bcds/del_vm.py` 为脚本路径，`/home/bcds/del_vm.log` 为日志路径）
***
## Proxmox

1. 导入小老鼠版的 qcow2 镜像和原装版的 raw 镜像
2. 原装版命令行 `qm create <vmid> --name <vmname> --memory 2048 --cores 1 --net0 virtio,bridge=br0 --scsihw virtio-scsi-pci --scsi0 local-lvm:0,import-from=/root/seedvm-disk001.raw --boot order=scsi0 --ostype l26` 创建一个虚拟机；小老鼠版命令行 `qm create <vmid> --name <vmname> --memory 2048 --cores 1 --net0 virtio,bridge=br0 --sata0 local-lvm:0,import-from=/root/seed-cloud.qcow2 --boot order=sata0 --ostype l26`
3. 网桥+NAT 设置脚本：

```bash
#!/bin/bash
 
set -e
 
# === 基本配置 ===
VM_BRIDGE="vmbr1"
BRIDGE_IP="192.168.100.1"
BRIDGE_NET="192.168.100.0"
BRIDGE_MASK="255.255.255.0"
OUT_IFACE=$(ip route get 1 | awk '{print $5; exit}')  # 自动识别出网网卡
 
echo "==> 使用出网网卡: $OUT_IFACE"
 
# === 1. 配置 vmbr1 网桥 ===
echo "==> 配置 vmbr1 网桥..."
 
cat <<EOF >> /etc/network/interfaces
 
auto $VM_BRIDGE
iface $VM_BRIDGE inet static
    address $BRIDGE_IP
    netmask $BRIDGE_MASK
    bridge_ports none
    bridge_stp off
    bridge_fd 0
EOF
 
# === 2. 启用 IP 转发 ===
echo "==> 启用 IP 转发..."
 
sysctl -w net.ipv4.ip_forward=1
sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf
 
# === 3. 添加 iptables SNAT 规则 ===
echo "==> 添加 iptables SNAT 转换..."
 
iptables -t nat -A POSTROUTING -s ${BRIDGE_NET}/24 -o $OUT_IFACE -j MASQUERADE
 
# 永久保存规则（如果支持）
if command -v iptables-save &>/dev/null; then
  iptables-save > /etc/iptables.rules
  echo -e "\npre-up iptables-restore < /etc/iptables.rules" >> /etc/network/interfaces
fi
 
# === 4. 安装 dnsmasq ===
echo "==> 安装 dnsmasq DHCP 服务器..."
 
apt update
apt install -y dnsmasq
 
# === 5. 配置 dnsmasq ===
echo "==> 写入 dnsmasq 配置..."
 
mkdir -p /etc/dnsmasq.d
 
# 5.1 确保主配置启用了 conf-dir
if ! grep -q '^conf-dir=/etc/dnsmasq.d/' /etc/dnsmasq.conf; then
  echo 'conf-dir=/etc/dnsmasq.d/,*.conf' >> /etc/dnsmasq.conf
fi
 
# 5.2 写入网桥专用配置
cat <<EOF > /etc/dnsmasq.d/$VM_BRIDGE.conf
interface=$VM_BRIDGE
bind-interfaces
dhcp-range=192.168.100.100,192.168.100.200,12h
dhcp-option=3,192.168.100.1
dhcp-option=6,8.8.8.8
EOF
 
# === 6. 重启网络和 dnsmasq ===
echo "==> 重启网络与 dnsmasq 服务..."
 
ifdown $VM_BRIDGE || true
ifup $VM_BRIDGE
systemctl restart dnsmasq
 
echo "✅ NAT + DHCP 配置完成！请将虚拟机网卡桥接到 $VM_BRIDGE 并启用 DHCP 获取 IP。"
```

4. 克隆 IP 一致问题，需要在模板当中运行以下命令行去除 machine-id：

```bash
sudo truncate -s 0 /etc/machine-id
sudo rm /var/lib/dbus/machine-id
sudo rm /etc/ssh/ssh_host_*
cat /dev/null > ~/.bash_history && history -c
```
***
## 需要改进的

- 虚拟机 docker 换源
- 虚拟机没有 HTTP Header Live 插件（？），要安装 firefox 版本还太低？
- 插件位置是否能移动到内容中？（即放到实验环境块中）
- 虚拟机剪贴板问题
- Moodle 用户注册（用户名不能大写？电子邮件 zju 邮箱不支持？）