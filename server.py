import os
import time
from flask import Flask, send_from_directory, request, redirect, url_for
from werkzeug.utils import secure_filename

from flask import render_template
from flask import request

app = Flask(__name__, static_url_path='')
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'classifierData/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav'])


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

# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    print(request)
    print(request.files)
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file:
        print(file)
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.name)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],  time.strftime("%I%M%S") + ".wav"))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('lightsDemo'))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
    app.run(debug=True)
