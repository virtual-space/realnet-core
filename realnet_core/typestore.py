from abc import ABC, abstractmethod


class TypeStore(ABC):

    @abstractmethod
    def create_type(self, name, items=None, data=None, attributes=None):
        pass

    @abstractmethod
    def retrieve_type(self, id):
        pass

    @abstractmethod
    def update_type(self, type):
        pass

    @abstractmethod
    def delete_type(self, id):
        pass

    @abstractmethod
    def find_types(self, query, cursor):
        pass
