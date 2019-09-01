

# CSS基础

## 1、CSS编写的位置

1. 可以将css编写在元素（标签）的style属性中，这种样式称之为**内联样式**。只对当前元素起作用，不方便复用属于表现与结构耦合不方便维护。

   `<p style="color:red;font-size:40px;">锄禾日当午，汗滴禾下土</p>`

2. 也可以将起编写在head标签中的style标签中，然后通过css选择器选中指定元素，称为**内联样式表**。

   ```html
   <head>
   	<meta charset="utf-8" />
   	<title>CSS</title>
   		
   	<style type="text/css">
   		p{
   			color:red;
   			font-size:40px;
   		}
   		
   	</style>
   		
   </head>
   ```

3. 将css编写成独立文件，然后在head标签中通过link标签引入,完全实现结构与表现分离，可以式样式表在其他页面中复用，同时利用浏览器的缓存加快页面加载速度提升用户体验。

   `<link rel="stylesheet" type="text/css" href="style.css" />`

## 2、CSS语法

### 1、基础语法说明

```html
	<style type="text/css">
			/*
				CSS的注释，作用和HTML注释类似，只不过它必须编写在style标签中，或者是css文件中
				CSS的语法：
					选择器 声明块
					
				选择器：
					- 通过选择器可以选中页面中指定的元素，
						并且将声明块中的样式应用到选择器对应的元素上
						
				声明块：
					- 声明块紧跟在选择器的后边，使用一对{}括起来，
						声明块中实际上就是一组一组的名值对结构，
							这一组一组的名值对我们称为声明，
						在一个声明块中可以写多个声明，多个声明之间使用;隔开，
						声明的样式名和样式值之间使用:来连接
			*/	
			p{
				color:red;
				font-size:50px;
			}
	</style>
```

### 2、常用选择器

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>常用选择器</title>
		<style type="text/css">
	</head>
	<body>
		<h1>悯农</h1>
		<p>锄禾日当午</p>
		<p>锄禾日当午</p>
		<p id="p1">锄禾日当午</p>
		<!-- 
			我们可以为元素设置class属性，
				class属性和id属性类似，只不过class属性可以重复
				拥有相同class属性值的元素，我们说他们是一组元素
				可以同时为一个元素设置多个class属性值，多个值之间使用空格隔开
		-->
		<p class="p2 hello">锄禾日当午</p>
		<p class="p2">锄禾日当午</p>
		<p class="p2">锄禾日当午</p>
		<p>锄禾日当午</p>
		<p>锄禾日当午</p>
		<p>锄禾日当午</p>
		<p class="p3">锄禾日当午</p>
		<span class="p3">汗滴禾下土</span>		
	</body>
</html>
```



#### 1.元素选择器

:通过元素选择器可以选择页面中的所有指定元素。

语法：**标签名 {}**

```css
p{
	color: red;
}
```



#### 2.id选择器

:通过元素的id属性值选中唯一的一个元素。

语法：**#id属性值 {}**

```css
#p1{
    font-size: 20px;
}
```

#### 3.类选择器

：通过元素的class属性选中一组元素。

语法：**.class属性值 {}**

```css
.hello{
    color: red;
}
```

#### 4.并集选择器（选择器分组)

：通过选择器分组可以同时选中多个选择器对应的元素。

语法：选择器1,选择器2,...,选择器n{}

```css
/*
 *为id为p1的元素，class为p2的元素，还有h1,同时设置一个背景颜色为黄色
*/
#p1 , .p2 , h1{
    background-color: yellow;
}
```

#### 5.交集选择器（复合选择器）

：可以选中同时满足多个选择器的元素。

语法：选择器1选择器2选择器n{}

```css
/*
 *为拥有class p3 span元素设置一个背景颜色为黄色
*/
span.p3{
    background-color: yellow;
}
```

#### 6.通配选择器

：可以用来选中页面中的所有元素。

语法：*{}

#### 7.后代元素选择器

：选中指定元素的指定后代。

语法：祖先元素 后代元素{}

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			/*
			 * 为div中的span设置一个颜色为绿色
			 * 后代元素选择器
			 * 	- 作用：
			 * 		- 选中指定元素的指定后代元素
			 * 	- 语法：
			 * 		祖先元素 后代元素{}	
			 */
			#d1 span{
				color: greenyellow;
			}
			/*
			 * 选中id为d1的div中的p元素中的span元素
			 */
			#d1 p span{
				font-size: 50px;
			}
			/*
			 * 为div的子元素span设置一个背景颜色为黄色
			 * 子元素选择器
			 * 	- 作用：
			 * 		- 选中指定父元素的指定子元素
			 * 	- 语法：
			 * 		父元素 > 子元素
			 * 
			 * IE6及以下的浏览器不支持子元素选择器
			 */
			div > span{
				background-color: yellow;
			}
		</style>
	</head>
	<body>
		<!--
			元素之间的关系
				父元素：直接包含子元素的元素
				子元素：直接被父元素包含的元素
				祖先元素：直接或间接包含后代元素的元素，父元素也是祖先元素
				后代元素：直接或间接被祖先元素包含的元素，子元素也是后代元素
				兄弟元素：拥有相同父元素的元素叫做兄弟元素			
		-->
		<div id="d1">
			<span>我是div标签中的span</span>
			<p><span>我是p标签中的span</span></p>
		</div>
		
		<div>
			<span>我是body中的span元素</span>
		</div>
	</body>
</html>
```

#### 8.子元素选择器

：选中指定父元素的指定子元素。

