from MovieWeb import app
from flask import render_template, flash, redirect, url_for
from MovieWeb.forms import RegistrationForm, LoginForm, MovieForm

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Đăng ký tài khoản thành công {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Đăng Ký", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'admin':
            flash(f'Đăng nhập thành công!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Đăng nhập thất bại, Vui lòng nhập tài khoản hợp lệ', 'danger')
    return render_template("login.html", title="Đăng Nhập", form=form)

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