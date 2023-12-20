from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Получение значений из переменных окружения
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT', default=3306, cast=int)
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')

# Формирование строки подключения
db_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создание объекта Engine
engine = create_engine(db_url)

# Создание сессии
Session = sessionmaker(bind=engine)
LocalSession = Session()

Base = declarative_base()

# Зависимость для предоставления сессии
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