语法：父元素 > 子元素{}

```html
	<body>
		<span>我是span</span>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
		<span>hello</span>
	</body>
```

```css
/*
* 为第一个p标签设置一个背景颜色为黄色
* :first-child 可以选中第一个子元素
* :last-child 可以选中最后一个子元素
* 这里的第一个和最后一个子元素必须是指定元素下的，而非同类中的。
*/
body > p:first-child{
    background-color: yellow;
}
p:last-child{
    background-color: yellow;
}
/*
* :nth-child 可以选中任意位置的子元素
* 该选择器后边可以指定一个参数，指定要选中第几个子元素
* even 表示偶数位置的子元素
* odd 表示奇数位置的子元素
* 这里选中的也是指定元素下的所有元素排序而非同类中。
*/
p:nth-child{
    background-color: yellow;
}
/*
* :first-of-type
* :last-of-type
* :nth-of-type
* 		和:first-child这些非常的类似，
* 		只不过child，是在所有的子元素中排列
* 		而type，是在当前类型的子元素中排列
*/
p:first-of-type{
    background-color: yellow;
}
p:last-of-type{
    background-color: yellow;
}
```



#### 9.属性选择器

：可以根据元素中属性或属性只来选中元素。

语法：

[属性名] 选取含有指定属性的元素

[属性名="属性值"] 选取含有指定属性值的元素

[属性名^="属性值"] 选取属性值以指定内容开头的元素

[属性名$="属性值"] 选取属性值以指定内容结尾的元素

[属性名*="属性值"] 选取属性值以包含指定内容的元素

```css
/*
*为所有具有title属性的p元素，设置一个背景颜色为黄色
*/
p[title]{
    background-color: yellow;
}
/*
*为title属性值是hello的元素设置一个背景颜色为黄色
*/
p[title="hello"]={
    background-color: yellow;
}
/*
*为title属性值以ab开头的元素设置一个背景颜色为黄色
*/
p[title^="ab"]{
    background-color: yellow;
}
/*
*为title属性值以c结尾的元素设置一个背景颜色
*/
p[title$="c"]{
    background-color: yellow;
}
/*
*为title属性值包含c的元素设置一个背景颜色
*/
p[title*="c"]{
    background-color: yellow;
}
```

#### 10.兄弟选择器：

选中后一个兄弟：语法：前一个 + 后一个

选中后面所有同类型兄弟： 语法： 前一个 ~ 后边所有

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			/*
			 * 为span后的一个p元素设置一个背景颜色为黄色
			 * 后一个兄弟元素选择器
			 * 	作用：可以选中一个元素后紧挨着的指定的兄弟元素
			 * 	语法：前一个 + 后一个
			 * 
			 */
			/*span + p{
				background-color: yellow;
			}*/
			
			/*
			 * 选中后边的所有兄弟元素
			 * 	语法：前一个 ~ 后边所有	
			 */
			span ~ p{
				background-color: yellow;
			}
		</style>
	</head>
	<body>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
		<span>我是一个span</span>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
	</body>
</html>
```



### 3、伪类

**伪类专门用来表示元素的一种特殊状态**，比如：访问过的超链接，普通超链接，比如获取焦点的文本框，当我们要为这些处在特殊状态的元素设置样式时，就可以使用伪类。

```html
	<body>	
		<a href="http://www.baidu.com">访问过的链接</a>
		<br /><br />
		<a href="http://www.baidu123456.com">没访问过的链接</a>
		
		<p>我是一个段落</p>
		
		<!-- 使用input可以创建一个文本输入框 -->
		<input type="text" />
	</body>
```

1. ":link"：普通超链接；
2. “:visited”：访问过的超链接；
3. “:hover”：鼠标移入（可应用到其他元素）；
4. “:active”：鼠标点击状态（可应用到其他元素）；
5. “::selection,::-moz-selection”：选中p标签内容的状态；

```css
/*
*为没有访问过的链接设置一个颜色为绿色
* :link
*		-表示普通的超链接（未访问过的链接）
*/
a:link{
    color: yellowgreen;
}
/*
*为访问过的超链接设置一个颜色为红色
* :visited
*		-表示访问过的链接
*浏览器是通过历史记录来判断是否被访问过，由于涉及到隐私问题所以:visited只能设置字体颜色
*/
a:visited{
    color: red;
}
/*
* :hover表示鼠标移入的状态
*/
a:hover{
    color: skyblue;
}
/*
* :active表示超链接被点击的状态（鼠标未抬起）
*/
a:active{
    color: black;
}
/*
* :active和:hover也可以为其他元素设置
* IE6中不支持这两个对除超链接以外的元素设置
*/
p:active{
    background-color: yellow;
}
p:hover{
    background-color: orange;
}
/*
*文本框获取焦点后修改背景颜色
*/
input:focus{
    background-color: yellow;
}
/*
* 为p标签中选中的内容设置样式
* 使用::selection伪类
* 注意：兼容火狐要使用::-moz-selection
*/
p::selection{
    background-color: orange;
}
p::-moz-selection{
    background-color: orange;
}
```

涉及到a的伪类有4个：“:link、:visited、:houver、:active”,这4个伪类的优先级是一样的。

### 4、伪元素

使用伪元素来表示元素中的一些特殊的位置。

1. ":first-letter"：选中p元素文本中的第一个字符；
2. ":first-line"：选中文本的第一行；
3. “:before”：表示元素最前边的部分，一般结合content样式；
4. “:after”：表示元素最后面的部分，content样式可以向before和after加入内容。

```css
/*
* 为p中第一个字符设置一个样式
*/
p:first-letter{
    color: red;
    font-size: 20px;
}
/*
*为p中第一行设置一个背景颜色
*/
p:first-line{
    background-color: yellow;
}
/*
* 选中p元素最前面的部分，并插入内容
*/
p:before{
    content: "我会出现在整个段落的最前面，";
    color: red;
}
p:after{
    content: "我会出现在整个段落的最后面.";
    color: red;
}
```

### 5、否定伪类

可以从已选中的元素中剔除某些元素。

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			/*
			 * 为所有的p元素设置一个背景颜色为黄色，除了class值为hello的
			 * 
			 * 否定伪类：
			 * 	作用：可以从已选中的元素中剔除出某些元素
			 * 	语法：
			 * 		:not(选择器)
			 */
			p:not(.hello){
				background-color: yellow;
			}
		</style>
	</head>
	<body>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
		<p class="hello">我是一个p标签</p>
		<p>我是一个p标签</p>
		<p>我是一个p标签</p>
	</body>
</html>
```

