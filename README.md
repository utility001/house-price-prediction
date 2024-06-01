# 🏠 Ames Housing Dataset

![house](images/house.jpg)

Accurate prediction of real estate prices is essential for making informed decisions in the property market. This project utilizes machine learning to estimate house prices based on a variety of features.

### **Features**  
The model predicts prices by analyzing a range of property attributes, including type, architectural style, neighborhood, and more.

### Data Source
The dataset was sourced from [kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)

### Steps
* **Exploratory Data Analysis (EDA):**
  - Conducted thorough exploratory analyses to understand the dataset, identify issues, and visualize feature relationships.

* **Data Cleaning and Preprocessing:**
  - Implemented various cleaning and preprocessing techniques to ensure high-quality data and robust models:
    + Removed duplicate rows
    + Ensured input consistency
    + Applied standard scaling
    + Utilized one-hot encoding

* **Model Building and Evaluation:**
  - The modelling was done via the Stochastic Gradient Regressor algorithm (SGDRegressor).
  - Performed hyperparameter tuning to enhance model performance and generalization.
  - Assessed model performance using the Root Mean Squared Erro metric (RMSE)

* **Serialization:**
  - Serialized the model for deployment in a live environment.

* **UI Development:**
  - I also built a User interface for demonstration purposes using Streamlit.

### Tools and Technologies
* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, scikit-learn, Streamlit
* **IDE/Notebook:** JupyterLab

### Note!
- This README will be updated as the project progresses.
- A deployment pipeline will be added in the future.