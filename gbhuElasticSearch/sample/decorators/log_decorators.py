from loguru import logger
from functools import wraps
def log(message=None):
    """
    装饰器工厂，接收一个前缀参数，并返回一个装饰器。
    """
    def decorator(func):
        """
        装饰器，接收一个函数作为参数，并返回一个新的函数。
        """
        def wrapper(*args, **kwargs):
            """
            包装函数，在被装饰函数执行前后添加逻辑。
            """
            logger.success(func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator