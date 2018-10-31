class Review:

    _all = []

    def __init__(self, reviewer, recipe, rating, comment = None):
        self._reviewer = reviewer
        self._recipe = recipe
        self._rating = rating
        self._comment = comment
        Review._all.append(self)

    @property
    def reviewer(self):
        return self._reviewer

    @reviewer.setter
    def reviewer(self, arg):
        self._reviewer = arg

    @property
    def recipe(self):
        return self._recipe
    
    @recipe.setter
    def recipe(self, arg):
        self._recipe = arg

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, arg):
        self._rating = arg

    @property
    def comment(self):
        return self._comment
    
    @comment.setter
    def comment(self, arg):
        self._comment = arg

    @classmethod
    def all(cls):
        return cls._all 