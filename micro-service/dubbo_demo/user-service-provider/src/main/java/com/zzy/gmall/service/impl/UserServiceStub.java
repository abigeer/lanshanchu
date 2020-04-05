package com.zzy.gmall.service.impl;

import com.zzy.gmall.bean.UserAddress;
import com.zzy.gmall.service.IUserService;
import org.springframework.util.StringUtils;

import java.util.List;

/**
 * @author zhaozeyu
 * create on 2020/3/28 23:20
 */
public class UserServiceStub implements IUserService {


    private final IUserService userService;

    /**
     * 传入的是userService远程的代理对象
     * @param userService
     */
    public UserServiceStub(IUserService userService) {
        super();
        this.userService = userService;
    }

    public List<UserAddress> getUserAddressList(String userId) {
        System.out.println("UserServiceStub.....");
        if(!StringUtils.isEmpty(userId)) {
            return userService.getUserAddressList(userId);
        }
        return null;
    }
}
