import redis
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.config import settings


class CustomBase(object):
    # 自动生出成表名字
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


engine = create_engine(settings.DATABASE_URL.__str__(), pool_pre_ping=True)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base(cls=CustomBase)


# MySql Dependency
def Get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Redis
def RedisConn(db=settings.REDIS_DB):
    redis_Pool = redis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=db,
                                      password=settings.REDIS_PASSWORD)

    return redis.Redis(connection_pool=redis_Pool)


if __name__ == '__main__':
    pass
