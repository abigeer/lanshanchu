# VUE入门基础2

## 1、vue中动画

为什么使用动画：动画能够提高用户体验，帮助用户更好的理解页面中的功能：

Vue再插入、更新或者移除DOM时，提供多种不同方式的应用过度效果。包括一下工具：

- 再CSS过度和动画中自动应用class；
- 可以配合使用第三方CSS动画库，如Animate.css;
- 在过渡钩子函数中使用js直接操作DOM；
- 可以配合使用第三方js动画库，如Velocity.js。

### 单元素/组件的过度

Vue提供了transition的封装组件，在下列情形中，可以给任何元素和组件添加进入/离开过度：

- 条件渲染（使用`v-if/v-else`）
- 条件展示（使用`v-show`）
- 动态组件
- 组件根节点

### 过渡类名

![](./images/capital-process.png)

在进入和离开的过度中，会有6个class切换：

1. `v-enter`：定义进入过渡的开始状态。在元素被插入之前生效，在元素被插入之后的下一帧移除。
2. `v-enter-active`：定义进入过渡生效时的状态。在整个进入过渡的阶段中应用，在元素被插入之前生效，在过渡/动画完成之后移除。这个类可以被用来定义进入过渡的过程时间，延迟和曲线函数。
3. `v-enter-to`：**2.1.8版及以上** 定义进入过渡的结束状态。在元素被插入之后下一帧生效 (与此同时 `v-enter` 被移除)，在过渡/动画完成之后移除。
4. `v-leave`：  定义离开过渡的开始状态。在离开过渡被触发时立刻生效，下一帧被移除。
5. `v-leave-active`：定义离开过渡生效时的状态。在整个离开过渡的阶段中应用，在离开过渡被触发时立刻生效，在过渡/动画完成之后移除。这个类可以被用来定义离开过渡的过程时间，延迟和曲线函数。
6. `v-leave-to`：**2.1.8版及以上** 定义离开过渡的结束状态。在离开过渡被触发之后下一帧生效 (与此同时 `v-leave` 被删除)，在过渡/动画完成之后移除。

对于这些在过渡中切换的类名来说，如果你使用一个没有名字的 `<transition>`，则 `v-` 是这些类名的默认前缀。如果你使用了 `<transition name="my-transition">`，那么 `v-enter` 会替换为 `my-transition-enter`。

`v-enter-active` 和 `v-leave-active` 可以控制进入/离开过渡的不同的缓和曲线，在下面章节会有个示例说明。

```html
<head>
    <script src="./lib/vue-.js"></script>
    <style>
        /*v-enter【这是一个时间点】是进入之前，元素的起始状态，此时还没有开始进入*/
        /*v-leave-to【这是一个时间点】是动画离开之后，离开的终止状态，此时，元素动画已经结束了*/
    	.v-enter,
        .v-leave-to {
            opacity: 0;
            transform: translateX(150px);
        }
        /* v-enter-active 【入场动画的时间段】 */
    	/* v-leave-active 【离场动画的时间段】 */
        .v-enter-active,
        .v-leave-active {
            transition: all 0.8s ease;
        }
        
        .my-enter,
        .my-leave-to {
            opacity: 0;
            transform: translateY(70px);
        }
        
        .my-enter-active,
        .my-leave-active{
            transition: all 0.8s ease;
        }
        
    </style>
</head>
<body>
    <div id="app">
        <input type="button" value="toggle" @click="flag=!flag">
        <!-- 需求： 点击按钮，让 h3 显示，再点击，让 h3 隐藏 -->
    	<!-- 1. 使用 transition 元素，把 需要被动画控制的元素，包裹起来 -->
    	<!-- transition 元素，是 Vue 官方提供的 -->
        <transition>
        	<h3 v-if="flag">这是一个H3</h3>
        </transition>
        
        <hr>
        
        <!--改变前缀-->
        <input type=button value="toggle2" @click="flag2=!flag2">
        <transition name="my">
        	<h6 v-if="flag2">这是一个H6</h6>
        </transition>
    </div>
    <script>
    	var vm = new Vue({
            el: '#app',
            data: {
                flag: false,
                flag2: false
            },
            methods: {}
        });
    </script>
</body>
```