### 6、样式继承

像儿子可以继承父亲的遗产一样，在CSS中，祖先元素上的样式，也会被他的后代元素所继承,

利用继承，可以将一些基本的样式设置给祖先元素，这样所有的后代元素将会自动继承这些样式。

但是并不是所有的样式都会被子元素所继承，比如：背景相关的样式都不会被继承 边框相关的样式 定位相关的。?

### 7、选择器的优先级

当使用不同的选择器，选中同一个元素时并且设置相同的样式时，这时样式之间产生了冲突，最终到底采用哪个选择器定义的样式，由选择器的优先级（权重）决定，优先级高的优先显示。?

```html
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			.p1{
				background-color: yellow;
			}
			
			p{
				background-color: red;
			}
			/*
			 * 当使用不同的选择器，选中同一个元素时并且设置相同的样式时，
			 * 	这时样式之间产生了冲突，最终到底采用哪个选择器定义的样式，由选择器的优先级（权重）决定
			 *  优先级高的优先显示。
			 * 
			 * 优先级的规则
			 * 		内联样式 ， 优先级  1000
			 * 		id选择器，优先级   100
			 * 		类和伪类， 优先级   10
			 * 		元素选择器，优先级 1 
			 * 		通配* ，    优先级 0
			 * 		继承的样式，没有优先级
			 * 
			 * 当选择器中包含多种选择器时，需要将多种选择器的优先级相加然后在比较，
			 * 	但是注意，选择器优先级计算不会超过他的最大的数量级，如果选择器的优先级一样，
			 * 	则使用靠后的样式。
			 * 
			 *  并集选择器的优先级是单独计算
			 * 	div , p , #p1 , .hello{}	
			 * 
			 *  可以在样式的最后，添加一个!important，则此时该样式将会获得一个最高的优先级，
			 * 	将会优先于所有的样式显示甚至超过内联样式，但是在开发中尽量避免使用!important
			 */
			*{
				font-size: 50px;
			}
			p{
				font-size: 30px;
			}
			#p2{
				background-color: yellowgreen;
			}
			p#p2{
				background-color: red;
			}
			.p3{
				color: green;
			}
			.p1{
				color: yellow;
				background-color: greenyellow !important;
			}
		</style>
	</head>
	<body>
		<p class="p1 p3" id="p2" style="background-color: orange;">我是一个段落
			<span>我是p标签中的span</span>
		</p>
	</body>
```

### 8、单位

#### 1.显示单位

```css
	<style type="text/css">
			/*
			 * 长度单位
			 * 		像素 px
			 * 			- 像素是我们在网页中使用的最多的一个单位，
			 * 				一个像素就相当于我们屏幕中的一个小点，
			 * 				我们的屏幕实际上就是由这些像素点构成的
			 * 				但是这些像素点，是不能直接看见。
			 * 			- 不同显示器一个像素的大小也不相同，
			 * 				显示效果越好越清晰，像素就越小，反之像素越大。
			 * 
			 * 		百分比 %
			 * 			- 也可以将单位设置为一个百分比的形式，
			 * 				这样浏览器将会根据其父元素的样式来计算该值
			 * 			- 使用百分比的好处是，当父元素的属性值发生变化时，
			 * 				子元素也会按照比例发生改变
			 * 			- 在我们创建一个自适应的页面时，经常使用百分比作为单位
			 * 
			 * 		em
			 * 			- em和百分比类似，它是相对于当前元素的字体大小来计算的
			 * 			- 1em = 1font-size
			 * 			- 使用em时，当字体大小发生改变时，em也会随之改变
			 * 			- 当设置字体相关的样式时，经常会使用em
			 * 			
			 */
			.box{
				width: 300px;
				height: 300px;
				background-color: red;
			}
			
			.box1{
				font-size: 20px;
				width: 2em;
				height: 50%;
				background-color: yellow;
			}
			
	</style>
```

#### 2.颜色单位

