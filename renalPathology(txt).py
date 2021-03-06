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

pd.set_option('display.max_columns', 23)  # 设置显示最大的列为23
pd.set_option('display.width', 1500)  # 数据显示的所有列的总宽度为1500，防止输出内容被换行
pd.set_option('max_colwidth', 100)  # 设置显示每列的宽度100
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
            if content == '病理号':
                pathology_data = pathology_data.append({'病理号': line.split(':')[1].split(' ')[0]}, ignore_index=True)
                print(line.split(':')[1].split(' ')[0])
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
                        line.split(':')[5].split(' ')[0].replace('\n', '')
                if len(line.split(':')) == 5:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '医院'] = \
                        line.split(':')[1].split(' ')[0]
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '科室'] = \
                        line.split(':')[2].split(' ')[0]
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '病区'] = \
                        line.split(':')[3].split(' ')[0].replace('\n', '')
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '临床诊断'] = \
                        line.split(':')[4].split(' ')[0].replace('\n', '')
            if content == '肾小球':
                if pathology_data.iloc[len(pathology_data) - 1]['肾小球总数'] is np.nan:
                    if '节段性硬化' in line:
                        pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '肾小球总数'] = \
                            line.split('数量 ')[1].split(' ')[0].replace('\n', '')
                        pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '球性硬化小球数'] = \
                            line.split('球性硬化 ')[1].split(' ')[0].replace('\n', '')
                        pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '节段性硬化数目'] = \
                            line.split('节段性硬化 ')[1].split(' ')[0].replace('\n', '')
                    else:
                        pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '肾小球总数'] = \
                            line.split('数量 ')[1].split(' ')[0].replace('\n', '')
                        pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '球性硬化小球数'] = \
                            line.split('球性硬化 ')[1].split(' ')[0].replace('\n', '')
            if content == '肾小球囊':
                if pathology_data.iloc[len(pathology_data) - 1]['肾小球囊'] is np.nan:
                    if '肾小球囊: ' in line:
                        pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '肾小球囊'] = \
                            line.split('肾小球囊: ')[1].replace('\n', '')  # 列表索引值超出范围
            if content == '内皮细胞':
                if pathology_data.iloc[len(pathology_data) - 1]['内皮细胞'] is np.nan:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '内皮细胞'] = \
                        line.split('内皮细胞:')[1].replace('\n', '')
            if content == '管腔':
                if pathology_data.iloc[len(pathology_data) - 1]['管腔'] is np.nan:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '管腔'] = \
                        line.split('管腔:')[1].replace('\n', '')
            if content == '系膜区':
                if pathology_data.iloc[len(pathology_data) - 1]['系膜区'] is np.nan:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '系膜区'] = \
                        line.split('系膜区:')[1].replace('\n', '')
            if content == '嗜复红蛋白':
                if pathology_data.iloc[len(pathology_data) - 1]['嗜复红蛋白'] is np.nan:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '嗜复红蛋白'] = \
                        line.split('嗜复红蛋白:')[1].replace('\n', '')
            if content == '肾小管':
                if pathology_data.iloc[len(pathology_data) - 1]['肾小管'] is np.nan:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '肾小管'] = \
                        line.split('肾小管:')[1].replace('\n', '')
            if content == '间质':
                if pathology_data.iloc[len(pathology_data) - 1]['间质'] is np.nan:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '间质'] = \
                        line.split('间质:')[1].replace('\n', '')
            if content == '血管':
                if pathology_data.iloc[len(pathology_data) - 1]['血管'] is np.nan:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '血管'] = \
                        line.split('血管:')[1].replace('\n', '')
            if content == '诊断':
                if pathology_data.iloc[len(pathology_data) - 1]['诊断'] is np.nan:
                    pathology_data.loc[pathology_data.index == (len(pathology_data) - 1), '诊断'] = \
                        line.split('诊断:')[1].split('诊断系数:')[0].replace(' ', '').replace('\n', '')

pathology_data.head()
# 将从txt文件提取到的信息保存为xlsx文件
pathology_data.to_excel('/home/mj/after_data/renalPathology_data/肾穿病理文本文件.xlsx', encoding='utf8')
"""
2. 数据读取
"""
# 1.读取xlsx
pathology_data = pd.read_excel('/home/mj/after_data/renalPathology_data/肾穿病理文本文件.xlsx', encoding='utf8')

