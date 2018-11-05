import logging
import functools
logging.basicConfig(level=logging.INFO)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("i am beginning")
        func(*args, **kwargs)
        # func()
        logging.info('i am end')
    return wrapper


@log
def test(name):
    logging.info('my name is: %s ' % name)


test('tom')
print __name__
