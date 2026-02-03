from sqlalchemy import column, Integer , String, Boolean, DateTime, Enum, Date
from sqlalchemy.orm import relationship
from configure.db import Base

class User(Base):
    __tablename__ = "tbb_usuarios"
    Id = column(Integer, primary_key=True, index=True)
    Rol_Id = column(Integer,foreignkey="tbc_roles.Id")