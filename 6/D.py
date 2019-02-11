class ShiftableList(list):
    # def __init__(self, list):
    #     super().__init__(list)
    #     self.list = list
    def checkInt(self, val):
        if type(val) != int:
            raise TypeError('Wrong input value')
    def shift(self, shift, dir = 'left'):
        shf = shift % self.__len__()
        lst = self.copy()
        for _ in range(shf):
            if dir == 'left':
                lst.append(lst.pop(0))
            else:
                lst.insert(0, lst.pop(-1))
        return lst
    def __rshift__(self, shift):
        self.checkInt(shift)
        if shift < 0:
            return self.__lshift__(abs(shift))
        else:
            return self.shift(shift, dir = 'right')
            
    def __lshift__(self, shift):
        self.checkInt(shift)
        if shift < 0:
            return self.__rshift__(abs(shift))
        else:
            return self.shift(shift, dir = 'left')