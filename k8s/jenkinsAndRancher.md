# 持续集成(CI)与容器管理

# 1.DockerMaven插件

微服务部署有两种方法：

1. 手动部署

   首先基于源码打包生成jar包或war包，将jar包上传至虚拟机并拷贝只JDK容器。

2. 通过Maven插件自动部署

   对于数量众多的微服务，手动部署无疑是非常麻烦的做法，并且容易出错。所以我们这里学习如何自动部署，这也是企业实际开发中经常使用的方法。

Maven插件的自动部署步骤：

1. 修改宿主机的docker配置，让其可以远程访问：由于远程操作docker，docker是默认关闭的

   `vi /lib/systemd/system/docker.service`

   其中ExecStart后添加配置`-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock`

2. 刷新配置，重启服务

   ```shell
   systemctl daemon-reload
   systemctl restart docker
   docker start registry
   ```

3. 在pom下增加配置

   ```xml
   <build>
   	<findName>app</findName>
       <plugins>
       	<plugin>
           	<groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-maven-plugin</artifactId>
           </plugin>
           <!--docker的maven插件，官网:https://github.com/spotify/docker-maven-plugin-->
           <plugin>
           	<groupId>com.spotify</groupId>
               <artifactId>docker-maven-plugin</artifactId>
               <version>0.4.13</version>
               <configuration>
                   <!--最终生成镜像名称-->
               	<imageName>私服地址（ip:5000）/${project.artifactId}:${project.version}</imageName>
                   <baseImage>jdk1.8</baseImage>
                   <!--相当于执行java -jar /应用名.jar-->
                   <entryPoint>["java","jar","/${project.build.finalName}.jar"]</entryPoint>
                   <resources>
                   	<resource>
                       	<targetPath>/</targetPath>
                           <directory>${project.build.directory}</directory>
                           <include>${project.build.finalName}.jar</include>
                       </resource>
                   </resources>
                   <dockerHost>http://ip:2375</dockerHost>
               </configuration>
           </plugin>
       </plugins>
   </build>
   ```

   以上配置会自动生成Dockerfile

   ```shell
   FROM jdk1.8
   ADD app.jar /
   ENTRYPOINT ["java","-jar","/app.jar"]	#自动执行java -jar /app.jar
   ```

4. 执行DockerMaven创建打包镜像

   再idea的terminal下执行一下命令，安装工程：

   `mvn install`

   到对应的工程目录下再执行以下命令：创建并上传镜像：

   `mvn docker:build -DpushImage`

   然后查看仓库中是否有该镜像

   http://ip:5000/v2/_catlog

   

# 2.持续集成工具 Jenkins

持续集成的作用：

- 保证团队开发人员提交代码质量，减轻了软件发布时的压力；
- 持续集成中的任何一个环节都是自动完成的，无需太多人工干预，有利于减少重复过程以节省时间、覅用和工作量；

## 2.2 Jenkins简介

Jenkins，原名Hudson,2011年改名为Jenkins，他是一个开源的实现持续集成的软件工具。官方网站：http://jenkins-ci.org/

Jenkins能实施监控集成中存在的错误，提供详细的日志文件和提醒功能，还能用图表的形式形象地展示项目构建的趋势和稳定性。

## 2.3 Jenkins安装

### 2.3.1 JDK安装

1. 将jdk-8u171-linux-x64.rpm上传至服务器

2. 执行安装命令

   `rpm -ivh jdk-8u171-linux-x64.rpm`

   RPM方式安装JDK，其根目录为：/usr/java/jdk1.8.0_171t

### 2.3.2 Jenkins安装与启动

1. 下载Jenkins

   `wget http://pkg.jenkins.io/redhat/jenkins-2.83-1.1.noarch.rpm`

   或将jenkins-2.83-1.1.noarch.rpm上传至服务器

2. 安装Jenkins

   `rpm -ivh jenkins-2.83-1.1.noarch.rpm`

3. 配置jenkins

   `vi /etc/sysconfig/jenkins`

   修改用户和端口

   ```txt
   JENKINS_USER="root"
   JENKINS_PORT="8888"
   ```

4. 启动服务

   `systemctl start jenkins`

5. 访问链接http://ip:8888

   从/var/lib/jenkins/secrets/initialAdminPassword中获取初始密码串

