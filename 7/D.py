class king_lion():
    def __init__(self):
        self._x = 47

    def get_x (self):
        return self._x

    def del_x (self):
        pass
    
    def set_x(self, value):
        if type(value) == int:
            self._x = value
            if value < -100 or value > 100:
                self._x = 0

    x = property(get_x, set_x, del_x)