class Shape():
    def __init__(self, n):
        self.name=n
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        self.__name = n