## 2.4 Jenkins插件安装

以安装maven插件为例，演示插件的安装

1.再Jenkins页面中点击左侧“系统管理”菜单 -> 插件管理 -> 可选插件，搜索maven

​	

## 2.5 全局工具配置

### 2.5.1 安装Maven与本地仓库

1. 上传maven到服务器

2. 解压

   `tar -zxvf apache-maven-3.5.4-bin.tar.gz`

3. 移动目录

   `mv apache-maven-3.5.4 /usr/local/maven`

4. 编辑setting.xml配置文件`vi /usr/local/maven/conf/settings.xml`,配置本地仓库目录内容如下：

   `<localRepository>/usr/local/repository</localRepository>`

5. 将开发环境的本地仓库上传至服务器，并移动到/usr/local/repository

   `mv reponsitory_boot /usr/local/repository`

   这样构建就不用再重新下载包了，缩短打包时间

### 2.5.2 全局工具配置

将各种环境目录告诉Jenkins

Jenkins选择系统管理 -> 全局工具配置

1. JDK配置：用于实现编译

   设置JAVA_HOME为：/usr/java/jdk1.8.0_171-amd64

2. Git配置（本地已经安装了Git软件）：用于拉去代码

3. Maven：用于构建

## 2.6 代码上传至Git服务器

### 2.6.1 搭建git仓库安装图形界面Gogs

> Gogs是一款极易搭建的自助Git服务。
>
> Gogs的目标是打造一个最简单，最快速和最放松的方式搭建自助Git服务。使用Go语言开发是的Gogs能够通过独立的二进制分发，并且支持go语言支持的所有平台，包括Linux,Mac OS X,Windows以及ARM平台

