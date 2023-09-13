import unittest
from utils import cache


@cache.cache
def test(*args, **kwargs):
    return dict({1: 1})


class TestCache(unittest.TestCase):
    def test_cache_decorator(self):
        self.assertIs(test(), test())
        self.assertIs(test('abc'), test('abc'))
        self.assertIs(test('abc', test=123), test('abc', test=123))

    def test_clear_cache(self):
        result = test('abc')
        cache.clear_cache(test)
        result2 = test('abc')
        self.assertIsNot(result, result2)


if __name__ == '__main__':
    unittest.main()
