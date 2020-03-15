# 1.Kubernetes集群

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