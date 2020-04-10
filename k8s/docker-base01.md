# 1.docker命令

## 1.0 linux常用命令和docker安装

> rz服务器接受文件
>
> sz服务器发送文件

tar命令

> 压缩命令
>
> `tar -zcvf 压缩后名称.tar（可以指全路径默当前目录） 要压缩目录`
>
> 解压命令
>
> `tar -xf 文件`

### 1.0.2docker在centos7下安装

> 查看CentOS版本
>
> `lsb_release -a`
>
> 查看系统位数和系统内核版本，docker要求内核版本在3.10以上
>
> `uname -r`
>
> yum更新
>
> `sudo yum update`
>
> 安装需要的软件包，yum-util提供yum-config-manager功能，另外两个是devicemapper驱动依赖的
>
> `sudo yum install -y yum-utils device-mapper-persistent-data lvm2`
>
> 设置yum源为阿里云
>
> `sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo`
>
> yum源安装
>
> 查看是否已安装docker列表
>
> `yum list installed | grep docker`
>
> 安装命令
>
> `yum -y install docker`
>
> -y表示不询问安装，直接安装成功
>
> 安装后查看docker版本
>
> `docker -v`

1.0.3 设置ustc镜像

ustc是老牌的linux镜像服务提供者，还在遥远得到Ubuntu5.04版本时候就在用，ustc的docker镜像加速很快。ustc docker mirror的优势之一就是不需要注册，是真正的公共服务

https://lug.ustc.edu.cn/wiki/mirrors/help/docker

编辑该文件

`vi /etc/docker/daemon.json`

