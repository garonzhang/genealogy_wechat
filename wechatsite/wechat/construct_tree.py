from queue import Queue
from . import member_opt as mo 

# to get the ancestors of current member
def get_ancestors(display_member_obj, display_member_list):
    if display_member_obj is None:
        print ("display_member_obj is None in get_ancestors()")
        return
    display_member_list.insert(0, display_member_obj)
    while True:
        display_member_obj = display_member_list.pop(0)
        father_id = display_member_obj.father_id
        if father_id is None or father_id == "":
            display_member_list.insert(0, display_member_obj) 
            break 
        father_member_obj = mo.get_display_member(father_id) 
        if father_member_obj is None:
            display_member_list.insert(0, display_member_obj) 
            break 
        
        son_display_member_list = mo.get_sons(father_id)
        if son_display_member_list == []:
            continue

        for display_member in list(reversed(son_display_member_list)):
            display_member_list.insert(0,display_member) 
        display_member_list.insert(0, father_member_obj) 
      

# to get the descendants of current member
def get_descendants(display_member_obj, display_member_list):
    if display_member_obj is None:
        return

    display_member_queue = Queue()
    display_member_queue.put(display_member_obj)

    is_current_node = True
    while not display_member_queue.empty():
        display_member_obj = display_member_queue.get()
        if is_current_node == True:
            is_current_node = False
        else:
            display_member_list.append(display_member_obj)

        son_display_member_list = mo.get_sons(display_member_obj.member_id)
        if son_display_member_list == []:
            continue

        for display_member in son_display_member_list:
            display_member_queue.put(display_member) 
   
    
def get_tree_nodes(display_member_obj):
    display_member_list = []

    get_ancestors(display_member_obj, display_member_list)
    get_descendants(display_member_obj, display_member_list)
    
    return display_member_list