"""
'肾小球囊'提取规则:
将出现的数字全部提出，提取后相加即为'新月体小球数目'
若无出现数字，则将其标注为数字0。
"""
# 2.匹配“肾小球囊”，提取出“新月体小球数目”
# （1）将“肾小球囊”列转换为str类型
pathology_data['肾小球囊'] = pathology_data['肾小球囊'].astype(str)
# （2）查看“肾小球囊”列出现的可能情况
print(pathology_data['肾小球囊'].value_counts())  # 144种， 1种为Nan
# （3）去除空格
pathology_data['肾小球囊'] = pathology_data['肾小球囊'].apply(lambda x: x.replace(' ', ''))
# （4）将“肾小球囊”列出现的“未见明显改变 1”修改为“未见明显改变”
pathology_data.loc[585, '肾小球囊'] = '未见明显改变'
# （5）提取出“肾小球囊”列的存在两个数字的列值
pathology_data[['肾小球囊1', '肾小球囊2']] = pathology_data['肾小球囊'].str.extract('(\d+)\D*(\d+)')
# （6）将“肾小球囊1”、“肾小球囊2”两列的Nan值填充为0
pathology_data[['肾小球囊1', '肾小球囊2']] = pathology_data[['肾小球囊1', '肾小球囊2']].fillna(0)
# （7）将“肾小球囊1”、“肾小球囊2”两列的数值转换为int型
pathology_data[['肾小球囊1', '肾小球囊2']] = pathology_data[['肾小球囊1', '肾小球囊2']].astype(int)
# （8）将“肾小球囊1”、“肾小球囊2”两列的数值相加
pathology_data['肾小球囊12'] = pathology_data['肾小球囊1'] + pathology_data['肾小球囊2']
# （9）删除临时列“肾小球囊1”、“肾小球囊2”
pathology_data = pathology_data.drop(pathology_data[['肾小球囊1', '肾小球囊2']], axis=1)
# （10）提取出“肾小球囊”列的存在一个数字的列值
pathology_data['新月体小球数目'] = pathology_data['肾小球囊'].str.extract('(\d+)')
# （11）将“新月体小球数目”列的Nan值填充为0
pathology_data['新月体小球数目'] = pathology_data['新月体小球数目'].fillna(0)
# （12）将“新月体小球数目”列的数值转换为int型
pathology_data['新月体小球数目'] = pathology_data['新月体小球数目'].astype(int)
# （13）将“新月体小球数目”与“肾小球囊12”列值进行对比，若“新月体小球数目”列中的值大于“肾小球囊12”对应的值，则替换“新月体小球数目”列中的值，反之不替换。
pathology_data['新月体小球数目'] = pathology_data.apply(lambda x: max(x['新月体小球数目'], x['肾小球囊12']), axis=1)
# （14）删除临时列“肾小球囊12”
del pathology_data['肾小球囊12']
"""
总结：（新月体小球数目、记录数量）
0     786
1      47
2      52
3      27
4      14
5       9
6       7
8       7
9       6
7       5
10      3
14      2
43      1
11      1
15      1
20      1
46      1
"""

