"""Circuitpython cache implementations."""


def clear_cache(func):
    func(reset_cache=True)


def cache(func):
    """Cache decorator implementation."""

    result_cache = {}

    def wrapper(*args, **kwargs):
        nonlocal result_cache

        if kwargs.get('reset_cache'):
            result_cache.clear()
            return

        key = (func, args, frozenset(kwargs.items()))

        if key in result_cache:
            return result_cache[key]

        result = func(*args, **kwargs)

        result_cache[key] = result

        return result

    return wrapper
