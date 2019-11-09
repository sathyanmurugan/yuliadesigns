import flask
import os
import json

app = flask.Flask(__name__)

@app.route('/')
def main():
	return "Hello"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)