import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier

from scipy.stats import mannwhitneyu

import pickle
import joblib
import json

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


def infer_model(df_plec):

    name_list = ['MLP','SVC','RF','XGB']
    type_list = ['Default','optuna','over','optuna_over']

    df_final = pd.DataFrame({
        'ID': df_plec.iloc[:,1024]
    })

    new_cols = {}

    for name_mod in name_list:
        for type_mod in type_list:

            if type_mod == 'Default' or type_mod == 'over':
                thres_list = [0.5, 0.5, 0.5, 0.5, 0.5]
            else:
                with open(f'../models/hyperparameter/{name_mod}/{name_mod}_{type_mod}/{name_mod}_{type_mod}_threshold.txt', 'rb') as f:
                    thres_list = json.load(f)

            for i in range(1,6):
                model = joblib.load(f'../models/model/{name_mod}/{name_mod}_{type_mod}/{name_mod}_{type_mod}_{i}_model.pkl')

                X_test = df_plec.iloc[:,:1024]
                y_pred = model.predict_proba(X_test)[:,1]
                label_test = df_plec.iloc[:,1024]
                
                df_ML = pd.DataFrame({
                'ID':label_test,
                'Pred':y_pred
                })
                df_ML['Pred_label'] = df_ML['Pred'].apply(lambda x: "Active" if x >= thres_list[(i-1)] else "Inactive")

                df_ML_prob_map = df_ML.set_index('ID')['Pred'].to_dict()
                df_ML_pred_map = df_ML.set_index('ID')['Pred_label'].to_dict()

                new_cols[f'{name_mod}_{type_mod}_{i}_prob'] = (df_final['ID'].map(df_ML_prob_map))
                new_cols[f'{name_mod}_{type_mod}_{i}_label'] = (df_final['ID'].map(df_ML_pred_map))

    
    df_final = pd.concat([df_final, pd.DataFrame(new_cols)], axis=1)
    
    return df_final
        