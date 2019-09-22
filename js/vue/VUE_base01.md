# VUE入门基础

## 1、简介

Vue.js是目前最火的前端框架，React是最流行的前端框架，两者均可用于网站和手机APP开发，Vue要借助Weex。

Vue.js是一套构建用户界面的框架，**只关注视图层**，不仅易上手，还便于与第三方库或既有项目整合。（Vue有配套的第三方库，可以整合起来做大型项目开发）。

Vue的一个核心该奶奶就是让用户不再操作DOM元素，让程序员可以更多的时间去关注业务逻辑。

## 2、MVC和MVVM区别与联系

MVC是后端分层开发的概念；

MVVM是前端视图层的概念，主要关注视图层分离，即：MVVM把前端的试图层，分为三个部分，M：Model、V：View、VM：ViewModel。

![MVC和MVVM关系图](./images/MVC_and_MVVM.png)

## 3、VUE基础

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <!-- 1.导入Vue的包 -->
        <script src="./../vue-2.4.0.js"></script>
    </head> 
    <body>
        <!--将来new的vue实例会控制这个元素的所有内容-->
        <!--Vue实例所控制的这个元素区域，就是 V:view层-->
        <div>
            <p>{{msg}}</p>
        </div>
        
        <script>
            //2.创建一个Vue实例
            //当我们导入包之后，在浏览器的内存中就多了一个Vue的构造函数；
            //注意：我们new出来的这个vm对象就是MVVM中VM的调度者；
            //对象中的data属性就是M:Model层
        	var vm = new Vue({
                el: '#app', //使用选择器语法选中元素，表示new的vue实例要控制页面上的区域。
                //data专门用来保存每个页面中的数据
                //data属性中存放的是el中要用到的数据
                data: {
                    //通过Vue提供的指令，可以很方便的把数据渲染到页面上，无需操作DOM。
                    msg: '欢迎学习VUE！'
                }
                methods: {}
            });
        </script>
    </body>
