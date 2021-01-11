"""
Copyright 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""

import logging, hashlib, os
from config import BASE_DIR

def hash_(string):
    return hashlib.sha1(string.encode()).hexdigest()

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def log(name, filename=None):
    # создаём logger
    logger = logging.getLogger(name)
    logger.setLevel( logging.DEBUG )

    # создаём консольный handler и задаём уровень
    if filename:
        ch = logging.FileHandler(os.path.join(  BASE_DIR, "Log" , filename ))
    else:
        ch = logging.StreamHandler()

    ch.setLevel(logging.DEBUG)

    # создаём formatter
    formatter = logging.Formatter('%(asctime)s : %(lineno)d : %(name)s : %(levelname)s : %(message)s')
    # %(lineno)d :
    # добавляем formatter в ch
    ch.setFormatter(formatter)

    # добавляем ch к logger
    logger.addHandler(ch)

    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warn('warn message')
    # logger.error('error message')
    # logger.critical('critical message')
    return logger