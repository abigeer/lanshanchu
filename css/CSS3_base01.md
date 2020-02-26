# CSS3最常用的新特性

## 第一章：新增选择器

> 原有选择器：id选择器（权重100）>  类选择器（权重10） > 标签选择器（权重1），在原有选择器基础上扩充CSS3选择器。 

第一组：

> :first-of-type()  选择该类型元素的第一个子元素
>
> :last-of-type() 选择该类型元素的最后一个子元素
>
> :nth-of-type() 从正序开始选择该类型的第几个子元素
>
> :nth-last-of-type()  从倒序开始选择该类型的第几个子元素

第二组：

> :first-child   选择第一个子元素
>
> :last-child    选择最后一个子元素
>
> :nth-child()    从正序开始选择第几个子元素
>
> :nth-last-child()	从倒序开始选择第几个子元素



```html
<body>
    <div class="paragraphs">
        <p>我是第一个p标签</p>
        <p>我是第二个p标签</p>
        <p>我是第三个p标签</p>
        <p>我是第四个p标签</p>
    </div>
   
    <input type="text">
    <input type="text" disabled="">
    
    <input type="radio" name="form1">
    <input type="radio" checked="" name="form1">
    
    <br>
    <a href="#news1">点击我让news1变绿色</a>
    <br>
    <a href="#news2">点击我让new2变橘红色</a>
    
    <div id="news1">
    	我的id是news1
    </div>
    <div id="news2">
    	我的id是news2
    </div>
</body>
```

