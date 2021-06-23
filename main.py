# 利用pickle 存储和读取文件
# 1.存储文件：
# 引入所需包，将列表元素存入data2的文件里面
import pickle
mylist2 = ['a', 'b', ['你好', '证明'], 1, 3, 5, 7]
df2 = open('E:\\data2.txt', 'wb')  # 注意一定要写明是wb 而不是w.
# 最关键的是这步，将内容装入打开的文件之中（内容，目标文件）
pickle.dump(mylist2, df2)
df2.close()
# 2.读取文件：
# 读取文件中的内容。注意和通常读取数据的区别之处
df = open('E:\\data2.txt', 'rb')  # 注意此处是rb
# 此处使用的是load(目标文件)
data3 = pickle.load(df)
df.close()
data3


