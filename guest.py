class Guest:

    _all = []

    def __init__(self, name):
        self._name = name
        Guest._all.append(self)

    # @classmethod
    # def most_popular(cls):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, arg):
        self._name = arg

    @classmethod
    def all(cls):
        return cls._all