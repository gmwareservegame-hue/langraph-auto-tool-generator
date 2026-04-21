import logging

logger = logging.getLogger(__name__)

def log_block(name: str, n: int = 12):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.debug(f"{'-' * n}{name}{'-' * n}")
            result = func(*args, **kwargs)
            logger.debug(f"{'-' * n}END_{name}{'-' * n}")
            return result
        return wrapper
    return decorator