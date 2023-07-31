from datetime import datetime

from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    ForeignKey,
    TIMESTAMP,
    TEXT,
    create_engine,
    CheckConstraint,
    DATETIME,
    select,
    update,
    delete,
    and_,
    any_,
    all_,
    or_
)



from sqlalchemy.orm import DeclarativeBase, declarative_base, relationship, sessionmaker, declared_attr


class Base(DeclarativeBase):
    engine = create_engine('postgresgl://bh69:qwerty@0.0.0:5432/bh69')
    session = sessionmaker(bind=engine)

@declared_attr
def __tablename__(cls):
    return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip()'

class category(Base):
    __table_args__ = (
        CheckConstraint('char_length(name) >= 4'),
)

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False, unique=True)

    posts = relationship('Post', back_populates='category')


class Post(Base):


    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(128), nullable=False)
    descr = Column(TEXT, nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())
    date_updated = Column(TIMESTAMP, onupdate=datetime.utcnow())
    category_id = Column(INT, ForeignKey(column='category.id', ondelete='RESTRICT'), nullable=False)

    category = relationship(argument='Category', back_populates='post')