```css
	<style type="text/css">
			.box1{
				width: 100px;
				height: 100px;
				/*
				 * 颜色单位：
				 * 	 在CSS可以直接使用颜色的单词来表示不同的颜色
				 * 		红色：red
				 * 		蓝色：blue
				 * 		绿色：green	
				 *   也可以使用RGB值来表示不同的颜色
				 * 		- 所谓的RGB值指的是通过Red Green Blue三元色，
				 * 			通过这三种颜色的不同的浓度，来表示出不同的颜色
				 * 		- 例子：rgb(红色的浓度,绿色的浓度,蓝色的浓度);
				 * 			- 颜色的浓度需要一个0-255之间的值，255表示最大，0表示没有
				 * 			- 浓度也可以采用一个百分数来设置，需要一个0% - 100%之间的数字
				 * 				使用百分数最终也会转换为0-255之间的数
				 * 				0%表示0
				 * 				100%表示255
				 *   也可以使用十六进制的rgb值来表示颜色，原理和上边RGB原理一样，
				 * 		只不过使用十六进制数来代替，使用三组两位的十六进制数组来表示一个颜色
				 * 		每组表示一个颜色	,第一组表示红色的浓度，范围00-ff
				 * 					第二组表示绿色的浓度，范围是00-ff
				 * 					第三组表示蓝色的浓度，范围00-ff
				 * 		语法：#红色绿色蓝色
				 * 		十六进制：
				 * 		0 1 2 3 4 5 6 7 8 9 a b c d e f
				 * 		00 - ff
				 * 		00表示没有，相当于rgb中的0
				 * 		ff表示最大，相当于rgb中255
				 * 		红色：
				 * 			#ff0000
				 * 		像这种两位两位重复的颜色，可以简写
				 * 			比如：#ff0000 可以写成 #f00
				 * 			#abc  #aabbcc		
				 * 			
				 */
				/*background-color: rgb(161,187,215);*/
				/*background-color: rgb(100%,50%,50%);*/
				/*background-color: #00f;*/
				/*background-color: #abc;*/ /*#aabbcc*/
				background-color: #084098;
			}
		</style>
```

### 9、文本

#### 1.字体的样式

> color 、font-size、font-family

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			.p1{
				/*设置字体颜色,使用color来设置文字的颜色*/
				color: red;
				/*
				 * 设置文字的大小,浏览器中一般默认的文字大小都是16px
				 	font-size设置的并不是文字本身的大小，
				 		在页面中，每个文字都是处在一个看不见的框中的
				 		我们设置的font-size实际上是设置格的高度，并不是字体的大小
				 		一般情况下文字都要比这个格要小一些，也有时会比格大，
				 		根据字体的不同，显示效果也不能	
				 * */
				font-size: 30px;
				/*
				 * 通过font-family可以指定文字的字体
				 * 	当采用某种字体时，如果浏览器支持则使用该字体，
				 * 		如果字体不支持，则使用默认字体
				 * 该样式可以同时指定多个字体，多个字体之间使用,分开
				 * 	当采用多个字体时，浏览器会优先使用前边的字体，
				 * 		如果前边没有在尝试下一个
				 */
				/*font-family: arial , 微软雅黑;*/
				/*
				 * 浏览器使用的字体默认就是计算机中的字体，
				 * 	如果计算机中有，则使用，如果没有就不用
				 * 
				 * 在开发中，如果字体太奇怪，用的太少了，尽量不要使用，
				 * 	有可能用户的电脑没有，就不能达到想要的效果。
				 */
				/*font-family: 华文彩云 , arial , 微软雅黑;*/
				font-family: "curlz mt";
			}
		</style>
	</head>
	<body>
		<p class="p1">
			我是一个p标签，ABCDEFGabcdefg
		</p>
	</body>
</html>
```

#### 2.字体的分类

> font-family

```html
	<body>
		<!-- 
			在网页中将字体分成5大类：
				serif（衬线字体）
				sans-serif（非衬线字体）
				monospace （等宽字体）
				cursive （草书字体）
				fantasy （虚幻字体）
			可以将字体设置为这些大的分类,当设置为大的分类以后，
				浏览器会自动选择指定的字体并应用样式
			一般会将字体的大分类，指定为font-family中的最后一个字体	
		-->
		<p style="font-size: 50px; font-family: serif;">衬线字体：我是一段文字，ABCDEFGabcdefg</p>
		<p style="font-size: 50px; font-family: sans-serif;">非衬线字体：我是一段文字，ABCDEFGabcdefg</p>
		<p style="font-size: 50px; font-family: monospace;">等宽字体：我是一段文字，IHABCDEFGabcdefg</p>
		<p style="font-size: 50px; font-family: cursive;">草书字体：我是一段文字，ABCDEFGabcdefg</p>
		<p style="font-size: 50px; font-family: fantasy;">虚幻字体：我是一段文字，ABCDEFGabcdefg</p>
	</body>