[地址](http://gitee.com/Unknown/gogs)

1. 下载镜像

   `docker pull gogs/gogs`

2. 创建容器

   `docker run -di --name=gogs -p 10022:22 -p 3000:3000 -v /var/gogsdata:/data gogs/gogs`

3. 访问http://ip:3000,数据库选择sqllite，其他设置并创建仓库。

2.6.2 提交代码

1. 再本地安装git
2. 在IDEA中选择菜单：FIle--settings,在窗口中选择Version Control --GIt
3. 选择菜单VCS --- Enable Version Control Integration...

IDEA中右键工程 -- Git -- Repository -- Remotes 来增加远程仓库地址，这个地址就是在Gogs中创建仓库后的仓库地址

Git--Add

Git -- commit repository

Git -- Repository -- push



## 2.7 任务的创建与执行

1. 回到Jenkins首页，点击新建按钮，输入名称，选择创建一个Maven项目，点击OK
2. 源码管理，选择Git，并把仓库地址拷贝到这里。Build 的Root POM ：项目目录/pom，Goals and options：clean package docker:build -DpushImage,这里会自动执行该命令

# 3.容器管理工具Rancher

## 3.1 Rancher介绍

Rancher是一个开源的企业级全栈话容器部署及管理平台。Rancher为容器提供一揽子基础架构服务：CNI兼容的网络服务、存储服务、主机管理、负载均衡、防护墙...Rancher让上述服务跨越公有云、私有云、虚拟机、物理机的环境运行，真正实现一键式应用部署和管理。

是docker的图像化管理工具，是企业运维工具。

https://www.cnrancher.com/

## 3.2 Rancher安装

1. 下载Rancher镜像（跑在在服务器上）

   `docker pull rancher/server`

2. 创建Rancher容器

   `docker run -di --name=rancher -p 9090:8080 rancher/server`

3. 在浏览器输入地址：http://192.168.184.136:9090



## 3.3 Rancher初始化

### 3.3.1 添加环境变量

Rancher支持将资源分组归属到多个环境。每个环境配置是隔离的，每个环境具有自己独立的基础架构资源及服务，并由一个或多个用户、团队或组织所管理。

例如，您可以创建独立的“开发”、“测试”及“生产”环境以确保环境之间的安全隔离，将开发环境的访问权限赋予全部人员，但限制“生产”环境的访问权限给一个小的团队。

Default --> 环境管理 --> 添加环境（名称，描述 --> 创建）

### 3.3.2 添加主机

这样可以远程管理一台docker主机

1. 选择基础架构 --> 主机 菜单，点击添加主机
2. 拷贝脚本，这个脚本是创建一个rancher代理容器，在要添加的主机上执行该脚本，这样主机和rancher服务就会建立连接。

3.3.3 添加应用

点击应用 --> 全部（或用户）,点击“添加应用”按钮（名称、描述 --> 创建）。

应用是一些列服务的分组，一个应用有多个微服务，而服务就相当与docker中的一个容器。



## 3.4 应用部署

在部署的主机对应的应用里部署

### 3.4.1 MySQL部署

点击“添加服务”（名称、描述、选择镜像、端口映射（相当于docker命令-p 宿主机ip:容器ip）、添加环境变量（MYSQL_ROOT_PASSWORD, 值为密码））

当显示Active时就表明服务已经创建成功。

### 3.4.2 RabbitMQ部署

镜像：rabbitmq:managerment，端口映射为5671 4369 15671 15672 25672

### 3.4.3 Redis部署

镜像：redis ,端口映射6379:6379

创建成功后，使用客户端测试连接

`redis-cli -h ip`

### 3.4.4 微服务部署

1. 搭建一个私有仓库

   启动私有仓库容器

   `docker run -di --name=registry -p 5000:5000 registry`

   打开浏览器输入地址http://ip:5000/v2/_catlog看到`{"repositories":[]}`表示私有仓库搭建成功，并且内容为空

   修改daemon.json

   `vi /etc/docker/daemon.json`

   添加一下内容，保存退出

   ```json
   {"insecure-registries":[宿主机ip:5000]}
   ```

2. 修改docker配置，允许远程访问

   `vi /lib/systemd/system/docker.service`

   其中ExecStart=后添加配置`-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock`

   这里的0.0.0.0表示任意ip都可访问，如果限制具体的ip则填具体ip

   修改后重启服务 

   ```shell
   systemctl daemon-reload
   systemctl restart docker
   docker start registry
   ```

3. 修改微服务工程，添加DockerMaven插件，创建镜像

4. 连接mysql数据库，执行建库脚本

5. 切换到服务，继续点击添加服务（名称，描述，镜像，端口映射）

## 3.5 扩容与缩容

当服务访问量教高就需要扩容容器，形成一个微服务集群。当访问量较低，可以缩减容器量，降低资源占用量。

### 3.5.1 扩容

1. 在Rancher将创建的微服务删除出

2. 重新创建该微服务，不设置端口映射：当有一个容器时设置端口映射可以，当多个容器映射一个端口时，就会冲突，这是将映射交给rancher自动管理。

3. 点击API --> Webhooks --> 添加接收器（名称、扩缩容服务（扩容）、目标服务（刚创建的服务）、步长（每次操作后，容器增加的数量），最小数量和最大数量）

   接收器相当于一个Url一个对外的接口，post这个url，就可以触发。

3.5.2 缩容

 和扩容的操作类似



3.6 负载均衡器

对服务扩容后，没有选择端口映射，这是无法访问，需要添加Rancher的负载均衡器。

在对应的应用界面 --> 添加容器下拉 --> 添加负载均衡(名称、描述、端口规则)



# 4 influxDB

## 4.1 什么时influxDB

influxDB是一个分布式时间序列数据库，用于存储监控数据，是运维常用的数据库。CAdvisor仅仅显示实时信息，但是存储监视数据。因此我们需要提供时序数据库用于存储CAdvisor组件提供的监控信息，以便显示除实时信息之外的时序数据。

## 4.2 influxDB安装

1. 下载镜像

   `docker pull tutum/influxdb`

2. 创建容器

   ```shell
   docker run -di -p 8083:8083 -p 8086:8086 --expose 8090 --expose 8099 --name influxsrv tutum/influxdb
   ```

   端口描述：8083web访问，8086数据写入

   

## 4.3 influxDB常用操作

### 4.3.1 创建数据库

`CREATE DATABASE "cadvisor"`

回车创建数据库

`SHOW DATABASES`

查看数据库

### 4.3.2 创建用户并授权

创建用户

`CREATE USER "cadvison" WITH PASSWORD 'cadvisor' WITH ALL PRIVILEGES`

查看用户

`SHOW USRES`

用户授权

```shell
grant all privileges on cadvisor to cadvisor		#给这个用户该数据库的所有权限
grant WRITE on cadvisor to cadvisor		#给这个用户写该数据库的权限
grant READ on cadvisor to cadvisor		#给用户读权限
```

### 4.3.3 查看采集的数据

切换到cadvisor数据库，使用一下命令查看采集的数据

`SHOW MEASUREMENTS`

刚开始还没有数据，如果想采集系统的数据，我们需要使用Cadvisor软件来实现



# 5 cAdvisor

## 5.1 什么是cAdvisor

Google开源的用于监控基础设施应用的工具，他是一个强大的监控工具(内存、CPU等占用情况)，不需要任何配置就可以通过运行在Docker主机上的容器来监控Docker容器，而且可以监控Docker主机，更多详细操作和配置选项可以查看Github上的cAdvisor项目文档。

监控数据就存储在influxDB

## 5.2 cAdvisor安装

1. 下载镜像

   `docker pull google/cadvisor`

2. 创建容器

   ```shell
   docker run --volume=/:/rootfs:ro --volume=/var/run:rw --volume=/sys:/sys:ro --volume=/var/lib/docker/:/var/lib/docker:ro --pulish=8080:8080 --detach=true --link influxsrv:influxsrv --name=cadvisor google/cadvisor -storage_driver=influxdb -storage_driver_db=cadvisor -storage driver host=influxsrv:8086
   ```

   link表示创建的influxDB的容器名

   -storage_driver表示连接influxdb数据库

   WEB前端访问地址

   http://宿主机ip:8080/containers/

   性能指标含义参照如下地址

   https://blog.csdn.net/ZHANG_H_A/article/detail/53097084

   再次查看influxDB，发现已经有很多数据被采集进来了

# 6 Grafana

cadvisor采集数据到influxDB中，而influxDB查看数据不直观，而grafana就是从influxDB中读数据用于绘制图表，直观展示数据。

## 6.1 什么是Grafana

Grafana是一个可视化面板（Dashboard），有着非常漂亮的图表和布局展示，功能齐全的度量仪表盘和图形编辑器。支持Graphite、zabble、InfluxDB、Prometheus和OpenTSDB作为数据源。

Grafana主要特性：灵活丰富的图形化选项；可以混合多种风格；支持白天和夜间模式；多个数据眼。

## 6.2 Grafana安装

1. 下载镜像

   `docker pull grafana/grafana`

2. 创建容器

   ```shell
   docker run -d -p 3001:3000 -e INFLUXDB_HOST=influxsrv -e INFLUXDB_PORT=8086 -e INFLUXDB_NAME=cadvisor -e INFLUXDB_USER=cadvisor -e INFLUXDB_PASS=cadvisor --link influxsrv:influxsrv --name grafana grafana/grafana
   ```

3. 访问

   http://宿主机ip:3001

   用户名和密码均为admin

4. 菜单介绍

   左侧第一个：创建

   第二个：仪表盘（Dashboards）

   第三个：报警

   第四个：设置，用户，数据源，插件等等

## 6.3 Grafana的使用

### 6.3.1 添加数据源

1. 点击第四个设置，Datasource --> Add Datasource

   setting(name,Type（选influxDB）)

   HTTP（URL（influxDB宿主机ip:8086）,Access(Server)）

   InfluxDB Details（Database（cadvisor），User和Password都是cadvisor）

2. 点击save and test

### 6.3.2 添加仪表盘

1. 选择菜单第二项仪表盘（Dashboards --> Manager）

2. 点击添加按钮

3. 点击Graph图标（新增后点击图表下拉选择Edit）

   General：中设置title和描述

   Metrics：中指定Data Source（InfluxDB），option中选择一个选项，Min time interval：30（间隔30秒采集一个数据）

   然后再下面编辑sql语句

   Axes：中选择x和y轴并选择计量单位

   最后点击保存，然后起名

### 6.3.3预警通知设置

再图表中设置预置当超过该值后，触发预警通知。

设置预警通知主要设置以什么方式通知。

1. 选择菜单 alerting --> Notification channels

2. 点击 Add channel按钮

   name，Type(webhook,该webhook的url就是rancher中的webhook，使用POST)

   点击sent test查看rancher中webhook是否被调用

3. 测试成功点击save

4. 回到对应的仪表盘Edit，再Alert中create Alert，设置阈值，Sent to选择创建的通知