# Student Stress Level Prediction

## Portfolio Project

Machine Learning project using MLP for student stress level prediction with data visualization, preprocessing, feature scaling, and model evaluation.

## Features

- Data preprocessing
- Data analysis 
- EDA 
- Visulization
- Data summary 
- remove Duplicates
- Removing Outliers 
- Fill nan data by "mean"
- Encoding string data by OneHotEncoder
- StandardScaler 
- ColumnTransformer 
- Smote 
- Model evaluation (Accuracy, confusion_matrix, classification_report)  
- Cross Val Score
- GridSearchCV for hyperparameters 
- Permutation Importance
- Shap 
- Make Pipeline 
- Saved Model and Preprocesser as pickle 

## model 
 
MLP

## Data

- i used "student-lifestyle-and-stress" dataset from kaggle 
- Dataset Link: https://www.kaggle.com/datasets/sridevilavanyacse/student-lifestyle-and-stress-prediction-dataset

## Accuracy

Test Accuracy: 81.67 % 

## About Files 

- app/Student_Stress_Level.py : for running model and get result 
- data/student-lifestyle-and-stress-dataset.csv
- pickle_files/student_stress_model.pickle: model and preprocessor pickle 
- pickle_files/column_transformer.pickle: just ct pickle
- pickle_files/simple_imputer.pickle: just simple imputer pickle
- pickle_files/mlp.pickle: just model(without preprocess) pickle
- mlp_project.ipynb: notebook project
- README.md
- requirements.txt
- .gitignore
- LICENSE

# For runnig project
- go to app folder -> Student_Stress_Level.py
- this is the file that you can run the model and get answer 

# Full Model
- go to -> mlp_project.ipynb 
- this is all code about visulization-preprocessing-model-evaluation-make pickles and ... 