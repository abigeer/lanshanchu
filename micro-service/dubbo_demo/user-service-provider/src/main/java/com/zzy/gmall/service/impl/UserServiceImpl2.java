package com.zzy.gmall.service.impl;

import com.zzy.gmall.bean.UserAddress;
import com.zzy.gmall.service.IUserService;

import java.util.Arrays;
import java.util.List;

/**
 * @author zhaozeyu
 * create on 2020/3/28 23:19
 */
public class UserServiceImpl2 implements IUserService {
    public List<UserAddress> getUserAddressList(String userId) {
        System.out.println("UserServiceImpl.....new...");
        // TODO Auto-generated method stub
        UserAddress address1 = new UserAddress(1, "北京市昌平区宏福科技园综合楼3层", "1", "李老师", "010-56253825", "Y");
        UserAddress address2 = new UserAddress(2, "深圳市宝安区西部硅谷大厦B座3层（深圳分校）", "1", "王老师", "010-56253825", "N");

        return Arrays.asList(address1,address2);
    }
}
