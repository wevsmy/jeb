# @Version: V1.0
# @Author: wevsmy
# @License: Apache Licence
# @Contact: wevsmy@gmail.com
# @Site: https://blog.weii.ink
# @Software: PyCharm
# @File: api.py
# @Time: 2020/6/10 下午4:31
from fastapi import APIRouter

from app.config.log_config import GetLogger

logger = GetLogger(__name__)  # 生成一个log实例

api_router = APIRouter()


@api_router.get("/")
async def index():
    return "test"


if __name__ == '__main__':
    pass
