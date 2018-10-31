class DinnerParty:

    _all = []

    def __init__(self):
        DinnerParty._all.append(self)

    @classmethod
    def all(cls):
        return cls._all
