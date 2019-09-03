# HTML基础

## 1、基础标签

标签是网页的基础框架，使用标签时不关注标签的显示样式，样式可以通过css来进行调整，而标签更关注自身的语义，对于搜索引擎来说会通过标签的语义来检索信息。

<html></html>:html根标签，一个页面中有且只有一个根标签，网页中的所有内容都应该写在html根标签中

<head></head>:head标签，该标签中的内容，不会在网页中直接显示，它用来帮助浏览器解析页面。
**title标签**:默认会显示在浏览器的标题栏中，搜索引擎检索时会首先检索title标签中的内容，它是网页中对搜索引擎来说最重要的内容，会影响到网页在搜索引擎中的排名。

```html
<html>
    <head>
		<!--告诉浏览器网页的编码字符集-->
        <meta charset="utf-8" />
        <title></title>
    </head>
</html>
```

**meta标签（自结束标签）**：用来设置网页的一些元数据，比如编码字符集，简介，关键字等。

```html
<head>
		<meta charset="utf-8" />
		<title></title>
		<!-- 
			使用meta标签还可以用来设置网页的关键字
		-->
		<meta name="keywords" content="HTML5,JavaScript,前端,Java" />
		<!-- 
			还可以用来指定网页的描述
			搜索引擎在检索页面时，会同时检索页面中的关键词和描述，但是这两个值不会影响页面在搜索引擎中的排名
		-->
		<meta name="description" content="发布h5、js等前端相关的信息" />
		<!-- 
			使用meta可以用来做请求的重定向
			<meta http-equiv="refresh" content="秒数;url=目标路径" />
		-->
		<meta http-equiv="refresh" content="5;url=http://www.baidu.com" />
	</head>
```



**h1~h6标签**：六级标题标签，关注标签的语义，对浏览器来说h1的重要性仅次于title，搜索引擎在查看完title后会立即查看h1的内容，一个网页中只有一个h1，一般只使用h1，h2，h3。h3之后基本不用。

**p标签**：表示一个段落标签，p标签中的文字默认会独占页面中的一行，并且p标签之间会有一个距离。（在html中字符之间写再多的空格浏览器都会解析成一个空格，换行也会解析成一个空格。）

**br（自结束标签）**：表示一个换行标签。

**hr（自结束标签）**：在页面中生成一个水平线。

**img（自结束标签）**：图片标签，向网页中引入一张外部图片。

​										属性：

​												src：设置一个外部图片的路径；

​												alt：设置图片不能显示时图片的路径，关键是搜索引擎通过alt来识别不同的图片；

​												width：用来设置图片的宽度，单位一般是px

​												height：用来设置图片的高度。



## 2、实体

在html中>和<不直接使用，需要使用特殊符号来表示这些特殊字符，称这些符号为实体（转义字符）。

"<"  ：&lt

">" ：&gt

空格：&nbsp

版权符号：&copy

引号：&quot

## 3、属性

1. class和id属性：我们可以为元素设置class属性，
   							class属性和id属性类似，只不过class属性可以重复
      							拥有相同class属性值的元素，我们说他们是一组元素
      							可以同时为一个元素设置多个class属性值，多个值之间使用空格隔开。

## 4、块元素和内联元素

**块级元素（block level element）**:块元素不论元素内容多少都会独占一行，即会以新行开始。div是一个块元素，**没有任何语义，它不会给其内的元素设置任何默认样式，组合其他标签的容器**，div主要是用来对网页布局的。

块元素例：<div>、<h1>、<p>、<ul>、<table>

**内联元素（inline element）**:内联元素不会独占一行，只占自身内容的大小，即不会以新行开头。span是一个内联元素，**没有任何语义，专门用来选中文字来为文字设置样式，作为文本的容器**。

内联元素例子：<span>、<a>、<img>、<iframe>、<td>

块元素主要用来做页面布局，内联元素用来选中文字设置样式。

**一般情况下，使用块元素包含内联元素，而不使用内联元素去包含块元素。**

1. a元素可以包含任意元素，除了它本身。
2. p元素不能包含任何块元素。

## 5、表格

HTML中使用table创建一个表格：

table：表格；

tr：在table标签内，表示表格的一行；

