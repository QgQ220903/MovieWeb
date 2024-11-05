from MovieWeb import app, db
from flask_admin import Admin
from MovieWeb.models import Movie
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name="MovieWeb", template_mode='bootstrap4')
class MovieView(ModelView):
    can_view_details = True
    can_export = True
    column_searchable_list = ['title', 'year', 'genres']
    column_exclude_list = ['thumbnail', 'description', 'directors', 'actors']
    column_labels = {
        'title' : 'Tên Phim',
        'genres' : 'Thể Loại',
        'year' : 'Năm Phát Hành',
        'country' : 'Quốc Gia',
        'duration' : 'Thời Lượng',
        'directors' : 'Đạo Diễn',
        'actors' : 'Diễn Viên',
        'description': 'Mô Tả',
        'thumbnail' : 'Đường dẫn ảnh'
    }
admin.add_view(MovieView(Movie, db.session))