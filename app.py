from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/correo")
def correo():
    return render_template("correo.html")

@app.route("/instagram_followers")
def instagram_followers():
    return render_template("instagram_followers.html")

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=777)