"""
“内皮细胞增生”提取规则：
“轻”提取0
“中”提取0
“重”提取0
“增生”提取1
“增生”+“轻”提取1
“增生”+“中”提取2
“增生”+“重”提取3
"""
# 3.匹配“内皮细胞”，提取出“内皮细胞增生”
# （1）将“内皮细胞”列转换为str类型
pathology_data['内皮细胞'] = pathology_data['内皮细胞'].astype(str)
# （2）查看“内皮细胞”列出现的可能情况
print(pathology_data['内皮细胞'].value_counts())   # 17种， 1种为Nan
# （3）去除空格
pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.replace(' ',''))
# （4）去除内皮细胞中出现的数字，以免对后续提取造成干扰
pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.translate(str.maketrans('','',digits)))
# （5）“内皮细胞”列中找到“增生”、“轻”、“中”、“重”，对应替换成需要提取的数字
pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.replace('增生', '1增生'))
pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.replace('轻', '0轻'))
pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.replace('中', '1中'))
pathology_data['内皮细胞'] = pathology_data['内皮细胞'].apply(lambda x: x.replace('重', '2重'))
# （6）取出“内皮细胞”列中包含关键词“增生”的记录，创建新表neipi
neipi = pathology_data[pathology_data['内皮细胞'].str.contains('增生')][['病理号', '内皮细胞']]  # 97
# （7）提取出neipi表的“内皮细胞”列的存在两个数字的列值
neipi[['内皮细胞1', '内皮细胞2']] = neipi['内皮细胞'].str.extract('(\d+)\D*(\d+)')
# （8）将neipi表的“内皮细胞1”、“内皮细胞2”两列的Nan值填充为0
neipi[['内皮细胞1', '内皮细胞2']] = neipi[['内皮细胞1', '内皮细胞2']].fillna(0)
# （9）将neipi表的“内皮细胞1”、“内皮细胞2”两列的数值转换为int型
neipi[['内皮细胞1', '内皮细胞2']] = neipi[['内皮细胞1', '内皮细胞2']].astype(int)
# （10）将neipi表的“内皮细胞1”、“内皮细胞2”两列的数值相加
neipi['内皮细胞12'] = neipi['内皮细胞1'] + neipi['内皮细胞2']
# （11）删除neipi表的临时列“内皮细胞1”、“内皮细胞2”
neipi = neipi.drop(neipi[['内皮细胞1', '内皮细胞2']], axis=1)
# （12）提取出neipi表的“内皮细胞”列的存在一个数字的列值
neipi['内皮细胞增生'] = neipi['内皮细胞'].str.extract('(\d+)')
# （13）将neipi表的“内皮细胞增生”列的Nan值填充为0
neipi['内皮细胞增生'] = neipi['内皮细胞增生'].fillna(0)
# （14）将neipi表的“内皮细胞增生”列的数值转换为int型
neipi['内皮细胞增生'] = neipi['内皮细胞增生'].astype(int)
# （15）将neipi表的“内皮细胞增生”与“内皮细胞12”列值进行对比，若“内皮细胞增生”列中的值大于“内皮细胞12”对应的值，则替换“内皮细胞增生”列中的值，反之不替换。
neipi['内皮细胞增生'] = neipi.apply(lambda x: max(x['内皮细胞增生'], x['内皮细胞12']), axis=1)
# （16）删除临时列“内皮细胞12”
del neipi['内皮细胞12']
# （17）将neipi表与pathology_data表进行“病理号”及“内皮细胞”列外连接合并
pathology_data = pd.merge(pathology_data, neipi, on=['病理号', '内皮细胞'], how='left').fillna(0)
"""
总结：（内皮细胞增生、记录数量）
0.0    873
1.0     62
2.0     24
3.0     11
"""
"""
“管腔”提取规则：
“轻”0
“中”0
“重”0
“狭窄”提取1
“狭窄”+“轻”1
“狭窄”+“中”2
“狭窄”+“重”3
“闭塞”提取3
“闭塞”+“轻”提取3
“闭塞”+“中”提取3
“闭塞”+“重”提取3
"""
# 4.匹配“管腔”，提取出“毛细血管管腔”
# （1）将“管腔”列转换为str类型
pathology_data['管腔'] = pathology_data['管腔'].astype(str)
# （2）查看“管腔”列出现的可能情况
print(pathology_data['管腔'].value_counts())  # 48种，1种为Nan
# （3）去除空格
pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.replace(' ', ''))
# （4）去除管腔中出现的数字，以免对后续提取造成干扰
pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.translate(str.maketrans('', '', digits)))
# （5）在“管腔”列中找到关键词“狭窄”、“闭塞”、“轻”、“中”、“重”，对应替换成需要提取的数字
pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.replace('狭窄', '1狭窄'))
pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.replace('轻', '0轻'))
pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.replace('中', '1中'))
pathology_data['管腔'] = pathology_data['管腔'].apply(lambda x: x.replace('重', '2重'))
# （6）查看“管腔”列中出现有无既出现“狭窄”，又出现“闭塞”的记录
print(len(pathology_data[pathology_data['管腔'].str.contains('狭窄') & pathology_data['管腔'].str.contains('闭塞')]))  # 0
# （7）取出“管腔”列中包含关键词“狭窄”的记录，创建新表xiazhai
xiazhai = pathology_data[pathology_data['管腔'].str.contains('狭窄')][['病理号', '管腔']]  # 238
# （8）提取出xiazhai表的“管腔”列存在两个数字的列值
xiazhai[['管腔1', '管腔2']] = xiazhai['管腔'].str.extract('(\d+)\D*(\d+)')
# （9）将xiazhai表的“管腔1”、“管腔2”两列的Nan值填充为0
xiazhai[['管腔1', '管腔2']] = xiazhai[['管腔1', '管腔2']].fillna(0)
# （10）将xiazhai表的“管腔1”、“管腔2”两列的数值转换为int型
xiazhai[['管腔1', '管腔2']] = xiazhai[['管腔1', '管腔2']].astype(int)
# （11）将xiazhai表的“管腔1”、“管腔2”两列的数值相加
xiazhai['管腔12'] = xiazhai['管腔1'] + xiazhai['管腔2']
# （12）删除xiazhai表的临时列“管腔1”、“管腔2”
xiazhai = xiazhai.drop(xiazhai[['管腔1', '管腔2']], axis=1)
# （13）提取出xiazhai表的“管腔”列的存在一个数字的列值
xiazhai['毛细血管管腔'] = xiazhai['管腔'].str.extract('(\d+)')
# （14）将xiazhai表的“毛细血管管腔”列的Nan值填充为0
xiazhai['毛细血管管腔'] = xiazhai['毛细血管管腔'].fillna(0)
# （15）将xiazhai表的“毛细血管管腔”列的数值转换为int型
xiazhai['毛细血管管腔'] = xiazhai['毛细血管管腔'].astype(int)
# （16）将xiazhai表的“毛细血管管腔”与“管腔12”列值进行对比，若“毛细血管管腔”列中的值大于“管腔12”对应的值，则替换“毛细血管管腔”列中的值，反之不替换。
xiazhai['毛细血管管腔'] = xiazhai.apply(lambda x: max(x['毛细血管管腔'], x['管腔12']), axis=1)
# （17）删除临时列“管腔12”
del xiazhai['管腔12']
# （18）将xiazhai表与pathology_data表进行“病理号”及“管腔”列外连接合并
pathology_data = pd.merge(pathology_data, xiazhai, on=['病理号', '管腔'], how='left').fillna(0)
# （19）将“管腔”列值中出现关键词“闭塞”的记录，“毛细血管管腔”全部改为3
pathology_data.loc[pathology_data['管腔'].str.contains('闭塞'), '毛细血管管腔'] = 3
"""
总结：（毛细血管管腔、记录数量）
0.0    670
1.0    159
3.0    114
2.0     27
"""
# 5.匹配“系膜区”，提取出“系膜区”
# （1）将“系膜区”，列转换为str类型
pathology_data['系膜区'] = pathology_data['系膜区'].astype(str)
# （2）查看“内皮细胞”列出现的可能情况
print(pathology_data['系膜区'].value_counts())  # 137种，1种为Nan
# （3）去除空格
pathology_data['系膜区'] = pathology_data['系膜区'].apply(lambda x: x.replace(' ',''))
"""
“嗜复红蛋白”提取规则：
“内皮下”提取1
“硬化区”提取2
“系膜区”提取1
“毛细血管壁”提取2
“系膜区”+“毛细血管壁”提取3
"""
# 6.匹配“嗜复红蛋白”，提取出“免疫复合物”
# （1）将“嗜复红蛋白”列转换为str类型
pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].astype(str)
# （2）查看“内皮细胞”列出现的可能情况
print(pathology_data['嗜复红蛋白'].value_counts())  # 28种，1种为Nan
# （3）去除空格
pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.replace(' ', ''))
# （4）去除嗜复红蛋白中出现的数字，以免对后续提取造成干扰
pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.translate(str.maketrans('', '', digits)))
# （5）在“嗜复红蛋白”列中找到关键词“毛细血管壁”、“系膜区”，对应替换成需要提取的数字
pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.replace('毛细血管壁', '2毛细血管壁'))
pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.replace('系膜区', '1系膜区'))
pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.replace('内皮下', '1内皮下'))
pathology_data['嗜复红蛋白'] = pathology_data['嗜复红蛋白'].apply(lambda x: x.replace('硬化区', '2硬化区'))
# （6）提取出“嗜复红蛋白”列存在两个数字的列值
pathology_data[['嗜复红蛋白1', '嗜复红蛋白2']] = pathology_data['嗜复红蛋白'].str.extract('(\d+)\D*(\d+)')
# （7）将“嗜复红蛋白1”、“嗜复红蛋白2”两列的Nan值填充为0
pathology_data[['嗜复红蛋白1', '嗜复红蛋白2']] = pathology_data[['嗜复红蛋白1', '嗜复红蛋白2']].fillna(0)
# （8）将“嗜复红蛋白1”、“嗜复红蛋白2”两列的数值转换为int型
pathology_data[['嗜复红蛋白1', '嗜复红蛋白2']] = pathology_data[['嗜复红蛋白1', '嗜复红蛋白2']].astype(int)
# （9）将“嗜复红蛋白1”、“嗜复红蛋白2”两列的数值相加
pathology_data['嗜复红蛋白12'] = pathology_data['嗜复红蛋白1'] + pathology_data['嗜复红蛋白2']
# （10）删除临时列“嗜复红蛋白1”、“嗜复红蛋白2”
pathology_data = pathology_data.drop(pathology_data[['嗜复红蛋白1', '嗜复红蛋白2']], axis=1)
# （11）提取出“嗜复红蛋白”列的存在一个数字的列值
pathology_data['免疫复合物'] = pathology_data['嗜复红蛋白'].str.extract('(\d+)')
# （12）将“免疫复合物”列的Nan值填充为0
pathology_data['免疫复合物'] = pathology_data['免疫复合物'].fillna(0)
# （13）将“免疫复合物”列的数值转换为int型
pathology_data['免疫复合物'] = pathology_data['免疫复合物'].astype(int)
# （16）将“免疫复合物”与“嗜复红蛋白12”列值进行对比，若“免疫复合物”列中的值大于“嗜复红蛋白12”对应的值，则替换“免疫复合物”列中的值，反之不替换。
pathology_data['免疫复合物'] = pathology_data.apply(lambda x: max(x['免疫复合物'], x['嗜复红蛋白12']), axis=1)
# （17）删除“嗜复红蛋白12”列
del pathology_data['嗜复红蛋白12']
"""
总结：（免疫复合物、记录数量）
0    685
2    212
1     51
3     22
"""

