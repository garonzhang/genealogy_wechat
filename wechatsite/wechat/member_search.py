import string
from .member import Member
from .member import DisplayMember
from . import member_opt as mo
from . import construct_tree as ct
from . import member_visualize as mv


def get_tree(member_id):
    unvalid_request = "<html><body>非法請求,小心被禁用</body></html>"

    display_member_obj = mo.get_display_member(member_id)
    if display_member_obj is None:
        return unvalid_request
    if display_member_obj.descent_no < 15:
        return unvalid_request

    display_member_list = ct.get_tree_nodes(display_member_obj)
    content = mv.get_table_content(display_member_list)
    return content 


def member_format(display_member_obj):
    member_info = "" +\
                   "编号："+str(display_member_obj.member_id)+"\n"+\
                   "世代："+str(display_member_obj.descent_no)+"\n"+\
                   "名字："+display_member_obj.member_name+"\n"+\
                   "性别："+ mo.get_sex_name(display_member_obj.sex)+"\n" +\
                   "排行："+str(display_member_obj.sort_order)+"\n"+\
                   "配偶名字："+display_member_obj.spouse_name+"\n" +\
                   "父亲："+display_member_obj.father_name+"\n"+\
                   "母亲："+display_member_obj.mother_name+"\n"+ \
                   "功名职业：" + display_member_obj.career + "\n" + \
                  "<a href='http://www.yinmahezhang.com/s_id?member_id="+str(display_member_obj.member_id)+"'>"+"查看"+"</a>"
    return member_info 

def member_list_format(display_member_list):
    content  = ""
    display_member_list = sorted(display_member_list, key = lambda member: member.descent_no)
    for display_member_obj in display_member_list:
        member_info = member_format(display_member_obj)
        content = content + member_info +"\n\n" 
    if content  == "":
        return "no records"
    return content

# to get the member list by keyword of member_name
def search_by_keyword(keyword):
    key = "nameid." + keyword.strip()
    member_ids = mo.r.smembers(key)

    display_member_list = []
    for member_id in member_ids:
        display_member_obj = mo.get_display_member(member_id.decode())
        display_member_list.append(display_member_obj)
    sort_display_member_list= sorted(display_member_list, key=lambda display_member: display_member.descent_no)
    content = mv.get_table_content(sort_display_member_list) 
    return content 
