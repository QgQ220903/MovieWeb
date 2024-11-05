# from flask import render_template, flash, redirect, url_for
# from MovieApp import app
# from MovieApp.forms import RegistrationForm, LoginForm
# from MovieApp.models import  User, Movie
# # from models import User, Movie
# from MovieApp import db
#
# movies = [
#     {
#         'id' : "1",
#         'title' : "Joker: Folie à Deux",
#         'description' : "Joker 2: Điên Có Đôi Joker: Folie à Deux 2024 là một phim tâm lý kinh dị âm nhạc của Mỹ do Todd Phillips đạo diễn và là phần hai của phim Joker năm 2019. Phim có sự trở lại của Joaquin Phoenix trong vai Joker, cùng với sự góp mặt của Lady Gaga vào vai Harley Quinn, nhân vật mới được giới thiệu là bạn gái của Joker. Phim cũng có sự tham gia của Zazie Beetz người tiếp tục vai diễn từ phần trước.Phần này đi sâu vào sự phát triển quan hệ giữa Arthur Fleck (Joker) và Harley Quinn ở bệnh viện tâm thần Arkham, nơi Arthur đang chờ xét xử vì các tội ác của mình. Nhiều luồng âm nhạc mạnh mẽ, khi Arthur tìm thấy niềm vui trong âm nhạc và chia sẻ điều này với Harley, cùng nhau họ đi tới một mối quan hệ phức tạp. ",
#         'release_year' : "2024",
#         'thumbnail' : "https://cinema.momocdn.net/img/37472853072716025-xqjsuwiihnPk5YTYgJQRTSfkQr6.jpg"
#     },
#
#     {
#         'id': "2",
#         'title': "The Judge from Hell ",
#         'description': "Thẩm Phán Đến Từ Địa Ngục The Judge from Hell 2024 Dự kiến sẽ phát sóng trên SBS TV vào ngày 21 tháng 9 năm 2024 và cũng sẽ có mặt trên PhimMoi. Phim được đạo diễn bởi Park Jin-pyo, với sự tham gia của Park Shin-hye và Kim Jae-young. Phim kể về Kang Bit-na một con quỷ chiếm hữu thể xác của một thẩm phán và bên cạnh đó còn gặp Han Da-on một thám tử nhân hậu. Cả hai cùng nhau đối mặt với thực tế khắc nghiệt hơn cả địa ngục, dẫn đến hành trình chuyển hóa của Bit-na trở thành một thẩm phán thực thụ. ",
#         'release_year': "2024",
#         'thumbnail': "https://www.elle.vn/wp-content/uploads/2024/09/05/606230/poster-phim-han-the-judge-from-the-hell.jpg"
#     },
#
#     {
#         'id': "3",
#         'title': "Venom: The Last Dance",
#         'description': "Joker 2: Điên Có Đôi Joker: Folie à Deux 2024 là một phim tâm lý kinh dị âm nhạc của Mỹ do Todd Phillips đạo diễn và là phần hai của phim Joker năm 2019. Phim có sự trở lại của Joaquin Phoenix trong vai Joker, cùng với sự góp mặt của Lady Gaga vào vai Harley Quinn, nhân vật mới được giới thiệu là bạn gái của Joker. Phim cũng có sự tham gia của Zazie Beetz người tiếp tục vai diễn từ phần trước.Phần này đi sâu vào sự phát triển quan hệ giữa Arthur Fleck (Joker) và Harley Quinn ở bệnh viện tâm thần Arkham, nơi Arthur đang chờ xét xử vì các tội ác của mình. Nhiều luồng âm nhạc mạnh mẽ, khi Arthur tìm thấy niềm vui trong âm nhạc và chia sẻ điều này với Harley, cùng nhau họ đi tới một mối quan hệ phức tạp. ",
#         'release_year': "2024",
#         'thumbnail': "https://m.media-amazon.com/images/M/MV5BZDMyYWU4NzItZDY0MC00ODE2LTkyYTMtMzNkNDdmYmFhZDg0XkEyXkFqcGc@._V1_.jpg"
#     },
#
#     {
#         'id': "4",
#         'title': "Tulsa King",
#         'description': "Joker 2: Điên Có Đôi Joker: Folie à Deux 2024 là một phim tâm lý kinh dị âm nhạc của Mỹ do Todd Phillips đạo diễn và là phần hai của phim Joker năm 2019. Phim có sự trở lại của Joaquin Phoenix trong vai Joker, cùng với sự góp mặt của Lady Gaga vào vai Harley Quinn, nhân vật mới được giới thiệu là bạn gái của Joker. Phim cũng có sự tham gia của Zazie Beetz người tiếp tục vai diễn từ phần trước.Phần này đi sâu vào sự phát triển quan hệ giữa Arthur Fleck (Joker) và Harley Quinn ở bệnh viện tâm thần Arkham, nơi Arthur đang chờ xét xử vì các tội ác của mình. Nhiều luồng âm nhạc mạnh mẽ, khi Arthur tìm thấy niềm vui trong âm nhạc và chia sẻ điều này với Harley, cùng nhau họ đi tới một mối quan hệ phức tạp. ",
#         'release_year': "2024",
#         'thumbnail': "https://m.media-amazon.com/images/M/MV5BMjBiNmI3YjMtNjJmNi00MTdiLTg5YTItMTk1MjcwOWIyZjY3XkEyXkFqcGc@._V1_.jpg"
#     },
#     {
#         'id': "5",
#         'title': "Joker: Folie à Deux",
#         'description': "Joker 2: Điên Có Đôi Joker: Folie à Deux 2024 là một phim tâm lý kinh dị âm nhạc của Mỹ do Todd Phillips đạo diễn và là phần hai của phim Joker năm 2019. Phim có sự trở lại của Joaquin Phoenix trong vai Joker, cùng với sự góp mặt của Lady Gaga vào vai Harley Quinn, nhân vật mới được giới thiệu là bạn gái của Joker. Phim cũng có sự tham gia của Zazie Beetz người tiếp tục vai diễn từ phần trước.Phần này đi sâu vào sự phát triển quan hệ giữa Arthur Fleck (Joker) và Harley Quinn ở bệnh viện tâm thần Arkham, nơi Arthur đang chờ xét xử vì các tội ác của mình. Nhiều luồng âm nhạc mạnh mẽ, khi Arthur tìm thấy niềm vui trong âm nhạc và chia sẻ điều này với Harley, cùng nhau họ đi tới một mối quan hệ phức tạp. ",
#         'release_year': "2024",
#         'thumbnail': "https://cinema.momocdn.net/img/37472853072716025-xqjsuwiihnPk5YTYgJQRTSfkQr6.jpg"
#     },
#
#     {
#         'id': "6",
#         'title': "Joker: Folie à Deux",
#         'description': "Joker 2: Điên Có Đôi Joker: Folie à Deux 2024 là một phim tâm lý kinh dị âm nhạc của Mỹ do Todd Phillips đạo diễn và là phần hai của phim Joker năm 2019. Phim có sự trở lại của Joaquin Phoenix trong vai Joker, cùng với sự góp mặt của Lady Gaga vào vai Harley Quinn, nhân vật mới được giới thiệu là bạn gái của Joker. Phim cũng có sự tham gia của Zazie Beetz người tiếp tục vai diễn từ phần trước.Phần này đi sâu vào sự phát triển quan hệ giữa Arthur Fleck (Joker) và Harley Quinn ở bệnh viện tâm thần Arkham, nơi Arthur đang chờ xét xử vì các tội ác của mình. Nhiều luồng âm nhạc mạnh mẽ, khi Arthur tìm thấy niềm vui trong âm nhạc và chia sẻ điều này với Harley, cùng nhau họ đi tới một mối quan hệ phức tạp. ",
#         'release_year': "2024",
#         'thumbnail': "https://cinema.momocdn.net/img/37472853072716025-xqjsuwiihnPk5YTYgJQRTSfkQr6.jpg"
#     },
#
#     {
#         'id': "7",
#         'title': "Joker: Folie à Deux",
#         'description': "Joker 2: Điên Có Đôi Joker: Folie à Deux 2024 là một phim tâm lý kinh dị âm nhạc của Mỹ do Todd Phillips đạo diễn và là phần hai của phim Joker năm 2019. Phim có sự trở lại của Joaquin Phoenix trong vai Joker, cùng với sự góp mặt của Lady Gaga vào vai Harley Quinn, nhân vật mới được giới thiệu là bạn gái của Joker. Phim cũng có sự tham gia của Zazie Beetz người tiếp tục vai diễn từ phần trước.Phần này đi sâu vào sự phát triển quan hệ giữa Arthur Fleck (Joker) và Harley Quinn ở bệnh viện tâm thần Arkham, nơi Arthur đang chờ xét xử vì các tội ác của mình. Nhiều luồng âm nhạc mạnh mẽ, khi Arthur tìm thấy niềm vui trong âm nhạc và chia sẻ điều này với Harley, cùng nhau họ đi tới một mối quan hệ phức tạp. ",
#         'release_year': "2024",
#         'thumbnail': "https://cinema.momocdn.net/img/37472853072716025-xqjsuwiihnPk5YTYgJQRTSfkQr6.jpg"
#     },
#
#     {
#         'id': "8",
#         'title': "Joker: Folie à Deux",
#         'description': "Joker 2: Điên Có Đôi Joker: Folie à Deux 2024 là một phim tâm lý kinh dị âm nhạc của Mỹ do Todd Phillips đạo diễn và là phần hai của phim Joker năm 2019. Phim có sự trở lại của Joaquin Phoenix trong vai Joker, cùng với sự góp mặt của Lady Gaga vào vai Harley Quinn, nhân vật mới được giới thiệu là bạn gái của Joker. Phim cũng có sự tham gia của Zazie Beetz người tiếp tục vai diễn từ phần trước.Phần này đi sâu vào sự phát triển quan hệ giữa Arthur Fleck (Joker) và Harley Quinn ở bệnh viện tâm thần Arkham, nơi Arthur đang chờ xét xử vì các tội ác của mình. Nhiều luồng âm nhạc mạnh mẽ, khi Arthur tìm thấy niềm vui trong âm nhạc và chia sẻ điều này với Harley, cùng nhau họ đi tới một mối quan hệ phức tạp. ",
#         'release_year': "2024",
#         'thumbnail': "https://cinema.momocdn.net/img/37472853072716025-xqjsuwiihnPk5YTYgJQRTSfkQr6.jpg"
#     }
#
# ]
#
# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template("home.html", movies = movies)
#
# @app.route("/movie_list")
# def movie_list():
#     return render_template("movie_list.html")
#
# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Đăng ký tài khoản thành công {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template("register.html", title="Đăng Ký", form=form)
#
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@gmail.com' and form.password.data == 'admin':
#             flash(f'Đăng nhập thành công!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash(f'Đăng nhập thất bại, Vui lòng nhập tài khoản hợp lệ', 'danger')
#     return render_template("login.html", title="Đăng Nhập", form=form)