"""
“肾小管”提取规则：
“轻”提取1
“中”提取2
“重”提取3
“多灶性萎缩／80%”提取80%
"""
# 7.匹配“肾小管”，提取出“肾小管萎缩”
# （1）将“肾小管”列转换为str类型
pathology_data['肾小管'] = pathology_data['肾小管'].astype(str)
# （2）查看“内皮细胞”列出现的可能情况
print(pathology_data['肾小管'].value_counts())  # 87种，1种为Nan
# （3）去除空格
pathology_data['肾小管'] = pathology_data['肾小管'].apply(lambda x: x.replace(' ', ''))
# （4）提取出“肾小管”列的存在一个数字的列值
pathology_data['肾小管萎缩'] = pathology_data['肾小管'].str.extract('(\d+)')
# （5）在“肾小管”中找到关键字“轻”、“中”、“重”，对应替换成需要提取的数字
pathology_data['肾小管'] = pathology_data['肾小管'].apply(lambda x: x.replace('轻', '1轻'))
pathology_data['肾小管'] = pathology_data['肾小管'].apply(lambda x: x.replace('中', '2中'))
pathology_data['肾小管'] = pathology_data['肾小管'].apply(lambda x: x.replace('重', '3重'))
# （6）取出“肾小管萎缩”列中位Nan值的记录，创建表shenxiaoguan
shenxiaoguan = pathology_data[pathology_data['肾小管萎缩'].isna()][['病理号', '肾小管']]
# （7）在shenxiaoguan表的“肾小管”列中提取出数字
shenxiaoguan['肾小管萎缩1'] = shenxiaoguan['肾小管'].str.extract('(\d+)')
# （8）将“肾小管萎缩”列的Nan值填充为0
pathology_data['肾小管萎缩'] = pathology_data['肾小管萎缩'].fillna('0')
# （9）将“肾小管萎缩”列值添加%
pathology_data['肾小管萎缩'] = pathology_data['肾小管萎缩'] + '%'
# （10）将shenxiaoguan表与pathology_data通过病理号进行外连接
pathology_data = pd.merge(pathology_data, shenxiaoguan, on=['病理号', '肾小管'], how='left')
# （11）当“肾小管萎缩”列值为0%时，“肾小管萎缩1”的值替代“肾小管萎缩”的值
for i in range(len(pathology_data)):
    if pathology_data.iloc[i]['肾小管萎缩'] == '0%':
        pathology_data.loc[i, '肾小管萎缩'] = pathology_data.iloc[i]['肾小管萎缩1']
