class Recipe:

    _all = []

    def __init__(self):
        Recipe._all.append(self)

    @classmethod
    def all(cls):
        return cls._all