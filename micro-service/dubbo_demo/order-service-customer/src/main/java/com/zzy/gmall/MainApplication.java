package com.zzy.gmall;

import java.io.IOException;

import com.zzy.gmall.service.IOrderService;
import org.springframework.context.support.ClassPathXmlApplicationContext;


public class MainApplication {
	
	@SuppressWarnings("resource")
	public static void main(String[] args) throws IOException {
		ClassPathXmlApplicationContext applicationContext = new ClassPathXmlApplicationContext("consumer.xml");
		
		IOrderService orderService = applicationContext.getBean(IOrderService.class);
		
		orderService.initOrder("1");
		System.out.println("调用完成....");
		System.in.read();
	}

}
