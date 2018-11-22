# -*- coding:utf-8 -*-
# Author Koctr


import logging
from conf import settings


def log(log_type):
    """
    写日志函数
    :param log_type: 日志类型 
    :return: 根据类型生成的logging对象
    """

    # 控制台输出handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(settings.LOG_LEVEL)

    # 文件输入handler
    log_file = '%s/logs/%s' % (settings.BASE_DIR, settings.LOG_TYPES[log_type])
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(settings.LOG_LEVEL)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
