from utils.enums import enum


@enum
class TestEnum(int):
    A = 1
    B = 2
    C = 3
    D: int


@enum
class TestEnum2(int):
    A = 1
    B = 2
    C = 3
    D: int


print(TestEnum.D)
