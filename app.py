from flask import Flask, render_template, request
import instaloader

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/correo")
def correo():
    return render_template("correo.html")

@app.route("/instagram_followers")
def instagram_followers():
    user_profile = request.args.get("profile_username")
    
    if not user_profile:
        return render_template("instagram_followers.html", mensaje="Falta el nombre de usuario.")

    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, user_profile)

        datos = {
            'result': {
                'username': profile.username,
                'followers': profile.followers,
                'followees': profile.followees,
                'mediacount': profile.mediacount
            },
            'message': 'Perfil encontrado'
        }
        return render_template("instagram_followers.html", datos=datos)

    except Exception:
        return render_template("instagram_followers.html", mensaje="No existe el usuario.")


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=777)