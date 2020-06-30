__all__ = ['cached']


import collections
import inspect
from decorator import decorator

results = collections.defaultdict(dict)


def cached(function):
    """`@cache` decorator, `cache(function)` - cache function result"""
    if not inspect.isfunction(function):
        err = "@cached requires function"
        raise TypeError(err)

    def wrapper(f, *args, **kwargs):
        key = str(args) + str(kwargs)
        funcresults = results[f]
        if key in funcresults:
            return funcresults[key]
        result = f(*args, **kwargs)
        results[f][key] = result
        return result
    return decorator(wrapper, function)
