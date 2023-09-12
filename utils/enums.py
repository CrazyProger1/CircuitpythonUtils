"""Circuitpython enums implementations."""


class Value:
    def __init__(self, value, name: str, enum_name: str):
        self.datatype = type(value)
        self.value = value
        self.name = name
        self.enum_name = enum_name

    def __eq__(self, other):
        if isinstance(other, self.datatype):
            return self.value == other
        elif isinstance(other, Value):
            return self is other

    def __str__(self):
        return f'<{self.enum_name}.{self.name}: {self.value}>'


class Enum:
    pass


def enum(cls):
    mro = cls.mro()
    datatype = mro[1]

    if datatype is object:
        datatype = int
    elif not issubclass(datatype, (str, int)):
        raise TypeError(f'Enum must inherit int or str, not {datatype}')

    attrs = {}

    values = set()

    for field, value in cls.__dict__.items():
        if isinstance(value, datatype):
            values.add(value)
            attrs.update({field: Value(
                value=value,
                name=field,
                enum_name=cls.__name__)
            })

    if datatype is int:
        annotations = cls.__dict__.get('__annotations__')
        if annotations:
            max_val = max(values)

            for field, ant in annotations.items():

                if field not in attrs and ant is int:
                    max_val += 1
                    attrs.update({field: Value(
                        value=max_val,
                        name=field,
                        enum_name=cls.__name__)
                    })
    new_cls = type(cls.__name__, (Enum,), attrs)
    return new_cls
