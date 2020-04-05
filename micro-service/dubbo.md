# 1.分布式基础理论

## 1.1 概念

> 《分布式系统原理与范型》定义：
>
> “分布式系统是若干独立计算机的集合，这些计算机对于用户来说就像单个相关系统。”
>
> 分布式系统（distributed system）是建立再网络之上的软件系统。

随着互联网的发展，网站的规模不断扩大，常规的垂直应用架构已无法应对，分布式服务架构以及流动计算架构势在必行，亟需一个治理系统确保架构有条不紊的演进。

## 1.2架构发展演变

![](.\images\应用系统架构.jpg)

- 单一应用架构

  应用功能集中在一个应用内，当网站流量很小时，只需一个应用，以减少部署节点和成本。此时，用于简化增删改查工作量的数据访问框架（ORM）是关键。

  缺点：

  1. 应用扩展比较难；
  2. 协同开发问题；
  3. 不利于升级维护；

- 垂直应用架构

  ​	当访问量逐渐增大，单一应用增加机器带来的加速度越来越小，`将应用拆分成几个互不相干的应用`，以提升效率。此时，用于加速前端页面开发的Web框架（MVC）是关键。

  通过切分业务来实现各个模块的独立部署，降低了维护和部署的难度，团队各司其职更易管理，性能扩展也更方便，更有针对性。

  缺点：

  - 公用木块无法重复利用，开发性的浪费。

- 分布式服务架构

  将核心业务抽取出来，作为独立的服务，服务间互相交互，形成稳定的服务中心，使前端应用能更快速的响应多变的市场需求。此时用于提高业务服用及整合的分布式服务框架（RPC）是关键。

  ![](.\images\分布式服务架构图.png)

- 流动计算架构

  当服务越来越多，容量的评估，小服务资源的浪费等问题逐渐显现，此时需要增加一个调度中心基于访问压力实时管理集群容量，提高集群利用率。此时，用于提高机器利用率的资源调度和治理中心（SOA Service Oriented Architecture）是关键。

  这个中心如zookeeper？

  ![](.\images\流动计算架构.png)

## 1.3RPC

