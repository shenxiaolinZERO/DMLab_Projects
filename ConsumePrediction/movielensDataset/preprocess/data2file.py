# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'

import pandas as pd
import print_to_file as p2f

#20180422

def main():

    train_file_flag = 1
    test_file_flag = 0
    data_dir = '..\\data'
    if train_file_flag == 1:
        train_file(data_dir)
    if test_file_flag == 1:
        ceshi_file(data_dir)


def ceshi_file(data_dir):
    test = pd.read_csv(data_dir + '\\test.csv')
    # test_item_list = []
    test_session_item_list = []
    user_session_dic = {}
    for i in range(test.shape[0]):  # df.shape[0]，df.shape[1]分别获取行数、列数
        cur_user = test.ix[i, 'userid']
        if cur_user in user_session_dic:
            user_session_dic[cur_user].append(test.ix[i, 'session_id'])
        else:
            user_session_dic[cur_user] = [test.ix[i, 'session_id']]
        test_session_item_list.append([test.ix[i, 'session_id'], [], []])

        item_bought = test.ix[i,'itemid1']
        test_session_item_list[i][1].append(item_bought)

        item_clicked = test.ix[i,'itemid2']
        # test_item_list.append(item_clicked)
        test_session_item_list[i][2].append(item_clicked)

    # test_item_list = list(set(test_item_list))
    p2f.print_data_lists_to_file(test_session_item_list, data_dir + '\\test\\session_item.txt')
    # p2f.print_list_to_file(test_item_list, data_dir + '\\test\\items.txt')
    p2f.print_list_dict_to_file(user_session_dic, data_dir + '\\test\\user_session.txt')

    print('test file already')



def train_file(data_dir):
    # 读取分好的数据,生成模型所用的session_item.txt,items.txt,user_session.txt
    train = pd.read_csv(data_dir + '\\train.csv')
    train_item_list = []
    train_session_item_list = []
    train_item_session_dic = {}
    user_session_dic = {}
    for i in range(train.shape[0]):
        cur_user = train.ix[i, 'userid']
        cur_session = train.ix[i, 'session_id']
        if cur_user in user_session_dic:
            user_session_dic[cur_user].append(cur_session)
        else:
            user_session_dic[cur_user] = [cur_session]
        train_session_item_list.append([cur_session, [], []])

        item_bought = train.ix[i,'itemid1']
        train_session_item_list[i][1].append(item_bought)
        if item_bought in train_item_session_dic:
            train_item_session_dic[item_bought][0].append(cur_session)
        else:
            train_item_session_dic[item_bought] = [[cur_session], []]

        item_clicked = train.ix[i, 'itemid2']
        train_session_item_list[i][2].append(item_clicked)
        if item_clicked in train_item_session_dic:
            train_item_session_dic[item_clicked][1].append(cur_session)
        else:
            train_item_session_dic[item_clicked] = [[], [cur_session]]

    p2f.print_data_lists_to_file(train_session_item_list, data_dir + '\\train\\session_item.txt')
    # p2f.print_list_to_file(train_item_list,data_dir + '\\dataset\\train\\items.txt')
    p2f.print_list_dict_to_file(user_session_dic, data_dir + '\\train\\user_session.txt')
    p2f.print_2lists_dict_to_file(train_item_session_dic, data_dir + '\\train\\item_session.txt')

    print('train file already')


if __name__ == '__main__':
    main()
