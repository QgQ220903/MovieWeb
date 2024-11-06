from MovieWeb import db, login_manager
from sqlalchemy import Column, Integer, String, Text
from MovieWeb import app
from flask_login import UserMixin

# hàm này để lấy ra người dùng thông qua id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Model của người dùng
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True) # khóa chính để định danh người dùng
    username = Column(String(20), unique=True, nullable=False) # tên đăng nhập
    email = Column(String(100), unique=True, nullable=False) # email
    image_file = db.Column(db.String(100), nullable=False, default='default.jpg') # ảnh đại diện
    password = db.Column(db.String(60), nullable=False) # mật khẩu
    
    def __str__(self):
        return self.email


# Model của bộ phim
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
