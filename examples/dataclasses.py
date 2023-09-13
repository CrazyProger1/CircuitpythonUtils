from utils.dataclasses import dataclass, Field


@dataclass
class TestDataclass:
    name = Field(str)

    def __post_init__(self):
        print('abc')

    @property
    def nm(self):
        return self.name


test = TestDataclass(name='hello')  # abc
print(test)  # TestDataclass<name=hello>

print(test.asdict())  # {'name': 'hello'}

print(test.nm)  # hello

test2 = TestDataclass()
# utils.exceptions.ValidationError: Field name of schema TestDataclass can't be null
