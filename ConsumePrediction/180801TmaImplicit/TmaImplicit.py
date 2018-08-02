# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

def TmaImplicit():
    write_path =

    dir_path = r'I:\Papers\consumer\codeandpaper\TmallCode\new_code_new_implicit\new_code\data\dataset1\afterSample\train'

    data_path = dir_path + '\implicit_sample3'

    result_data_path = data_path

    f = open(write_path, 'w')
    for cur_data_list in data_lists:
        x = cur_data_list[0]
        x_list1 = cur_data_list[1]      # 购买的商品
        x_list2 = cur_data_list[2]      # 点击不购买的商品
        list1_len = len(x_list1)
        list2_len = len(x_list2)