# （12）删除“肾小管萎缩1”列
del pathology_data['肾小管萎缩1']
# （13）将“肾小管萎缩”列的Nan值填充为0
pathology_data['肾小管萎缩'] = pathology_data['肾小管萎缩'].fillna('0')
"""
总结：（肾小管萎缩、记录总数）
0      567
1       52
5%      46
10%     42
15%     41
3%      23
25%     21
8%      21
20%     16
80%     15
2%      13
75%     13
60%     11
30%     11
50%     10
45%      9
40%      9
3        7
85%      7
70%      6
2        6
1%       5
55%      5
35%      4
90%      4
6%       3
95%      1
98%      1
88%      1
"""

"""
“间质”提取规则：（间质纤维化\间质炎症细胞浸润）
“轻”提取1
“中”提取2
“重”提取3
“纤维化”提取1
“纤维化”+“轻”1
“纤维化”+“中”2
“纤维化”+“重”3

“轻”提取1
“中”提取2
“重”提取3
“单个核细胞浸润”提取1
“单个核细胞浸润”+“轻”1
“单个核细胞浸润”+“中”2
“单个核细胞浸润”+“重”3
“淋巴细胞浸润”提取1
“淋巴细胞浸润”+“轻”1
“淋巴细胞浸润”+“中”2
“淋巴细胞浸润”+“重”3
"""
# 8.匹配“间质”，提取出“间质纤维化”
# （1）将“间质”列转换为str类型
pathology_data['间质'] = pathology_data['间质'].astype(str)
# （2）查看“内皮细胞”列出现的可能情况
print(pathology_data['间质'].value_counts())  # 76种，1种为Nan
# （3）去除空格
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace(' ', ''))
# （4）去除间质中出现的数字，以免对后续提取造成干扰
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.translate(str.maketrans('', '', digits)))
# （5）在“间质”列中找到关键词“纤维化”、“轻”、“中”、“重”，对应替换成需要提取的数字
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('纤维化', '1纤维化'))
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('轻', '0轻'))
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('中', '1中'))
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('重', '2重'))
# （6）取出“间质”列中包含关键词“纤维化”的记录，创建新表xianweihua
xianweihua = pathology_data[pathology_data['间质'].str.contains('纤维化')][['病理号', '间质']]  # 305
# （7）提取出xianweihua表的“间质”列的存在两个数字的列值
xianweihua[['间质1', '间质2']] = xianweihua['间质'].str.extract('(\d+)\D*(\d+)')
# （8）将xianweihua表的“间质1”、“间质2”两列的Nan值填充为0
xianweihua[['间质1', '间质2']] = xianweihua[['间质1', '间质2']].fillna(0)
# （9）将xianweihua表的“间质1”、“间质2”两列的数值转换为int型
xianweihua[['间质1', '间质2']] = xianweihua[['间质1', '间质2']].astype(int)
# （10）将xianweihua表的“间质1”、“间质2”两列的数值相加
xianweihua['间质12'] = xianweihua['间质1'] + xianweihua['间质2']
# （11）删除xianweihua表的临时列“间质1”、“间质2”
xianweihua = xianweihua.drop(xianweihua[['间质1', '间质2']], axis=1)
# （12）提取出xianweihua表的“间质”列的存在一个数字的列值
xianweihua['间质纤维化'] = xianweihua['间质'].str.extract('(\d+)')
# （13）将xianweihua表的“间质纤维化”列的Nan值填充为0
xianweihua['间质纤维化'] = xianweihua['间质纤维化'].fillna(0)
# （14）将xianweihua表的“间质纤维化”列的数值转换为int型
xianweihua['间质纤维化'] = xianweihua['间质纤维化'].astype(int)
# （15）将xianweihua表的“间质纤维化”与“间质12”列值进行对比，若“间质纤维化”列中的值大于“间质12”对应的值，则替换“间质纤维化”列中的值，反之不替换。
xianweihua['间质纤维化'] = xianweihua.apply(lambda x: max(x['间质纤维化'], x['间质12']), axis=1)
# （16）删除临时列“间质12”
del xianweihua['间质12']
# （17）将xianweihua表与pathology_data表进行“病理号”及“间质”列外连接合并
pathology_data = pd.merge(pathology_data, xianweihua, on=['病理号', '间质'], how='left').fillna(0)
"""
总结：（间质纤维化、记录数量）
0.0    665
1.0    147
2.0     84
3.0     74
"""

