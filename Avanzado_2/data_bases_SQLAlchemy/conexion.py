from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

nombre_db = "Avanzado_2/data_bases_SQLAlchemy/empleados.sqlite"
engine = create_engine(f"sqlite:///{nombre_db}")
Session = sessionmaker(bind=engine)
session = Session()

ModeloBase = declarative_base()

