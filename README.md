# Phishing Detection System using Machine Learning

## Project Overview

This project is a **Machine Learning-based Phishing Website Detection System** developed using **Python**, **Flask**, and **Random Forest**.

The application analyzes a website URL and predicts whether it is:

- ✅ Legitimate Website
- ⚠️ Phishing Website

The project includes:

- Machine Learning model training
- URL feature extraction
- Command-line phishing detector
- Flask web application

---

# Project Structure

```
Phishing-Detection/
│
├── data/
│   └── dataset.csv
│
├── model/
│   └── phishing_model.pkl
│
├── templates/
│   └── index.html
│
├── app.py
├── detector.py
├── feature_extractor.py
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Dataset

Download the dataset from:

https://data.mendeley.com/datasets/3jddhy2f6s/1

After downloading, copy the dataset into the `data` folder.

The final structure should look like:

```
data/
└── dataset.csv
```

---

# Software Requirements

Install the following before running the project:

- Python 3.10 or later
- Git
- pip

Check the installed versions:

```bash
python3 --version

git --version

pip3 --version
```

---

# Step 1 - Clone the Repository

Open Terminal.

Run:

```bash
git clone https://github.com/YOUR_USERNAME/Phishing-Detection.git
```

Replace:

```
YOUR_USERNAME
```

with your GitHub username.

---

# Step 2 - Enter the Project Folder

```bash
cd Phishing-Detection
```

Check the files:

```bash
ls
```

You should see:

```
app.py
train.py
detector.py
feature_extractor.py
requirements.txt
templates
data
```

---

# Step 3 - Create a Virtual Environment

Create a Python virtual environment.

```bash
python3 -m venv venv
```

This creates a folder named:

```
venv
```

---

# Step 4 - Activate the Virtual Environment

### Linux / Kali Linux / Ubuntu

```bash
source venv/bin/activate
```

If successful, your terminal changes to:

```
(venv) user@kali:~/Phishing-Detection$
```

### Windows

```cmd
venv\Scripts\activate
```

---

# Step 5 - Install Required Packages

Install all Python libraries.

```bash
pip install -r requirements.txt
```

Packages installed:

- Flask
- pandas
- numpy
- scikit-learn
- joblib
- requests
- tldextract
- beautifulsoup4
- python-whois

---

# Step 6 - Download the Dataset

Download:

https://data.mendeley.com/datasets/3jddhy2f6s/1

Extract it.

Copy:

```
dataset.csv
```

into:

```
Phishing-Detection/data/
```

Check:

```bash
ls data
```

Output:

```
dataset.csv
```

---

# Step 7 - Train the Machine Learning Model

Run:

```bash
python3 train.py
```

The program will:

- Read the dataset
- Extract URL features
- Train the Random Forest model
- Save the trained model

Expected output:

```
precision
recall
f1-score

Model Saved
```

A new file should appear:

```
model/phishing_model.pkl
```

---

# Step 8 - Run the Command Line Detector

Start the detector:

```bash
python3 detector.py
```

Example:

```
Enter URL:

https://google.com
```

Output:

```
Legitimate Website
```

Example:

```
http://fake-bank-login.xyz
```

Output:

```
Phishing Website
```

Exit:

```
q
```

---

# Step 9 - Run the Flask Web Application

Start the server.

```bash
python3 app.py
```

Output:

```
Running on http://127.0.0.1:5000
```

---

# Step 10 - Open the Web Browser

Visit:

```
http://127.0.0.1:5000
```

You will see the phishing detection webpage.

Enter a URL.

Click:

```
Check
```

The application predicts whether the URL is:

- Legitimate
- Phishing

---

# Git Commands

## Check Repository Status

```bash
git status
```

---

## Add All Files

```bash
git add .
```

---

## Commit Changes

```bash
git commit -m "Updated project"
```

---

## Push Changes

```bash
git push
```

---

## Download Latest Changes

```bash
git pull
```

---

# Common Errors

## ModuleNotFoundError

Install packages again:

```bash
pip install -r requirements.txt
```

---

## Dataset Not Found

Error:

```
FileNotFoundError
```

Solution:

Ensure:

```
data/dataset.csv
```

exists.

---

## Model File Missing

Run:

```bash
python3 train.py
```

This generates:

```
model/phishing_model.pkl
```

---

## Virtual Environment Not Activated

Activate:

Linux:

```bash
source venv/bin/activate
```

Windows:

```cmd
venv\Scripts\activate
```

---

# Technologies Used

- Python
- Flask
- Machine Learning
- Random Forest
- Pandas
- NumPy
- Joblib
- HTML
- CSS

---

# Future Improvements

- Deep Learning model
- URL reputation checking
- WHOIS integration
- DNS feature extraction
- Improved user interface
- REST API support

---

# Authors

Kabilar

Contributors:

- Adhipan

---

# License

This project is intended for educational and research purposes.
