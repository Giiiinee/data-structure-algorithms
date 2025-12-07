1.用`pandas`读入`users2.csv`
2.计算`recently_logged`的缺失率
  - 保留两位小数
  - 写入`task0101_2.txt`
3.用`register_time`填补`recently_logged`
  - 导出为`users2_new.csv`
  - 确保新文件里`recently_logged`没有缺失值

文件路径
["D:\文件\py\pythonProject1\蓝桥杯\缺失值\1.1\1.csv"]

```python
user_id,register_time,recently_logged,school,number_of_classes_join,learn_time
101,2025/2/1 09:00,,A大学,1,3
102,2025/2/3 10:30,2025/2/5 08:00,B大学,2,6
103,2025/2/5 14:20,,C大学,1,2
104,2025/2/8 19:00,2025/2/9 20:00,A大学,3,15
105,2025/2/10 08:10,,B大学,2,9
106,2025/2/12 13:45,2025/2/13 09:30,C大学,1,4
```
