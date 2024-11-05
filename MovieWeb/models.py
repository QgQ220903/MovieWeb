from MovieWeb import db
from sqlalchemy import Column, Integer, String, Text
from MovieWeb import app


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    
    def __str__(self):
        return self.email


class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True) # Khóa chính của movie
    title = Column(String(100), nullable=False) # tên phim
    genres = Column(String(200), nullable=False)  # Lưu trữ nhiều thể loại, ngăn cách bởi dấu phẩy
    year = Column(Integer, nullable=False) # Năm phát hành
    directors = Column(String(200), nullable=False)  # Lưu trữ nhiều đạo diễn, ngăn cách bởi dấu phẩy
    actors = Column(String(200), nullable=False)  # Lưu trữ nhiều diễn viên, ngăn cách bởi dấu phẩy
    country = Column(String(100), nullable=False) # Quốc gia phim
    duration = Column(Integer, nullable=False) #  Thời lượng
    description = Column(Text, nullable=False) # mô tả ngắn
    thumbnail = Column(String(200), nullable=False) # ảnh bìa phim
    def __str__(self):
        return self.title


if __name__ == '__main__':
    with app.app_context():  # Bắt đầu application context
        db.create_all()
