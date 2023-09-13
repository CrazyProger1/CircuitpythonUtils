from utils.enums import enum


@enum(int)
class TestEnum:
    A = 1
    B = 2
    C = 3
    D: int


@enum(int)
class TestEnum2:
    A = 1
    B = 2
    C = 3
    D: int

    @classmethod
    def get_d(cls):
        return cls.D


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

print(TestEnum2.get_d())  # <TestEnum2.D: 4>
