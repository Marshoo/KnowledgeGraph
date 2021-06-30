import numpy as np
import pandas as pd
import jsonlines
# 导入原始数据
with open("/home/mj/data/jingshen/emr-left-jingshen-20160101-20190630.jsonl", "r+", encoding="utf8") as f:
    data_list = [json.loads(line) for line in f]

data_df = pd.DataFrame(data_list)    # 将 list 转换成 DataFrame
# 更换列名标签
data_df.rename(columns={'visit_no':'个人信息标识符', 'gender_code':'性别', 'birthday':'年龄',
                        'reg_date':'就诊时间', 'orig_dept':'就诊科室', 'test_card_no':'病历文件标识'
                        }, inplace=True)
emr_list = data_df['emr'].tolist()   # 提取 data_list 中的信息
emr_df = pd.DataFrame(emr_list)
df = emr_df.join(pd.DataFrame(emr_df[0].values.tolist()))   # 提取emr_df每行字典中的信息
df2 = pd.DataFrame(df, columns=['主诉', '现病史', '体格检查', '辅助检查', '诊断', '处理意见', '备注', '签名'])