</html>    
```

1. 引入vue.js库；
2. 使用new实例化一个vue实例，这个实例表示vm层，实例中的data属性表示m：model层。
3. 通过vue实例的el属性和选择器选中页面元素，然后在元素中使用{{}}（插值表达式），将data中的数据渲染到元素。

## 4、Vue指令

> Vue指令在调用的时候都是以v-开头。
>
> 使用指令绑定后指令中使用的都是vue中定义的变量。

1. v-cloak指令

   v-cloak指令能够解决插值表达式闪烁的问题（页面渲染初始显示{{msg}}随后渲染为data内容）。

   ```html
   <head>
       <script src='...'></script>
       <style>
       	[v-cloak] {
       		display: none;
       	}
       </style>
   </head>
   <body>
       <div id="app">
           <p v-cloak>+++++{{msg}}-----</p>
       </div>
       
       <script>
       	var vm = new Vue({
               el: '#app',
               data: {
                   msg: '123'
               }
           });
       </script>
   </body>
   ```

   + 使用css样式设置插值元素的display为none；
   + 插值表达式只会替换自己的占位符，不会把真个元素内容清空替换，即显示：++++123----.

2. v-text和v-html指令

   ```html
   <body>
   	<div id="app">
           <p v-cloak>++++{{msg}}----</p>
           <!--显示结果：123-->
           <p v-text="msg">=========</p>
           <!--显示结果：<h1>你好！</h1>-->
           <div>{{msg2}}</div>
           <!--显示结果：<h1>你好！</h1>-->
           <div v-text="msg2"></div>
           <!--显示结果：h1标题的格式的内容-->
           <div v-html="msg2">121212</div>
       </div>
       
       <script>
       	var vm = new Vue({
               el: '#app',
               data: {
                   msg: '123',
                   msg2: '<h1>你好！</h1>'，
               }
           });
       </script>
   </body>
   ```

   + v-text可以将内容清空后替换为指定data中的内容；
   + v-html可以将data内容以html文档格式显示。

3. v-bind指令的三种用法

   v-bind是Vue中提供的用于绑定属性的指令。

   - v-bind指令用于绑定元素属性

   + 直接使用v-bind
   + 使用简化指令：
   + 在绑定的时候，拼接绑定内容：`:title="btnTitle + ', 这是追加的内容'"`
   + v-bind中可以写合法的js表达式。
   + 使用绑定指令后，可以不使用插值表达式就可以引用vm中的数据。

   ```html
   <body>
       <div id="app">
   		<input type="button" value="按钮" v-bind:title="mytitle + '123'">
       	<input type="button" value="按钮" :title="mytitle + '123'">
       </div>
       <script>
       	var vm = new Vue({
               el: '#app',
               data: {
                   mytitle: '这是一个自定义title'
               }
           });
       </script>
   </body>
   ```

4. v-on指令和跑马灯实例

   + v-on指令用于事件绑定机制。
   + 指令简写使用“@”，click是点击事件，有其他事件hover等。
   + 在vue实例内部访问数据使用this，比如在methods，如果方法内部再定义方法，这个内部方法建议使用箭头函数可以继续使用this。
   + 方法后跟括号可以向其中传递参数，也可以写js表达式。

   ```html
   <body>
       <div id="app">
           <input type="button" value="按钮" :title="mytitle + '123'" v-on:click="alert('hello')">
           <input type="button" value="按钮2" @click="show">
       </div>
       
       <script>
       	var vm = new Vue({
               el: '#app',
               data: {
                   mytitle: ’这时一个自定义的title‘
               },
               methods: {
                   show: function(){
                       alert('hello')
                   }
               }
           });
       </script>
   </body>
   ```

   跑马灯实例

   ```html
   <body>
   	<div id="app">
           <input type="button" value="浪起来" @click=“lang”>
           <input type="button" value="低调" @click="stop">
           <h4>{{ msg }}</h4>
       </div>
       
       <script>
           //注意：vm实例中，如果要获取data上的数据，或者想要调用methods中的方法，必须通过“this.数据属性名”,或者”this.方法名“来访问，这里的this就表示我们new出来的vm实例对象。
       	var vm = new Vue({
               el: '#app',
               data: {
                   msg: '猥琐发育，别浪~~',
                   intervalId: null
               },
               methods: {
                   lang(){
                       if(this.intervalId != null) return;
                       this.intervalId = setInterval(() => {
                           var start = this.msg.substring(0,1);
                           var end = this.msg.substring(1);
                           this.msg = start + end;
                       }, 400);
                       //注意：vm实例，会监听自己身上data中所有数据的改变，只要数据易发生改变，就会自动把最新的数据，从data中同步到页面中去。
                   }
                   stop(){
               		clearInterval(this.intervalId);
           			this.intervalId = null;
           		}
               }
           });
       </script>
   </body>
   ```

   **v-on事件修饰符**

   + .stop	阻止冒泡

     比如父元素和子元素中都有点击事件，当点击子元素时先执行子元素事件后冒泡到父元素事件。

     ```html
     <body>
     	<div id="app" @click="fatherclick">
             <input type="button" value="按钮" @click.stop="childclick">
         </div>
     </body>
     ```

     添加".stop"这样就会阻止事件向上冒泡。

   + .prevent    阻止默认事件

     ```html
     <div id="app">
     	<a href="http://wwww.baidu.com" @click.prevent="linkClick">有问题去百度</a>
     </div>
     ```

     会阻止a标签的默认行为，不跳转到百度

   + .capture    添加默认事件

     实现捕获出发事件的机制

     ```html
     <div class="inner" @click.capture="divHandler">
         <input type="button" value="戳他" @click="btnHandler"
     </div>
     ```

     

   + .self            只当事件在该元素本身（比如不是子元素）触发时触发回调

     ```html
     <div class="inner" @click.self="divHandler">
         <input type="button" value="戳他" @click="btnHandler">
     </div>
     ```

     

   + .once          事件只触发一次

     `<a href="http://www.baidu.com" @click.prevent.once="linkClick">有问题，先去百度</a>`

   **.self和.stop的区别**

   ```html
   <!--.self只会阻止自身冒泡行为的出发，不会阻止其他-->
   <div class="outer" @click="div2Handler">
   	<div class="inner" @click.self="divHandler">
           <input type="button" value="戳他" @click="btnHandler">
       </div>
   </div>
   ```

   > **注意：修饰符可以串联书写使用**

5. v-model指令和双向数据绑定

   v-bind只能实现数据的单向绑定，从M自动绑定到V，无法实现数据的双向绑定。

   v-model指令可以实现数据的双向绑定，**v-model指令只能用在表单元素中，实现表单元素和Model中数据的双向绑定**。

   ```html
   <body>
       <div id="app">
           <input type="text" style="width:100%;" v_model="msg">
       </div>
       
       <script>
       	var vm = new Vue({
               el: '#app',
               data: {
                   msg: '大家都是好学生，爱敲代码，哎学习，爱思考，简直是完美，没瑕疵！'
               }，
               methods: {}
           });
       </script>
   </body>
   ```

6. v-for指令和key属性

   1. 迭代普通数组

      ```html
      <body>
          <div id="app">
          	<p v-for="(item, i) in list">索引值：{{i}} --- 每一项： {{item}}</p>
          </div>
          <script>
          	var vm = new Vue({
                  el: '#',
                  data: {
                      list: [1,2,3,4,5,6]
                  },
                  methods: {}
              });
          </script>
      </body>
      ```

   2. 迭代对象数组

      ```html
      <body>
          <div id="app">
          	<p v-for="(user, i) in list">Id：{{ user.id }} --- 名字：{{ user.name }} --- 索引：{{i}}</p>
          </div>
          <script>
          	var vm = new Vue({
                  el: '#',
                  data: {
                      list: [
                          { id: 1, name: 'zs1' },
                			{ id: 2, name: 'zs2' },
                			{ id: 3, name: 'zs3' },
                			{ id: 4, name: 'zs4' }
                      ]
                  },
                  methods: {}
              });
          </script>
      </body>
      ```

   3. 迭代对象

      ```html
      <body>
        <div id="app">
          <!-- 注意：在遍历对象身上的键值对的时候， 除了 有  val  key  ,在第三个位置还有 一个 索引  -->
          <p v-for="(val, key, i) in user">值是： {{ val }} --- 键是： {{key}} -- 索引： {{i}}</p>
        </div>
      
        <script>
          // 创建 Vue 实例，得到 ViewModel
          var vm = new Vue({
            el: '#app',
            data: {
              user: {
                id: 1,
                name: '托尼·屎大颗',
                gender: '男'
              }
            },
            methods: {}
          });
        </script>
      </body>
      ```

   4. 迭代数字

      ```html
      <body>
        <div id="app">
          <!-- in 后面我们放过  普通数组，对象数组，对象， 还可以放数字 -->
          <!-- 注意：如果使用 v-for 迭代数字的话，前面的 count 值从 1 开始 -->
          <p v-for="count in 10">这是第 {{ count }} 次循环</p>
        </div>
      
        <script>
          // 创建 Vue 实例，得到 ViewModel
          var vm = new Vue({
            el: '#app',
            data: {},
            methods: {}
          });
        </script>
      </body>
      ```

   key属性的使用

   > 2.2.0+版本中，当使用组件中使用v-for时，key现在是必须的。

   当 Vue.js 用 v-for 正在更新已渲染过的元素列表时，它默认用 “**就地复用**” 策略。如果数据项的顺序被改变，Vue将**不是移动 DOM 元素来匹配数据项的顺序**， 而是**简单复用此处每个元素**，并且确保它在特定索引下显示已被渲染过的每个元素。

   

   为了给 Vue 一个提示，**以便它能跟踪每个节点的身份，从而重用和重新排序现有元素**，你需要为每项提供一个唯一 key 属性。

   ```html
   <body>
     <div id="app">
   
       <div>
         <label>Id:
           <input type="text" v-model="id">
         </label>
   
         <label>Name:
           <input type="text" v-model="name">
         </label>
   
         <input type="button" value="添加" @click="add">
       </div>
   
       <!-- 注意： v-for 循环的时候，key 属性只能使用 number获取string -->
       <!-- 注意： key 在使用的时候，必须使用 v-bind 属性绑定的形式，指定 key 的值 -->
       <!-- 在组件中，使用v-for循环的时候，或者在一些特殊情况中，如果 v-for 有问题，必须 在使用 v-for 的同时，指定 唯一的 字符串/数字 类型 :key 值 -->
       <p v-for="item in list" :key="item.id">
         <input type="checkbox">{{item.id}} --- {{item.name}}
       </p>
     </div>
   
     <script>
       // 创建 Vue 实例，得到 ViewModel
       var vm = new Vue({
         el: '#app',
         data: {
           id: '',
           name: '',
           list: [
             { id: 1, name: '李斯' },
             { id: 2, name: '嬴政' },
             { id: 3, name: '赵高' },
             { id: 4, name: '韩非' },
             { id: 5, name: '荀子' }
           ]
         },
         methods: {
           add() { // 添加方法
             this.list.unshift({ id: this.id, name: this.name })
           }
         }
       });
     </script>
   </body>
   ```

7. v-if和v-show指令

   > 一般来说，v-if 有更高的切换消耗而 v-show 有更高的初始渲染消耗。因此，如果需要频繁切换 v-show 较好，如果在运行时条件不大可能改变 v-if 较好。

   ```html
   <body>
     <div id="app">
       <!-- <input type="button" value="toggle" @click="toggle"> -->
       <input type="button" value="toggle" @click="flag=!flag">
       <!-- v-if 的特点：每次都会重新删除或创建元素 -->
       <!-- v-show 的特点： 每次不会重新进行DOM的删除和创建操作，只是切换了元素的 display:none 样式 -->
   
       <!-- v-if 有较高的切换性能消耗 -->
       <!-- v-show 有较高的初始渲染消耗 -->
   
       <!-- 如果元素涉及到频繁的切换，最好不要使用 v-if, 而是推荐使用 v-show -->
       <!-- 如果元素可能永远也不会被显示出来被用户看到，则推荐使用 v-if -->
       <h3 v-if="flag">这是用v-if控制的元素</h3>
       <h3 v-show="flag">这是用v-show控制的元素</h3>
   
     </div>
     <script>
       // 创建 Vue 实例，得到 ViewModel
       var vm = new Vue({
         el: '#app',
         data: {
           flag: false
         },
         methods: {
           /* toggle() {
             this.flag = !this.flag
           } */
         }
       });
     </script>
   </body>
   ```

   

## 5、简易计算器案例

```html
<body>
    <div id="app">
        <input type="text" v-model="n1">
        <select v-model="opt">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="text" v-model="n2">
        <input type="button" value="=" @click="calc">
        <input type="text" v-model="result">
    </div>
    
    <script>
    	var vm = new Vue({
            el: '#app',
            data: {
                n1: 0,
                n2: 0,
                result: 0,
                opt: '+'
            },
            methods: {
                calc() {
                    //逻辑
                    switch (this.opt) {
                        case '+':
                            this.result = parseInt(this.n1) + parseInt(this.n2);
                            break;
                        case '-':
                            this.result = parseInt(this.n1) - parseInt(this.n2);
                            break;
                        case '*':
                            this.result = parseInt(this.n1) * parseInt(this.n2);
                            break;
                        case '/':
                            this.result = parseInt(this.n1) / parseInt(this.n2);
                            break;
                    }
                    var codestr = 'parseInt(this.n1)' + this.opt + 'parseInt(this.n2)';
                    this.result = eval(codestr);
                }
            }
        });
    </script>
