from abc import ABC, abstractmethod


class Stream(ABC):

    @abstractmethod
    def map(self, object, function):
        pass

