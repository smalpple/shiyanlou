from sqlalchemy import create_engine,Column, Integer, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine('mysql://biyong:Biyong12315.@140.143.207.54:3306/shiyanlou',echo=True)
Base = declarative_base()
#print(engine.execute('select * from user join course on course.teacher_id = user.id ').fetchall())

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    def __repr__(self):
        return "<User(name=%s)>" % self.name

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    teacher_id = Column(Integer,ForeignKey('user.id'))
    teacher = relationship('User')

    def __repr__(self):
        return '<Course(name=%s)>' % self.name

class Lab(Base):
    __tablename__ = 'lab'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    course_id = Column(Integer,ForeignKey('course.id'))
    course = relationship('Course',backref='labs')
    def __repr__(self):
        return '<Lab(name=%s)>' % self.name



if __name__ == '__main__':

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    #print(session.query(User).filter(User.name=='by').first())

    '''
    添加
    '''
    course = session.query(Course).first()
    lab1 = Lab(name='ORM Basic',course_id=course.id)
    lab2 = Lab(name='guanxi sql',course=course)
    # session.add(lab1)
    # session.add(lab2)
    # session.commit()
    #print(course.labs)

    '''
    更新
    '''
    course.name = 'Pyhton fenixi'
    session.add(course)
    session.commit()
    print("====",lab1.course)
    print("====",lab2.course)
    print("====",session.query(Course).all())
    session.close()