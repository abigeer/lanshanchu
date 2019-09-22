# Vue基础（Webpack）03

## 1.nrm使用

> 1. nrm
>
>    nrm(npm registry manager)是npm的镜像源管理工具，有时候国外资源太慢，使用这个就可以快速地在npm源间切换；
>
> 2. 安装nrm
>
>    在命令行执行命令，npm install -g nrm,全局安装nrm；
>
> 3. 使用
>
>    执行命令nrm ls查看可选的源
>
>    ```shell
>    nrm ls
>    
>    *npm ---- https://registry.npmjs.org/
>    
>    cnpm --- http://r.cnpmjs.org/
>    
>    taobao - http://registry.npm.taobao.org/
>    
>    eu ----- http://registry.npmjs.eu/
>    
>    au ----- http://registry.npmjs.org.au/
>    
>    sl ----- http://npm.strongloop.com/
>    
>    nj ----- https://registry.nodejitsu.com/
>    ```
>
>    其中带有*的是当前使用的源，上面的输出表明当前源是官方源。
>
> 4. 切换
>
>    如果要切换到taobao源，执行命令nrm use taobao；
>
> 5. 增加
>
>    可以增加定制的源，特别适用于添加企业内部的私有源
>
>    ```shell
>    nrm add <registry> <url> //其中reigstry为源名，url为源的路径。
>    ```
>
> 6. 删除
>
>    ```shell
>    nrm del <registry>
>    ```
>
> 7. 测试速度
>
>    可以测试响应源的响应时间
>
>    ```shell
>    nrm test npm
>    ```

## 2.网页中常引用的静态资源

- JS
  - .js  .jsx  .coffee  .ts(TypeScript 类C#语言)
- CSS
  - .css  .less  .sass  .scss
- Images
  - .jpg  .png  .gif  .bmp  .svg
- 字体文件（Fonts）
  - .svg  .ttf  .eot  .woff  .woff2
- 模板文件
  - .ejs  .jade  .vue(这是在webpack中定义组件的方式，推荐这么使用)

## 3.网页中引入静态资源多了以后的问题？？

1. 网页加载速度慢，因为要发起很多的二次请求；
2. 要处理错综复杂的依赖关系。

### 通常解决方式

1. 合并，压缩，精灵图，图片的Base64编码；
2. 使用requireJS，也可以使用webpack可以解决各个包之间的复杂依赖关系；

## 4、webpack

### 什么是webpack？？

webpack是前端的一个项目构建工具，它是基于Node.js开发出来的一个前端工具；

### 如何解决静态资源过多问题？？

1. 使用Gulp，是基于task任务的；
2. 使用webpack，是基于整个项目进行构建的；
   - 借助于webpack这个前端自动化构建工具，可以完美实现资源的合并、打包、压缩等诸多功能；
   - [webpack官网](http://webpack.github.io/)
   - [webpack中文网](https://www.webpackjs.com/)

### webpack安装的两种方式

1. 运行`npm i webpack -g`全局安装webpack，这样就能在全局使用webpack的命令；
2. 在项目根目录中运行`npm i webpack --save-dev`安装到项目依赖中。