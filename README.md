# 📊 Students Performance Indicator

![Screenshot (199)](https://github.com/user-attachments/assets/d976672a-81cd-4f92-8b4b-1b1f4e2b9f70)


## 🚀 Project Overview
The **Students Performance Indicator** is a data-driven project aimed at analyzing student performance based on various factors such as gender, parental education, lunch type, test preparation course, and scores in mathematics, reading, and writing. By leveraging machine learning models, this project provides predictive insights into student outcomes, helping educators and policymakers improve academic performance.

## 🎯 Key Features
- **Data Cleaning & Preprocessing**: Handling missing values, encoding categorical data, and feature scaling.
- **Exploratory Data Analysis (EDA)**: Understanding correlations and patterns using statistical analysis and visualization.
- **Machine Learning Models**: Implementing regression and classification algorithms to predict student performance.
- **Model Evaluation & Optimization**: Fine-tuning models for better accuracy and interpretability.
- **Deployment**: Deploying the trained model as an API using Flask/Streamlit for real-world applications.

## 🏗️ Tech Stack
- **Programming Language**: Python 🐍
- **Libraries & Frameworks**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn
- **Machine Learning Models**: Linear Regression, Decision Trees, Random Forest, XGBoost
- **Deployment**: Flask / Streamlit (optional)

## 📂 Project Structure
```bash
📂 Students-Performance-Indicator
├── 📁 .ebextensions       # Elastic Beanstalk configuration
├── 📁 .vscode             # VS Code workspace settings
├── 📁 artifacts           # Model artifacts and saved outputs
├── 📁 catboost_info       # CatBoost model information
├── 📁 logs                # Logging information
├── 📁 mlruns              # MLflow tracking experiments
├── 📁 notebook            # Jupyter notebooks for analysis
│   ├── 1.EDA STUDENT PERFORMANCE.ipynb        # Exploratory Data Analysis
│   ├── 2.MODEL TRAINING.ipynb  # Model Training
│   ├── mlflow.db          # MLflow database for experiment tracking
├── 📁 source              # Source code for preprocessing and modeling
│   ├── components         # Core components of the application
|   │     ├──__init__.py
│   │     ├── data_ingestion.py
│   │     ├──data_transformation.py
│   │     ├──model_trainer.py  
│   │
│   ├── pipeline           # Data processing and ML pipeline scripts
│   │       ├──__init__.py
│   │       ├── predict_pipeline.py
│   │       ├──train_pipeline.py
│   ├── __init__.py        # Package initializer
│   ├── exception.py       # Custom exception handling
│   ├── logger.py          # Logging utility
│   ├── utils.py           # Helper functions
├── 📁 template            # Templates for UI or deployment
│    ├──home.html
│    ├──index.htme
├── 📁 venv                # Virtual environment
├── 📄 .gitignore          # Git ignore configuration
├── 📄 README.md           # Project documentation
├── 📄 app.py              # Main application script
├── 📄 application.py      # Alternate application script
├── 📄 requirements.txt    # Dependencies list
└── 📄 setup.py            # Setup script for installation
```

## 🔍 Exploratory Data Analysis (EDA)
- Distribution of students' scores across different subjects.
- Impact of parental education and lunch type on performance.
- Correlation analysis to identify key influencing factors.

## 🤖 Machine Learning Models
- **Regression Models**: Predicting students' overall performance.
- **Classification Models**: Classifying students as high, medium, or low performers.
- **Feature Importance Analysis**: Identifying key predictors of success.

## 📈 Model Performance
| Model            | Accuracy (%) |
|-----------------|-------------|
| Linear Regression | 87.97       |
| Ridge             | 88.06
| Random Forest    | 85.45       |
| XGBoost         | 93.5        |

## 🚀 Getting Started
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Adity-star/Students-Performance-indicator.git
cd Students-Performance-indicator
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Project
```bash
python app.py
```

## 🎯 Future Enhancements
- Integration with a web dashboard for interactive analysis.
- Deployment as an AI-powered recommendation system for educators.
- Expanding dataset with more features for improved accuracy.

## 🏆 Contributing
Contributions are welcome! Feel free to fork the repository, raise issues, and submit pull requests.

## 📝 License
This project is licensed under the MIT License.

## 🌟 Connect with Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/aditya-akuskar-27b43533a/)  [![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/Adity-star)

---

⭐ **If you found this project useful, don't forget to star the repository!**
