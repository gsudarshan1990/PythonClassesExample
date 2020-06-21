class Patient:
    def __init__(self,name,age,id_num,num_children=0):
        self.name = name
        self.age =age
        self._id_num = id_num
        self._num_children = num_children
    @property
    def id_num(self):
        return self._id_num

    @id_num.setter
    def id_num(self,new_id_num):
        if isinstance(new_id_num,str):
            self._id_num = new_id_num
        else:
            print('Enter the appropriate value')
    @property
    def num_children(self):
        return self._num_children

    @num_children.setter
    def num_children(self,new_num_children):
        if isinstance(new_num_children,int):
            self._num_children = new_num_children
        else:
            print('Enter the digit')

p1=Patient('sonu',30,'abcdef')
print(p1.age)
print(p1.id_num)
p1.id_num='bcdef'
print(p1.id_num)
print(p1.num_children)