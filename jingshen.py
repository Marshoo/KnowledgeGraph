import numpy as np
import pandas as pd
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