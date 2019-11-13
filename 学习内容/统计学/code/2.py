# coding:utf-8
import pandas as pd
import numpy as np

from matplotlib import pyplot


def draw_box(heights):
    # 创建箱形图
    # 第一个参数为待绘制的定量数据
    pyplot.boxplot([heights], labels=['data'])
    # 第二个参数为数据的文字说明
    pyplot.title('The data distribution ')
    pyplot.show()


if __name__ == '__main__':
    path = '../file/实践一.xlsx'
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
    print("极差是：%s" % (data['data'].max() - data['data'].min()))
    print("方差是：%s" % (data['data'].var()))
    print("标准差：%s" % data['data'].std())
    print("偏度：%s" % data['data'].skew())
    print("峰度：%s" % data['data'].kurt())

    draw_box(data['data'])
