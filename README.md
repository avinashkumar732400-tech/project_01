# 💼 Salary Prediction App

## 📌 Project Overview

The **Salary Prediction App** is a Machine Learning web application built using Python and Streamlit. It allows users to enter job-related information, such as work year, experience level, employment type, job title, remote work ratio, and company size, to generate a salary prediction using a pre-trained Machine Learning model.

The application features an interactive user interface with animations, a background image, and a glassmorphism design to provide a modern user experience.

## ✨ Features

- **Salary Prediction:** Predict salary using a pre-trained Machine Learning model.
- **Interactive UI:** Simple and user-friendly Streamlit interface.
- **Job Information Inputs:** Enter work year, experience level, employment type, job title, and other details.
- **Data Encoding:** Uses Scikit-learn's `LabelEncoder` to encode categorical data.
- **Animated Interface:** Includes Lottie animations and a loading indicator.
- **Modern Design:** Background image, gradient overlay, and glassmorphism styling.
- **Prediction Feedback:** Displays the predicted salary and an animation when the prediction completes.

## 🛠️ Technologies Used

- **Python**
- **Streamlit** for the web interface
- **Pandas** for data processing
- **NumPy** for numerical operations
- **Scikit-learn** for data encoding and Machine Learning
- **Pickle** for loading the trained model
- **Requests** for retrieving Lottie animations
- **Streamlit-Lottie** for displaying animations

## 📂 Project Structure

```text
Salary-Prediction-App/
│
├── app.py                  # Main Streamlit application
├── model.pkl               # Pre-trained ML model
├── salaries.csv            # Dataset used for categorical encoders
├── requirements.txt        # Python dependencies
├── bg.jpg                  # Background image
├── Untitled0.ipynb         # Jupyter Notebook for model development
└── README.md               # Project documentation
```

**Note:** Keep the actual filenames consistent with the filenames referenced in your Python code. The background image and notebook are optional only if your application does not depend on them.

## 🚀 How to Use

1. Launch the application.
2. Enter the required job and employment details.
3. Select the relevant experience level, employment type, and company size.
4. Click **Predict Salary**.
5. View the predicted salary displayed on the screen.

## 🧠 Machine Learning Workflow

1. Load the trained Machine Learning model.
2. Load the salary dataset.
3. Create label encoders for categorical columns.
4. Collect user input through the Streamlit interface.
5. Encode categorical inputs.
6. Pass the input data to the trained model.
7. Display the predicted salary.

## 🎯 Project Objective

The objective of this project is to demonstrate how Machine Learning can be integrated into a web application to generate salary predictions from employment-related information.

## 🔮 Future Improvements

- Improve prediction accuracy through model evaluation and feature engineering.
- Add salary visualizations and insights by experience level and job title.
- Support multiple currencies and salary ranges.
- Add model performance metrics and prediction explanations.
- Deploy the application online for public access.

## 📄 License

This project is intended for educational and portfolio purposes. Add an appropriate open-source license if you plan to distribute it for reuse.
