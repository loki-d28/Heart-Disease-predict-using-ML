Overview of project:
     This project leverages machine learning to predict whether a patient has heart disease based on various health metrics and medical history. The dataset is preprocessed, encoded, and used to train a classification model, specifically the Naive Bayes classifier. The trained model is then evaluated for accuracy and used to make predictions.

Dataset:
The dataset contains the following features:

Age: Age of the patient
Sex: Gender of the patient (0 = Female, 1 = Male)
ChestPainType: Type of chest pain experienced (encoded)
RestingBP: Resting blood pressure (in mm Hg)
Cholesterol: Serum cholesterol level (in mg/dl)
FastingBS: Fasting blood sugar (> 120 mg/dl) (1 = True, 0 = False)
RestingECG: Resting electrocardiographic results (encoded)
MaxHR: Maximum heart rate achieved
ExerciseAngina: Exercise-induced angina (1 = Yes, 0 = No)
Oldpeak: ST depression induced by exercise relative to rest
ST_Slope: Slope of the peak exercise ST segment (encoded)
HeartDisease: Target variable (1 = Heart disease, 0 = Normal)

Project Steps:

1. Preprocessing
  The dataset is preprocessed to handle categorical variables using label encoding. Label encoding converts categorical values into numerical format suitable for machine learning algorithms.

2. Feature Selection
  Features are separated into input features (X) and the target label (y).

3. Data Splitting
  The data is split into training and testing sets using an 80-20 split to evaluate the model's performance on unseen data.

4. Model Training
  A Naive Bayes classifier (GaussianNB) is trained using the training data.

5. Evaluation
  The model's performance is evaluated using the test set. The accuracy score is calculated to determine how well the model predicts heart disease.

6. Prediction
  The trained model is used to predict heart disease for new input data.

Requirements:

Libraries
pandas
numpy
scikit-learn
To install the required libraries