```

#### 3.字体的其他样式

>  font 、font-weight 、font-style、font-variant

```html
	<style type="text/css">
			.p1{
				color: red;
				font-size: 30px;
				font-family: "微软雅黑";
				/*
				 * font-style可以用来设置文字的斜体
				 * 	- 可选值：
				 * 		normal，默认值，文字正常显示
				 * 		italic 文字会以斜体显示
				 * 		oblique 文字会以倾斜的效果显示
				 * 	- 大部分浏览器都不会对倾斜和斜体做区分，
				 * 		也就是说我们设置italic和oblique它们的效果往往是一样的
				 *  - 一般我们只会使用italic
				 */
				font-style: italic;
				/*
				 * font-weight可以用来设置文本的加粗效果：
				 * 		可选值：
				 * 			normal，默认值，文字正常显示
				 * 			bold，文字加粗显示
				 * 
				 * 	该样式也可以指定100-900之间的9个值，
				 * 		但是由于用户的计算机往往没有这么多级别的字体，所以达到我们想要的效果
				 * 		也就是200有可能比100粗，300有可能比200粗，但是也可能是一样的
				 */
				font-weight: bold;
				/*
				 * font-variant可以用来设置小型大写字母
				 * 		可选值：
				 * 			normal，默认值，文字正常显示
				 * 			small-caps 文本以小型大写字母显示
				 * 
				 * 小型大写字母：
				 * 		将所有的字母都以大写形式显示，但是小写字母的大写，
				 * 			要比大写字母的大小小一些。
				 */
				font-variant: small-caps ;
			}
			.p2{
				/*设置一个文字大小*/
				font-size: 50px;
				/*设置一个字体*/
				font-family: 华文彩云;
				/*设置文字斜体*/
				font-style: italic;
				/*设置文字的加粗*/
				font-weight: bold;
				/*设置一个小型大写字母*/
				font-variant: small-caps;
			}
			.p3{
				/*
				 * 在CSS中还为我们提供了一个样式叫font，
				 * 	使用该样式可以同时设置字体相关的所有样式,
				 * 	可以将字体的样式的值，统一写在font样式中，不同的值之间使用空格隔开
				 * 
				 * 使用font设置字体样式时，斜体 加粗 小大字母，没有顺序要求，甚至可写可不写，
				 * 	如果不写则使用默认值，但是要求文字的大小和字体必须写，而且字体必须是最后一个样式
				 * 	大小必须是倒数第二个样式
				 * 
				 * 实际上使用简写属性也会有一个比较好的性能
				 */
				font: small-caps bold italic 60px "微软雅黑";
			}
		</style>
	</head>
	<body>
		<p class="p3">我是一段文字，ABCDEFGabcdefg</p>
		<p class="p1">我是一段文字，ABCDEFGabcdefg</p>
		<p class="p2">我是一段文字，ABCDEFGabcdefg</p>
	</body>
```

#### 4.行间距

> font、line-height

```css
		<style type="text/css">
			/*
			 * 在CSS并没有为我们提供一个直接设置行间距的方式，
			 * 	我们只能通过设置行高来间接的设置行间距，行高越大行间距越大
			 * 使用line-height来设置行高 
			 * 	行高类似于我们上学单线本，单线本是一行一行，线与线之间的距离就是行高，
			 * 	网页中的文字实际上也是写在一个看不见的线中的，而文字会默认在行高中垂直居中显示
			 * 
			 * 行间距 = 行高 - 字体大小
			 */
			.p1{
				font-size: 20px;
				/*
				 * 通过设置line-height可以间接的设置行高，
				 * 	可以接收的值：
				 * 		1.直接就收一个大小
				 * 		2.可以指定一个百分数，则会相对于字体去计算行高
				 * 		3.可以直接传一个数值，则行高会设置字体大小相应的倍数
				 */
				/*line-height: 200%;*/
				line-height: 2;
			}
			.box{
				width: 200px;
				height: 200px;
				background-color: #bfa;
				/*
				 * 对于单行文本来说，可以将行高设置为和父元素的高度一致，
				 * 	这样可以是单行文本在父元素中垂直居中
				 */
				line-height: 200px;
			}
			.p2{
				/*
				 * 在font中也可以指定行高
				 * 	在字体大小后可以添加/行高，来指定行高，该值是可选的，如果不指定则会使用默认值
				 */
				font: 30px "微软雅黑";
				line-height: 50px;
			}
		</style>
```

#### 5.文本的样式

> text-transform：设置文本的大小写。
>
> text-decoration：可以用来设置文本的修饰
>
> letter-spacing：可以指定字符间距
>
> word-spacing：可以设置单词之间的距离，实际上就是设置词与词之间空格的大小。
>
> text-align：用于设置文本的对齐方式
>
> text-indent：用来设置首行缩进

```css
		<style type="text/css">
			.p1 {
				/*
				 * text-transform可以用来设置文本的大小写
				 * 	可选值：
				 * 		none 默认值，该怎么显示就怎么显示，不做任何处理
				 * 		capitalize 单词的首字母大写，通过空格来识别单词
				 * 		uppercase 所有的字母都大写
				 * 		lowercase 所有的字母都小写
				 */
				text-transform: lowercase;
			}
			.p2 {
				/*
				 * text-decoration可以用来设置文本的修饰
				 * 		可选值：
				 * 			none：默认值，不添加任何修饰，正常显示
				 * 			underline 为文本添加下划线
				 * 			overline 为文本添加上划线
				 * 			line-through 为文本添加删除线
				 */
				text-decoration: line-through;
			}
			a {
				/*超链接会默认添加下划线，也就是超链接的text-decoration的默认值是underline
				 	如果需要去除超链接的下划线则需要将该样式设置为none
				 * */
				text-decoration: none;
			}
			.p3 {
				/**
				 * letter-spacing可以指定字符间距
				 */
				/*letter-spacing: 10px;*/
				/*
				 * word-spacing可以设置单词之间的距离
				 * 	实际上就是设置词与词之间空格的大小
				 */
				word-spacing: 120px;
			}
			.p4{
				/*
				 * text-align用于设置文本的对齐方式
				 * 	可选值：
				 * 		left 默认值，文本靠左对齐
				 * 		right ， 文本靠右对齐
				 * 		center ， 文本居中对齐
				 * 		justify ， 两端对齐
				 * 				- 通过调整文本之间的空格的大小，来达到一个两端对齐的目的
				 */
				text-align: justify ;
			}
			.p5{
				font-size: 20px;
				/*
				 * text-indent用来设置首行缩进
				 * 	当给它指定一个正值时，会自动向右侧缩进指定的像素
				 * 	如果为它指定一个负值，则会向左移动指定的像素,
				 * 		通过这种方式可以将一些不想显示的文字隐藏起来
				 *  这个值一般都会使用em作为单位
				 */
				text-indent: -99999px;
			}
		</style>
