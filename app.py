from flask import Flask, render_template, request
# import numpy as np
# import pickle
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import TfidfVectorizer
import fasttext

app = Flask(__name__)

# with open('vect.pkl', 'rb') as f:
# 	vect = pickle.load(f)
 
model = "samurai"
def load_da_model():
	global model
	model = fasttext.load_model("trained.ftz")
	# with open('sexual_assault.pkl', 'rb') as f:
	# 	model = pickle.load(f)


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
		# txt = vect.transform([stuff['inp']])
		# total = np.sum(model.predict(txt).toarray())
		# print(total)
		predicted = model.predict(stuff['inp'].lower())
		res = "hate" if predicted[0][0][-1]=='1' else "not hate"
		if res == "hate":
			verdict = "watch what you say, dumbass"
		else:
			verdict = "this is fine"
	return render_template('pred.html', shit=stuff['inp'], pred=res, verdict=verdict)

if __name__ == '__main__':
	load_da_model()
	app.run(host='0.0.0.0', debug=True, port=5000)
