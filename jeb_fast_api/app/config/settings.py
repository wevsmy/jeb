# @Version: V1.0
# @Author: wevsmy
# @License: Apache Licence
# @Contact: wevsmy@gmail.com
# @Site: https://blog.weii.ink
# @Software: PyCharm
# @File: settings.py
# @Time: 2020/6/10 下午4:31
from os.path import abspath, dirname, join

from starlette.config import Config
from starlette.datastructures import Secret, URL

config = Config(".env")

PROJECT_NAME = config('PROJECT_NAME', cast=str, default="jeb_project")
PROJECT_DESCRIPTION = config('PROJECT_DESCRIPTION', cast=str, default="jeb_project")
PROJECT_PATH = dirname(dirname(dirname(abspath(__file__))))  # ~/jeb_fast_api
# ex PROJECT_STATIC_PATH = ~/jeb_fast_api/app/static
PROJECT_STATIC_PATH = join(PROJECT_PATH, "app/static")

DEBUG = config('DEBUG', cast=bool, default=False)
TESTING = config('TESTING', cast=bool, default=False)
LOG_PATH = join(PROJECT_PATH, "log")  # log文件的目录
SECRET_KEY = config('SECRET_KEY', cast=Secret, default="as24asz4")

# 生产环境域名
DOMAIN = config('DOMAIN', cast=str, default="http://127.0.0.1")

# mysql
MYSQL_HOST = config('MYSQL_HOST', cast=str, default="localhost")
MYSQL_PORT = config('MYSQL_PORT', cast=str, default="3306")
MYSQL_USER = config('MYSQL_USER', cast=str, default="user")
MYSQL_PASSWORD = config('MYSQL_PASSWORD', cast=str, default="password")
MYSQL_DB = config('MYSQL_DB', cast=str, default="db")

_default_database_url = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

DATABASE_URL: URL = config('DATABASE_URL', cast=URL, default=_default_database_url)

if TESTING:
    DATABASE_URL: URL = DATABASE_URL.replace(path='test_' + DATABASE_URL.path.split("/")[1])

# redis
# redis 0 号为默认库
# redis 1 号为短链接映射库
REDIS_HOST = config('REDIS_HOST', cast=str, default="localhost")
REDIS_PORT = config('REDIS_PORT', cast=int, default=6379)
REDIS_PASSWORD = config('REDIS_PASSWORD', default=None)
REDIS_DB = config('REDIS_DB', cast=int, default=0)
REDIS_SHORT_URL_DB = config('REDIS_SHORT_URL_DB', cast=int, default=1)

# 微信公众号配置
WX_PUBLIC_TOKEN = config('WX_PUBLIC_TOKEN', cast=str, default="token")
WX_PUBLIC_APP_ID = config('WX_PUBLIC_APP_ID', cast=str, default="id")
WX_PUBLIC_APP_SECRET = config('WX_PUBLIC_APP_SECRET', cast=str, default="secret")

# SMS
SMS_USER = config('SMS_USER', cast=str, default="")
SMS_PASSWORD = config('SMS_PASSWORD', cast=str, default="")

if __name__ == '__main__':
    pass
