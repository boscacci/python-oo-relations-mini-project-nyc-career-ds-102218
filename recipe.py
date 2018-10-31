class Recipe:

    _all = []

    def __init__(self, description):
        self._description = description
        Recipe._all.append(self)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, arg):
        self._description = arg
    
    @classmethod
    def all(cls):
        return cls._all