class Patient:
    def __init__(self,name,age,id_num,num_children=0):
        self.name = name
        self.age = age
        self._id_num = id_num
        self._num_children = num_children

    def get_id_num(self):
        return self._id_num

    def set_id_num(self,new_id):
        if isinstance(new_id,str):
            self._id_num=new_id
        else:
            print("Please enter the valid string")

    def get_num_children(self):
        return self._num_children

    def set_num_children(self,num_child):
        if isinstance(num_child,int) and 0<num_child<5:
            self._num_children=num_child
        else:
            print("Enter the valid number")

p1=Patient("sonu",29,"abc")
print(p1.get_id_num())
print(p1.get_num_children())

p1.set_id_num("cde")
p1.set_num_children(4)

print(p1.get_id_num())
print(p1.get_num_children())