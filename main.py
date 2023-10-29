from flask import Flask, render_template, request, send_file, session
from flask_session import Session
import qrcode
import sqlite3

app = Flask(__name__)

# セッションをセットアップ
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def add_user_db(line_name, line_email, line_password, instagram_url, twitter_url, facebook_url, tiktok_url):
    db_name = 'User_db'
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    status = False

    cur.execute("SELECT * FROM user_table WHERE line_name = '" + line_name + "' and line_email = '" + line_email + "' and line_password = '" + line_password + "';")

# ホームページを表示するルート
@app.route("/", methods = ["GET"])
def index():
    # # セッションからユーザーごとの情報を取得
    user_data = session.get("user_data")
    return render_template("index.html", user_data=user_data)
    # if request.method == "GET":
        
    # return render_template("index.html")

@app.route("/private")
def private():
    return render_template('private.html')

@app.route("/business")
def business():
    return render_template('business.html')

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        line_url = request.form["line_url"]
        instagram_url = request.form["instagram_url"]
        twitter_url = request.form["twitter_url"]
        facebook_url = request.form["facebook_url"]
        tiktok_url = request.form["tiktok_url"]

    add_user_db(line_url, instagram_url, twitter_url, facebook_url, tiktok_url)

    return render_template('account.html', line_url = line_url,  instagram_url = instagram_url, twitter_url = twitter_url, facebook_url = facebook_url, tiktok_url = tiktok_url)


if __name__ == "__main__":
    app.run(debug=True)