### 使用第三方CSS动画库

1. 导入动画类库

   `<link rel="stylesheet" type="text/css" href="./lib/animate.css">`

2. 定义transition及属性：

   ```html
   <transition
               enter-active-class="bounceIn"
               leave-active-class="bounceOut"
               :duration="{enter: 200, leave: 400}" >
       <h3 v-if="flag" class="animated">
          这是要给H3
       </h3>
   </transition>
   ```

3. 案例：

   ```html
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title>Document</title>
     <script src="./lib/vue-2.4.0.js"></script>
     <link rel="stylesheet" href="./lib/animate.css">
     <!-- 入场 bounceIn    离场 bounceOut -->
   </head>
   
   <body>
     <div id="app">
       <input type="button" value="toggle" @click="flag=!flag">
       <!-- 需求： 点击按钮，让 h3 显示，再点击，让 h3 隐藏 -->
       <!-- <transition enter-active-class="animated bounceIn" leave-active-class="animated bounceOut">
         <h3 v-if="flag">这是一个H3</h3>
       </transition> -->
   
       <!-- 使用 :duration="毫秒值" 来统一设置 入场 和 离场 时候的动画时长 -->
       <!-- <transition enter-active-class="bounceIn" leave-active-class="bounceOut" :duration="200">
         <h3 v-if="flag" class="animated">这是一个H3</h3>
       </transition> -->
   
       <!-- 使用  :duration="{ enter: 200, leave: 400 }"  来分别设置 入场的时长 和 离场的时长  -->
       <transition 
       enter-active-class="bounceIn" 
       leave-active-class="bounceOut" 
       :duration="{ enter: 200, leave: 400 }">
         <h3 v-if="flag" class="animated">这是一个H3</h3>
       </transition> 
     </div>
   
     <script>
       // 创建 Vue 实例，得到 ViewModel
       var vm = new Vue({
         el: '#app',
         data: {
           flag: false
         },
         methods: {}
       });
     </script>
   </body>
   ```

   使用钩子函数模拟小球半场动画

   动画中的钩子函数

   ```html
   <transition
     v-on:before-enter="beforeEnter"
     v-on:enter="enter"
     v-on:after-enter="afterEnter"
     v-on:enter-cancelled="enterCancelled"
   
     v-on:before-leave="beforeLeave"
     v-on:leave="leave"
     v-on:after-leave="afterLeave"
     v-on:leave-cancelled="leaveCancelled"
   >
     <!-- ... -->
   </transition>
   // ...
   methods: {
     // --------
     // 进入中
     // --------
   
     beforeEnter: function (el) {
       // ...
     },
     // 当与 CSS 结合使用时
     // 回调函数 done 是可选的
     enter: function (el, done) {
       // ...
       done()
     },
     afterEnter: function (el) {
       // ...
     },
     enterCancelled: function (el) {
       // ...
     },
   
     // --------
     // 离开时
     // --------
   
     beforeLeave: function (el) {
       // ...
     },
     // 当与 CSS 结合使用时
     // 回调函数 done 是可选的
     leave: function (el, done) {
       // ...
       done()
     },
     afterLeave: function (el) {
       // ...
     },
     // leaveCancelled 只用于 v-show 中
     leaveCancelled: function (el) {
       // ...
     }
   }
   ```

   小球半场动画案例：

   ```html
   <head>
       <script src="./lib/vue-.js"></script>
       <style>
           .ball{
               width: 15px;
               height:15px;
               border-radius: 50%;
               background-color: red;
           }
       </style>
   </head>
   <body>
       <div id="app">
           <input type="button" value="快到碗里来" @click="flag=!flag">
           <!--1.使用transition元素把小球包裹进来-->
           <transition
             @before-enter="beforeEnter"
             @enter="enter"
             @after-enter="afterEnter">
           	<div class="ball" v-show="flag"></div>
           </transition>
       </div>
       <script>
       	var vm = new Vue({
               el:'#app',
               data: {
                   flag: false
               },
               methods: {
                   //注意:动画钩子函数的第一个参数：el，表示要执行动画的那个DOM元素，是一个远摄关JS DOM对象
                   //可以认为，el是通过document.getElementById('')方式获取到的原生JS DOM对象
                   beforeEnter(el) {
                       //beforeEnter表示动画入场之前，此时，动画尚未开始，可以在beforeEnter中，设置元素开始动画之前的其实样式
                       //设置小球开始动画之前的起始位置
                       el.style.transform = "translate(0,0)"
                   },
                   enter(el, done){
                       // 这句话，没有实际的作用，但是，如果不写，出不来动画效果；
             			// 可以认为 el.offsetWidth 会强制动画刷新
                       el.offsetWidth
                       // enter 表示动画 开始之后的样式，这里，可以设置小球完成动画之后的，结束状态
                       el.style.transform = "translate(150px, 450px)"
                       el.style.transform = 'all 1s ease'
                       // 这里的 done， 起始就是 afterEnter 这个函数，也就是说：done 是 afterEnter 函数的引用
                       done()
                   },
                   afterEnter(el){
                       // 动画完成之后，会调用 afterEnter
             			// console.log('ok')
                       this.flag = !this.flag
                   }
               }
           });
       </script>
       
   </body>
   ```

   ### 列表动画

   ```html
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
     <title>Document</title>
     <script src="./lib/vue-2.4.0.js"></script>
     <style>
       li {
         border: 1px dashed #999;
         margin: 5px;
         line-height: 35px;
         padding-left: 5px;
         font-size: 12px;
         width: 100%;
       }
   
       li:hover {
         background-color: hotpink;
         transition: all 0.8s ease;
       }
   
   
   
       .v-enter,
       .v-leave-to {
         opacity: 0;
         transform: translateY(80px);
       }
   
       .v-enter-active,
       .v-leave-active {
         transition: all 0.6s ease;
       }
   
       /* 下面的 .v-move 和 .v-leave-active 配合使用，能够实现列表后续的元素，渐渐地漂上来的效果 */
       .v-move {
         transition: all 0.6s ease;
       }
       .v-leave-active{
         position: absolute;
       }
     </style>
   </head>
   
   <body>
     <div id="app">
   
       <div>
         <label>
           Id:
           <input type="text" v-model="id">
         </label>
   
         <label>
           Name:
           <input type="text" v-model="name">
         </label>
   
         <input type="button" value="添加" @click="add">
       </div>
   
       <!-- <ul> -->
         <!-- 在实现列表过渡的时候，如果需要过渡的元素，是通过 v-for 循环渲染出来的，不能使用 transition 包裹，需要使用 transitionGroup -->
         <!-- 如果要为 v-for 循环创建的元素设置动画，必须为每一个 元素 设置 :key 属性 -->
         <!-- 给 ransition-group 添加 appear 属性，实现页面刚展示出来时候，入场时候的效果 -->
         <!-- 通过 为 transition-group 元素，设置 tag 属性，指定 transition-group 渲染为指定的元素，如果不指定 tag 属性，默认，渲染为 span 标签 -->
         <transition-group appear tag="ul">
           <li v-for="(item, i) in list" :key="item.id" @click="del(i)">
             {{item.id}} --- {{item.name}}
           </li>
         </transition-group>
       <!-- </ul> -->
   
     </div>
   
     <script>
       // 创建 Vue 实例，得到 ViewModel
       var vm = new Vue({
         el: '#app',
         data: {
           id: '',
           name: '',
           list: [
             { id: 1, name: '赵高' },
             { id: 2, name: '秦桧' },
             { id: 3, name: '严嵩' },
             { id: 4, name: '魏忠贤' }
           ]
         },
         methods: {
           add() {
             this.list.push({ id: this.id, name: this.name })
             this.id = this.name = ''
           },
           del(i) {
             this.list.splice(i, 1)
           }
         }
       });
     </script>
   </body>
   ```

   

