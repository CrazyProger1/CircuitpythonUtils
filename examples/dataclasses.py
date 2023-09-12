from utils.dataclasses import dataclass, Field


@dataclass
class TestDataclass:
    name = Field(str)


test = TestDataclass(name='hello')
print(test)  # TestDataclass<name=hello>

test2 = TestDataclass()
# utils.exceptions.ValidationError: Field name of schema TestDataclass can't be null
