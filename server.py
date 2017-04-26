from flask import Flask, send_from_directory
from flask import render_template
from flask import request
#app = Flask(static_folder = '/Users/vishnuchittari/gesturelink')
app = Flask(__name__, static_url_path='')

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

@app.route('/survey')
def survey():
	return render_template("survey.html")

@app.route('/lights-demo', methods=["GET"])
def lightsDemo():
    type = request.args.get('type')
    return render_template("lights-demo.html")

@app.route('/music-player-demo', methods=["GET"])
def musicPlayerDemo():
    type = request.args.get('type')
    return render_template("music-player-demo.html")

@app.route('/lock-doors-demo', methods=["GET"])
def lockDoorsDemo():
    type = request.args.get('type')
    return render_template("lock-doors-demo.html")

@app.route('/testing', methods=["GET"])
def testing():
    type = request.args.get('type')
    return render_template("example_simple_exportwav.html")

@app.route('/sound-example', methods=["GET"])
def soundExample():
    type = request.args.get('type')
    return render_template("sound-example.html")

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == "__main__":
    app.run()
