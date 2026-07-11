# 🎓 Placement Prediction System

An AI-powered web application that predicts a student's placement probability using Machine Learning. The application provides an interactive dashboard where users can enter their academic details and instantly receive a placement prediction along with personalized recommendations.

---

## 📌 Features

- 🎯 Predict placement probability
- 📊 Interactive dashboard using Streamlit
- 📈 Plotly Gauge Chart visualization
- 👤 Student profile summary
- 💡 AI-based recommendations
- ⭐ Confidence level prediction
- 🎨 Professional dark theme UI

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Plotly
- Joblib
- Git & GitHub

---

## 📂 Project Structure

```text
placement-prediction/
│
├── data/
│   └── placement_data.csv
│
├── models/
│   └── placement_model.pkl
│
├── src/
│   ├── app.py
│   ├── train_model.py
│   ├── generate_dataset.py
│   └── predict.py
│
├── notebooks/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/pulatakarthik/placement-prediction.git
```

Go to the project folder

```bash
cd placement-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run src/app.py
```

---

## 📊 Machine Learning Features

The model uses the following inputs:

- CGPA
- Aptitude Score
- Internship Experience
- Projects Completed
- Active Backlogs

---

## 📷 Application Preview

*(Screenshots will be added here after deployment.)*

---

## 🔮 Future Improvements

- Login System
- Database Integration
- Resume Analysis
- Company-wise Prediction
- Placement Analytics Dashboard
- Cloud Deployment

---

## 👨‍💻 Author

**Pulata Karthik**

Computer Science Engineering Student

GitHub: https://github.com/pulatakarthik

---

## ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.
## 📸 Application Screenshots

### 🏠 Home Screen

![Home Screen](assets/home.png)

---

### 📊 High Placement Prediction

![High Prediction](assets/high_prediction.png)

---

### 📉 Low Placement Prediction

![Low Prediction](assets/low_prediction.png)