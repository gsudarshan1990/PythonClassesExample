class Player:
    def __init__(self,username,rank,id_num,time_period):
        self.username = username
        self._rank =rank
        self.__id_num = id_num
        self.__time_period = time_period

P1 = Player("rahul",100,123,1423)
print(P1.username)
print(P1._rank)
print(P1._Player__time_period)
print(P1._Player__id_num)