from flask import Flask, render_template, request, session, url_for, redirect
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route("/")
def index():
	api_key = str(open("api.txt", "r").read().splitlines())
	elements = ["http://api.wunderground.com/api/",api_key[2:17],"/conditions/q/NY/Ithaca.json"]
	url = "".join(elements)
	json_obj = urlopen(url)
	data = json.load(json_obj)
	temperature = data['current_observation']['temperature_string']
	return render_template("base.html", temperature=temperature)


# Default port:
if __name__ == '__main__':
    app.run(debug=True)
