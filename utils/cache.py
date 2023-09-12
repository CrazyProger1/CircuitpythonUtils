def cache(func):
    result_cache = {}

    def wrapper(*args, **kwargs):
        nonlocal result_cache
        key = (func, args, frozenset(kwargs.items()))

        if key in result_cache:
            return result_cache[key]

        result = func(*args, **kwargs)

        result_cache[key] = result

        return result

    return wrapper


