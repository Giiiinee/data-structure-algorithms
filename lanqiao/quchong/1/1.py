#去重
import pandas as pd
users=pd.read_csv(r"D:\文件\py\pythonProject1\蓝桥杯\去重\1\1.csv")
users_sorted=users.sort_values(by='course_join_time',ascending=False)
users_dup=users_sorted.drop_duplicates(subset=['user_id','course_id'],keep='first')
users_dup.to_csv("clean_study_dup.csv",index=False)
