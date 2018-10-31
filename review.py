class Review:

    _all = []

    def __init__(self, guest):
        self._guest = guest
        Review._all.append(self)

    @property
    def guest(self):
        return self._guest

    @guest.setter
    def guest(self, arg):
        self._guest = arg
    

    @classmethod
    def all(cls):
        return cls._all 