</body>
```



## 6、在Vue中使用样式

### 1、使用class样式

```html
<head>
    <style>
        .red {
            color: red;
        }
        .thin {
            font-weight: 200px;
        }
        .italic {
            font-style: italic;
        }
        .active {
            letter-spacing: 0.5em;
        }
    </style>
</head>
<body>
    <!--<h1 class=“red thin”>这是一个很大很大的H1，大到你无法想象！！！</h1>-->
    
    <!--1.数组-->
    <!--<h1 :class="['thin', 'italic']">这是一个很大很大的H1，大到你无法想象！！！</h1>-->
    
    <!--2.数组中使用三元表达式-->
    <h1 :class="['thin','italic', flag?'active':'']">这是一个很大很大的H1，大到你无法想象！！！</h1>
        
    <!--3.嵌套对象：数组中使用对象来代替三元表达式，提高代码可读性-->
    <h1 :class"['thin', 'italic', {'active':flag}]">这是一个很大很大的H1，大到你无法想象！！！</h1>
    
    <!--直接使用对象：在为 class 使用 v-bind 绑定 对象的时候，对象的属性是类名，由于 对象的属性可带引号，也可不带引号，所以 这里我没写引号；  属性的值 是一个标识符-->
    <h1 :class="classObj">这是一个很大很大的H1，大到你无法想象！！！</h1>
    
    <script>
    	var vm = new Vue({
            el: '#app',
            data: {
                flag: true,
                classObj: {
                    red: true,
                    thin: true,
                    italic: false,
                    active: false
                }
            }
            methods: {}
        });
    </script>    	
</body>
```



### 2、使用内联样式-style

1. 直接在元素上通过`:style`的形式，书写样式对象

`<h1 :style="{color: 'red', 'font-size': '40px'}">这是一个善良的H1</h1>`

2. 将样式对象定义到data中，并直接应用到`:style`中；

3. 在`:style`中通过数组，应用多个data上的样式；

```html
<body>
	<div id="app">
        <h1 :style=“styleObj1”>这是一个h1</h1>
        <h1 :style="[styleObj1, styleObj2]">
            这是一个h1
        </h1>
    </div>
    
    <script>
    	var vm = new Vue({
            el: '#app',
            data: {
                styleObj1: {color: 'red', 'font-weight':200px},
                styleObj2: {'font-style': 'italic'}
            }
        });
    </script>
</body>
```



## 7、过滤器

> 概念：Vue.js允许你自定义过滤器，**可被用作一些常见的文本格式化**。过滤器可以用在两个地方：**mustache插值和v-bind表达式**。过滤器应该被添加在js表达式的尾部，由”管道“符“|”指示。



> 过滤器语法：`Vue.filter('过滤器的名称'，function(data){})`
>
> 过滤器中的function，第一个参数，已经被规定死了，永远都是过滤器管道符前面传递过来的数据。

### 全局过滤器

定义在vm对象外部。

过滤器在插值表达式中的格式：

```html
<div class="app">
	<p>{{msg | msgFormat("疯狂+1", '123') | test}}</p>
</div>
```

过滤器可以多个，多个过滤器串联，msg表示要过滤的字符串，过滤器是一个函数，可以传入参数列表。

过滤器定义：

```html
<script>
    //定义一个Vue全局过滤器，名字叫做msgFormat
	Vue.filter('msgFormat', function(msg, arg, arg2) {
        //函数的第一个参数是固定的，是要过滤的字符串，后面是过滤器调用时候传递的参数列表
        //字符串的replace方法第一个参数除了可以是一个子串还可以是一个正则式
        return msg.replace(/单纯/g, arg + arg2)
    });
    Vue.filter('test', function(msg){
        return msg+'=======';
    });
    
    //创建Vue实例，得到ViewModel
    var vm = new Vue({
        el: '#app',
        data: {
            msg: '曾经，我也是一个单纯的少年，单纯的我，傻傻的问，谁是世界上最单纯的男人'
        }
        methods:{}
    });
</script>
```

> 当全局过滤器和私有过滤器同名时，采用就近原则，即使用元素的私有过滤器。

### 私有过滤器

```html
<div class="app">
    <p>{{msg | msgFormat(msg, arg, arg2) | test}}</p>
</div>
<script>
	var vm = new Vue({
        el: '#app',
        data: {
            msg:'曾经，我也是一个单纯的少年，单纯的我，傻傻的问，谁是世界上最单纯的男人'
        },
        methods: {},
        filters: {
            //私有过滤器只能在当前vm对象控制的view区域进行使用
            msgFormat(msg, arg, arg2){
                return msg.replace(/单纯/g,arg+arg2);
            },
            test(msg){
                return msg+'==========';
            }
        }
    });
