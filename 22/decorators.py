from functools import wraps


def make_html(element):
    def decorator_function(func):
        def wrapper_function(*args, **kwargs):
            return f'<{element}>{func(*args, **kwargs)}</{element}>'
        return wrapper_function
    return decorator_function
            