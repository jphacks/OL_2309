from flask import Flask, render_template, request, send_file, session
from flask_session import Session
import qrcode
import sqlite3
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# セッションをセットアップ
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# def add_user_db(line_name, line_email, line_password, instagram_url, twitter_url, facebook_url, tiktok_url):
#     db_name = 'User.db'
#     con = sqlite3.connect(db_name)
#     cur = con.cursor()

#     status = False

#     cur.execute("SELECT * FROM user_table WHERE line_name = '" + line_name + "' and line_email = '" + line_email + "' and line_password = '" + line_password + "';")


def add_user_db(username, password, line_url, instagram_url, twitter_url, facebook_url, tiktok_url):
    conn = sqlite3.connect('User.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM user_table WHERE username = ?", (username,))
    if cur.fetchone():

        print("Username already exists!")
    else:
        
        cur.execute("INSERT INTO user_table (username, password, line_url, instagram_url, twitter_url, facebook_url, tiktok_url) VALUES (?, ?, ?, ?, ?, ?, ?)", (username, password, line_url, instagram_url, twitter_url, facebook_url, tiktok_url))
        conn.commit()

    conn.close()

# ログイン画面を表示するルート
# @app.route("/")
# def login():
#     return render_template("login.html")

# ホームページを表示するルート
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
    # # セッションからユーザーごとの情報を取得
        user_data = session.get("user_data")
        return render_template("index.html", user_data=user_data)
    # if request.method == "GET":
        
    # return render_template("index.html")

@app.route("/private", methods = ["GET", "POST"])
def private():
    if request.method == "GET":
        return render_template('private.html')

@app.route("/business", methods = ["GET", "POST"])
def business():
    return render_template('business.html')

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "GET":
        username = request.form["username"]
        password = request.form["password"]
        line_url = request.form["line_url"]
        instagram_url = request.form["instagram_url"]
        twitter_url = request.form["twitter_url"]
        facebook_url = request.form["facebook_url"]
        tiktok_url = request.form["tiktok_url"]

        add_user_db(username, password, line_url, instagram_url, twitter_url, facebook_url, tiktok_url)
        return redirect(url_for('account'))

    return render_template('account.html')


if __name__ == "__main__":
    app.run(debug=True)