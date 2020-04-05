# 多线程编程

> - 进程：进程是系统进行资源分配的基本单位，有独立的内存空间。
>
> - 线程：线程是CPU调度和分派的基本单位，线程依附于进程存在，每个线程会共享父进程的资源。
>
> - 协程：协程是一种用户态的轻量级线程，协程的调度完全由用户控制，协程间切换只需要保存任务的上下文，没有内核的开销。
>
> 常用的Windows、Linux等操作系统都采用抢占式多任务，如何调度线程完全由操作系统决定，程序不能决定什么时候执行，以及执行多长时间。
>
> Java语言内置了多进程支持，一个Java程序实际上是以个JVM进程，JVM进程用一个主线程来执行main()方法，在main()方法内部，又可以启动多个线程。

## 线程上下文切换

由于中断处理，多任务处理，用户态切换等原因会导致CPU从一个线程切换到另一个线程，切换过程需要保存当前进程的状态并恢复另一个进程的状态。

上下文切换的代价是高昂的，以为在核心上交换线程会花费很多时间。上下文切换的延迟取决于不同的因素，大概在50到100纳秒之间。考虑到硬件平均在每个核心上每纳秒执行12条指令，那么一次上下文切换可能花费600到1200条指令的延迟时间。实际上，上下文切换占用了大量程序执行指令的时间。

如果存在跨核上下文切换（Cross-Core Context Switch），可能会导致CPU缓存失败（CPU从缓存访问数据的成本大约是3到40个时钟周期，从主存访问数据的成本大约是100到300个时钟周期），这种场景的切换成本会更加昂贵。

## Golang的并发对比

Golang从2019年正式发布，从语言级别支持并发，通过轻量级协程gGoroutine来实现程序并发运行。

Goroutine非常轻量，主要体现在以下两个方面：

- 上下文切换代价小：Goroutine上下文切换只涉及到三个寄存器（PC/SP/DK）的值修改；而对比线程的上下文切换则需要涉及模式切换（从用户态切换到内核态）、以及16个寄存器、PC、SP..等寄存器的刷新。
- 内存占用少：线程栈空间通常是2M，Goroutine栈空间最小2K；

Golang程序中可以轻松支持10w级别的Goroutinn运行，而线程数量达到1k时，内存占用就达到2G。

## 创建新线程

```java
//方法一：通过集成Thread类
public class Main{
    public static void main(String[]args){
        System.out.println("main start...");
        Thread t = new MyThread();
        t.start();	//启动新线程
        System.out.println("main end...");
    }
}
class MyThread extends Thread {
    @Override
    public void run(){
        System.out.println("start new thread!");
    }
}
//方法二：通过实现Runable接口
public class Main{
    public static void main(String[] args){
        System.out.println("main start...");
        Thread t = new Thread(new MyRunnable());
        t.start();
        System.out.println("main end...");
    }
    class MyRunnable implements Runnable{
        @Override
        public void run(){
            System.out.println("start new Thread!");
        }
    }
}
//使用Java8引入lambda语法简写
public class Main{
    public static void main(String[]args){
        Thread t = new Thread(() -> {
            System.out.println("start new thread!");
        });
    }
}
```

- 启动线程调用start()方法，会自动调用线程的run()方法，直接调用run()无效。

- 在线程中调用Thread.sleap()，传入毫秒参数，强迫线程停止一段时间。
- 使用`Thread.setPriority(int n)//1~10,默认是5 `设置线程的优先级

## 线程的状态

在Java程序中，一个线程对象只能调用一次start()方法，并在新线程中执行run()方法。一旦run()方法执行完毕，线程就结束了。因此，Java线程的状态有以下几种：

- New：新创建的线程，尚未执行；
- Runnable：运行中的线程，正在执行run()方法的Java代码；
- Blocked：运行中的线程，因为某些操作被阻塞而挂起；
- Waiting：运行中的线程，因为某些操作在等待中；
- Timed Waiting：运行中的线程，以为执行sleep()方法正在计时等待；
- Terminated：线程已终止，因为run()方法执行完毕。

状态转移：New --> (Runnable、Blocked、Waiting、Timed Waiting) --> Terminated

线程终止的原因有：

- 线程正常终止：run()方法执行到return语句放回；
- 线程意外终止：run()方法因为未捕获的异常导致线程终止；
- 对某个线程的Thread实例调用stop()方法强制终止（强烈不推荐使用）。

一个线程可以等待另一个线程知道运行结束。

如在main主线程调用，等待t线程执行完毕再继续执行主线程，Thread.join(long)重载方法可以传入一个等待时间。

```java
public class Main{
    public static void main(String[]args) throws InterruptedException{
        Thread t = new Thread(()->{
            System.out.println("hello");
        });
        t.start();
        t.join();
        System.out.println("end");
    }
}
```

## 线程中断

如果线程需要执行一个长时间任务，就可能需要线程中断。中断线程就是给该线程发送一个信号，该线程收到信号后结束执行run()方法，是的自身线程能立刻运行结束。

如从网络下载一个大文件，如果网速很慢，用户点击取消，这是就需要中断下载线程的执行。

要中断线程，只需要对目标线程调用interrupt()方法，目标线程需要反复检测自身状态是否哦是interrupter状态，如果是，就立刻结束运行。

```java
public class Main{
    public static void main(String[] args) throws InterruptedException{
        Thread t = new Thread(){
            public void run(){
                int n = 0;
                while(!isInterrupted()){
                    n++;
                    System.out.println(n+"hello!");
                }
            }
        };
        t.start();
        Thread.sleep(1); //暂停1毫秒
        t.interrupt();	//中断t线程
        t.join();	//等待t线程结束
        System.out.println("end");
    }
}
```

如果线程处于等待状态，如t.join()会让main线程进入等待状态，此实对main线程调用interrupt()，join()方法会立刻抛出InterruptedException，因此目标线程只要捕获到join()方法抛出的InterruptedException，就说明其他线程对其调用了interrupt()方法，通常情况下该线程应该立刻结束运行。

```java
public class Main{
    public static void main(String[]args) throws InterruptedException{
        Thread t = new Thread(){
            public void run(){
                Thread hello = new HelloThread();
                hello.start();
                try{
                    hello.join();
                }catch(InterruptedException e){
                    System.out.println("interrupted");
                }
                hello.interrupt();
            }
        };
        t.start();
        Thread.sleep(1000);
        t.interrupt();
        t.join();
        System.out.println("end");
    }
}

class HelloThread extends Thread{
    public void run(){
        int n = 0;
        while(!isInterrupted()){
            n++;
            System.out.print(n+ "hello");
            try{
                Thread.sleep(100);
            }catch(InterruptedException e){
                break;
            }
        }
    }
}
```

`main`线程通过调用`t.interrupt()`从而通知`t`线程中断，而此时`t`线程正位于`hello.join()`的等待中，此方法会立刻结束等待并抛出`InterruptedException`。由于我们在`t`线程中捕获了`InterruptedException`，因此，就可以准备结束该线程。在`t`线程结束前，对`hello`线程也进行了`interrupt()`调用通知其中断。如果去掉这一行代码，可以发现`hello`线程仍然会继续运行，且JVM不会退出。











































