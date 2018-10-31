class Course:

    _all = []

    def __init__(self, recipe):
        self._recipe = recipe
        Course._all.append(self)

    @property
    def recipe(self):
        return self._recipe

    @recipe.setter
    def recipe(self, arg):
        self._recipe = arg

    @classmethod
    def all(cls):
        return cls._all