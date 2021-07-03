"""
EMPI患者主索引
字段：
1.肾小球总数        √
2.球性硬化小球数     √
3.新月体小球数目     √
4.节段性硬化数目     √
5.内皮细胞增生     √
6.毛细血管管腔     √
7.系膜区            ×
8.系膜细胞           ×
9.系膜基质          ×
10.免疫复合物         √
11.肾小管萎缩         √
12.间质纤维化         √
13.间质炎症细胞浸润     √
14.间质血管病变         ×
15.诊断             √
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
1.读取扫描文件，将其以xlsx文件保存
"""
file = '/home/mj/data/renalPathology_data/肾穿病理文本文件.txt'

pathology_data = pd.DataFrame(columns=[
    '病理号', '姓名', '性别', '年龄', '住院号', '送检日期', '医院', '科室', '病区', '临床诊断', '送检者',
    '肾小球总数', '球性硬化小球数', '肾小球囊', '节段性硬化数目', '内皮细胞', '管腔', '系膜区',
    '嗜复红蛋白', '肾小管', '间质', '血管', '诊断'
])

with open(file, encoding='utf8') as f:
    for i, line in enumerate(f.readlines()):
        if line != '\n':
            content = line.split(':')[0].replace(' ', '')
            if content == '姓名':
                pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '姓名'] = \
                      line.split(':')[1].split(' ')[0].replace('\n', '')
                pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '性别'] = \
                      line.split(':')[2].split(' ')[0].replace('\n', '')
                pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '年龄'] = \
                      line.split(':')[3].split(' ')[0].replace('\n', '')
                pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '住院号'] = \
                      line.split(':')[4].split(' ')[0].replace('\n', '')
                pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '送检日期'] = \
                      line.split(':')[5].split(' ')[0].replace('\n', '')
            if content == '医院':
                if len(line.split(':')) == 6:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '医院'] = \
                       line.split(':')[1].split(' ')[0]
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '科室'] = \
                       line.split(':')[2].split(' ')[0]
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '病区'] = \
                       line.split(':')[3].split(' ')[0]
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '临床诊断'] = \
                       line.split(':')[4].split(' ')[0]
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '送检者'] = \
                       line.splir(':')[5].split(' ')[0].replace('\n', '')
                if len(line.split(':')) == 5:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '医院'] = \
                       line.split(':')[1].split(' ')[0]
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '科室'] =\
                       line.split(':')[2].split(' ')[0]
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '病区'] = \
                       line.split(':')[3].split(' ')[0]
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '临床诊断'] = \
                       line.split(':')[4].split(' ')[0].replace('\n', '')
            if content == '肾小球':
                if pathology_data.iloc[len(pathology_data) - 1]['肾小球总数'] is np.nan:
                    if '节段性硬化' in line:
                        pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '肾小球总数'] =\
                           line.split('数量 ')[1].split(' ')[0].replace('\n', '')
                        pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '球性硬化小球数'] = \
                           line.split('球性硬化 ')[1].split(' ')[0].replace('\n', '')
                        pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '节段性硬化数目'] = \
                           line.split('节段性硬化 ')[1].split('')[0].replace('\n', '')