th：在tr标签内，表示表头的一列，表头的默认样式是字体加粗居中等默认效果；

td：在tr标签内，表示表格的一列；

- td的colsapn属性表示横向合并单元格，后面跟合并的单元格个数；
- td的rowspan属性表示纵向合并单元格。

## 6、长表格

有一些情况下表格是非常长的，这时候就需要将表格分为三个部分，表头、表格的主题、表格底部。

在HTML中为我们提供了三个标签：

- thead：表头
- tbody：表格主体
- tfoot：表格底部

这三个标签的作用，就是来区分表格的不同部分，他们都是table的子标签，都需要直接写到table中，tr需要写到这些标签当中。

1. thead中的内容，永远会显示在表格头部；
2. tfoot中的内容，永远会显示在表格底部；
3. tbody中的内容，永远都会显示在表格中间；

通常情况下我们直接写tr而不包含tbody，浏览器会自动在表格中添加tbody并且将所有的tr都放到tbody中，所以注意tr并不是table的子元素，通过table > tr无法选中行，需要通过tbody>tr选中。

```html
<head>
	<style type="text/css">
    	
    </style>
</head>
<body>
    <table>
        <thead>
        	<tr>
            	<td>日期</td>
                <td>收入</td>
                <td>支出</td>
                <td>合计</td>
            </tr>
        </thead>
        <tfoot>
            <td></td>
            <td></td>
            <td>合计</td>
            <td>￥100.00</td>
        </tfoot>
        <tbody>
        	<tr>
				<td>10.24</td>
				<td>500</td>
				<td>300</td>
				<td>200</td>
			</tr>
			<tr>
				<td>10.24</td>
				<td>500</td>
				<td>300</td>
				<td>200</td>
			</tr>
        </tbody>
    </table>
</body>
```

## 7、表单

表单的作用就是用来将用户信息提交给服务器的。

form：form标签用来创建一个表单；

- form标签中必须指定action属性，表示表单提交的服务器地址；
- form创建的仅仅是一个空白表单，还需向form中添加不同的表单项。

form：fieldset：表单中可以使用fieldset来为表单项进行分组，可以将表单项中的同一组放到fieldset中。

fieldset：legend：fieldset可以使用子标签legend，用来指定组名；

input：用来创建一个表单项；

- 用type属性指定类型；
  - text表示一个文本框；
  - password表示一个密码框；
  - radio表示一个单选按钮，单选按钮可以通过name属性进行分组，name属性相同的是一组按钮，单选按钮不需要用户填写内容，要填写value属性给出默认值。
  - checkbox表示多选框，和单选按钮类似；
  - submit表示提交按钮，用于提交表单，value属性表示文字上内容；
  - reset表示一个表单重置按钮，表单恢复默认值；
  - botton表示一个单纯的按钮，value属性设置按钮上的文字，需要使用js绑定时间使用。
- name属性表示提交内容的名字；
- value属性可选表示内容的默认值
- checked：如果希望在单选框或者是多选框中指定默认选中的选项则可以在希望选中的项中添加check=“checked”

label：表示表单项前文字；

- 使用这个标签可以用css设置样式；
- for属性指向表单项的id，填写这个属性当选中这个label自动聚焦到指定表单项；

textarea：创建一个文本域表单项。

select：下拉列表，使用select来创建一个下拉表单，指定name属性；

- multiple="multiple"下拉列表变为一个多选的下拉列表；

select：option：表示下拉列表项，设置value属性；

- 通过在option中添加selected=“selected”来讲选项设置为默认选中。

select：optgrounp：将option分组。

button：表示按钮，使用和input类似，使用起来更加灵活，使用type来指示按钮类型：

- submit：表示提交按钮，用于提交表单和`<input type="submit" value="提交">`功能一样；
- reset：表示重置表单，和`<input type="reset" value="重置">`功能一样；
- button：表示普通按钮，和`<input type="button" value="按钮">`功能一样；

