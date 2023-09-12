from utils.cache import cache


class TestClass:
    def __init__(self, arg=1):
        pass


class TestClass2:
    pass


@cache
def get_instance(cls, *args, **kwargs):
    return cls(*args, **kwargs)


@cache
def func():
    print('Call')


print(get_instance(TestClass) is get_instance(TestClass))  # True
print(get_instance(TestClass) is get_instance(TestClass2))  # False
print(get_instance(TestClass, 2) is get_instance(TestClass))  # False
print(get_instance(TestClass, 3) is get_instance(TestClass, 3))  # True

func()  # Call
func()  # Nothing
