from abc import ABC, abstractmethod


class ItemStore(ABC):

    @abstractmethod
    def create_item(self, type, name=None, attributes=None):
        pass

    @abstractmethod
    def retrieve_item(self, id):
        pass

    @abstractmethod
    def update_item(self, item):
        pass

    @abstractmethod
    def delete_item(self, id):
        pass

    @abstractmethod
    def find_items(self, query, cursor):
        pass
