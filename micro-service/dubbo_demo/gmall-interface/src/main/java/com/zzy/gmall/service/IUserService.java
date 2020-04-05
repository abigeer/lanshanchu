package com.zzy.gmall.service;

import com.zzy.gmall.bean.UserAddress;

import java.util.List;

/**
 * @author zhaozeyu
 * create on 2020/3/28 23:14
 */
public interface IUserService {

    /**
     * 按照用户id返回所有的收货地址
     * @param userId
     * @return
     */
    public List<UserAddress> getUserAddressList(String userId);

}
