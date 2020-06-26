class ElectronicDevice:
    def __init__(self,switch,in_built_stabiliser):
        self.switch = switch
        self.in_built_stabilizer = in_built_stabiliser


class Computer(ElectronicDevice):
    def __init__(self,switch,in_built_stabiliser,screen_type):
        ElectronicDevice.__init__(self,switch,in_built_stabiliser)
        self.screen_type = screen_type

class TV(ElectronicDevice):
    def __init__(self,switch,in_built_stabilizer,mode_of_input):
        super().__init__(switch,in_built_stabilizer)
        self.mode_of_input =mode_of_input

class Laptop(Computer):
    def __init__(self,switch,in_built_stabilizer,screen_type,laptop_brand):
        Computer.__init__(self,switch,in_built_stabilizer,screen_type)
        self.laptop_brand = laptop_brand

class Desktop(Computer):
    def __init__(self,switch,in_built_stabilizer,screen_type,mother_board_type):
        Computer.__init__(self,switch,in_built_stabilizer,screen_type)
        self.mother_board_type = mother_board_type


d1=Desktop("Indian","yes","OLED","NVIDIA")
l1=Laptop("USA","No","LED","AMD")