# 9.匹配“间质”，提取出“间质炎症细胞浸润”
# （1）去除间质中出现的数字，以免对后续提取造成干扰
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.translate(str.maketrans('', '', digits)))
# （2）在“间质”列中找到关键词“纤维化”、“轻”、“中”、“重”，对应替换成需要提取的数字
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('单个核细胞浸润', '1单个核细胞浸润'))
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('淋巴细胞浸润', '1淋巴细胞浸润'))
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('轻', '0轻'))
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('中', '1中'))
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('重', '2重'))
pathology_data['间质'] = pathology_data['间质'].apply(lambda x: x.replace('大量', '2大量'))
# （3）查看“间质”列中出现有无既出现“单个核细胞浸润”，又出现“淋巴细胞浸润”的记录
print(len(pathology_data[pathology_data['间质'].str.contains('单个核细胞浸润') & pathology_data['间质'].str.contains('淋巴细胞浸润')]))  # 0
# （6）取出“间质”列中包含关键词“单个核细胞浸润”、“淋巴细胞浸润”的记录，创建新表xibaojinrun
xibaojinrun = pathology_data[pathology_data['间质'].str.contains('单个核细胞浸润') |
                            pathology_data['间质'].str.contains('淋巴细胞浸润')][['病理号', '间质']]  # 209
