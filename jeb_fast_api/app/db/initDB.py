def init_db(db_session):
    from app.db.base import Base, engine
    Base.metadata.create_all(bind=engine)

    # user = db_session.query(User).filter(User.id == 1).first()
    print("test", type(db_session), db_session)
    pass


if __name__ == '__main__':
    pass