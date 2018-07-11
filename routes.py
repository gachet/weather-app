from flask import Flask, render_template, request, session, url_for, redirect
from flask_bootstrap import Bootstrap
import datetime
from urllib.request import urlopen
import json

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
	api_key = str(open("api.txt", "r").read().splitlines())
	elements = ["http://api.wunderground.com/api/",api_key[2:18],"/conditions/q/NY/Ithaca.json"]
	url = "".join(elements)
	json_obj = urlopen(url)
	data = json.load(json_obj)
	temperature = data['current_observation']['temperature_string']
	icon = data['current_observation']['icon_url']
	time = datetime.datetime.now()
	return render_template("base.html", temperature=temperature, icon=icon, time=time)


# Default port:
if __name__ == '__main__':
    app.run(debug=True)
