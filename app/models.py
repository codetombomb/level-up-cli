from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

fact_user = Table(
    'fact_users',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('fact_id', ForeignKey('facts.id'), primary_key=True),
    extend_existing=True,
)

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)

    facts = relationship("Fact", secondary=fact_user, back_populates='users')

    def __repr__(self):
        return f'<User id={self.id}, username={self.username}>'

class Fact(Base):

    __tablename__ = 'facts'

    id = Column(Integer(), primary_key=True)
    text = Column(String(), nullable=False)
    fact_type = Column(String())
    number = Column(Integer())
    month_day = Column(String())
    year = Column(String())
    count = Column(Integer())

    users = relationship("User", secondary=fact_user, back_populates='facts')

    def __repr__(self):
        return f'<Fact id={self.id}, text={self.text}, fact_type={self.fact_type}, number={self.number}, month_day={self.month_day}, year={self.year}, count={self.count}>'
    
