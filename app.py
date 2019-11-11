import flask
import os
import json

app = flask.Flask(__name__)

@app.route('/')
def main():
	return flask.render_template('main.html', title="Yulia's Portfolio")

@app.route('/project')
def project():
	return flask.render_template('project.html', title="Yulia's Portfolio")


@app.route('/exportCV')
def exportCV():
	return flask.send_from_directory(app.static_folder,'CV.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    #app.run()	