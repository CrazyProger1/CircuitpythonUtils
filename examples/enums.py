from utils.enums import enum


@enum
class TestEnum(int):
    A = 1
    B = 2
    C = 3
    D: int


print(TestEnum.__dict__)
print(TestEnum.B)
