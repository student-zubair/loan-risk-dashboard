# 📊 Loan Risk Dashboard & Prediction System

## 🌐 Live Application

[Loan Risk Dashboard](https://loan-risk-dashboard-zxz5dz3zn5qv3amfpn9ozs.streamlit.app/)

---

# 📌 Project Overview

The Loan Risk Dashboard & Prediction System is an end-to-end Machine Learning and Business Intelligence application developed using Streamlit, Scikit-learn, and Pandas.

This project combines:

* Interactive analytics dashboards
* Loan risk visualization
* Customer credit analysis
* Machine learning-based loan risk prediction
* User authentication and session handling

The application enables users to:

* Analyze customer financial behavior
* Visualize credit and delinquency patterns
* Predict loan approval risk using a trained machine learning model
* Interact with dynamic filters similar to Power BI dashboards

---

# 🚀 Features

## 🔐 Authentication System

* Login-based access control
* Session management using Streamlit session state
* Protected dashboard and prediction pages

---

## 📊 Interactive Dashboard

The dashboard provides real-time analytics and customer insights.

### Dashboard KPIs

* Total Customers
* Average Monthly Income
* Average Credit Score
* Average Delinquency Count

### Dashboard Visualizations

* Credit Score Distribution
* Income Distribution
* Delinquency vs Credit Score Analysis
* Risk Distribution
* Gender Distribution

### Dynamic Filters

Users can filter the dashboard based on:

* Gender
* Age
* Income
* Credit Score
* Delinquency Count

---

## 🤖 Loan Risk Prediction

The prediction module uses a trained Random Forest Classifier to determine customer loan risk.

### Prediction Inputs

* Age
* Monthly Income
* Credit Score
* Delinquency History
* Employment Information
* Credit Utilization Metrics
* Loan Activity Metrics
* Enquiry Information

### Prediction Output

The model predicts:

* Low Risk
* High Risk

---

# 🧠 Machine Learning Workflow

## 1️⃣ Data Cleaning

* Missing value handling
* Invalid value correction
* Data type conversion
* Duplicate removal

## 2️⃣ Feature Engineering

* Risk categorization
* Credit behavior transformation
* Feature selection
* Derived metrics creation

## 3️⃣ Data Preprocessing

* Encoding categorical variables
* Numeric conversion
* Handling skewness and outliers
* Missing value imputation

## 4️⃣ Model Building

Models explored:

* Logistic Regression
* Random Forest Classifier

Final selected model:

* Random Forest Classifier

## 5️⃣ Model Evaluation

Evaluation metrics used:

* Accuracy Score
* ROC-AUC Score
* Classification Report
* Confusion Matrix

## 6️⃣ Model Deployment

* Model serialized using Joblib
* Streamlit deployment
* Interactive prediction interface

---

# 🛠️ Technologies Used

## Frontend & Dashboard

* Streamlit

## Data Analysis

* Pandas
* NumPy

## Data Visualization

* Streamlit Charts
* Matplotlib

## Machine Learning

* Scikit-learn
* Random Forest Classifier
* Logistic Regression

## Model Serialization

* Joblib

## Version Control

* Git
* GitHub

---

# 📂 Project Structure

```bash
loan_app/
│
├── app.py
├── dashboard_data.csv
├── RFC.pkl
├── features.pkl
├── requirements.txt
├── .gitignore
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Predict.py
```

---

# 📈 Dashboard Dataset Optimization

To maintain privacy and improve deployment performance:

* Confidential raw banking datasets were excluded
* Only dashboard-safe columns were retained
* A reduced deployment dataset was created
* Cached data loading was implemented for performance optimization

### Final Deployment Dataset

* Rows: ~51,000+
* Columns: 5 dashboard-safe attributes

This significantly improved:

* App speed
* Deployment size
* Data privacy
* Dashboard responsiveness

---

# 🔒 Data Privacy & Security

This project was designed with privacy considerations:

* Sensitive raw datasets are excluded using `.gitignore`
* Only analytics-safe data is deployed
* Customer identifiers were removed
* Session-based authentication implemented
* Dashboard dataset reduced for public deployment

---

# ⚡ Performance Optimizations

Implemented optimizations include:

* Streamlit caching (`@st.cache_data`)
* Reduced deployment dataset
* Optimized filtering logic
* Controlled chart sampling
* Efficient dataframe operations

---

# ▶️ Installation & Local Setup

## 1️⃣ Clone Repository

```bash
git clone <repository-link>
```

## 2️⃣ Navigate to Project Folder

```bash
cd loan_app
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv credit_env1
```

## 4️⃣ Activate Environment

### Windows

```bash
credit_env1\Scripts\activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Run Application

```bash
streamlit run app.py
```

---

# 🌐 Deployment

The application is deployed using Streamlit Cloud.

### Deployment Steps

1. Push project to GitHub
2. Configure `requirements.txt`
3. Exclude confidential files using `.gitignore`
4. Deploy through Streamlit Cloud

---

# 📊 Key Learning Outcomes

This project demonstrates:

* End-to-end ML workflow
* Data preprocessing techniques
* Business dashboard creation
* Streamlit deployment
* Interactive analytics development
* Feature engineering
* Model deployment
* Performance optimization
* Data privacy handling

---

# 🔮 Future Improvements

Potential future enhancements:

* Database integration
* Cloud-based model APIs
* Advanced authentication system
* Role-based access control
* Dark mode UI
* Plotly interactive charts
* Explainable AI visualizations
* Real-time loan scoring
* Docker deployment

---

# 👨‍💻 Author

## Mohammed Zubair

Computer Science Engineering Graduate

### Areas of Interest

* Data Analytics
* Machine Learning
