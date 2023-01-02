import json


class User:
    def __init__(self, **kwargs):
        self.__id = '2' if 'id' not in kwargs.keys() else kwargs['id']
        self.__email = 'janet.weaver@reqres.in' if 'email' not in kwargs.keys() else kwargs['email']
        self.__first_name = 'Janet' if 'first_name' not in kwargs.keys() else kwargs['first_name']
        self.__last_name = 'Weaver' if 'last_name' not in kwargs.keys() else kwargs['last_name']

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_dict(self):
        return self.__dict__

    def update_dict(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_json(self):
        return json.dumps(self.__dict__)
