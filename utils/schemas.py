from utils.cache import cache
from utils.exceptions import ValidationError


class Field:
    def __init__(self, datatype: type, default=None, nullable=False):
        self.datatype = datatype
        self.default = default
        self.nullable = nullable


class Schema:

    @classmethod
    @cache
    def fields(cls) -> dict:
        result = {}

        for name, value in cls.__dict__.items():
            if isinstance(value, Field):
                result.update({name: value})

        return result

    @classmethod
    def validate(cls, obj: dict):
        for field, field_type in cls.fields().items():
            value = obj.get(field, field_type.default)
            datatype = field_type.datatype

            if isinstance(value, dict) and issubclass(datatype, Schema):
                datatype.validate(value)
            elif value is None and not field_type.nullable:
                raise ValidationError(f"Field {field} of schema {cls.__name__} can't be null")
            elif value and not isinstance(value, datatype):
                raise ValidationError(
                    f"Field {field} of schema {cls.__name__} must be type of {datatype}, not {type(value)}"
                )

    def model_dump(self) -> dict:
        self.validate(obj=self.__dict__)

        result = {}

        for field, field_type in self.fields().items():
            value = getattr(self, field, field_type.default)

            if isinstance(value, Schema):
                value = value.model_dump()

            result.update({field: value})

        return result

    @classmethod
    def model_validate(cls, obj: dict) -> "Schema":
        cls.validate(obj=obj)

        instance = cls()

        for field, field_type in cls.fields().items():
            value = obj.get(field, field_type.default)

            if issubclass(field_type.datatype, Schema) and isinstance(value, dict):
                value = field_type.datatype.model_validate(value)

            setattr(instance, field, value)

        return instance

    def __str__(self):
        field_values_string = ' '.join(field + '=' + str(value) for field, value in self.__dict__.items())
        return f'{self.__class__.__name__}<{field_values_string}>'
