import json


class Type:

    def __init__(self, id, name, attributes=None):
        self.id = id
        self.name = name
        self.attributes = attributes

    def to_dict(self):
        attrs = {}
        if self.attributes
        return {'id': self.id, 'name': self.name, 'attributes': self.attributes if isinstance(self.attributes, dict) else self.attributes.to_dict()}

    def to_json(self):
        t = {'id': self.id, 'type': '', 'name': self.name}
        return json.dumps(self)

    @classmethod
    def from_dict(cls, data):
        t = json.loads(data)
        return Type(t.id, t.name, t.attributes)

    @classmethod
    def from_json(cls, data):
        t = json.loads(data)
        return Type(t.id, t.name, t.attributes)
