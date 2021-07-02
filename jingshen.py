import json
import pandas as pd
# 导入原始数据
with open("/home/mj/data/jingshen/emr-left-jingshen-20160101-20190630.jsonl", "r+", encoding="utf8") as f:
    data_list = [json.loads(line) for line in f]

data_df = pd.DataFrame(data_list)  # 将 list 转换成 DataFrame

# 更换列名标签
data_df.rename(columns={'visit_no': '个人信息标识符', 'gender_code': '性别', 'birthday': '年龄',
                        'reg_date': '就诊时间', 'orig_dept': '就诊科室', 'test_card_no': '病历文件标识',
                        'Icd10Id': '诊断ICD编码', 'Icd10Name': '诊断ICD名称'
                        }, inplace=True)
emr_list = data_df['emr'].tolist()  # 提取 data_list 中的信息，准备将主诉、现病史等信息分离出来
emr_df = pd.DataFrame(emr_list)
df = emr_df.join(pd.DataFrame(emr_df[0].values.tolist()))  # 提取emr_df每行字典中的信息
df2 = pd.DataFrame(df, columns=['主诉', '现病史', '体格检查', '辅助检查', '诊断', '处理意见', '备注', '签名'])

# 将签名列拆分
qianming = df['签名'].str.split(pat=None, n=-1, expand=True).rename(columns={0: '科室', 1: '医师签名', 2: '签署日期'})
# 获取医生签名
qianming_2 = pd.DataFrame(qianming['医师签名'].str[5:8])

# 合并所有表格
df3 = pd.concat([data_df, df2, qianming_2], axis=1)
all_df = pd.DataFrame(df3, columns=['个人信息标识符', '性别', '年龄', '病历文件标识', '就诊时间', '就诊科室', '主诉', '现病史',
                                    '体格检查', '辅助检查', '诊断', '诊断ICD名称', '诊断ICD编码', '处理意见', '备注', '医师签名'])
all_df.rename(columns={'诊断': '诊断名称'})

# 性别数值转换
all_df['性别'].replace(['1', '2'], ['男', '女'], inplace=True)

# 将生日转换成年龄，数据中的生日已经是标准时间格式
all_df['年龄'] = pd.to_datetime(all_df['年龄'])
# 获取当前年份
import datetime as dt

now_year = dt.datetime.today().year  # 当前年份
all_df['age'] = now_year - all_df['年龄'].dt.year  # 获得年龄
all_df = all_df.drop(['年龄'], axis=1)  # 删掉原来的列
all_df.rename(columns={'age': '年龄（岁）'}, inplace=True)  # 重命名
all_df = all_df.drop_duplicates()

all_df.to_excel('/home/mj/after_data/jingshen.xlsx', index=False)
# test  test test

