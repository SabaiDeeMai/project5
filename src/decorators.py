import functools
import logging


def log(filename=None):
    """Автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки."""
    def decorator(func):
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            logger.handlers.clear()

        if filename:
            handler = logging.FileHandler(filename, encoding='utf-8')
        else:
            handler = logging.StreamHandler()

        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__} Inputs: {args}, kwargs={kwargs}")
                raise

        return wrapper
    return decorator