</script>
```

## 8、按键修饰符

> 在监听键盘事件时，我们经常需要检查详细的按键。vue允许为v-on在监听键盘事件时添加按键修饰符。

```html
<!--只有‘key'在'Enter'时调用‘vm.submit()’-->
<input v-on:keyup.enter="submit">
```

vue提供了绝大多数的按键别名：

- .enter
- .tab
- .delete
- .esc
- .space
- .up
- .down
- .left
- .right

### 自定义按键修饰符

1.通过`Vue.config.keyCodes.名称 = 按键值`来自定义按键修饰符的别名。

`Vue.config.keyCodes.f2 = 113;`

2.使用自定义按键修饰符：

`<input type="text" v-model="name" @keyup.f2="add">`

## 9、自定义指令

除了Vue内置的指令（v-model和v-show）外Vue也允许自定义指令。

### 局部自定义指令

vm中接收一个directives对象。

>  指令在定义时候没有v-，在调用时候要添加v-。

**输入框聚焦和改变样式案例**

```html
<div id="app">
    <input type="text" v-model="searchName" v-focus v-color="'red'" v-font-weight="900
                                                                                   ">
</div>

<script>
	var vm = new Vue({
        el: '#app',
        data: {},
        methods: {},
        //自定义局部指令v-color和v-focus
        //directvies对象中定义局部指令，局部指令对象内部
        //使用钩子函数，钩子函数可以在特定的阶段，执行相关的操作
        directvies:{
            focus: {
                //在元素刚绑定了指令的时候，还没有插入到DOM中去，这时候，调用focus方法没有作用。
                //一个元素只有插入到DOM中之后，才能获取焦点。
                //所以不能使用bind钩子函数，使用inserted钩子函数。
                inserted(el) {
                    //inserted表示元素插入到DOM中的时候，会执行inserted函数（出发一次）。
                    el.focus();
                    //和JS行为有关的操作，最好在inserted中去执行，防止js行为不生效。
                }
            },
            color: {
                //样式只要通过指令绑定给了元素，不管这个元素有没有被插入到页面中去，这个元素肯定有了一个内联样式。
                //将来元素肯定会显示到页面中，这时候，浏览器的渲染引擎必然会解析样式，应用给这个元素。
                bind(el, color) {
                    el.style.color = color.value;
                }
            },
            'font-weight': function(el, binding2) {
                //自定义指令的简写形式，等同于定义了bind和update两个钩子函数
                el.style.fontweight = binding2.value;
                
            }
        }
    });
</script>
```

> 注意：**在每个函数中，第一个参数，永远是el，表示被绑定了指令的那个元素，这个el参数，是一个原生的JS对象。**
>
> 和JS行为有关的操作放到inserted钩子函数中；
>
> 和样式有关的操作放到bind钩子函数中。

### 全局自定义指令

```html
<div id="app">
	<input type="text" v-model="searchName" v-focus v-color="'red'" v-font-weight="900">
</div>
<script>
	Vue.directive('focus',{
        bind: function(el){
            
        },
        inserted: function(el){
            el.focus()
        }
    });
    Vue.directive('color',{
        bind:function(el, color){
            el.style.color=color.value;
        }
    });
    Vue.directive('font-weight',{
        bind:function(el,binding){
            el.style.font-weight=binding.value;
        }
    })
