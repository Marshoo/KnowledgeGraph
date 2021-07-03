"""
EMPI患者主索引
字段：
1.肾小球总数        √
2.球性硬化小球数     √
3.新月体小球数目     √
4.节段性硬化数目     √
5.内皮细胞增生     √
6.毛细血管管腔     √
7.系膜区     √
8.系膜细胞     √
9.系膜基质     √
10.免疫复合物     ×
11.肾小管萎缩     √
12.间质纤维化     √
13.间质炎症细胞浸润     √
14.间质血管病变     ×
15.诊断            √
16.硬化小球比例      √
17.节段硬化小球比例   √
18.新月体小球比例     √

计算指标
硬化小球比例：球性硬化小球数/肾小球总数
节段硬化小球比例：节段性硬化数目/肾小球总数
新月体小球比例：新月体小球数目/肾小球总数
"""

import pandas as pd
import numpy as np
from string import digits

pd.set_option('display.max_columns', 23)   # 设置显示最大的列为23
pd.set_option('display.width', 1500)   # 数据显示的所有列的总宽度为1500，防止输出内容被换行
pd.set_option('max_colwidth', 100)     # 设置显示每列的宽度100
pd.set_option('display.max_rows', None)  # 设置显示所有行

"""
读取数据
"""
# 1.读取数据 HIS系统病理筛选.xlsx
renal_data = pd.read_excel('/home/mj/data/renalPathology_data/HIS系统病理筛选.xlsx')
# 2.查看是否每条记录都有“光镜”字符串
is_gj = renal_data[renal_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].str.contains('光镜：')]
renal_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'] = renal_data['DBMS_LOB.SUBSTR(A.DIAG_DESC,4000)'].apply\
    (lambda x: x.split("光镜：")[1])
"""
“诊断”共有3种情况：
a.小结：......
b.小结：1、……；\n2、……；\n3:、……；
c.医生没有写小结
"""