[go-micro微服务通俗解释](https://zhuanlan.zhihu.com/p/58985155)

- 什么叫RPC

> PRC(Remote Procedure Call)是指远程过程调用，**是一种进程间通信方式**。**他是一种技术的思想，而不是规范。**它允许程序调用另一个地址空间（通常是共享网络的另一台机器上）的过程或函数，而不用程序源显式编码这个远程调用的细节。即程序员无论是调用本地的还是远程的函数，本质上编写的调用代码基本相同。

- RPC基本原理

  ![](.\images\rpc原理.png)

![](.\images\rpc.png)

**RPC两个核心模块：通讯、序列化/反序列化。**



# 2.dubbo核心概念



## 2.1 简介

Apache Dubbo是一款高性能，轻量级的开源Java RPC框架，它提供了三大核心能力：

1. 面向接口的远程方法调用；
2. 智能容错和负载均衡；
3. 服务自动注册和发现。

## 2.2基本概念

![](.\images\dubbo.png)

> **服务提供者（Provider）：**暴露服务的服务提供方，**服务提供者在启动时，向注册中心注册自己提供的服务。**
>
> 
>
> **服务消费者（Customer）：**调用远程服务的服务消费方，**服务消费者在启动时，向注册中心订阅自己所需的服务，服务消费者，从提供者地址了列表中，基于软负载均衡算法，选一台提供者进行调用，如果调用失败，再选另外一台调用。**
>
> 
>
> **注册中心（Registry）:**注册中心返回服务提供者地址列表给消费者，如果有变更，注册中心将基于长连接推送变更数据给消费者。
>
> 
>
> **监控中心（Monitor）：**服务消费者和提供者，在内存中累计调用次数和调用时间，定时每分钟发送一次统计数据到监控中心。

- 调用关系说明：
  - 服务容器负责启动，加载，运行服务提供者。
  - 服务提供者在启动时，向注册中心注册自己提供的服务。
  - 服务消费者在启动时，向注册中心订阅自己所需的服务。
  - 注册中心返回服务提供者地址列表给消费者，如果有变更，注册中心将基于长连接推送变更过呢个数据给消费者。
  - 服务消费者，从提供者地址列表中，基于软负载均衡算法，选一台提供者进行调用，如果调用失败，再选了另外一台调用。
  - 服务消费者和提供者，在内存中累调用次数和调用时间，定时每分钟发送一次统计数据到监控中心。

# 3.dubbo环境搭建

## 3.1 windows安装zookeeper

| 1.下载zookeeper<br /> 网址：https://zookeeper.apache.org/releases.html |
| ------------------------------------------------------------ |
| 2、解压zookeeper<br />解压运行zkServer.cmd ，初次运行会报错，没有zoo.cfg配置文件 |
| 3、修改zoo.cfg配置文件<br />将conf下的zoo_sample.cfg复制一份改名为zoo.cfg即可。<br />注意几个重要位置:<br />dataDir=./   临时数据存储的目录（可写相对路径）<br />clientPort=2181   zookeeper的端口号<br />修改完成后再次启动zookeeper |
| 4、使用zkCli.cmd测试<br />`ls /`：列出zookeeper根下保存的所有节点<br />create –e /zzy 1024：创建一个zzy节点，值为1024<br />get /zzy：获取/zzy节点的值 |

在windows下`.`代表当前目录`..`代表父目录

## 3.2 windows安装 dubbo-admin管理控制台

> dubbo本身并不是一个服务软件。它其实就是一个jar包，能够帮助你的Java程序连接到zookeeper，并利用zookeeper消费、提供服务。所以不用在Linux上启动什么dubbo服务。
>
> 但是为了让用户更好的管理监控众多的dubbo服务，官网提供了一个可视化的监控程序，不过这个监控即使不装也不影响使用。

1. 下载dubbo-admin

   到dubbo的github地址:



## 3.3 windows安装dubbo-monitor

在程序中配置有两种方式，自动发现和直连：

customer.xml

```xml
<!--连接监控中心：自动发现-->
<dubbo:monitor protocol="registry"></dubbo:monitor>
<!--直连监控中心-->
<dubbo:monitor address="监控中心ip:port"></dubbo:monitor>
```

provider.xml

```xml
<!--连接监控中心：自动发现-->
<dubbo:monitor protocol="registry"></dubbo:monitor>
<!--直连监控中心-->
<dubbo:monitor address="监控中心ip:port"></dubbo:monitor>
```





## 3.4 Linux-安装zookeeper

1. 首先是要安装jdk环境
2. 安装zookeeper

| 1.下载zookeeper<br />wget 指定zookeeper的.tar.gz包地址       |
| ------------------------------------------------------------ |
| 2.解压缩<br />tar -zxvf 包名.tar.gz                          |
| 3.移动到指定位置，并改名为zookeeper<br />mv zookeeper-XXX xxx/zookeeper |

3. 开机启动zookeeper

   - 复制如下脚本：

     ```shell
     #!/bin/bash
     #chkconfig:2345 20 90
     #description:zookeeper
     #processname:zookeeper
     ZK_PATH=/usr/local/zookeeper
     export JAVA_HOME=/usr/local/java/jdk1.8.0_171
     case $1 in
              start) sh  $ZK_PATH/bin/zkServer.sh start;;
              stop)  sh  $ZK_PATH/bin/zkServer.sh stop;;
              status) sh  $ZK_PATH/bin/zkServer.sh status;;
              restart) sh $ZK_PATH/bin/zkServer.sh restart;;
              *)  echo "require start|stop|status|restart"  ;;
     esac
     
     ```

   - 把脚本注册为Service

     ![](.\images\zookeeper-linux.png)

   - 增加权限

     ![](.\images\zookeeper-linux1.png)

   - 配置zookeeper

     - 初始化zookeeper配置文件

       拷贝xxx/zookeeper/conf/zoo_sample.cfg到同一个目录改名为zoo.cfg

       `cp zoo_sample.cfg zoo.cfg`

     - 启动zookeeper

       `service zookeeper start`





















