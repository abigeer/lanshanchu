# 1.Kubernetes集群安装

Kubernetes用于协调高度可用的计算机集群，这些计算机集群被连接作为单个单元工作。Kubernetes在一个集群上以更有效的方式自动分发和调度容器应用程序。Kubernetes集群由两种类型的资源组成

- Master是集群的调度节点
- Nodes是应用程序实际运行的工作节点

下面是快速部署k8s集群的过程，k8s集群部署有几种方式：kubeadm、minikube和二进制包。前两者属于自动部署，简化部署操作，这里使用二进制包部署，因为自动部署屏蔽了很多细节，使得对各个模块感知很少，非常不利于学习。

## 1.1 环境准备与规划

- 推荐配置2核2G

  Docker version 17.05.0-ce

  | 角色   | IP   | 组件                                                         |
  | ------ | ---- | ------------------------------------------------------------ |
  | master |      | etcd、kube-apiserver、kube-controller-manager、kube-scheduler、docker |
  | node1  |      | kube-proxy、kubelet、docker                                  |
  | node2  |      | kube-proxy、kubelet、docker                                  |

- 查询默认防火墙状态（关闭后显示not running,开启后显示running）

  firewall-cmd --state

- 关闭防火墙

  systemctl stop firewalld.service

- 禁止firewall开机启动

  systemctl disable firewalld.service

- 获取kubernetes二进制包

  [地址](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.9.md)

  页面表格总找到Server Binaries中的kubernetes-server-linux-amd64.tar.gz文件，下载到本地。

  该压缩包包括了k8s需要运行的全部服务程序文件

## 1.2 Master安装

### 1.2.1 Docker安装

1. 设置yum源

   ```shell
   #更新yum
   yum update
   vi /etc/yum.repos.d/docker.repo
   
   [dockerrepo]
   name=Docker.Repository
   baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
   enabled=1
   gpgcheck=1
   gpgkey=https://yum.dockerproject.org/gpg
   ```

2. 安装docker

   `yum install docker-engine`

3. 查看docker版本

   `docker -v`

### 1.2.2 etcd安装

https://github.com/etcd.io/etcd/releases

选择etcd-v3.3.9-linux-arm64.tar.gz.asc二进制包传输到linux服务器

安装rzsz传输，`yum install lrzsz`

```shell
mkdir k8s
cd k8s  #在/usr/local下,用pwd查看当前目录
rz
tar -zxvf 文件名

```

将etcd和etcdctl文件复制到/usr/bin目录

配置systemd服务文件 `vi /usr/lib/systemd/system/etcd.service`