```

## 3、盒子模型

盒子模型包含四部分：内容content、内边距padding（内容到边框的距离）、边框（border）、外边距margin（元素间的距离）。

**内容（content）**：

+ 使用width和heigth设置内容的宽高。
+ 使用background-color：设置背景颜色。

**边框（border）**：

+ border-width：设置边框宽度：四个值（上、右、下、左），三个值（上、左右、下），两个值（上下、左右），CSS中还提供了四个border-xxx-width，xxx表示四个值（top right bottom left）。

+ border-color：设置边框颜色。其他同上。

+ border-style：设置边框样式。值的顺序同上，none（无边框）、solid（实线）、dotted（点状边框）、dashed（虚线）、double（双线）。

  ```css
  		.box{
  				width: 200px;
  				height: 200px;
  				background-color: #bfa;
  				/*设置边框
  				 	大部分的浏览器中，边框的宽度和颜色都是有默认值，而边框的样式默认值都是none
  				 * */
  				/*border-width:10px ;
  				border-color: red;
  				border-style: solid;*/
  				/*
  				 * border
  				 * 	- 边框的简写样式，通过它可以同时设置四个边框的样式，宽度，颜色
  				 * 	- 而且没有任何的顺序要求
  				 * 	- border一指定就是同时指定四个边不能分别指定
  				 * 
  				 * border-top border-right border-bottom border-left
  				 * 	可以单独设置四个边的样式，规则和border一样，只不过它只对一个边生效
  				 */
  				/*border: red solid 10px   ;*/
  				/*border-left: red solid 10px   ;*/
  				
  				/*border-top: red solid 10px;
  				border-bottom: red solid 10px;
  				border-left: red solid 10px;*/
  				border: red solid 10px;
  				border-right: none;
  			}
  ```

**内边距（padding）**:

内边距会影响盒子的可见框的大小，元素的背景会延伸到内边距.

盒子的大小由内容区、内边距和边框共同决定。

padding的数据规则和boder-width一至。

```css
		.box1{
				width: 200px;
				height: 200px;
				background-color: #bfa;
				/*设置边框*/
				border: 10px red solid;
				/*
				 * 内边距（padding），指的是盒子的内容区与盒子边框之间的距离
				 * 	一共有四个方向的内边距，可以通过：
				 * 		padding-top
				 * 		padding-right
				 * 		padding-bottom
				 * 		padding-left
				 * 			来设置四个方向的内边距
				 * 
				 * 内边距会影响盒子的可见框的大小，元素的背景会延伸到内边距,
				 * 	盒子的大小由内容区、内边距和边框共同决定
				 * 	盒子可见框的宽度 = border-left-width + padding-left + width + padding-right + border-right-width
				 *  可见宽的高度 = border-top-width + padding-top + height + padding-bottom + border-bottom-width
				 */
				/*设置上内边距*/
				/*padding-top: 100px;*/
				/*设置右内边距*/
				/*padding-right: 100px;
				padding-bottom: 100px;
				padding-left: 100px;*/
				
				/*
				 * 使用padding可以同时设置四个边框的样式，规则和border-width一致
				 */
				/*padding: 100px;*/
				
				/*padding: 100px 200px;*/
				
				/*padding: 100px 200px 300px;*/
				
				padding: 100px 200px 300px 400px;
			}
			/*
			 * 创建一个子元素box1占满box2
			 */
			.box2{
				width: 100%;
				height: 100%;
				background-color: yellow;
			}
