from flask import Flask, render_template, request, session, url_for, redirect

api_key = open("api.txt", "r").readline()
print(api_key)


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


# Default port:
if __name__ == '__main__':
    app.run()
