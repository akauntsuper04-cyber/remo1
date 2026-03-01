from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/roster")
def roster():
    return render_template("roster.html")

@app.route("/matches")
def matches():
    return render_template("matches.html")

@app.route("/match1")
def match1():
    return render_template("match1.html")

@app.route("/match2")
def match2():
    return render_template("match2.html")

@app.route("/rules")
def rules():
    return render_template("rules.html")

if __name__ == "__main__":
    app.run(debug=True)