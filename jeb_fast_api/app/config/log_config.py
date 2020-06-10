# @Version: V1.0
# @Author: wevsmy
# @License: Apache Licence
# @Contact: wevsmy@gmail.com
# @Site: https://blog.weii.ink
# @Software: PyCharm
# @File: log_config.py
# @Time: 2020/6/10 下午4:31

import logging.config
import os

from app.config.settings import PROJECT_NAME, LOG_PATH

# 记录文件日志输出的格式
standard_format = '%(asctime)s - %(threadName)s - %(name)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'  # 其中name为getlogger指定的名字
# 终端日志输出的格式
simple_format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s'

logfile_dir = LOG_PATH

logfile_name = PROJECT_NAME + '.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.makedirs(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，['default', 'console'],即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}


def GetLogger(name=None):
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    return logging.getLogger(name)


# logger = logging.getLogger("fastapi")

if __name__ == '__main__':
    logger = GetLogger(__name__)  # 生成一个log实例
    logger.info('info message')
    logger.debug('debug message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
