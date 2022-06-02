
from flask import Flask, render_template, request, flash,url_for

app = Flask(__name__)
app.secret_key = "bdsjkjkdsnVKJ"
@app.route("/hello")
def index():
    flash("whats your name?")
    return render_template ("index.html")

@app.route("/greet/", methods =["POST","GET"])
def greet():
    flash("Hi " + str(request.form["name_input"]) + " great to see you! ")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)


