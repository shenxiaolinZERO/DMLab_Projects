# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
import read_from_file as rff
import sys
import os
import pandas as pd


#
def generate_session_user_item():
    dir_path = r'I:\Papers\consumer\codeandpaper\TmallCode\new_code_new_implicit\new_code\data\dataset1\afterSample\train'

    data_path = dir_path + '\implicit_sample3'

    result_data_path = data_path

    if not os.path.exists(result_data_path):
        os.makedirs(result_data_path)

    session_item_data = rff.get_2lists_dict(data_path + '\session_item.txt')
    user_session_data = rff.get_int_list_dict(data_path + '\copyof_user_session.txt')

    session_user_dic = dict()
    for u in user_session_data:
        for session in user_session_data[u]:
            session_user_dic[session] = u
    for session in session_item_data:
        session_item_data[session].insert(0, [session_user_dic[session]])
    print_3lists_dict_to_file(session_item_data, result_data_path + '\\session_user_item.txt')


def textToPd_5session():
    dir_path = r'I:\Papers\consumer\codeandpaper\TmallCode\new_code_new_implicit\new_code\data\dataset1\afterSample\train'

    data_path = dir_path + '\implicit_sample3'


    result_data_path = data_path

    data_file = data_path + '\session_user_item.txt'
    # 可以通过指定read_csv的sep参数来修改默认的分隔符
    all_data = pd.read_csv(data_file, sep=';')
    # print(all_data.head(10))
    userId = all_data.iloc[:, 1]
    # print(userid)
    sessionId = all_data.iloc[:, 0]
    # print(itemid)
    winner = all_data.iloc[:, 2]
    loser = all_data.iloc[:, 3]
    # print(rating)

    data_new1 = pd.DataFrame({
        'userId': userId,
        'sessionId': sessionId,
        'winner': winner,
        'loser': loser
    })


    print("去除user冷启动前·共有session个数：", data_new1.shape)

    # 计算每个user的session个数
    df2 = (data_new1[['userId', 'sessionId', 'winner', 'loser']].groupby(
        data_new1['userId']).agg(lambda x: tuple(x)))
    df2['userId'] = df2['userId'].apply(lambda x: x[0])
    df2['user_len'] = df2['sessionId'].apply(lambda x: len(x))
    # print(df2.head())
    df3 = df2[['userId', 'user_len']]

    ### merge df1 and df3
    data_new2 = pd.merge(data_new1, df3, on='userId')

    # 去除user冷启动
    df5 = data_new2[data_new2['user_len'] >= 5]

    data_new2[['userId', 'user_len','sessionId', 'winner', 'loser']].to_csv(
        result_data_path +'\\TmaImplicit_sample3.csv', index=False)

    print("去除user冷启动后·共有session个数：",df5.shape)
    print("1.generate_data_new()已完成！")




# 输出的辅助函数
def print_3lists_dict_to_file(dic, write_path):
    # print(11)
    f = open(write_path, 'w')
    try:
        for key in dic.keys():
            f.write(str(key) + ';')
            list1 = dic[key][0]
            for e in list1:
                if e == list1[-1]:
                    f.write(str(e) + ';')
                else:
                    f.write(str(e) + ',')
            list2 = dic[key][1]
            for e in list2:
                if e == list2[-1]:
                    f.write(str(e) + ';')
                else:
                    f.write(str(e) + ',')
            list3 = dic[key][2]
            for e in list3:
                if e == list3[-1]:
                    f.write(str(e) + '\n')
                else:
                    f.write(str(e) + ',')
    except Exception as e:
        print(e)
    finally:
        f.close()

if __name__ == '__main__':
    # generate_session_user_item()
    # textToPd_5session()




