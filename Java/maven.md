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

## 2.1 解决jar包冲突

当在pom中通过坐标引入依赖时，如引入一个spring的依赖，此时会导入多个依赖包，当单独引入引入一个独立的包时会产生冲突

如下：spring-context依赖于spring-core,会自动导入一个5.0.2.REALEASE版本的spring-core。

而spring-beans也依赖于spring-core,而这个spring-core是4.2.4版本。

```xml
<dependencies>
    <dependency>
    	<groupId>org.springframework</groupId>
        <artifactId>spring-beans</artifactId>
        <version>4.2.4.RELEASE</version>
        <!--排除spring-core依赖-->
        <exclusions>
        	<exclusion>
            	<groupId>org.springframework</groupId>
                <artifactId>spring-core</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
	<dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>5.0.2.RELEASE</version>
    </dependency>
</dependencies>
```

> maven工程要导入jar包的坐标，就必须要考虑解决jar包冲突。
>
> 1. 方式一：
>
>    第一声明优先原则：哪个jar包的坐标在靠上的位置，这个jar包就是先声明的（这时就在项目中引入这个版本的先声明版本的jar包），先声明的jar包坐标下的依赖包，可以优先进入项目中。
>
> 2. 方式二：
>
>    - maven导入jar包中的一些概念：
>
>      - 直接依赖：项目中直接导入的jar包，就是该项目的直接依赖包；
>      - 传递依赖：项目中没有直接导入的jar包，可以通过项目直接依赖jar包传递到项目中去。
>
>    - 路径近者优先原则：
>
>      直接依赖路径比传递依赖路径近，那么最终项目进入的jar包会是路径近的直接依赖jar包。（如果项目中同一个jar包即存在直接依赖，又存在传递依赖，此时项目中进入的是直接依赖版本的jar包）。
>
> 3. 方式三：
>
>    直接排除法：（**推荐使用**）
>
>    当要排除某个jar包下的依赖包，在配置exclusions标签时，内部可以不写版本号，因为依赖包此时使用的版本号和本jar包版本一样。

当要引入一个新的jar包时，要关注新jar包的依赖包，然后观察maven依赖管理中当前对应改包的版本。

## 2.2 pom标签讲解

1. dependencyManagement

   用于锁定jar包版本：

   maven工程是可以分父子依赖关系的。

   凡是依赖别的项目后，拿到的别的项目的依赖包，都属于传递依赖。（父项目的dependencies下的依赖包都会传递给子项目）

   如果在子项目中再导入一套jar包，这套jar包属于直接依赖，会覆盖掉传递依赖。

   dependencyManagemant用于解决这个问题，可以把父项目中主要jar包锁住，这样当子项目即便有同名jar包的直接依赖也无法覆盖。

   dependencyManagement只起到锁定jar包的作用，不会实际给工程中导入jar包，实际导入jar包由dependencies完成，因此当要锁定一个jar包时，不能删除dependencies中引入的。

2. 统一管理jar包版本

   ```xml
   <properties>
   	<spring.version>...</spring.version>
       <slf4j.version>...</slf4j.version>
       ...
   </properties>
   ```

   然后可以使用EL表达式引用`${spring.version}`



# 3.工程的拆分与聚合

## 3.1 介绍

在一个项目中，不同部分可能会重用相同的代码，如一个商城系统，买家和卖家查询商品使用的dao层代码是相同的，如果在卖家和买家模块同时写两份dao层代码的话，就会造成代码难以维护。

maven解决代码可重用和便于维护问题的解决方式：

> maven把一个完整的项目，分成不同的独立模块，这些模块都有各自独立的坐标。那个地方需要其中某个模块，就直接引用该模块的坐标即可。
>
> 今后开发项目，先考虑的问题不是如何编写dao、service、controller、utils。而是要考虑，这些模块是否已经存在，如果存在直接引用，这就是maven拆分的思想。
>
> 把拆零散的模块聚合到一起编写一个完整的项目，就是maven聚合思想。

## 3.2 父子工程

- 创建步骤：

1. idea中新建一个project，工程下可以只保留pom和.idea文件
2. 在工程下创建module，根据需求创建module。

创建后父工程的pom文件中会出现：

```xml
<modules>
	<module>子模块名</module>
    ...
</modules>
```

子模块中的pom文件会出现：

```xml
<parent>
	<groupId></groupId>
    <artifactId></artifactId>
    <version></version>
</parent>
```



- 工程(project)和模块(module)的关系：

  工程不等于完整的项目，模块也不等于完整的项目，一个完整的项目看的是代码，代码完整，就可以说这是一个项目，和此项目是工程和模块没有关系。

- 模块间继承和依赖的概念：

  工程天生只能使用自己内部资源，工程天生是独立的。后天可以和其他工程或模块建立关联关系。

  > 引用其他项目需要将其他像项目install打包安装到本地仓库，然后引用即可。

  模块天生是不独立的，模块天生是属于父工程的，模块一旦创建，所有父工程的资源都可用。

  父子工程之间：子模块天生集成父工程，可以使用父工程所有资源。子模块之间天生是没有任何关系的。

  父子工程之间不需要建立关系，继承关系是先天的，不需要手动建立。

  平级直接的引用叫依赖，依赖不是先天的，依赖是需要后天建立的。

# 4.nexus私服搭建

[Linux上搭建nexus私服](https://www.cnblogs.com/muzi1994/p/6026144.html)

