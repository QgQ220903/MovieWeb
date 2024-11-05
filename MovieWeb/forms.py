from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    confirm_password = PasswordField('Xác nhận mật khẩu', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Đăng Ký')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    remember = BooleanField('Nhớ đăng nhập')
    submit = SubmitField('Đăng Nhập')

class MovieForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[DataRequired()])
    genres = StringField('Thể loại', validators=[DataRequired()])
    year = IntegerField('Năm', validators=[DataRequired()])
    directors = StringField('Đạo diễn', validators=[DataRequired()])
    actors = StringField('Diễn viên', validators=[DataRequired()])
    country = StringField('Quốc gia', validators=[DataRequired()])
    duration = IntegerField('Thời lượng', validators=[DataRequired()])
    description = TextAreaField('Mô tả', validators=[DataRequired()])
    thumbnail = StringField('Ảnh bìa', validators=[DataRequired()])
    submit = SubmitField('Lưu')