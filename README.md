#  Customer Churn Prediction

A machine learning project that predicts whether a customer will churn (leave) or stay, based on their profile and service usage data. This project demonstrates **end-to-end Data Science workflow**: data preprocessing, model training, evaluation, and deployment with Streamlit.

---

##  Features

* Data preprocessing & feature engineering
* Logistic Regression model with evaluation metrics
* Interactive Streamlit app for predictions
* Well-structured code and notebook for reproducibility

---

##  Project Structure

```
DataScience-portfolio/
│── app.py                   # Streamlit app  
│── churn_model.pkl          # Saved trained model  
│── notebooks/               # Jupyter notebooks for EDA & modeling  
│── data/                    # Dataset (ignored in GitHub if large)  
│── .gitignore               # Ignored files  
│── requirements.txt         # Python dependencies  
│── README.md                # Project documentation  
```

---

##  Installation

1. Clone the repository:

```bash
git clone git@github.com:Iamkvng01/DataScience-portfolio.git
cd DataScience-portfolio
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Fill in customer details in the web interface to predict churn.

---

## Model Performance

* Accuracy: \~73%
* F1 Score (Churn = "Yes"): \~0.65
* Confusion Matrix and Classification Report included in notebook

---

## Learnings

This project highlights:

* Importance of data preprocessing (encoding, scaling)
* Handling class imbalance
* Using pipelines for clean workflows
* Deploying ML models with Streamlit

---

##  Tech Stack

* **Python** (pandas, numpy, scikit-learn)
* **Jupyter Notebook** for EDA and modeling
* **Streamlit** for app deployment
* **Git/GitHub** for version control

