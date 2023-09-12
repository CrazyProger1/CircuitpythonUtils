"""Circuitpython lightweight Pydantic implementation."""

from utils.cache import cache
from utils.exceptions import ValidationError


class Field:
    def __init__(self, datatype: type, default=None, nullable: bool = False):
        self.datatype = datatype
        self.default = default
        self.nullable = nullable


class Schema:
    def __init__(self, **data):
        cls = self.__class__

        annotations = cls.__dict__.get('__annotations__')

        if annotations:
            for field, ant in annotations.items():
                default_val = getattr(self, field, None)

                if isinstance(default_val, Field):
                    continue

                setattr(cls, field, Field(ant, default=default_val, nullable=default_val is not None))

        for field, field_type in self.get_fields().items():
            value = data.get(field, field_type.default)

            self.validate_field(
                name=field,
                field_type=field_type,
                value=value
            )

            if issubclass(field_type.datatype, Schema) and isinstance(value, dict):
                value = field_type.datatype.model_validate(value)

            setattr(self, field, value)

    @classmethod
    @cache
    def get_fields(cls) -> dict:
        result = {}

        for name, value in cls.__dict__.items():
            if isinstance(value, Field):
                result.update({name: value})

        return result

    @classmethod
    def validate_field(cls, name: str, field_type: Field, value):
        datatype = field_type.datatype

        if isinstance(value, dict) and issubclass(datatype, Schema):
            datatype.validate(value)
        elif value is None and not field_type.nullable:
            raise ValidationError(f"Field {name} of schema {cls.__name__} can't be null")
        elif value and not isinstance(value, datatype):
            raise ValidationError(
                f"Field {name} of schema {cls.__name__} must be type of {datatype}, not {type(value)}"
            )

    @classmethod
    def validate(cls, obj: dict):
        for field, field_type in cls.get_fields().items():
            value = obj.get(field, field_type.default)
            cls.validate_field(field, field_type, value)

    def model_dump(self) -> dict:

        result = {}

        for field, field_type in self.get_fields().items():
            value = getattr(self, field, field_type.default)

            self.validate_field(
                name=field,
                field_type=field_type,
                value=value
            )

            if isinstance(value, Schema):
                value = value.model_dump()

            result.update({field: value})

        return result

    @classmethod
    def model_validate(cls, obj: dict) -> "Schema":
        instance = cls(**obj)
        return instance

    def __str__(self):
        field_values_string = ' '.join(field + '=' + str(value) for field, value in self.__dict__.items())
        return f'{self.__class__.__name__}<{field_values_string}>'
