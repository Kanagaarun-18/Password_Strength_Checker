from flask import Flask, render_template, request, redirect, url_for, session
from analyzer import analyze_password

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.get("/")
def index():
    result = session.pop("result", None)
    return render_template("index.html", result=result)

@app.post("/")
def analyze():
    password = request.form["pwd"]
    result = analyze_password(password)

    session["result"] = result

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)