## 2、组件

### 1.组件的创建方式

```html
<body>
    <div id="app">
        <!-- 如果要使用组件，直接，把组件的名称，以 HTML 标签的形式，引入到页面中，即可 -->
        <mycoml></mycoml>
    </div>
    
    <script>
    	// 1.1 使用 Vue.extend 来创建全局的Vue组件
    	// var com1 = Vue.extend({
    	//   template: '<h3>这是使用 Vue.extend 创建的组件</h3>' // 通过 template 属性，指定了组件要展示的HTML结构
    	// })
    	// 1.2 使用 Vue.component('组件的名称', 创建出来的组件模板对象)
    	// Vue.component('myCom1', com1)
    	// 如果使用 Vue.component 定义全局组件的时候，组件名称使用了 驼峰命名，则在引用组件的时候，需要把 大写的驼峰改为小写的字母，同时，两个单词之前，使用 - 链接；
    	// 如果不使用驼峰,则直接拿名称来使用即可;
    	// Vue.component('mycom1', com1)

    	// Vue.component 第一个参数:组件的名称,将来在引用组件的时候,就是一个 标签形式 来引入 它的
    	// 第二个参数: Vue.extend 创建的组件  ,其中 template 就是组件将来要展示的HTML内容
    	Vue.component('mycom1', Vue.extend({
      	template: '<h3>这是使用 Vue.extend 创建的组件</h3>'
    	}))


    	// 创建 Vue 实例，得到 ViewModel
    	var vm = new Vue({
      		el: '#app',
      		data: {},
      		methods: {}
    	});
    </script>
</body>
```

