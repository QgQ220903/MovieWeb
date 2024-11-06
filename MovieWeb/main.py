from collections import UserDict

from MovieWeb import app, bcrypt
from flask import render_template, flash, redirect, url_for
from MovieWeb.forms import RegistrationForm, LoginForm, MovieForm
from MovieWeb.models import  Movie, User
from flask_login import login_user, current_user, logout_user

@app.route("/")
@app.route("/home")
def home():
    movies = Movie.query.all()
    return render_template("home.html", movies = movies)

@app.route("/movie_list")
def movie_list():
    movies = Movie.query.all()
    return render_template("movie_list.html", movies = movies)

@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template('movie.html', movie=movie)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Đăng ký tài khoản thành công', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # next_page = request.args.get('next')
            return redirect(url_for('home'))
        else:
            flash('Đăng nhập thất bại, vui lòng kiểm tra email và mật khẩu', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))



# Thêm mới phim
@app.route('/movies/add', methods=['GET', 'POST'])
def add_movie():
    form = MovieForm()
    if form.validate_on_submit():
        # Tạo đối tượng Movie với dữ liệu lấy từ form
        movie = Movie(
            title=form.title.data,
            genres=form.genres.data,
            year=form.year.data,
            directors=form.directors.data,
            actors=form.actors.data,
            country=form.country.data,
            duration=form.duration.data,
            description=form.description.data,
            thumbnail=form.thumbnail.data
        )
        db.session.add(movie)
        db.session.commit()
        flash('Thêm phim thành công!', 'success')
        return redirect(url_for('movie_list'))
    return render_template('add_movie.html', form=form)




if __name__ == '__main__':
    from MovieWeb.admin import *
    app.run(debug=True)