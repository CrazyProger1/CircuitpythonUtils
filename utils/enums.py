"""Circuitpython enums implementations."""


class Value:
    def __init__(self, value, name: str, enum_name: str):
        self.datatype = type(value)
        self.value = value
        self.name = name
        self.enum_name = enum_name

    def __eq__(self, other):
        return self.value == other

    def __str__(self):
        return f'<{self.enum_name}.{self.name}: {self.value}>'


class Enum:
    fields: dict


def enum(cls):
    mro = cls.mro()
    datatype = mro[1]

    if datatype is object:
        datatype = int
    elif not issubclass(datatype, (str, int)):
        raise TypeError(f'Enum must inherit int or str, not {datatype}')

    attrs = {}

    for field, value in cls.__dict__.items():
        print(field, value)
        if isinstance(value, datatype):
            attrs.update({field: Value(
                value=value,
                name=field,
                enum_name=cls.__name__)
            })

    new_cls = type(cls.__name__, (Enum,), attrs)
    return new_cls
