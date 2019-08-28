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
           <p v-cloal>+++++{{msg}}-----</p>
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

   + 直接使用v-bind
   + 使用简化指令：
   + 在绑定的时候，拼接绑定内容：`:title="btnTitle + ', 这是追加的内容'"`
   + v-bind中可以写合法的js表达式。

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

2. 将样式对象定义到data中，并直接应用到`.style`中；

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

## 