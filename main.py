from src import create_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = 'root'
password = 'root12345'
host = 'localhost'
port = 3306
db_name = "redbus"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}",echo=True)
with engine.connect() as conn:
    conn.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    
    
Session = sessionmaker(bind=engine)

if __name__ =='__main__':
    create_app.run(debug=True)