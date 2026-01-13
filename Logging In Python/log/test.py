
from logg import logging

def sub(a,b):
    logging.debug('Function (sub) is working')
    return a-b

logging.debug('Function(Sub) is executed')

sub(8,2)