```

**外边距（margin）**:

外边距指当前盒子与其他盒子的距离，外边距不影响可见框的大小，但会影响盒子的位置。

由于页面中的元素都是靠左考上摆放的，所以当设置上和左外边距时会导致盒子自身的位置变化，当设置下或者右时会改变其他盒子的位置。

+ margin有四个方向：margin-top、margin-right、margin-bottom、margin-left.

+ margin和padding以及border-weight的规则一至,可以同时设置四个方向的外边距。

+ 如果外边距设置的是负值，则元素会向反方向移动。

+ ```css
  				/*
  				 * margin还可以设置为auto，auto一般只设置给水平方向的margin
  				 * 	如果只指定，左外边距或右外边距的margin为auto则会将外边距设置为最大值
  				 * 	垂直方向外边距如果设置为auto，则外边距默认就是0
  				 * 
  				 * 如果将left和right同时设置为auto，则会将两侧的外边距设置为相同的值，
  				 * 	就可以使元素自动在父元素中居中，所以我们经常将左右外边距设置为auto
  				 * 	以使子元素在父元素中水平居中
  				 * 
  				 */
  ```

+ 垂直外边距重叠：在网页中垂直方向的外边距会发生外边距重叠，所谓的外边距重叠指兄弟元素之间的相邻外边距会取最大值而不是取和。如果父子元素的垂直外边距相邻了，则子元素的外边距会设置给父元素。

+ 子元素的大小如果超出了父元素的content则子元素会溢出，如果在显示上子元素与父元素相邻的话，子元素设置margin不会影响到父元素的兄弟元素。

**默认样式**：

浏览器为了在页面中没有样式时也显示比较好的效果，设置了默认的padding和margin，这些默认的样式是不需要的。

```css
*{
    margin: 0;
    padding: 0;
}
```

### 2、内联样式的盒子模型

> 内容区 、内边距、边框、外边距

+ 内容区

  内联样式不能设置width和height

+ 内边距

  内联样式可以设置水平方向的内边距padding-left、padding-right

  内联样式可以设置垂直方向的内边距padding-top、padding-bottom，但不会影响页面布局（即如果周围有其他元素不会产生挤压而是遮挡）。

+ 边框

  可以设置边框，但垂直的边框不会影响到页面的布局（即不会影响其他元素的布局（位置）而是遮挡）。

+ 外边距

  内联元素支持水平方向的外边距，不支持垂直方向的外边距。

  两个相邻的内联元素水平方向的外边距是求和而不是重叠。

## 4、布局属性

### 1、display属性

display属性用来改变元素的性质，可选值包括：

+ inline：可将一个元素变成内联元素显示；
+ block：可将一个元素变成一个块级元素显示；
+ inline-block：将一个元素设置为“行内块元素”，即一个元素（既有内联元素的特点，又有块元素的特点）即可以设置 width和height又不会独占一行；
+ none：不显示元素，并且元素不会在页面中占有位置。

### 2、visibility属性

用于设置元素是否可见，可选值：

+ visible：默认值，元素默认在页面中显示；
+ hidden：元素隐藏，和display:none不同的是，隐藏的元素会在页面中占据位置。

### 3、overflow属性

用于处理子元素溢出父元素。

理论上子元素最大可以占据父元素的内容区的大小，默认情况下如果子元素的大小超出了父元素的大小，则超出部分会在父元素以外显示，超出部分称溢出内容。

overflow可选值：

+ visible：默认值，不会对溢出内容做处理，默认显示在父元素以外；
+ hidden：溢出的内容会被修剪，不会显示；
+ scroll：为父元素设置滚动条，通过拖动滚动条来查看子元素完整内容，无论子元素是否溢出，都会为父元素在垂直和水平方向添加滚动条；
+ auto：会根据需求自动添加滚动条，需要水平就添加水平方向，需要垂直方向就添加垂直方向，如果不需要就不添加。

## 5、布局

### 1、文档流

**文档流处在网页的最底层，它表示的是网页中的一个位置，我们创建的元素默认都处在文档流中。**

元素在文档流中的特点：

+ 块元素：
  1. 块元素在文档流中会独占一行，块元素会自上而下排列；
  2. 块元素在文档流中默认宽度是父元素的100%；
  3. 块元素在文档流中的高度默认被内容撑开。
+ 内联元素：
  1. 内联元素在文档流中只占自身的大小，默认从左向右排列，如果一行不能容纳所有内联元素，则换到下一行，重新自左向右排列；
  2. 在文档流中，内联元素的宽和高会默认被内容撑开。

块元素默认的宽高值为auto，当宽度值为auto时，此时设置内边距不会影响可见框的大小，而是自动调整，以适应内边距。

### 2、浮动

使用float属性，设置元素浮动（像氢气球一样），从而脱离文档流。

块元素在文档流中默认是垂直排列，如果希望块元素在页面中水平排列，可以使用float来使元素浮动，从而使块元素脱离文档流。

可选值：

+ none：默认值，元素默认在文档流中排列；
+ left：元素会脱离文档流，向页面左侧浮动；
+ right：元素会脱离文档流，向页面右侧浮动。

效果：当一个元素设置浮动后（float属性是一个非none值），元素会立即脱离文档流，元素脱离文档流后，它下面的元素会立即向上移动，元素浮动以后，会尽量向页面的左上或右上漂浮，**直到遇到父元素的边框或者其他的浮动元素**。

1. 如果浮动元素上边是一个没有浮动的块元素，则浮动元素不会超过块元素；
2. 浮动的元素不会超过它上边的兄弟愿随，最多并排；
3. 浮动的元素不会盖住文字，文字会自动环绕在浮动元素周围（常用浮动过来设置文字环绕图片的效果），如p标签上有一个块元素浮动，p标签上移，但是浮动元素不会挡住文字。
4. 在文档流中，子元素的宽度默认占父元素的全部，当元素设置浮动后，会完全脱离文档流，块元素脱离文档流以后，高度和宽度都被内容撑开。
5. 开启span的浮动，内联元素脱离文档流以后会变成块元素可以设置宽高。

### 3、清除浮动

```html
<head>
    <style type="text/css">
    	.box1 {
    		width: 100px;
    		height: 100px;
    		background-color: yellow;
    		float: left;
    	}
    	.box2 {
    		width: 200px;
    		height: 200px;
    		background-color: yellowgreen;
            /*清除其他元素浮动对本元素的影响*/
            /*clear: left;*/
            float: right;
    	}
        .box3 {
            width: 300px;
            height: 300px;
            background-color: skyblue;
            clear: both
        }
    </style>
</head>
<body>
	<div class="box1"></div>
    <div class="box2"></div>
    <div class="box3"></div>
