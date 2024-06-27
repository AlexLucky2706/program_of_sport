from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, JSON, Integer, String, ForeignKey, Boolean
from database import Base
# from program.models import Program
# # Смешная история что раз я здесь импортировал это то alembic отсюда и создает таблицы поэтому дальше в самих папках с models приходится везде писать extend_existing=True типо уже создана таблица
# from result.models import Result
# # Смешная история что раз я здесь импортировал это то alembic отсюда и создает таблицы поэтому дальше в самих папках с models приходится везде писать extend_existing=True типо уже создана таблица

class Person(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    family = Column(String)
    age = Column(Integer)
    email = Column(String)
    program = Column(Integer, ForeignKey("program.id"))
    result = Column(Integer, ForeignKey("result.id"))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
