#缺失值处理
import pandas as pd
users=pd.read_csv(r"D:\文件\py\pythonProject1\蓝桥杯\users.csv")
rate=users['recently_logged'].isna().mean()
with open("task0101.txt","w")as f:
    f.write(f"{rate:.2f}")
users['recently_logged']=users['recently_logged'].fillna(users['regieter_time'])
users.to.csv("users_news.csv",index=false)