### 2.组件的创建方式2

```html
<body>
  <div id="app">
    <!-- 还是使用 标签形式,引入自己的组件 -->
    <mycom2></mycom2>
  </div>

  <script>
    // 注意:不论是哪种方式创建出来的组件,组件的 template 属性指向的模板内容,必须有且只能有唯一的一个根元素
    Vue.component('mycom2', {
      template: '<div><h3>这是直接使用 Vue.component 创建出来的组件</h3><span>123</span></div>'
    })

    // 创建 Vue 实例，得到 ViewModel
    var vm = new Vue({
      el: '#app',
      data: {},
      methods: {}
    });
  </script>
</body>
```

### 3.组件创建的方式3

```html
<body>
  <div id="app">
    <mycom3></mycom3>
    <!-- <login></login> -->
  </div>


  <div id="app2">
    <mycom3></mycom3>
    <login></login>
  </div>

  <!-- 在 被控制的 #app 外面,使用 template 元素,定义组件的HTML模板结构  -->
  <template id="tmpl">
    <div>
      <h1>这是通过 template 元素,在外部定义的组件结构,这个方式,有代码的只能提示和高亮</h1>
      <h4>好用,不错!</h4>
    </div>
  </template>

  <template id="tmpl2">
    <h1>这是私有的 login 组件</h1>
  </template>

  <script>
    Vue.component('mycom3', {
      template: '#tmpl'
    })

    // 创建 Vue 实例，得到 ViewModel
    var vm = new Vue({
      el: '#app',
      data: {},
      methods: {}
    });


    var vm2 = new Vue({
      el: '#app2',
      data: {},
      methods: {},
      filters: {},
      directives: {},
      components: { // 定义实例内部私有组件的
        login: {
          template: '#tmpl2'
        }
      },

      beforeCreate() { },
      created() { },
      beforeMount() { },
      mounted() { },
      beforeUpdate() { },
      updated() { },
      beforeDestroy() { },
      destroyed() { }
    })
  </script>
</body>
```

### 4.组件中的data和methods

```html
<body>
  <div id="app">
    <mycom1></mycom1>
  </div>

  <script>
    // 1. 组件可以有自己的 data 数据
    // 2. 组件的 data 和 实例的 data 有点不一样,实例中的 data 可以为一个对象,但是 组件中的 data 必须是一个方法
    // 3. 组件中的 data 除了必须为一个方法之外,这个方法内部,还必须返回一个对象才行;
    // 4. 组件中 的data 数据,使用方式,和实例中的 data 使用方式完全一样!!!
    Vue.component('mycom1', {
      template: '<h1>这是全局组件 --- {{msg}}</h1>',
      data: function () {
        return {
          msg: '这是组件的中data定义的数据'
        }
      }
    })

    // 创建 Vue 实例，得到 ViewModel
    var vm = new Vue({
      el: '#app',
      data: {},
      methods: {}
    });
  </script>
</body>
```

