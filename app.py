from flask import Flask
from flask import request
from flask import render_template

import joblib

from feature_extractor import extract_features

app = Flask(__name__)

model = joblib.load(
    "phishing_model.pkl"
)

@app.route("/", methods=["GET","POST"])
def home():

    result = ""

    if request.method == "POST":

        url = request.form["url"]

        prediction = model.predict(
            [extract_features(url)]
        )[0]

        if prediction == 0:
            result = "⚠️ Phishing Website"
        else:
            result = "✅ Legitimate Website"

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
