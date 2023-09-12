"""Dataclasses implementation based on schemas"""

from utils.schemas import Field, Schema


def dataclass(cls):
    attrs = {}
    for field, field_type in cls.__dict__.items():
        if isinstance(field_type, Field):
            attrs.update({field: field_type})

    return type(cls.__name__, (Schema,), attrs)