</script>
```

### 钩子函数

一个指令定义对象可以提供如下几个钩子函数（均可选）；

- bind：只调用一次，指令第一次绑定到元素时调用。在这里可以进行一次性初始化设置，这里用来绑定style。
- inserted：表示元素插入到DOM中的时候，会执行inserted函数（触发一次）；
- update：当VNode更新的时候会执行update，可能会触发多次。

### 钩子函数的参数

- el表示被绑定的dom元素，可以用来直接操作DOM；

- binding：一个对象，包含以下属性：

  - name：指令名，不包括‘v-’前缀；
  - value：指令的绑定值，例如v-my-directive="1+1",绑定值为2；
  - `name`：指令名，不包括 `v-` 前缀。
  - `value`：指令的绑定值，例如：`v-my-directive="1 + 1"` 中，绑定值为 `2`。
  - `oldValue`：指令绑定的前一个值，仅在 `update` 和 `componentUpdated` 钩子中可用。无论值是否改变都可用。
  - `expression`：字符串形式的指令表达式。例如 `v-my-directive="1 + 1"` 中，表达式为 `"1 + 1"`。
  - `arg`：传给指令的参数，可选。例如 `v-my-directive:foo` 中，参数为 `"foo"`。
  - `modifiers`：一个包含修饰符的对象。例如：`v-my-directive.foo.bar` 中，修饰符对象为 `{ foo: true, bar: true }`。

  ### 对象字面量

  ```html
  <div v-demo="{ color: 'white', text: 'hello!' }"></div>
  Vue.directive('demo', function (el, binding) {
    console.log(binding.value.color) // => "white"
    console.log(binding.value.text)  // => "hello!"
  })
  ```

  

## 10、生命周期函数

- Vue的生命周期就是从Vue实例创建、运行、到销毁期间，伴随的各种各样的事件，这些事件，统称为生命周期；

- 生命周期钩子就是生命周期事件的别名而已：生命周期钩子 = 生命周期函数 = 生命周期事件；

- 主要的生命周期函数：

  ![](./images/lifecycle.png)

- - **创建期间的声明周期函数：**
  - beforeCreate：Vue实例刚刚被创建出来，此时，还没有初始化data和methods属性；
  - created：实例已经在内存中创建OK，此时data和methods已经创建OK，此时还没有开始编译模板；
  - 模板编译期：把Vue中的指令进行执行，最终在内存中生成一个编译好的最终模板字符串，然后把这个模板字符串渲染为内存中的DOM，此时，只是在内存中渲染好了模板，并没有挂载到页面上；
  - beforeMount：此时已经完成了模板的编译，但是还没有挂载到页面中；
  - mounted：此时，已经将编译好的模板，挂载到了页面指定的容器中显示；
  - **运行期间的声明周期函数：**
  - beforeUpdate:状态更新之前执行此函数，此时data中的状态值是最新的，但是界面上显示的数据还是旧的，因为此时还没有开始重新渲染DOM节点；
  - updated：实例更新完毕之后调用此函数，此时data中的状态值和界面上显示的数据，已经完成了更新，界面已经被重新渲染好了；
  - **销毁期间的生命周期函数：**
  - beforeDestory：实例销毁之前调用，这一步，实例仍然完全可以用；
  - destroyed：Vue实例销毁后调用，调用后，Vue实例指示的所有东西都会解除绑定，所有的事件监听器会被移除，所有的子实例也会被销毁。

## 11、使用vue-resource实现get、post、jsonp请求

jquery提供了ajax请求的简写方式，vue-resource是vue生态的异步请求包，除了vue-resource之外，还可以使用axios的第三方包实现                            数据的请求。

1. 常见的数据请求类型？get  post  jsonp

2. 测试的URL请求资源地址：

   - get请求地址：http://vue.studyit.io/api/getlunbo
   - post请求地址：http://vue.studyit.io/api/post
   - jsonp请求地址：http://vue.studyit.io/api/jsonp

   先引入vue.js再引入vue-sorce.js，后者依赖于前者。

   ```html
   <head>
       <script src="./lib/vue-2.4.0.js"></script>
       <script src=".lib/vue-resource-1.3.4.js"></script>
   </head>
   <body>
       <div id="app">
           <input type="button" value="get请求" @click="getInfo">
           <input type="button" value="post请求" @click="postInfo">
           <input type="button" value="jsonp请求" @click="jsonpInfo">
       </div>
       
       <script>
       	//创建vue实例，得到ViewModel
           var vm = new Vue({
               el: "#app",
               data: {},
               methods: {
                   getInfo(){  //发起get请求
                       //使用promise设置回调函数
                       this.$http.get('http://vue.studyit.io/api/getlunbo').then(function(result){
                           //通过result.body拿到服务器返回的成功的数据
                           console.log(result.body)
                       })
                   },
                   postInfo() {
                       this.$http.post('http://vue.studyit.io/api/post',{},{emulateJson: true}).then(result => { //发起post请求
                           //手动发起的 Post 请求，默认没有表单格式，所以，有的服务器处理不了
                           //通过 post 方法的第三个参数， { emulateJSON: true } 设置 提交的内容类型 为 普通表单数据格式
                           console.log(result.body)
                       })
                   },
                   jsonpInfo(){
                       this.$http.json('http://vue.studyit.io/api/jsonp').then(result => { //发起jsonp请求 application/x-wwww-form-urlencoded
                           console.log(result.body)
                       })
                   }
               }
           });
       </script>
   </body>
   
   ```

3. JSONP的实现原理

   - 由于浏览器的安全性限制，不允许AJAX访问协议不同、域名不同、端口号不同的数据接口，浏览器认为这种访问不安全；

   - 可以通过动态创建script标签的形式，吧script标签的src属性，指向数据接口的地址，因为script标签不存在跨域限制，这种数据获取方式，乘坐为JSONP（注意：根据JSONP的实现原理，知晓，JSONP只支持GET请求）

   - 具体实现过程：

     - 先在客户端定义一个回调方法，于定义对数据的操作；

     - 再把这个回调方法的名称，通过url传参的形式，提交到服务器的数据接口；

     - 服务器的数据接口组织好要发送给客户端的数据，再拿着客户端传递过来的回调方法名称，拼接出一个调用这个方法的字符串，发送给客户端去解析执行；

     - 客户端拿到服务器返回的字符串之后，当作script脚本去解析执行，这样就能够拿到JSONP的数据了；

     - Node.js，来手动实现一个JSONP的请求例子：

       ```html
       	const http = require('http');
           // 导入解析 URL 地址的核心模块
           const urlModule = require('url');
       
           const server = http.createServer();
           // 监听 服务器的 request 请求事件，处理每个请求
           server.on('request', (req, res) => {
             const url = req.url;
       
             // 解析客户端请求的URL地址
             var info = urlModule.parse(url, true);
       
             // 如果请求的 URL 地址是 /getjsonp ，则表示要获取JSONP类型的数据
             if (info.pathname === '/getjsonp') {
               // 获取客户端指定的回调函数的名称
               var cbName = info.query.callback;
               // 手动拼接要返回给客户端的数据对象
               var data = {
                 name: 'zs',
                 age: 22,
                 gender: '男',
                 hobby: ['吃饭', '睡觉', '运动']
               }
               // 拼接出一个方法的调用，在调用这个方法的时候，把要发送给客户端的数据，序列化为字符串，作为参数传递给这个调用的方法：
               var result = `${cbName}(${JSON.stringify(data)})`;
               // 将拼接好的方法的调用，返回给客户端去解析执行
               res.end(result);
             } else {
               res.end('404');
             }
           });
       
           server.listen(3000, () => {
             console.log('server running at http://127.0.0.1:3000');
           });
       ```

       