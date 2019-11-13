# coding:utf-8
import pandas as pd
import numpy as np

if __name__ == '__main__':
    path = '实践一.xlsx'
    data = pd.read_excel(path, encoding='utf-8')
    print("众数是：%s" % data['data'].mode().values)
    print("中位数是：%s" % data['data'].median())
    print("上四分位是：%s" % data['data'].quantile(q=0.25))
    print("下四分位是：%s" % data['data'].quantile(q=0.75))
    print("简单平均数是：%s" % data['data'].mean())
    da = data['data'].groupby(data['data']).count().reset_index(name="count")
    print("加权平均数是：%s" % ((da['data'] * da['count']).sum() / da['count'].sum()))
    # data['mul']=data['data'].cumprod().head(300)
    # print("几何平均数是：%s" %)