</body>
```

由于受到box1浮动的影响，box2整体向上移动了100px，

我们有时希望清除掉其他元素浮动对当前元素产生的影响，这是可以用clear属性来完成该功能；

> clear可以用来清除其他浮动元素对挡墙元素的影响，可选值：
>
> - none：默认值，不清除浮动影响；
> - left：清除左侧浮动元素对当前元素的影响；
> - right：清除右侧浮动元素对当前元素的影响；
> - both：清除两侧浮动元素对当前元素的影响，清除对当前元素影响最大的那个元素的浮动。



## 6、解决高度塌陷问题

**高度塌陷解释**：在文档流中，父元素的高度默认是被子元素撑开的，即子元素多高父元素就多高。当为子元素设置浮动后，子元素完全脱离文档流，此时会导致子元素无法撑起父元素的高度，导致父元素高度塌陷。由于父元素高度塌陷了，则父元素下的所有元素都会向上移动，导致布局混乱。

### 方式一

可以将父元素的高度写死，以避免高度塌陷的问题，但是这样父元素的高度就无法自动适应子元素的高度，所以这种方案不推荐使用。

### 方式二

> 根据W3C的标准，在页面中元素都有一个隐含的属性角坐Block Formatting Context,简称**BFC**，该属性可以设置打开或者关闭，默认是关闭的。
>
> 当开启元素的BFC后，元素将会具有如下特性：
>
> 1. 父元素的垂直外边距不会和子元素重叠；
> 2. 开启BFC的元素不会被浮动元素覆盖；
> 3. 开启BFC的元素可以包含浮动的子元素。
>
> 如何开启元素的BFC：
>
> 1. 设置元素浮动
>    - 使用这种方式开启，虽然可以撑开父元素，待会导致父元素的宽度丢失，而且使用这种方式也会导致下边的元素上移，不能解决问题。
> 2. 设置元素绝对定位；
> 3. 设置元素为inline-block
>    - 可以解决问题，但是会导致宽度丢失，不推荐使用。
> 4. 将元素的overflow设置为一个非visible的值。
>    - 推荐方式：将**overflow设置为hidden是副作用最小的开**启BFC的方式。
>
> 在IE6及以下的浏览器中并不支持BFC，所以使用这种方式不能兼容IE6。在IE6中虽然没有BFC，但是具有另外一个隐含的属性叫做**hasLayout**，该属性的作用和BFC类似，所以在IE6中可以通过打开hasLayout来解决问题，开启方式很多，尽量选择使用一种副作用最小的：**直接将元素的zoom设置为1即可**。
>
> - zoom表示放大的意思，后面跟着一个数值，写几就表示放大几倍。
> - zoom: 1 表示不放大元素，但是通过该样式可以开启hasLayout；
> - zoom这个样式在IE中支持，其他浏览器不支持。
>
> ` overflow: hidden;
>
> zoom: 1; `

### 方式三

> 可以直接在高度塌陷的父元素的最后，添加一个空白的div，
>
> 由于这个div并没有浮动，所以他是可以撑开父元素的高度的，
>
> 然后对其设置clear属性清除浮动影响，基本没有副作用。
>
> 虽然可以解决问题，但是会在页面中添加多余结构。

```html
<head>
    <style type="text/css">
        .box1 {
            border: 1px solid red;
        }
        .box2 {
            width: 100px;
            height: 100px;
            background-color: blue;
            float: left;
        }
        .clear {
            clear: both
        }
    </style>
</head>
<body>
    <div class="box1">
        <div class="box2"></div>
        <div class="clear"></div>
    </div>
</body>
```

### 方式四

通过after伪类选中父元素box的后边，并添加一个空元素块对齐设置clear属性，这样基本没有副作用，最推荐使用。

```html
<head>
    <style type="text/css">
        .box1 {
            border: 1px solid red;
        }
        .box2 {
            width: 100px;
            height: 100px;
            background-color: blue;
            float: left;
        }
        .clearfix:after {
            /*添加一个内容*/
            content: "";
            /*转换为一个块元素*/
            display: block;
            /*清除两侧浮动*/
            clear:both
        }
        .clearfix {
            /*IE6不支持使用zoom开启haslayout*/
            zoom: 1
        }
    </style>
</head>
<body>
    <div class="box1 clearfix">
    	<div class="box2"></div>
    </div>
</body>
```





## 7、导航条案例

```html
	<head>
		<meta charset="utf-8">
		<title>导航</title>
		<style type="text/css">	
			/* 清空默认样式 */
			* {
				margin: 0;
				padding: 0;
			}
			
			/* 设置ul */
			.nav {
				/* 去除符号样式 */
				list-style: none;
				background-color: #6495ED;
				/* 在IE6中设置宽度,默认会把hasLayout属性打开 */
				width: 1000px;
				/* 使用margin设置居中 */
				margin: 50px auto;
				
				/* 解决高度塌陷 */
				overflow: hidden;
				zoom: 1;
			}
			
			.nav li {
				float: left;
				width: 10%;
			}
			
			.nav a{
				/* 将a设置为块元素 */
				display: block;
				/* 为a指定一个宽度 */
				width: 100%;
				/* 设置文字居中 */
				text-align: center;
				/* 去掉a中文字修饰 */
				text-decoration: none;
				/* 设置上下边距 */
				padding: 5px 0;
				/* 字体白色加粗 */
				color: white;
				font-weight: bold;
			}
			
			/* 设置伪类 */
			.nav a:hover {
				background-color: #c00;
			}
		</style>
		
	</head>
	<body>
		<ul class="nav">
			<li><a href="#">首页</a></li>
			<li><a href="#">搞笑</a></li>
			<li><a href="#">人文</a></li>
			<li><a href="#">科普</a></li>
			<li><a href="#">动漫</a></li>
			<li><a href="#">首页</a></li>
			<li><a href="#">搞笑</a></li>
			<li><a href="#">人文</a></li>
			<li><a href="#">科普</a></li>
			<li><a href="#">动漫</a></li>
		</ul>
	</body>
```



