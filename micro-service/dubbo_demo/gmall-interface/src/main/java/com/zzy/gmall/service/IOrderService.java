package com.zzy.gmall.service;

import com.zzy.gmall.bean.UserAddress;

import java.util.List;

/**
 * @author zhaozeyu
 * create on 2020/3/28 23:14
 */
public interface IOrderService {

    /**
     * 初始化订单
     * @param userId
     */
    public List<UserAddress> initOrder(String userId);
}
