#缺失值处理 同类复习
import pandas as pd
users=pd.read_csv(r"D:\文件\py\pythonProject1\蓝桥杯\缺失值\1.1\1.csv")
rate=users['recently_logged'].isna().mean()
with open("task0101_2.txt","w")as f:
    f.write(f"{rate:.2f}")
users['recently_logged']=users['recently_logged'].fillna(users['register_time'])
users.to_csv("users2_new.csv")
