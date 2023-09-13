"""Dataclasses implementation based on schemas"""

from utils.schemas import Field, Schema


class Dataclass(Schema):
    def __init__(self, **data):
        super(Dataclass, self).__init__(**data)

        self.__post_init__()

    def __post_init__(self):
        pass

    def asdict(self):
        return self.model_dump()


def dataclass(cls):
    attrs = dict(cls.__dict__)
    fields_to_ignore = {'__dict__', }

    for field in fields_to_ignore:
        attrs.pop(field)

    return type(cls.__name__, (Dataclass,), attrs)
