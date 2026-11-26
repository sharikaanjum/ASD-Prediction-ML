# 🧠 Autism Prediction Web App

A machine learning web application that predicts the likelihood of Autism Spectrum Disorder (ASD) based on key demographic and medical features. Built with Python, Scikit-learn, and Streamlit.

---

## 📌 Project Overview

Early screening for Autism Spectrum Disorder is critical for timely intervention. This project uses a Logistic Regression model trained on real-world ASD screening data to assist in early-stage prediction based on simple user inputs.

This was developed as an undergraduate final project, later upgraded with a full Streamlit web interface for accessibility.

---

## 🚀 Live Demo

> Run locally using the steps below. Deployment to Streamlit Cloud coming soon.

---

## 🖼️ App Screenshot

![Autism Prediction App](screenshot.png)

> *Add a screenshot of your running app here by placing an image named `screenshot.png` in the project folder*

---

## 🛠️ Tech Stack

| Layer | Tools Used |
|---|---|
| Language | Python 3.x |
| ML Model | Scikit-learn (Logistic Regression) |
| Data Processing | Pandas, NumPy |
| Web App | Streamlit |
| Model Serialization | Pickle |
| IDE | Jupyter Notebook, VS Code |

---

## 📁 Project Structure

```
autism-prediction/
│
├── app.py                    # Streamlit web application
├── autism_prediction1.ipynb  # Model training notebook
├── model.pkl                 # Trained Logistic Regression model
├── gender_encoder.pkl        # LabelEncoder for gender
├── ethnicity_encoder.pkl     # LabelEncoder for ethnicity
├── train.csv                 # Training dataset
└── README.md
```

---

## 📊 Dataset

- Source: [Kaggle ASD Screening Dataset](https://www.kaggle.com/datasets/faizunnabi/autism-screening)
- Records: ~800 entries
- Target variable: `Class/ASD` (1 = Autism likely, 0 = Not likely)

**Features used for prediction:**

| Feature | Description |
|---|---|
| Age | Age of the individual |
| Gender | Male / Female |
| Ethnicity | Ethnic background |
| Jaundice | History of jaundice at birth |
| Family History | Family history of autism |

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/autism-prediction.git
cd autism-prediction
```

### 2. Install dependencies

```bash
pip install streamlit scikit-learn pandas numpy
```

### 3. Run the app

```bash
python -m streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## 🧪 Model Details

- **Algorithm:** Logistic Regression
- **Preprocessing:** Label Encoding for categorical features (gender, ethnicity)
- **Features:** 5 input features
- **Training:** Scikit-learn with `max_iter=1000`

---

## 📈 Results

The model was trained and evaluated on the ASD screening dataset. Logistic Regression was chosen for its interpretability and efficiency on tabular medical data.

---

## 🔮 Future Improvements

- Add the full A1–A10 behavioural screening questionnaire
- Try advanced models (Random Forest, XGBoost) for better accuracy
- Deploy to Streamlit Cloud with a public URL
- Add model explainability using SHAP values
- Include confidence score with each prediction

---

## 👨‍💻 Author

**Basheer** — Undergraduate Student, Data Science & Machine Learning  
📧 [your-email@example.com]  
🔗 [LinkedIn Profile](https://linkedin.com/in/your-profile)  
🐙 [GitHub](https://github.com/your-username)

---

## 📄 License

This project is for educational purposes. Dataset credits to the original Kaggle contributors.
