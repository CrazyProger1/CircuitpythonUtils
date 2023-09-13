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

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return f'<{self.enum_name}.{self.name}: {self.value}>'

    def __int__(self):
        return int(self.value)

    def __repr__(self):
        return str(self)


class Enum:
    values: frozenset

    def __new__(cls, *args, **kwargs):
        args_len = len(args)
        if args_len == 1:
            arg = args[0]

            return getattr(cls, arg, None)


def enum(datatype: type = int):
    if not issubclass(datatype, (str, int)):
        raise TypeError(f'Enum only supports int or str')

    def decorator(cls):
        nonlocal datatype

        attrs = {}

        values = set()
        field_to_ignore = {'__dict__', }
        int_values = set()

        for field, value in cls.__dict__.items():
            if field in field_to_ignore:
                continue

            if isinstance(value, datatype):
                int_values.add(value)
                val = Value(
                    value=value,
                    name=field,
                    enum_name=cls.__name__)

                attrs.update({field: val})
                values.add(val)
            else:
                attrs.update({field: value})

        if datatype is int:
            annotations = cls.__dict__.get('__annotations__')
            if annotations:
                max_val = max(int_values)

                for field, ant in annotations.items():

                    if field not in attrs and ant is int:
                        max_val += 1
                        val = Value(
                            value=max_val,
                            name=field,
                            enum_name=cls.__name__)
                        attrs.update({field: val})
                        values.add(val)

        attrs.update({'values': frozenset(values)})

        new_cls = type(cls.__name__, (Enum,), attrs)
        return new_cls

    return decorator


def int_enum(func):
    return enum(int)(func)


def str_enum(func):
    return enum(str)(func)
