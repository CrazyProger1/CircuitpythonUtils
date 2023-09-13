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


d = TestEnum.D

print(d in TestEnum.values)  # True
print(len(TestEnum.values))  # 4
print(TestEnum.D)  # <TestEnum.D: 4>

for value in TestEnum.values:
    print(value)
# <TestEnum.A: 1>
# <TestEnum.B: 2>
# <TestEnum.C: 3>
# <TestEnum.D: 4>

print(TestEnum('A'))  # <TestEnum.A: 1>

print(list(TestEnum.values))  # [<TestEnum.A: 1>, <TestEnum.B: 2>, <TestEnum.C: 3>, <TestEnum.D: 4>]

print(3 in TestEnum.values)  # True

print(TestEnum.B.name)  # B
print(TestEnum.B.value)  # 2

print(TestEnum2.B in TestEnum.values)  # False
