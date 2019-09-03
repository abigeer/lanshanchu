# CSS基础

## 1、开班信息练习

## 2、定位

> 定位：
>
> - 定位指的是将指定的元素摆放到页面的任意位置，通过定位可以任意的摆放元素；
> - 通过position属性来设置元素的定位：
> - 可选值：
>   1. static：默认值，元素没有开启定位；
>   2. relative：开启元素的相对定位；
>   3. absolute：开启元素的绝对定位；
>   4. fixed：开启元素的固定定位（也是一种绝对定位）。

### 1. 相对定位

当元素的position属性设置为relative时，则开启了元素的相对定位

1. 开启元素的相对定位而不设置偏移量时，元素不会发生任何变化；
2. 相对定位是相对于元素在文档流中原来的位置进行定位的；
3. 相对定位的元素不会脱离文档流；
4. 相对定位会使元素提升一个层级；
5. 相对定位不会改变元素的性质，块元素还是块元素，内联元素还是内联元素。

当元素开启了定位（position属性值是一个非static的值）时，可以通过left、right、top、bottom四个属性来设置元素的偏移量：

- left：元素相对与其定位位置的左侧偏移量；
- right：元素相对于其定位位置的右侧便宜量；
- top：元素相对于其定位位置的上边的偏移量；
- bottom：元素相对于其定位位置下边的偏移量。

通常偏移量只需要使用其中两个就可以对一个元素进行定位，一般选择水平方向的一个偏移量和垂直方向的偏移量来为一个元素进行定位。

```html
<head>
    <style type="text/css">
        .box1 {
            width: 200px;
            height: 200px;
            background-color: red;
        }
        .box2 {
            widht: 200px;
            height: 200px;
            background-color: yellow;
            /*开启定位*/
            position: relative;
            /*将box1向右下移动和box3并排*/
            left: 200px;
            top: 200px;
        }
        .box3 {
            width: 200px;
            height: 200px;
            background-color: yellowgreen;
        }
        .s1 {
            positioin: relative;
            /*开启定位后元素属性没有变依然是内联元素不能试着宽高*/
            width: 200px;
            height: 200px;
            background-color: yellow；
        }
    </style>
</head>
<body>
    <div class="box1"></div>
    <div class="box2"></div>
    <div class="box3"></div>
    <span class="s1">我是一个span</span>
</body>
```

### 2.绝对定位

当元素的position属性设置为absolute时，则开启了元素的绝对定位：

1. 开启绝对定位，会使元素脱离文档流；

2. 开启绝对定位后，如果不设置偏移量，则元素的位置不会发生变化；

3. 绝对定位是相对于离他最近的开启了定位的祖先元素进行定位的（一般情况，开启了子元素的绝对定位都会同时再开启父元素的相对定位），如果父元素没有开启定位则相对与body进行定位；
4. 绝对定位会使元素提升一个层级；
5. 绝对定位会改变元素的性质：
   - 内联元素变成块元素（inline-block）；
   - 块元素的宽和高默认都被内容撑开。

```html
<head>
    <style>
        .box1 {
            width: 200px;
            height: 200px;
            background-color: red;
        }
        .box2 {
            width: 200px;
            height: 200px;
            background-color: yellow;
            /*开启绝对定位:基于父元素box4定位*/
            position: absolute;
            left: 100px;
            top: 100px;
        }
        .box3{
            width: 300px;
            height: 300px;
            background-color: yellowgreen;
        }
        .box4 {
            width: 300px;
            height: 300px;
            background-color: orange;
            /*开启元素的相对定位使开启绝对定位的子元素相对其进行定位*/
            position: absolute;
        }
        .s1 {
            position: absolute;
            /*开启绝对定位，元素属性改变，内联元素变为块元素*/
            width: 100px;
            height: 100px;
            background-color: yellow;
        }
    </style>
</head>
<body>
    <div class="box1"></div>
    <div class="box5">
        <div class="box4">
            <div class="box2"></div>
        </div>
    </div>
    <div class="box3"></div>
    <span class="s1">我是一个span</span>
</body>
```

