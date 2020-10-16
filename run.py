from flask import Flask, render_template, url_for, request, redirect, make_response
from random import choice
import json, csv
from time import time
from random import random
from flask import Flask, render_template, make_response
# import numpy as np
# import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, TemperatureS, TemperatureN]

# @app.route('graph_example')

    TemperatureS = choice((-55, -52))
    TemperatureN = choice((-12, -10))

    data = [time() * 1000, TemperatureS, TemperatureN]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)