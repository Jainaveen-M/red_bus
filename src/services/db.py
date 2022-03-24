from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import sessionmaker

username = 'root'
password = 'root12345'
host = 'localhost'
port = 3306
db_name = "redbus"
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}",echo=True)
    
Session = sessionmaker(bind=engine)
Inspect= sqlalchemy.inspect(engine)
if __name__ =='__main__':
    from src import create_app
    create_app.run(debug=True)
    