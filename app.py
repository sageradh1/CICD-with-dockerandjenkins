from flask import Flask,render_template

app = Flask(__name__)

app.config["ENV"] = "development"

#again
@app.route("/")
def home():
	return "Jenkins pipeline is working well CICD pipeline"

if __name__=="__main__":
	app.run(debug=True,host='0.0.0.0',port=4000)
