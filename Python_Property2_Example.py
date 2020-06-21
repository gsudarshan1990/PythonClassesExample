class Patient:
    def __init__(self,name,age,id_num,num_children=0):
        self.name = name
        self.age = age
        self._id_num =id_num
        self._num_childern = num_children

    def get_id_num(self):
        return self._id_num

    def set_id_num(self,new_id):
        if isinstance(new_id,str):
            self._id_num = new_id
        else:
            print("Enter the valid string")
    id_num=property(get_id_num,set_id_num)

    def get_num_children(self):
        return self._num_childern

    def set_num_children(self,new_num_children):
        if isinstance(new_num_children,int):
            self._num_childern=new_num_children
        else:
            print("Enter the valid integer")
    num_children=property(get_num_children,set_num_children)

p1=Patient('sonu',30,'3535')
print(p1.id_num)
print(p1.num_children)
p1.id_num='abcdef'
p1.num_children=2
print(p1.id_num)
print(p1.num_children)