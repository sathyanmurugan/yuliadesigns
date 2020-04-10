import flask
import os
import json

app = flask.Flask(__name__)

@app.route('/')
def main():
	return flask.render_template('main.html', title="Yulia's Portfolio")

@app.route('/poster')
def poster():
	return flask.render_template('poster.html', title="Poster")

@app.route('/iconset')
def iconset():
	return flask.render_template('iconset.html', title="Icons")

@app.route('/editorui')
def editorui():
	return flask.render_template('editorui.html', title="Editor UI")	

@app.route('/treatwell')
def treatwell():
	return flask.render_template('treatwell.html', title="Working from here")

@app.route('/motion')
def motion():
	return flask.render_template('motion.html', title="Motion studies")	

@app.route('/appredesign')
def appredesign():
	return flask.render_template('appredesign.html', title="App redesign")	

@app.route('/contenthub')
def contenthub():
	return flask.render_template('contenthub.html', title="Content hub")	

@app.route('/presentation')
def presentation():
	return flask.render_template('presentation.html', title="Presentation layout")	

@app.route('/campaign')
def campaign():
	return flask.render_template('campaign.html', title="Campaign")

@app.route('/moonwalk')
def moonwalk():
	return flask.render_template('moonwalk.html', title="Moon Walk")	

@app.route('/exportCV')
def exportCV():
	return flask.send_from_directory(app.static_folder,'CV_yulia.pdf', as_attachment=True, cache_timeout=0)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    #app.run()	