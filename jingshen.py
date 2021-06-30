import numpy as np
import pandas as pd
<<<<<<< HEAD
import jsonlines
import json
# 导入原始数据
with open("/home/mj/data/jingshen/emr-left-jingshen-20160101-20190630.jsonl", "r+", encoding="utf8") as f:
    data_list = [json.loads(line) for line in f]

data_df = pd.DataFrame(data_list)    # 将 list 转换成 DataFrame


# 更换列名标签
data_df.rename(columns={'visit_no':'个人信息标识符', 'gender_code':'性别', 'birthday':'年龄',
                        'reg_date':'就诊时间', 'orig_dept':'就诊科室', 'test_card_no':'病历文件标识',
                        'Icd10Id':'诊断ICD编码','Icd10Name': '诊断ICD名称'
                        }, inplace=True)
emr_list = data_df['emr'].tolist()   # 提取 data_list 中的信息，准备将主诉、现病史等信息分离出来
emr_df = pd.DataFrame(emr_list)
df = emr_df.join(pd.DataFrame(emr_df[0].values.tolist()))   # 提取emr_df每行字典中的信息
df2 = pd.DataFrame(df, columns=['主诉', '现病史', '体格检查', '辅助检查', '诊断', '处理意见', '备注', '签名'])


# 将签名列拆分
qianming = df['签名'].str.split(pat=None, n=-1, expand=True).rename(columns={0:'科室', 1:'医师签名', 2:'签署日期'})
# 获取医生签名
qianming_2 = pd.DataFrame(qianming['医师签名'].str[5:8])



# 合并所有表格
df3 = pd.concat([data_df, df2, qianming_2], axis=1)
all_df = pd.DataFrame(df3, columns=['个人信息标识符', '性别', '年龄', '病历文件标识', '就诊时间', '就诊科室', '主诉', '现病史',
                                    '体格检查', '辅助检查', '诊断', '诊断ICD名称', '诊断ICD编码', '处理意见', '备注', '医师签名'])
all_df.rename(columns={'诊断':'诊断名称'})


# 性别数值转换
all_df['性别'].replace(['1','2'], ['男性','女性'],inplace=True)


# 将生日转换成年龄，数据中的生日已经是标准时间格式
all_df['年龄'] = pd.to_datetime(all_df['年龄'])
# 获取当前年份
import datetime as dt
now_year = dt.datetime.today().year                     # 当前年份
all_df['age'] = now_year - all_df['年龄'].dt.year       # 获得年龄
all_df = all_df.drop(['年龄'],axis=1)                   # 删掉原来的列
all_df.rename(columns={'age':'年龄'}, inplace=True)     # 重命名

import xlrd

all_df.to_excel('/home/mj/after_data/jingshen.xlsx')
=======
# 导入个人信息标识符、诊断ICD名称、诊断ICD编码
diagnosis_df = pd.read_csv('D:\\data\\jingshen-20160101-20190630\\diagnosis-jingshen-20160101-20190630.csv')
# 将辅助检查 json 文件整理成 DataFrame 形式
import json
f = open('D:\\data\\jingshen-20160101-20190630\\ae_0_30239.json', encoding='utf-8')
ae_data = json.load(f)
ae_data_list = ae_data['data']
ae_data_df = pd.DataFrame(ae_data_list)
ae_data_df.rename(columns={'content':'辅助检查'},inplace=True)
# 将主诉 json 文件整理成 DataFrame 形式
f2 = open('D:\\data\\jingshen-20160101-20190630\\cc_0_93645.json', encoding='utf-8')
cc_data = json.load(f2)
cc_data_list = cc_data['data']
cc_data_df = pd.DataFrame(cc_data_list)
cc_data_df.rename(columns={'content':'主诉'}, inplace=True)
# 将体格检查 json 文件整理成 DataFrame 形式
f3 = open('D:\\data\\jingshen-20160101-20190630\\pe_0_93645.json', encoding='utf-8')
pe_data = json.load(f3)
pe_data_df = pd.DataFrame(pe_data['data'])
pe_data_df.rename(columns={'content':'体格检查'},inplace=True)
# 将 jingshen_basic.csv 文件整理成 DataFrame 形式
jingshen_basic = pd.read_csv('D:\\data\\jingshen-20160101-20190630\\jingshen_basic.csv')
jingshen_basic = jingshen_basic.drop(['len(cc)', 'len(hpi)', 'len(pe)', 'len(ae)'],inplace=True, axis=1)
jingshen_basic.rename(columns={'visit_no':'个人信息标识符', 'gender_code':'性别', 'birthday':'年龄',
                               'reg_date':'就诊时间', 'orig_dept':'就诊科室', 'Icd10Id':'诊断ICD编码',
                               'Icd10Name':'诊断ICD名称', 'doctor_name':'医师签名'}, inplace=True)
# 将目前提出来变量合并
df_1 = pd.concat([jingshen_basic, cc_data_df, pe_data_df, ae_data_df], axis=1)
>>>>>>> 4a6c1ab23620ae755511c7e31e7785c445ae7a44