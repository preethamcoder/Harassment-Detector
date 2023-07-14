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
		text = ' '.join(stuff['inp'].split())
		print(text, end=' ')
		predicted = model.predict(text.lower())
		res = "inappropriate" if predicted[0][0][-1]=='1' else "okay"
		print(f"This is {res}.")
		if res == "inappropriate":
			verdict = "Can't be saying that."
			col = "orange"
			img = "static/images/no.png"
		else:
			verdict = "At least you aren't a drag to hang with."
			col = "#0f0"
			img = "static/images/ok.jpeg"
	return render_template('pred.html', say=text, pred=res, verdict=verdict, box=col, img=img)

if __name__ == '__main__':
	load_da_model()
	app.run(host='0.0.0.0', debug=True, port=5000)