# （7）提取出xibaojinrun表的“间质”列的存在两个数字的列值
xibaojinrun[['间质1', '间质2']] = xibaojinrun['间质'].str.extract('(\d+)\D*(\d+)')
# （8）将xibaojinrun表的“间质1”、“间质2”两列的Nan值填充为0
xibaojinrun[['间质1', '间质2']] = xibaojinrun[['间质1', '间质2']].fillna(0)
# （9）将xibaojinrun表的“间质1”、“间质2”两列的数值转换为int型
xibaojinrun[['间质1', '间质2']] = xibaojinrun[['间质1', '间质2']].astype(int)
# （10）将xibaojinrun表的“间质1”、“间质2”两列的数值相加
xibaojinrun['间质12'] = xibaojinrun['间质1'] + xibaojinrun['间质2']
# （11）删除xxibaojinrun表的临时列“间质1”、“间质2”
xibaojinrun = xibaojinrun.drop(xibaojinrun[['间质1', '间质2']], axis=1)
# （12）提取出xibaojinrun表的“间质”列的存在一个数字的列值
xibaojinrun['间质炎症细胞浸润'] = xibaojinrun['间质'].str.extract('(\d+)')
# （13）将xibaojinrun表的“间质炎症细胞浸润”列的Nan值填充为0
xibaojinrun['间质炎症细胞浸润'] = xibaojinrun['间质炎症细胞浸润'].fillna(0)
# （14）将xibaojinrun表的“间质炎症细胞浸润”列的数值转换为int型
xibaojinrun['间质炎症细胞浸润'] = xibaojinrun['间质炎症细胞浸润'].astype(int)
# （15）将xibaojinrun表的“间质炎症细胞浸润”与“间质12”列值进行对比，若“间质炎症细胞浸润”列中的值大于“间质12”对应的值，则替换“间质炎症细胞浸润”列中的值，反之不替换。
xibaojinrun['间质炎症细胞浸润'] = xibaojinrun.apply(lambda x: max(x['间质炎症细胞浸润'], x['间质12']), axis=1)
# （16）删除临时列“间质12”
del xibaojinrun['间质12']
# （17）将xibaojinrun表与pathology_data表进行“病理号”及“间质”列外连接合并
pathology_data = pd.merge(pathology_data, xibaojinrun, on=['病理号', '间质'], how='left').fillna(0)
"""
总结：（间质炎症细胞浸润、记录数量）
0.0    761
1.0    130
2.0     47
3.0     32
"""

