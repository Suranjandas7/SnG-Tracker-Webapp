#webapp
from flask import Flask
from flask import request
from flask import render_template
from sng import *

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def form():
	return render_template("form.html")

@app.route("/", methods = ['POST'])
def my_form_post():
	caller = []
	text = request.form['text'].encode('utf-8')
	text = str(text).split(',')
	sng = SnG(text)
	return sng.return_stats()
	
if __name__ == "__main__":
	app.run()
	app.debug = True