### 3、固定定位

当元素的position属性设置为fixed时，则开启了元素的固定定位，固定定位也是一种绝对定位，他的大部分特点都和绝对定位一样，不同的是：

- 固定定位永远都是相对于浏览器窗口进行定位的；
- 固定定位会固定在浏览器窗口的某个位置，不会随滚动条滚动。

```html
<head>
    <style type="text/css">.box1{
				width: 200px;
				height: 200px;
				background-color: red;
			}
			.box2{
				width: 200px;
				height: 200px;
				background-color: yellow;
                /*开启固定定位*/
				position: fixed;
				/*相对于浏览器窗口*/
				left: 0px;
				top: 0px;
			}
			.box3{
				width: 200px;
				height: 200px;
				background-color: yellowgreen;
			}	
		</style>
</head>
	<body style="height: 5000px;"><div class="box1"></div>
		<div class="box4" style="width: 300px; height: 300px; background-color: orange; position: relative;">
			<div class="box2"></div>
		</div>
		<div class="box3"></div>
	</body>
```



## 3、层级

层级是html中z轴方向的位置。

如果定位元素的层级是一样的，则下边的元素会盖住上边的元素，通过z-index属性可以用来设置元素的层级，可以为z-index指定一个正整数作为值，该值将会作为当前元素的层级，层级越高，越优先显示。

**对于没有开启定位的元素不能使用z-index，父元素的层级再高也无法覆盖子元素。**

使用opacity可以用来设置元素背景的透明，需要一个0-1之间的值：

- 0表示完全透明；
- 1表示完全不透明；
- 0.5表示半透明。

opacity属性在IE8及以下的浏览器中不支持，在IE8及以下的浏览器中使用：

alpha(opacity=透明度)

透明度，需要一个0-100的值：

- 0表示完全透明；
- 100表示完全不透明；
- 50表示半透明。

```html
<head>
    <style type="text/css">
        .box {
            width: 200px;
            height: 200px;
            background-color: red;
            /*开启相对定位*/
            position: relative;
            /*设置层级为2*/
            z-index: 2;
            /*设置透明度*/
            opacity: 0.5;
            /*兼容ie8及以下*/
            filter: alpha(opacity=50);
        }
        .box2 {
            width: 200px;
            height: 200px;
            background-color: yellow;
            position: absolute;
            top: 100px;
            left: 100px;
            z-index: 25;
            opacity: 0.5;
            filter: alpha(opacity=50)
        }
        .box3 {
            width: 200px;
            height: 200px;
            background-color: yellowgreen;
            position: absolute;
            top: 200px;
            left: 200px;
            z-index: 30;
            opacity: 0.5;
            filter: alpha(opacity=50);
        }
        .box4 {
            width: 200px;
            height: 200px;
            background-color: orange;
            position: relative;
            /*父元素box4层级再高也盖不住子元素box5*/
            z-index: 20;
            top: 500px;
        }
        .box5 {
            width: 100px;
            height: 100px;
            background-color: skyblue;
            position: absolute;
            z-index: 10;
        }
    </style>
</head>
<body style="height: 5000px">
    <div class="box1"></div>
    <div class="box2"></div>
    <div class="box3"></div>
    <div class="box4">
        <div class="box5"></div>
    </div>
</body>
```

## 4、背景

- background-color用来设置背景颜色；

- background-image: url(相对路径)；来设置背景图片：
  - 语法：background-image: url(相对路径)；
  - 如果背景图片大于元素，默认会显示图片的左上角；
  - 如果背景图片和元素一样大，则会将背景图片完全显示；
  - 如果背景图片小于元素大小，则会默认将背景图片平埔坪以充满元素；
  - 可以同时为一个元素指定背景颜色和背景图片，这样背景颜色将会作为背景图片的底色，一般情况下设置背景图片时都会同时指定一个背景颜色。
  
