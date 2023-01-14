
from flask import Flask, jsonify, render_template, send_from_directory


#comprime i pacchetti per maggiori performance
app = Flask(__name__)



@app.route('/flaskback', methods=["GET"])
def flaskback():
    x = {'id': 'Frase caricata dal backend'}
    res = jsonify(x)
    res.headers["Content-Type"] = "application/json"
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(port=3000)
