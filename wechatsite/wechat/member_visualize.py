from wechat.member import DisplayMember 
from . import member_opt as mo


def format_info(display_member_obj):
    if display_member_obj is None:
        return ""
    mother_name  = display_member_obj.mother_name
    if mother_name is None:
        mother_name = ""

    career = display_member_obj.career
    if career is None:
        career = ""

    content = "<tr>"+\
                   "<td>"+str(display_member_obj.descent_no)+"世</td>"+\
                   "<td>"+display_member_obj.member_name+"</td>"+\
                   "<td>"+mo.get_sex_name(display_member_obj.sex)+"</td>" +\
                   "<td>"+str(display_member_obj.sort_order)+"</td>"+\
                   "<td>"+display_member_obj.spouse_name+"</td>" +\
                   "<td>"+display_member_obj.father_name+"</td>"+\
                   "<td>"+mother_name+"</td>" + \
                   "<td>" + career + "</td>"

    if display_member_obj.descent_no > 14:
        content = content + "<td><a href='http://www.yinmahezhang.com/s_id?mid="+str(display_member_obj.member_id)+"'>"+"查看"+"</a></td>"
    else:
        content = content + "<td>  </td>"

    content = content + "</tr>"
    return content 

def get_table_content(display_member_list):
    content = '''<html>
                      <table border=1 width=100% align=center>
		          <tr bgcolor='#C2C2C2'>
                            <td>世代号</td>
                            <td>名字</td>
                            <td>性别</td>
                            <td>排行</td>
                            <td>配偶</td>
                            <td>父亲</td>
                            <td>母亲</td>
                            <td>功名职业</td>
                            <td>上下世</td>
                        </tr>
                  '''
    cnt = 0
    for display_member_obj in display_member_list:
        if display_member_obj is None:
            continue
        row_content = format_info(display_member_obj)
        content += row_content
        cnt += 1
    
    content += "<h3>共查询到 "+ str(cnt) + " 条记录，若数据有遗漏或错误，请直接通过公众号进行反馈，在输入反馈内容之前请务必输入冒号(:)</h3></table></html>"
    return content
