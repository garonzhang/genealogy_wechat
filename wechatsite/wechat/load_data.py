from member import Member
import csv
import json
import redis

r = redis.Redis(host='127.0.0.1', port=6379)

def get_substrings(s):
    sub_list = [s[i:i + x + 1] for x in range(len(s)) for i in range(len(s) - x)]
    return sub_list


if __name__ == "__main__":
    with open('data/tb_members.csv', newline='') as csvfile:
        csvReader = csv.reader(csvfile)
        for content in csvReader:
            member_id = int(content[0])
            member_name = content[1]
            print(member_name)
            descent_no = int(content[3])
            
            if content[4] == "" or content[4] is None:
                father_id = -1
            else:
                father_id = int(content[4])

            if content[5] == "" or content[5] is None:
                sort_order = 1
            else:
                sort_order = int(content[5])

            if content[13] != "":
                father_id = int(content[13])
                sort_order = int(content[14])
            mother_name = None
            if content[15] != "":
                mother_name = content[15]
            carrer = content[9]
            if carrer is None:
                career = ""

            sex = content[2]
            spouse_name = content[7]
            member_obj = Member(member_id, member_name, descent_no, father_id, sex, sort_order, spouse_name, mother_name, career)
            json_info  = json.dumps(member_obj, default = lambda obj:obj.__dict__, sort_keys=True, indent=4, ensure_ascii=False)

            r.set("member."+str(member_id), json_info)
            r.sadd("sons."+str(father_id), member_id)
    
            sub_names = get_substrings(member_name)
            for sub_name in sub_names:
                if sub_name == '张':
                    continue
                r.sadd("nameid."+sub_name, member_id)
       
