from utils.cache import cache


class TestClass:
    pass


class TestClass2:
    pass


class Singleton:
    @cache
    def __new__(cls, *args, **kwargs):
        return super(Singleton, cls).__new__(cls, *args, **kwargs)


@cache
def get_single_instance(cls, *args, **kwargs):
    return cls(*args, **kwargs)


print(get_single_instance(TestClass) is get_single_instance(TestClass))  # True
print(get_single_instance(TestClass) is get_single_instance(TestClass2))  # False
print(Singleton() is Singleton())  # True
