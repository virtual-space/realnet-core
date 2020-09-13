from abc import ABC, abstractmethod

# lambda x, y: x ** y
class Transform(ABC):

    def __init__(self, function=(lambda *args, **kwargs: args)):
        self.function = function

    def map(self, function):
        return Transform((lambda x: function(x)))

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)