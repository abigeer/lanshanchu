# 1.Maven（专家）基础

## 1.1 介绍

1. apache组织提供的一个顶级项目（apache项目由Java开发，顶级项目是根目录）；
2. maven是一个由Java开发的工具；
3. 作用：
   - 管理项目构建生命周期
   - 管理项目中的jar
   - 管理项目基础信息（文档管理、测试报告）



## 1.2 项目构建生命周期

- 一般流程：开发 、编译、打包、发布

  - 打包：jar包和war包

- 专业流程：

  清理(clean) -> 编译(compile) -> 测试(test) -> 报告 -> 打包 -> 发布



## 1.3 项目中jar管理

1. jar包管理难度：
   - 定位较难
   - jar包之间依赖较难
   - jar之间冲突
   - jar管理

## 1.4 Maven如何管理jar

[本地仓库库] -> [局域网私服仓库] -> [中央仓库]

可配置镜像仓库

![](./images/maven-repository.png)

[repository和mirror区别](https://www.cnblogs.com/bollen/p/7143551.html)

mirror相当于一个拦截器，可以拦截对中央仓库的访问，并定向到指定的镜像仓库。<mirrorof>标签配置要被镜像的repository的id。

![](./images/mirror.png)

## 1.5 maven项目信息管理

- 生成api文档
- 生成测试报告

一般测试人员使用，开发不用。

## 1.6 Maven安装于配置

1. 【安装】:解压即可使用，复制到没有中文和空格目录下
2. 【配置】：
   - 【JAVA_HOME】环境变量配置
   - 【MAVEN_HOME】配置到maven的b安装目录下
   - 【path】添加path %MAVEN_HOME%\bin

## 1.7 maven本地仓库

常用maven命令：`mvn clean`、`mvn compile`、`mvn package`

默认仓库位置在当前用户系统目录下的.m2/repository/

## 1.8 重新设置MAVEN本地仓库地址

maven安装目录下/conf/setting.xml中定位<localRepository>标签，配置本地仓库位置。

## 1.9 MAVEN工程结构

1. MAVEN可以管理工程，必须按照【约定结构】来创建

2. 结构（重点）：

   src目录:  (源代码)

   ​	|_main(主要开发)

   ​		|_java (开发Java文件)

   ​		|_resource （开发配置文件）

   ​	|_test （主要进行测试）

   ​		|_java (测试Java文件)

   ​		|_resource （测试配置文件）

   target目录: (编译后的class文件，在创建项目时，不需要创建。MAVEN命令执行时自动创建)

   pom.xml文件 （核心配置文件，从mavan中引入jar包）

## 1.10 MAVEN常见命令（项目构建周期）

1. `mvn clean`：删除当前工程中target

2. `mvn compile`：将当前工程中main文件夹下的所有Java编译为class，并输送到当前工程中的target中

3. `mvn test`：调用test文件夹下所有测试类总的所有测试方法，并生成测试报告。

4. `mvn package`：将工程中test文件夹下所有的Java测试类的方法调用执行进行测试生成【测试报告】

   如果测试成功，将main目录下的所有class文件打成指定格式包送到当前工工程的target目录下。

5. `mvn install`:于package命令执行基本一致，只是将打好的包推送到maven的本地仓库中。

6. `mvn deploy`:推送到远程仓库。

## 1.11 MAVEN坐标

用于唯一定位jar包

<groupId>域名反写</groupId>

<artifactId>项目名</artifactId>

<version>项目版本号</version>



# 2.Maven高级

2.1 解决jar包冲突

当在pom中通过坐标引入依赖时，如引入一个spring的依赖，此时会导入多个依赖包，当单独引入引入一个独立的包时会产生冲突

如下：spring-context依赖于spring-core,会自动导入一个5.0.2.REALEASE版本的spring-core。

而spring-beans也依赖于spring-core,而这个spring-core是4.2.4版本。

```xml

<dependencies>
    <dependency>
    	<groupId>org.springframework</groupId>
        <artifactId>spring-beans</artifactId>
        <version>4.2.4.RELEASE</version>
    </dependency>
	<dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.0.2.RELEASE</version>
    </dependency>
</dependencies>
```

