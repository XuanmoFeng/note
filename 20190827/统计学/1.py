# coding:utf-8
import pandas as pd
import numpy as np

if __name__ == '__main__':
    path = '8名学生的考试成绩数据.csv'
    data = pd.read_csv(path, encoding='utf-8', delimiter=',')
    # 找出统计学等于75分的学生
    a1 = data.query('统计学成绩==["75"]')
    print(a1['姓名'].values)
    # ['赵颖' '袁方']

    # 英语成绩最高的前三名学生
    data['row_number'] = data['英语成绩'].rank(ascending=0, method='first').astype(int)
    print(data[data['row_number'] <= 3]['姓名'].values)
    # ['王翔' '李华' '陈风']

    # 四门课程都大于70分的学生
    a2 = data[(data['英语成绩'] > 70) & (data['统计学成绩'] > 70) & (data['数学成绩'] > 70) & (data['经济学成绩'] > 70)]['姓名'].values
    print(a2)
    # ['王翔' '赵颖' '陈风']
