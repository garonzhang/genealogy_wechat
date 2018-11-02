# family_tree
## Description
- to constuct family tree
- to generate the familty book
- only support python3
- python3 src/test.py

## Data Structure
 - memberinfo
   key = "member."+member_id, value = member_info

 - member_name:member_ids
   key = "nameid."+member_name, value = [member_id] 

## 导入数据
   redis_cli 进入 redis 控制台，然后执行 flushall
   python3 load_data.py
