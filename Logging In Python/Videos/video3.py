import logging

#Logging settings
logging.basicConfig(
    
    level=logging.DEBUG,
    format='%(asctime)s -%(name)s -%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('Math.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('MathsTool')

def Add(a,b):
    result = a+b
    logger.debug(f'Addition of {a} + {b} = {result}')
    
    return result

Add(2,3)



