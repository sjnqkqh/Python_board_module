from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base, engine


class User(Base):
    __tablename__ = "TB_USER"
    __table_name__ = "TB_USER"

    USER_ID = Column(Integer, primary_key=True, index=True)
    NICKNAME = Column(String(40), nullable=True)

    posts = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__ = "TB_BOARD"
    __table_name__ = "TB_BOARD"

    POST_ID = Column(Integer, primary_key=True, index=True)
    USER_ID = Column(Integer, ForeignKey("TB_USER.USER_ID"))
    TITLE = Column(String(255), index=True)
    CONTENT = Column(String(100), index=True)

    author = relationship("User", back_populates="posts")


User.__table__.create(bind=engine, checkfirst=True)
Post.__table__.create(bind=engine, checkfirst=True)
