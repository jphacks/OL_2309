from flask import Flask, render_template, request, send_file, session
from flask_session import Session
import qrcode
import sqlite3

app = Flask(__name__)

# セッションをセットアップ
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# ホームページを表示するルート
@app.route("/")
def index():
    # セッションからユーザーごとの情報を取得
    user_data = session.get("user_data")
    return render_template("index.html", user_data=user_data)

@app.route("/private")
def private():
    return render_template('private.html')

@app.route("/business")
def business():
    return render_template('business.html')

# QRコードを生成して表示するルート
@app.route("/generate_qrcode", methods=["POST"])
def generate_qrcode():
    data = request.form.get("data")
    user_data = {
        "data": data,
    }
    # ユーザーごとの情報をセッションに保存
    session["user_data"] = user_data

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_path = "temp_qrcode.png"
    img.save(img_path)
    return send_file(img_path, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
