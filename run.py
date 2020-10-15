from flask import Flask, render_template, url_for, request, redirect, make_response
from random import choice
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, TemperatureS, TemperatureN]

    TemperatureS = choice((-55, -52))
    TemperatureN = choice((-14, -10))

    data = [time() * 1000, TemperatureS, TemperatureN]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)