[windows平台下docker配置说明](https://docs.microsoft.com/zh-cn/virtualization/windowscontainers/manage-docker/configure-docker-daemon)

在文件中输入以下内容：

`C:\Program Files\Docker\Docker\resources\windows-daemon-options.json`

> {
>
> "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
>
> }

运行

> docker服务端启动和关闭命令，linux系统下docker

```shell
systemctl start docker
systemctl restart docker
systemctl stop docker END
systemctl status docker		#docker运行状态
systemctl enable docker		#开机启动
dockers version	#查看是否启动成功
docker info		#查看docker概要信息
```



## 1.1镜像命令

```shell
docker images		#查看当前镜像，包括镜像名，版本号tag，镜像大小
```

> 搜索镜像
>
> 从网络中查找需要的镜像

`docker search 镜像名`

- NAME：仓库名
- DESCRIPTION：镜像描述
- STARS：用户评价，反应一个进行受欢迎程度
- OFFICIAL：是否官方
- AUTOMATED：自动构建，表示该镜像，由Docker Hub自动构建流程创建

> 拉取镜像
>
> 从中央仓库中下载镜像到本地，拉去镜像只给名称不给tag则默认是latest

`docker pull 镜像名称:tag`

> 删除镜像
>
> 按照镜像的ID删除或镜像名称

上传镜像

`docker push`

`docker rmi 镜像ID或镜像名称`

> 删除所有镜像

```shell
docker rmi `docker images -q`
```



## 1.2 容器命令

### 1.2.1 查看容器

```shelll
docker ps		#查看正在运行的容器
docker ps -a	#查看所有容器，包括停止的容器
docker ps -l	#查看最后一次运行的容器
docker ps -f status=exited	#查看停止的容器
```

### 1.2.2 创建与启动容器

> 创建容器

`docker run`

参数如下：

- -i：表示运行容器
- -t：表示容器启动后会进入其命令行。将加入这两个参数后，容器创建就能登录进去，即分配一个伪终端。
- --name：为创建的容器名
- -v：表示目录映射关系（前者是宿主机目录，后者是映射到宿主机上的目录），可以使用多个-v做多个目录或文件映射。注意：最好做目录映射，在宿主机上做修改，然后共享到容器上。
- -d：在run后面家上一个-d参数，则会创建一个守护式同期在后台运行（这样创建容器后不会自动登录容器，如果只加-i -t两个参数，创建后就会自动进入容器）
- -p：表示端口映射，前者是宿主机端口，后者是容器内的映射端口。可以使用多个-p做多个端口映射。

> 1.交互式方式创建容器,直接进入容器
>
> `docker run -it --name=容器名称 镜像名称:tag /bin/bash`
>
> 退出容器,回到宿主机，此时容器停止，状态时Exited(0)
>
> `exit`
>
> 2.以守护方式
>
> 创建容器
>
> `docker run -id --name=容器名 镜像名:tag`
>
> 进入容器
>
> `docker exec -it 容器名 /bin/bash`
>
> 退出，容器，但是容器在后台运行,状态时Up

### 1.2.3 停止与启动容器

> 停止容器

`docker stop 容器名称（或者容器ID）`

> 启动容器

`docker start 容器名称（或者容器ID）`

### 1.2.4 文件拷贝

> 如果需要将文件拷贝到容器内，可以使用cp命令

`docker cp 需要拷贝的文件或目录 容器名称（或ID）：容器目录`

> 也可以将文件从容器内拷贝出来

`docker cp 容器名称（或ID）:容器目录(需要拷贝的文件或目录) 本地路径`

### 1.2.5 目录挂载

> 在创建容器的时候，将宿主即的目录与容器内的目录进行映射，这样就可以通过修改宿主机某个目录的文件，从而去影响容器，使用-v参数后跟 宿主机目录：容器目录

`docker run -id -v 宿主机目录:容器目录 --name=容器名 镜像名：tag`

### 1.2.6 查看容器IP地址

> 可以通过以下命令查看容器运行的各种数据

`docker inspect 容器名（容器ID）`

> 也可以直接执行下面的命令直接输出IP地址，指定format参数

`docker inspect --format='{{.NetworkSetting.IPAddress}}' 容器名称（容器ID）`

### 1.2.7 删除容器

`docker rm 容器名称（容器ID）`

1.2.8 查看容器日志

`docker logs 容器id前几位不重复字符`

# 2.应用部署

## 2.1 MySQL部署

1. 拉取mysql镜像

   `docker pull centos/mysql-57-centos7`

2. 创建容器

   `docker run -di --name=容器名 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 镜像名`

   -p代表端口映射，格式为 宿主机映射端口：容器运行端口，这样就可以把容器的端口映射为宿主机的某一个端口；

   -e代表添加环境变量 MYSQL_ROOT_PASSWORD是root用户的登录密码

3. 进入mysql容器

   `docker exec -it 容器名 /bin/bash`

4. 登录mysql

   `mysql -u root -p`

## 2.2 tomcat部署

1. 拉取镜像

   `docker pull tomcat:7-jre7`

2. 创建容器

   `docker run -di --name=mytomcat -p 9000:8000 -v /usr/local/webapps:/usr/local/tomcat/webapps tomcat:7-jre7`

   -p表示端口映射，将容器端口8000映射到宿主机9000端口。

   

## 2.3 Nginx部署

1. 拉取镜像

   `docker pull nginx`

2. 创建Nginx容器

   `docker run -di --name=mynginx -p 80:80 nginx`

   etc目录下的nginx目录

## 2.4 Redis部署

1. 拉取镜像

   `docker pull redis`

2. 创建容器

   `docker run -di --name=myredis -p 6379:6379 redis`

再windows下的redis安装目录下，使用redis客户端连接远程的redis

`redis-cli -h ip`



# 3.备份与迁移

## 3.1 容器保存为镜像

​	`docker commit mynginx（容器名） mynignx_i（镜像名：tag）`

## 3.2 镜像备份

> 通过一下命令将镜像保存为tar文件

​	`docker save -o mynginx_i`

## 3.3 镜像恢复与迁移

> 首先删除掉mynginx_i镜像，然后执行一下命令进行恢复
>
> `docker load -i mynginx_i.rar`
>
> -i 表示输入的文件

# 4.Dockerfile

dockerfile是由一系列命令和参数构成的脚本，这些命令应用于基础镜像并最终创建一个新的镜像。

1. 对于开发人员：可以为开发团队提供一个完全一致的开发环境；
2. 对于测试人员：可以直接拿开发时所构建的镜像或者通过Dockerfile文件构建一个新的镜像开始工作；
3. 对于运维人员：在部署时，可以实现应用的无缝移植。

> 用Dockerfile构建镜像是一条标准路径，容器启动后可以自动执行Dockerfile中的命令。

## 4.1 常用命令

[Dockerfile知识](https://www.cnblogs.com/edisonchou/p/dockerfile_inside_introduction.html)

| 命令                               | 作用                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| FROM image_name:tag                | 定义了使用那个基础镜像启动构建流程（不存在会先下载）         |
| MAINTAINER user_name               | 生命镜像的创建者                                             |
| ENV key value                      | 设置环境变量（可以写多条）                                   |
| RUN command                        | 是Dockerfile的核心部分（可以写多条）（创建目录或者拷贝文件等） |
| ADD source_dir/file dest_dir/file  | 将宿主机的文件复制到容器内，如果是一个压缩文件，将会在复制后自动解压 |
| COPY source_dir/file dest_dir/file | 和ADD相似，如果有解压文件并不能解压                          |
| WORKDIR path_dir                   | 设置工作目录（当前命令是在这个工作目录执行）                 |
| CMD                                | 容器启动时执行的脚本                                         |

## 4.2 Dockerfile构建jdk1.8镜像

基础镜像centos7

```shell
#1.创建一个构建镜像用的目录
mkdir -p /usr/local/dockerjdk8
#2.将jdk8安装包放入该目录
#3.在该目录下创建Dockerfile文件，Dockerfile文件名固定
vi Dockerfile
########################
FROM centos:7	#基础镜像
MAINTAINTER zzy		#创建者
WORKDIR /usr		#设置当前目录
RUN mkdir /usr/local/java
ADD jdk-8u171-linux-x64.gz /usr/local/java/

ENV JAVA_HOME /usr/local/java/jdk1.8.0_171
ENV JRE_HOME $JAVA_HOME/jre
ENV CLASSPATH $JAVA_HOME/bin/dt.jar:$JAVA_HOME/lib/tool.jar:$JRE_HOME/lib:$CLASSPATH
ENV PATH $JAVA_HOME/bin:$PATH
########################

#4.构建
docker build -t='jdk1.8' .		#-t表示构建镜像的名称，点表示当前目录，在当前目录下找到Dockerfile
```

# 5.Docker私有仓库

私有仓库用于存储企业内部的镜像，公有仓库存储一些通用的镜像。

## 5.1 私有仓库搭建与配置

1. 拉取私有仓库镜像

   私有仓库也是一个镜像，名字叫registry

   `docker pull registry`

   启动

   `docker run -di --name=registry -p 5000:5000 registry`

   > 启动容器，访问5000端口：http://ip:5000/v2/_catalog
   >
   > 页面有{"repositories":{}}表示成功安装了私有仓库

2. 修改daemon.json

   `vi /etc/docker/daemon.json`

   添加一下内容，保存退出

   > {"insecure-registries":["ip:5000]}

   此步用于让docker新人私有仓库地址

3. 重启docker服务

   `systemctl restart docker`

## 5.2 将镜像上传至私有仓库

1. 标记此镜像为私有仓库的镜像

   `docker tag jdk1.8 ip:5000(即私服地址)/jdk1.8`

2. 上传标记的镜像

   `docker push ip:5000/jdk1.8`