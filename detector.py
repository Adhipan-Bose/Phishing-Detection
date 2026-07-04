import joblib

from feature_extractor import extract_features

model = joblib.load(
    "phishing_model.pkl"
)

while True:

    url = input(
        "\nEnter URL (q to quit): "
    )

    if url == "q":
        break

    result = model.predict(
        [extract_features(url)]
    )[0]

    if result == 1:
        print("\n[!] Phishing Website")
    else:
        print("\n[+] Legitimate Website")
