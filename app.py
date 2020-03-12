from flask import Flask,render_template

app = Flask(__name__)

app.config["ENV"] = "development"


@app.route("/")
def home():
	return "Home page"

if __name__=="__main__":
	app.run(debug=True,host='0.0.0.0',port=4000)