```txt
[Unit]
Description=Etcd Server
After=network.target
[Service]
Type=simple
EnvironmentFile=-/etc/etcd/etcd.conf
WorkingDirectory=/var/lib/etcd/
ExecStart=/usr/bin/etcd
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

创建目录`mkdir /var/lib/etcd`

启动与测试etcd服务

```shell
systemctl daemon-reload
systemctl enable etcd.service
mkdir -p /var/lib/etcd/
systemctl start etcd.service
systemctl status etcd.service  	#查看服务状态
etcdctl cluster-health
```

### 1.2.3 kube-apiserver服务安装

将kubernetes-server-linux-amd64.tar.gz文件传输到服务器

解压`tar -zxvf 文件名`

进入到kubernetes的bin目录下

解压后将kube-apiserver、kube-controller-manager、kube-scheduler以及管理要使用的kubectl二进制命令文件放到/usr/bin目录，即完成这个服务的安装

`cp kube-apiserver kube-controller-manager kube-scheduler kubectl /usr/bin/`

下面是对kube-apiserver服务进行配置

编辑（创建）systemd服务文件`vi /usr/lib/systemd/system/kube-apiserver.service`

```txt
[Unit]
Description=kubernetes API Server
Documentation=https://github.com/kubernetes/kubernetes
After=etcd.service
Wants=etcd.service
[Service]
EnvironmentFile=/etc/kubernetes/apiserver
ExecStart=/usr/bin/kube-apiserver $KUBE_API_ARGS
Restart=on-failure
Type=notify
[Install]
wantedBy=multi-user.target
```

创建配置文件

mkdir /etc/kubernetes

vi /etc/kubernetes/apiserver

```txt
KUBE_API_ARGS="--storage-backend-etcd3 --etcd-servers=http://127.0.0.1:2379 --insecure-bind-address=0.0.0.0 --insecure-port:8080 --service-cluster-ip-range=169.169.0.0/16 --service-node-port-range=1-65535 --admission-control=NamespaceLifecycle,NamespaceExists,LimitRanger,SecurityContextDeny,ServiceAccount,DefaultStorageClass,ResourceQuota --logtostderr=true --log-dir=/var/log/kubernetes --v=2"
```

### 1.2.4 kube-controller-manager服务

kube-controller-manager服务依赖于kube-apiserver服务；

配置(创建)systemd服务文件：`vi /usr/lib/systemd/system/kube-controller-manager-service`

```txt
[Unit]
Description=kubernetes Controller Manager
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=kube-apiserver.service
[Service]
EnvironmentFile=-/etc/kukbernetes/controller-manager
Execstart=/usr/bin/kube-controller-manager $KUBE_CONTROLLER_MANAGER_ARGS
Restart=on-failure
LimitNOFILE=65536
[Install]
WantedBy=multi-user.target
```

配置文件: vi /etc/kubernetes/controller-manager

注意自己ip设置成master的ip

```txt
KUBE_CONTROLLER_MANAGER_ARGS="--master=http://ip地址 --logtostderr=true --log-dir=/var/kubernetes --v=2"
```



### 1.2.5 kube-scheduler服务

kube-scheduler服务也依赖于kube-apiserver服务

配置systemd服务文件：`vi /usr/lib/systemd/system/kube-scheduler.service`

```txt
[Unit]
Description=kubernetes Scheduler
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=kube-apiserver.service
Requires=kube-apiserver.service
[Service]
EnvironmentFile=-/etc/kubernetes/scheduler
ExecStart=/usr/bin/kube-scheduler $KUBE_SCHEDULER_ARGS
Restart=on-failure
LimitNOFILE=65536
[Install]
WantedBy=multi-user.target
```

配置文件：`vi /etc/kubernetes/scheduler`

```txt
KUBE_SCHEDULER_ARGS="--master=http://master的ip:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"
```



1.2.6 启动

完成以上配置后，按顺序启动服务

systemctl daemon-reload

systemctl enable etcd

systemctl start etcd

systemctl status etcd

systemctl enable docker

systemctl start docker

systemctl status docker

systemctl enable kube-apiserver

systemctl start kube-apiserver

systemctl status kube-apiserver

systemctl enable kube-controller-manager

systemctl start kube-controller-manager

systemctl status kube-controller-manager

systemctl enable kube-scheduler

systemctl start kube-scheduler

systemctl status kube-schduler

systemctl stop firewalld

## 1.3 Node1安装

在Node1节点上，以同样的方式把从压缩保重解压的二进制文件(kubernetes-server-linux-amd64.tar.gz)在加压目录(kubernates/server/bin)将kubelet kube-proxy放到/usr/bin目录中，在Node1节点上需要预先安装docker。

### 1.3.1 kubelet服务安装

配置systemd服务文件:`vi /usr/lib/systemd/system/kubelet.service`

```txt
[Unit]
Description=kubernetes kubelet Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=docker.service
Requires=docker.service
[Service]
WorkingDirectory=/var/lib/kubelet
EnvironmentFile=-/etc/kubernetes/kubelet
ExecStart=/usr/bin/kubelet $KUBELET_ARGS
Restart=on-failure
KillMode=process
[Install]
WantedBy=multi-user.target
```

mkdir /var/lib/kubelet

配置文件：

mkdir /etc/kubernetes

`vi /etc/kubernetes/kubelet`

这里配置的host的ip是node节点本机的ip

```txt
KUBELET_ARGS="--kubeconfig=/etc/kubernetes/kubeconfig --hostname-override=Node节点ip --logtostderr=false --log-dir=/var/log/kubernetes --v=2 --fail-swap-on=false"
```

创建kubeconfig文件，用于kubelet连接Master ApiServer的配置文件

`vi /etc/kubernetes/kubeconfig`

yaml文件缩进格式注意

```txt
apiVersion: v1
king: Config
clusters:
 - cluster:
    Server: http://Mast主机ip:8080
   name: local
contexts:
 - context:
    cluster: local
   name: mycontext
current-context: mycontext
```



### 1.3.2 kube-proxy服务

kube-proxy服务依赖于network服务，所以一定要保证network服务正常，如果network服务启动失败，常见解决方案有以下几种：

1. 和NetworkManager服务有冲突，这个好解决，直接关闭NetworkManager服务就好了，`service Network stop`,并且禁止开机启动`chkconfig NetworkManager off`，之后重启就好了
2. 和配置文件的MAC地址不匹配，这个也好解决，使用ip addr(或ipconfig)查看mac地址将/etc/sysconfig/network-scripts/ifcfg-xxx中的HWADDR改为查看到的mac地址
3. 设定开机启动一个名为NetworkManager-wait-online服务，命令为：`systemctl enable NetworkManager-wait-online.service`
4. 查看/etc/sysconfig/network-scripts下，将其余无关的网卡位置文件全删掉，避免不必要的影响，即值留一个以ifcfg开头的文件。

配置systemd服务文件：`vi /usr/lib/systemd/system/kube-proxy.service`

```txt
[Unit]
Description=kubernetes kube-proxy Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=network.service
Requires=network.service
[Service]
EnvironmentFile=-/etc/kubernetes/proxy
ExecStart=/usr/bin/kube-proxy $KUBE_PROXY_ARGS
Restart=on-failure
LimitNOFILE=65536
KillMode=process
[Install]
WantedBy=multi-user.target
```

配置文件

`vi /etc/kubernetes/proxy`

```txt
KUBE_PROXY_ARGS="--master=http://master主机ip:8080 --hostname-override=node节点ip --logtostderr=err --log-dir=/var/log/kubernetes --v=2"
```

1.3.3 启动