- background-repeat：用于设置图片的重复方式，可选值：
  - repeat： 默认值，背景图片会水平和垂直同时重复平铺；
  - no-repeat：背景图片不会重复，有多大就显示多大；
  - repeat-x：背景图片沿水平方向重复；
  - repeat-y：背景图片沿垂直方向重复；
  
- background-position:可以调整背景图片在元素中的位置，可选值：
  - 可以使用top right left bottom center中的两个值搭配；
  - top left：表示左上，bottom right：表示右下
  - 如果只给出一个值，则第二个值默认是center。
  - 也可以指定便宜像素，第一个值为水平第二个值为垂直，可正可负。background-position: -80px -40px; 向左上移动。
  
- background-attachment用来设置背景图片是否随页面一起滚动，可选值：
  - scroll，默认值，背景图片随着窗口滚动
  - fixed，背景图片会固定在某一位置，不随页面滚动
  - 不随窗口滚动的图片，我们一般都是设置给body，而不设置给其他元素
  - 当背景图片的background-attachment设置为fixed时，背景土坯那的定位永远相对于浏览器窗口。
  
  ```html
  <head>
      <style type="text/css">
          body {
              height: 5000px;
              background-image: url();
              background-repeat: no-repeat;
              background-position: center;
              /*当背景图片的background-attachment设置为fixed时，背景图片的定位永远相对于浏览器的窗口*/
              background-attachment: fixed;
          }
      </style>
  </head>
  <body>
      
  </body>
  ```
  
  
  
- background
  - 通过该属性可以同时设置所有背景相关的样式；
  - 没有顺序的要求，谁在前谁在后都行；
  - 也没有数量的要求，不写的样式就使用默认值；
  - 如：background: #bfa url(img/3.png) center center no-repeat fixed;

## 5、导航条

当导航条的颜色是垂直方向为渐变色时，可以取一个像素宽度的图片，进行repeat-x操作.

```html
<head>
    <style type="text/css">
        .box {
            width: 990px;
            height: 32px;
            background-color: #bfa;
            margin: 50px auto;
            /*宽度为一个像素的图片*/
            background-image: url(img/bg.gif);
            background-repeat: repeat-x;
        }
    </style>
</head>
<body>
    <div class="box1></div>
</body>
```





## 6、雪碧图

将几幅图片放到一张图片上，这样减少网络请求次数提高体验。

练习：设置按钮(链接a)不同转态的背景图片

```html
<head>
	<style type="text/css">
        .btn:link {
            display: block;
            width: 93px;
            height: 29px;
            background-image: url(img/btn/btn2.png)
        }
        .btn:hover{
            /*当hover状态时，希望图片向左移动*/
            background-position: -93px,0px;
        }
        .btn:active {
            /*当时active转态时，希望图片再向左移动*/
            background-position: -186px 0px;
        }
    </style>
</head>
<body>
    <a class="btn" href="#"></a>
</body>
```

如果不使用雪碧图设置btn背景出现的问题：

当用户第一次点击按钮改变btn转态时图片间有一个快速的闪烁，不同转态使用不同背景图片，浏览器第一次加载会发送请求，当转换另外一个转态时又发送一个请求然后加载该图片，由于请求加载过程需要一定时间所以会产生闪烁现象。

使用雪碧图可以解决问题，优点：

1. 将多张图片整合为一张图片，浏览器只需要发送一次请求就可以同时加载多个图片，可以提高访问效率，提高用户体验；
2. 将多张图片整合为一张图片，减小了图片的总大小，提高请求速度，增加用户体验。



## 7、使用css对表格设置样式

