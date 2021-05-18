class Student:
    def __init__(self, value):
        self._name = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass


a = Student("first")
print(a.name)
a.name = "second"  #无法成功，因为setter方法没有任何操作
print(a.name)
