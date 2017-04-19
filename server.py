from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/slides')
def slides():
    return render_template("Slides.html")

@app.route('/proposal')
def proposal():
    return render_template("Proposal.html")

@app.route('/demo')
def demo():
    return render_template("demo.html")


if __name__ == "__main__":
    app.run()