# 10.匹配“血管”，提取出“间质血管病变”
# （1）将“血管”列转换为str类型
pathology_data['血管'] = pathology_data['血管'].astype(str)
# （2）查看“内皮细胞”列出现的可能情况
print(pathology_data['血管'].value_counts())  # 45种，1种为Nan
# （3）去除空格
pathology_data['血管'] = pathology_data['血管'].apply(lambda x: x.replace(' ', ''))


"""
计算指标
硬化小球比例：球性硬化小球数/肾小球总数
节段硬化小球比例：节段性硬化数目/肾小球总数
新月体小球比例：新月体小球数目/肾小球总数
"""
# 11.计算硬化小球比例
# （1）硬化小球比例：球性硬化小球数/肾小球总数
pathology_data['球性硬化小球数'] = pathology_data['球性硬化小球数'].astype(str)
pathology_data['球性硬化小球数'] = pathology_data['球性硬化小球数'].apply(lambda x: x.replace(',', ''))
pathology_data['球性硬化小球数'] = pathology_data['球性硬化小球数'].astype(int)
pathology_data['肾小球总数'] = pathology_data['肾小球总数'].astype(str)
pathology_data['肾小球总数'] = pathology_data['肾小球总数'].apply(lambda x: x.split('(')[0])
pathology_data['肾小球总数'] = pathology_data['肾小球总数'].astype(int)
pathology_data['硬化小球比例'] = pathology_data['球性硬化小球数'] / pathology_data['肾小球总数']
# （2）解决出现分母为0计算出的结果
pathology_data.replace([np.inf, -np.inf], np.nan, inplace=True)
# （3）将Nan值填充为0
pathology_data['硬化小球比例'] = pathology_data['硬化小球比例'].fillna(0)

# 12.计算节段硬化小球比例
# （1）节段硬化小球比例：节段性硬化数目/肾小球总数
pathology_data['节段硬化小球比例'] = pathology_data['节段性硬化数目'] / pathology_data['肾小球总数']
# （2）解决出现分母为0计算出的结果
pathology_data.replace([np.inf, -np.inf], np.nan, inplace=True)
# （3）将Nan值填充为0
pathology_data['节段硬化小球比例'] = pathology_data['节段硬化小球比例'].fillna(0)

# 13.计算新月体小球比例
# （1）新月体小球比例：新月体小球数目/肾小球总数
pathology_data['新月体小球比例'] = pathology_data['新月体小球数目'] / pathology_data['肾小球总数']
# （2）解决出现分母为0计算出的结果
pathology_data.replace([np.inf, -np.inf], np.nan, inplace=True)
# （3）将Nan值填充为0
pathology_data['新月体小球比例'] = pathology_data['新月体小球比例'].fillna(0)

# 14.保存处理后的文件
# （1）删除原始列
pathology_data = pathology_data.drop(pathology_data[['肾小球囊', '内皮细胞', '管腔', '嗜复红蛋白', '肾小管', '间质']], axis=1)
# （2）保存为xlsx文件
pathology_data.to_excel("/home/mj/after_data/renalPathology_data/after_肾穿病理文本文件.xlsx",
                        encoding='utf8', index=False)