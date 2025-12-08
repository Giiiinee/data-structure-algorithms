#百分数解析（同类型）
import pandas as pd
study=pd.read_csv(r"D:\文件\py\pythonProject1\蓝桥杯\百分比解析\2\1.csv")
col=study['learn_process'].astype(str)
study['learn_pct']=col.str.extract(r'(\d+)')
print(study[['learn_process','learn_pct']])
invalid_count=study['learn_pct'].isna().sum()
with open("task0102_03.txt","w") as f:
    f.write(str(invalid_count))
study_clean=study.dropna(subset=['learn_pct'])
study_clean.loc[:,'learn_pct']=study_clean['learn_pct'].astype(int)
study_clean.to_csv("study3_new.csv",index=False)
