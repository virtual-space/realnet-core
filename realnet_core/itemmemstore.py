from .type import Type
from .item import Item
from .itemstore import ItemStore

import uuid


class ItemMemStore(ItemStore):

    def __init__(self):
        self.types = {}
        self.items = {}
        self.data = {}

    def create_type(self, name, items=None, data=None, attributes=None):
        references = []
        if items:
            references = [existing for existing in [self.items.get(item.id) for item in items] if existing]
        id = uuid.uuid4()
        new = Type(id, name, references, attributes)
        self.types[id] = new
        return new

    def retrieve_type(self, id):
        return self.types.get(id)

    def update_type(self, type):

        if type is None:
            return None

        self.types[type.id] = type
        return type

    def delete_type(self, id):
        return self.types.pop(id)

    def find_types(self, query, cursor):
        return None

    def create_item(self, type, name=None, attributes=None):

        if type is None:
            return None

        id = uuid.uuid4()
        new = Item(id, name if name else type.name, type, attributes)
        self.items[id] = new

        return new

    def retrieve_item(self, id):
        return self.items.get(id)

    def update_item(self, item):
        if item is None:
            return None

        self.items[item.id] = item

        return item

    def delete_item(self, id):
        return self.items.pop(id)

    def find_items(self, query, cursor):
        return None

