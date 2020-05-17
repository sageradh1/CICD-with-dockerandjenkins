from flask import Flask,render_template

app = Flask(__name__)

app.config["ENV"] = "development"

#changes
@app.route("/")
def home():
	return "Jenkins pipeline is working well with flask in clothing store"

if __name__=="__main__":
	app.run(debug=True,host='0.0.0.0',port=4000)
