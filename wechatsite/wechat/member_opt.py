import string
from .member import Member
from .member import DisplayMember
import redis
import json
from queue import Queue

r = redis.Redis(host='127.0.0.1', port=6379)

def handle(d):
    return Member(d["member_id"],
                  d["member_name"],
                  d["descent_no"], 
                  d["father_id"], 
                  d["sex"], 
                  d["sort_order"],
                  d["spouse_name"]) 

def get_member_info(member_id):
    key = "member." + str(member_id)
    if r.exists(key):
        value = r.get(key)
    else:
        value = ""
    return value

def get_sex_name(sex):
    if sex == "1":
        return '男'
    else:
       return '女'

def get_display_member(member_id):
    member_info = get_member_info(member_id)
    if member_info == "":
        return None
        
    father_name = ""
    mother_name = ""

    member_obj = json.loads(member_info, object_hook=handle)
    father_id = member_obj.father_id
    father_info = get_member_info(father_id)
    if father_info != "":
        father_obj = json.loads(father_info, object_hook=handle)
        if father_obj.sex == "1":
            father_name = father_obj.member_name
            mother_name = father_obj.spouse_name
        else:
            mother_name = father_obj.member_name
            father_name = father_obj.spouse_name

    display_member_obj = DisplayMember(member_obj.member_id,\
                             member_obj.member_name,\
                             member_obj.descent_no, \
                             member_obj.father_id, \
                             member_obj.sex, \
                             member_obj.sort_order, \
                             member_obj.spouse_name, \
                             father_name, \
                             mother_name)
    return display_member_obj

def get_sons(member_id):
    son_display_member_list = []

    key = "sons." + str(member_id)
    son_member_ids = r.smembers(key)
    if son_member_ids == set(): 
       return son_display_member_list 

    for son_member_id in son_member_ids:
        son_member_obj = get_display_member(int(son_member_id.decode()))
        if son_member_obj is None:
           continue 
        son_display_member_list.append(son_member_obj)
    son_display_member_list = sorted(son_display_member_list, key = lambda son: son.sort_order)

    return son_display_member_list
