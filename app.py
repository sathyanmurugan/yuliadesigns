import flask
import os
import json
import constants

app = flask.Flask(__name__)

@app.route('/')
def main():
	return flask.render_template(
		'main.html', 
		title="Yulia's Portfolio",
		presentation_1_url=constants.PDP_PRESENTATION_URL,
		presentation_2_url=constants.CHECKOUT_PRESENTATION_URL,
		presentation_3_url=constants.COBROWSING_PRESENTATION_URL,
		)

@app.route('/exportCV')
def exportCV():
	return flask.send_from_directory(app.static_folder,'CV.pdf', as_attachment=True, cache_timeout=0)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    #app.run()	