```html
<body>
    <form action="target.html">
        <!--使用fieldset分组-->
        <fieldset>
            <!--指定组名-->
            <legend>用户信息</legend>
            <label for="um">用户名</label>
            <input id="um" type="text" name="username"/><br/><br/>
            <label for="pwd">密码</label>
            <input id="pwd" type="password" name="password"/> <br/><br/>
            
        </fieldset>
        <fieldset>
            <legend>用户爱好</legend>
            <!--单选按钮-->
            性别 <input type="radio" name="gender" value="male" id="male" checked="checked"><label for="male">男</label>
            <input type="radio" name="gender" value="female" id="female"><label for="female">女</label><br/><br/>
            <!--多选框-->
            爱好 <input type="checkbox" name="hobby" value="zq"/>足球
            <input type="checkbox" name="hobby" value="lq" />篮球
            <input type="checkbox" name="hobby" value="ymq" checked="checked" />羽毛球
            <input type="checkbox" name="hobby" value="ppq" checked="checked" />乒乓球
            <br/><br/>
            <!--下拉列表-->
            你喜欢的明星
            <select name=“star”>
                <optgroup lable="男明星">
                	<option value="lxl">李小龙</option>
                	<option value="cgk">陈国坤</option>
                	<optionv value="zxc">周星驰</option>
                </optgroup>
                <optgroup label="女明星">
                	<option value="lyf">刘亦菲</option>
                    <option value="xyjy">新垣结衣</option>
                    <option value="lyq">梁咏琪</option>
                </optgroup>
            </select>
            <br/><br/>
            自我介绍
            <textarea name="info"></textarea>
            
            <input type="submit" value="提交"/>
            <input type="reset" value="重置">
            <input type="button" value="按钮"><br/>
            
            <button type="submit">提交</button>
            <button type="reset">重置</button>
            <button type="button">按钮</button>
        </fieldset>
    </form>
</body>
```

## 8、框架集

框架集和内联框架类似，都是用于在一个页面中引入其他的外部页面，

框架集可以同时引入多个页面，而内联框架只能引入一个页面。

在h5标准中，推荐使用框架集，而不使用内联框架。

frameset和iframe一样，它里边的内容都不会被搜索引擎所检索；
所以如果搜索引擎检索到的页面是一个框架页的话，它是不能去判断里边的内容的；
使用框架集则意味着页面中不能有自己的内容，只能引入其他的页面，而我们每单独加载一个页面；
浏览器都需要重新发送一次请求，引入几个页面就需要发送几次请求，用户的体验比较差；
如果非得用建议使用frameset而不使用iframe	；

frameset：使用frameset穿件一个框架集，**frameset不能喝body同时出现在页面中**。

属性：

- rows：指定框架集中的所有的页面，一行一行的排列；
- cols：指定框架集中所有的页面，一列一列的排列；
- 这两个属性frameset必须选择一个，并且需要在属性中指定每一个部分所占大小

frameset中也可以在嵌套frameset。

```html
<frameset cols="30%, * , 30%">
    <frame src=“01.表格.html” />
    <frame src="02.表格.html"/>
    <frameset rows="30%, 50%, *">
    	<frame src="04..."></frame>
    	...
    </frameset>
</frameset>
```

## 9、hack语句

IE中支持

## 10、IE6对png24图片支持问题

IE6中对png24图片的支持度不高，如果使用的图片是png24格式，则会导致透明效果无法显示，解决方案：

1. 可以使用png8代替png24，在ps中改变图片格式，但是图片png8的清晰度会受影响；
2. 使用js解决问题，想页面中引入jquery，写js语句解决。

```html
	<head>
        <style type="text/css">
			.box1{
				width: 200px;
				height: 200px;
				background-image: url(img/3.png);
				background-repeat: no-repeat;
			}
			.box2{
				width: 200px;
				height: 200px;
				background-image: url(img/4.png);
				background-repeat: no-repeat;
			}
		</style>
	</head>
	<body style="background-color: #bfa;">
		<div class="box1"></div>
		<div class="box2"></div>
		<img src="img/3.png"/>
		
		<!-- 在body标签的最后引入外部的JS文件 -->
		<script type="text/javascript" src="js/DD_belatedPNG_0.0.8a-min.js"></script>
		<!--再创建一个新的script标签，并且编写一些js代码 -->
		<script type="text/javascript">
			DD_belatedPNG.fix("*");
		</script>
	</body>
```

