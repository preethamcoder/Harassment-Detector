from flask import Flask, render_template, request
import fasttext

app = Flask(__name__)

model = "samurai"
def load_da_model():
	global model
	model = fasttext.load_model("trained.ftz")

@app.route('/')
def home():
	return render_template("index.html")

@app.route("/home.html")
def meth():
    return render_template("home.html")

@app.route('/pred.html', methods=['GET', 'POST'])
def predict_da_text():
	if request.method == 'POST':
		stuff = request.form
		text = stuff['inp']
		print(text)
		predicted = model.predict(text.lower())
		res = "hate" if predicted[0][0][-1]=='1' else "not hate"
		if res == "hate":
			verdict = "watch what you say, dumbass"
		else:
			verdict = "this is fine"
	return render_template('pred.html', shit=text, pred=res, verdict=verdict)

if __name__ == '__main__':
	load_da_model()
	app.run(host='0.0.0.0', debug=True, port=5000)

