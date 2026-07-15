import logging
import os

os.makedirs('logs', exist_ok=True)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename='logs/app.log')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')


