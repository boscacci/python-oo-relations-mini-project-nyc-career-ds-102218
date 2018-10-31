class DinnerParty:

    _all = []

    def __init__(self, courses):
        self._courses = courses
        DinnerParty._all.append(self)

    @property
    def course1(self):
        return self._course1
    
    @course1.setter
    def course1(self,arg):
        self._course1 = arg

    @property
    def course2(self):
        return self._course2
    
    @course2.setter
    def course2(self,arg):
        self._course2 = arg

    @property
    def course3(self):
        return self._course3
    
    @course3.setter
    def course3(self,arg):
        self._course3 = arg

    @classmethod
    def all(cls):
        return cls._all
