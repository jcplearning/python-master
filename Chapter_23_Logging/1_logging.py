import logging
import os
import uuid 

os.makedirs('logs', exist_ok=True)

file = 'logs\\' + os.path.basename(__file__) + '_' +str(uuid.uuid1()) + '.log'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename=file)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')


