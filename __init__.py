from flask import Flask, render_template
from forms import LoginForm
 
app = Flask(__name__)
app.config.from_pyfile("config.py")

# @app.route("/")
# def index():
#     return render_template(
#         "index.html"
#     )

@app.route("/login")
def login():
    title = "Авторизация"
    login_form = LoginForm()
    return render_template(
        "login.html", page_title = title, form = login_form
    )




if __name__ == "__main__":
    app.run(debug=True)