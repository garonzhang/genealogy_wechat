class Member:
    def __init__(self,
            member_id, 
            member_name, 
            descent_no, 
            father_id, 
            sex, 
            sort_order, 
            spouse_name,
            mother_name):
        self.member_id = member_id
        self.member_name = member_name
        self.descent_no = descent_no
        self.father_id = father_id
        self.sex = sex
        self.sort_order = sort_order 
        self.spouse_name = spouse_name
        self.mother_name = mother_name


class DisplayMember(Member):
    def __init__(self,
            member_id, 
            member_name, 
            descent_no, 
            father_id, 
            sex, 
            sort_order, 
            spouse_name, 
            father_name, 
            mother_name):
        Member.__init__(self,member_id, member_name, descent_no, father_id, sex, sort_order, spouse_name)
        self.father_name = father_name
        self.mother_name = mother_name

