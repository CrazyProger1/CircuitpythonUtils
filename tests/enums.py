import unittest
from utils import enums


@enums.enum(int)
class TestIntEnum:
    A: int
    B: int = 1
    C: int = 2
    D: int


@enums.enum(int)
class TestIntEnum2:
    A: int
    B: int = 1
    C: int = 2
    D: int


@enums.enum(str)
class TestStringEnum:
    a = 'abc'
    b = 'cba'


@enums.enum(str)
class TestStringEnum2:
    a = 'abc'
    b = 'cba'


class TestEnums(unittest.TestCase):
    def test_int_enums(self):
        self.assertIs(TestIntEnum.D, TestIntEnum('D'))
        self.assertNotEqual(TestIntEnum.A, TestIntEnum2.A)
        self.assertEqual(TestIntEnum.C, 2)
        self.assertEqual(TestIntEnum.C, TestIntEnum.C.value)
        self.assertIn(TestIntEnum.C, TestIntEnum.values)
        self.assertNotIn(TestIntEnum.C, TestIntEnum2.values)

    def test_str_enums(self):
        self.assertIs(TestStringEnum.a, TestStringEnum('a'))
        self.assertNotEqual(TestStringEnum.a, TestStringEnum2.a)
        self.assertEqual(TestStringEnum.a, 'abc')
        self.assertEqual(TestStringEnum.b, TestStringEnum.b.value)
        self.assertIn(TestStringEnum.b, TestStringEnum.values)
        self.assertNotIn(TestStringEnum.a, TestStringEnum2.values)


if __name__ == '__main__':
    unittest.main()
