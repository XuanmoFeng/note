# 4.描述性统计

代码实现

```
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
    print("极差是：%s"%(data['data'].max()-data['data'].min()))
    print("方差是：%s"%(data['data'].var()))
    print("标准差：%s"%data['data'].std())

```

![实践结果](https://github.com/XuanmoFeng/note/blob/master/%E5%AD%A6%E4%B9%A0%E5%86%85%E5%AE%B9/%E7%BB%9F%E8%AE%A1%E5%AD%A6/image/%E6%8F%8F%E8%BF%B0%E6%80%A7%E6%95%B0%E6%8D%AE%E5%AE%9E%E8%B7%B5.png)