```html
<head>
    <style type="text/css">
        table {
            /*表格是块元素设置宽度*/
            width: 300px;
            /*居中*/
            margin: 0 auto;
            /*边框
            border: 1px solid black;
            */
            /*table和td边框之间默认有一个距离，通过border-spacing属性可以设置这个距离
            border-spacing: 0px;
            */
            /*
            border-collapse可以用来设置表格的边框合并，如果设置了边框合并，则border-spacing自动失效
            */
            border-collapse: collapse;
            /*设置背景样式*/
            /*background-color: #bfa;*/
        }
        /*设置表格边框*/
        td,th {
            border: 1px solid black;
        }
        
        /*设置隔行变色*/
        tr:nth-child(even) {
            background-color: #bfa;
        }
        /*设置鼠标移入到tr后，变色*/
        tr:hover {
            background-color: #ff0;
        }
    </style>
</head>
<body>
    <table>
        <tr>
        	<th>学号</th>
            <th>姓名</th>
            <th>性别</th>
        </tr>
        <tr>
        	<th>1</th>
            <th>孙悟空</th>
            <th>男</th>
        </tr>
        <tr>
        	<th>2</th>
            <th>唐僧</th>
            <th>男</th>
        </tr>
        <tr>
        	<th>3</th>
            <th>女儿国国王</th>
            <th>女</th>
        </tr>
    </table>
</body>
```

## 8、表格布局（了解）

以前的表格更多情况下实际上是用来对页面进行布局的，但是这种方式早被css淘汰。

- 表格的列数由td虽多的哪行决定；
- 表格是可以嵌套的，可以在td中设置一个表格；

```html
<body>
		<table border="1" width="100%">
			<tr height="100px">
				<td colspan="2"></td>
			</tr>
			<tr height="400px">
				<td width="20%"></td>
				<td width="80%">
					<table border="1" width="100%" height="100%">
						<tr>
							<td></td>
						</tr>
						<tr>
							<td></td>
						</tr>
					</table>
				</td>
			</tr>
			<tr height="100px">
				<td colspan="2"></td>
			</tr>
		</table>	
	</body>
```

## 9、完善clearfix

子元素和父元素相邻的垂直外边距会发生重叠，子元素的垂直外边距会传递给父元素，使用空的table标签可以隔离父子元素的外边距，阻止外边距的重叠。

```html
<head>
    <style type="text/css">
        .box1 {
            width: 300px;
            height: 300px;
            background-color: red;
        }
        .box2 {
            width: 200px;
            height: 200px;
            background-color: yellow;
            /*此时父元素和子元素的垂直外边距重合，设置子元素的垂直外边距后会传递给父元素*/
            margin-top: 100px;
        }
        /*解决办法*/
        .box1:before {
            content: "";
            display: table;
        }
    </style>
</head>
<body>
    <div class="box1">
        <div class="box2"></div>
    </div>
</body>
```

由于display的table值也是可以起到块元素的作用，此时可以同时解决高度塌陷和父子元素垂直方向外边距重合问题。

```html
<head>
    <style type="text/css">
        .box1 {
            width: 300px;
            height: 300px;
            background-color: red;
        }
        .box2 {
            width: 200px;
            height: 200px;
            background-color: yellow;
            margin-top: 100px;
        }
        .box3 {
            border: 10px red solid;
        }
        .box {
            width: 100px;
            height: 100px;
            background-color: yellowgreen;
            float: left;
        }
        /*父子元素垂直外边距重合和高度塌陷解决*/
        .clearfix:before,
        .clearfix:after {
            content: "";
            display: table;
            clear: both;
        }
        /*兼容IE*/
        .clearfix {
            zoom: 1;
        }
    </style>
</head>
<body>
    <!--父子元素垂直方向外边距重合问题-->
    <div class="box1 clearfix">
        <div class="box2"></div>
    </div>
    <!--高度塌陷问题-->
    <div class="box3 clearfix">
        <div class="box4"></div>
    </div>
</body>
```