### 5.组件的data必须是一个函数

组件的函数必须放回要给对象

```html
<body>
  <div id="app">
    <counter></counter>
    <hr>
    <counter></counter>
    <hr>
    <counter></counter>
  </div>


  <template id="tmpl">
    <div>
      <input type="button" value="+1" @click="increment">
      <h3>{{count}}</h3>
    </div>
  </template>

  <script>
    var dataObj = { count: 0 }

    // 这是一个计数器的组件, 身上有个按钮,每当点击按钮,让 data 中的 count 值 +1
    Vue.component('counter', {
      template: '#tmpl',
      data: function () {
        // return dataObj
        return { count: 0 }
      },
      methods: {
        increment() {
          this.count++
        }
      }
    })

    // 创建 Vue 实例，得到 ViewModel
    var vm = new Vue({
      el: '#app',
      data: {},
      methods: {}
    });
  </script>
</body>
```

### 6.组件的切换

场景需求：在登陆和注册首页，点击不同的按钮组件切换

#### 1.方式一（不推荐）

```html
<body>
  <div id="app">
    <a href="" @click.prevent="flag=true">登录</a>
    <a href="" @click.prevent="flag=false">注册</a>

    <login v-if="flag"></login>
    <register v-else="flag"></register>

  </div>

  <script>
    Vue.component('login', {
      template: '<h3>登录组件</h3>'
    })

    Vue.component('register', {
      template: '<h3>注册组件</h3>'
    })

    // 创建 Vue 实例，得到 ViewModel
    var vm = new Vue({
      el: '#app',
      data: {
        flag: false
      },
      methods: {}
    });
  </script>
</body>
```

#### 2.方式二

```html
<body>
  <div id="app">
    <a href="" @click.prevent="comName='login'">登录</a>
    <a href="" @click.prevent="comName='register'">注册</a>
    <!-- Vue提供了 component ,来展示对应名称的组件 -->
    <!-- component 是一个占位符, :is 属性,可以用来指定要展示的组件的名称 -->
    <component :is="comName"></component>
    <!-- 总结:当前学习了几个 Vue 提供的标签了??? -->
    <!-- component,  template,  transition,  transitionGroup  -->
  </div>
  <script>
    // 组件名称是 字符串
    Vue.component('login', {
      template: '<h3>登录组件</h3>'
    })

    Vue.component('register', {
      template: '<h3>注册组件</h3>'
    })

    // 创建 Vue 实例，得到 ViewModel
    var vm = new Vue({
      el: '#app',
      data: {
        comName: 'login' // 当前 component 中的 :is 绑定的组件的名称
      },
      methods: {}
    });
  </script>
</body>
```

#### 3.切换动画效果

```html
<head>
  <script src="./lib/vue-2.4.0.js"></script>
  <style>
    .v-enter,
    .v-leave-to {
      opacity: 0;
      transform: translateX(150px);
    }

    .v-enter-active,
    .v-leave-active {
      transition: all 0.5s ease;
    }
  </style>
</head>

<body>
  <div id="app">
    <a href="" @click.prevent="comName='login'">登录</a>
    <a href="" @click.prevent="comName='register'">注册</a>

    <!-- 通过 mode 属性,设置组件切换时候的 模式 -->
    <transition mode="out-in">
      <component :is="comName"></component>
    </transition>

  </div>

  <script>
    // 组件名称是 字符串
    Vue.component('login', {
      template: '<h3>登录组件</h3>'
    })

    Vue.component('register', {
      template: '<h3>注册组件</h3>'
    })

    // 创建 Vue 实例，得到 ViewModel
    var vm = new Vue({
      el: '#app',
      data: {
        comName: 'login' // 当前 component 中的 :is 绑定的组件的名称
      },
      methods: {}
    });
  </script>
</body>
```

