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
- background
  - 通过该属性可以同时设置所有背景相关的样式；
  - 没有顺序的要求，谁在前睡在后都行；
  - 也没有数量的要求，不写的样式就使用默认值；
  - 如：background: #bfa url(img/3.png) center center no-repeat fixed;

