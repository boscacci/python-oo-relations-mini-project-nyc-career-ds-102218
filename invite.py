class Invite:

    _all = []

    def __init__(self, guest, dinner_party):
        self._guest = guest
        self._dinner_party = dinner_party
        self._accepted = None
        Invite._all.append(self)

    @property
    def guest(self):
        return self._guest

    @guest.setter
    def guest(self, arg):
        self._guest = arg

    @property
    def dinner_party(self):
        return self._dinner_party

    @dinner_party.setter
    def dinner_party(self, arg):
        self._dinner_party = arg

    @property
    def accepted(self):
        return self._accepted
    
    @accepted.setter
    def accepted(self, arg):
        self._accepted = arg

    @classmethod
    def all(cls):
        return cls._all