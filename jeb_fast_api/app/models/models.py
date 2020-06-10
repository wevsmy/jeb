# 数据库模型
from datetime import datetime

from sqlalchemy import Column

from app.db.base import Base


# 前端传来的数据表,作为用户表
class User(Base):
    id = Column(Integer, primary_key=True, index=True)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now, default=datetime.now)


if __name__ == '__main__':
    pass
