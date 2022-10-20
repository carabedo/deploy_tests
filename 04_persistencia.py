#persistencia.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import numpy as np


df=pd.read_csv('amazon.csv')
X_train, X_test, y_train, y_test = train_test_split(df['Reviews'], 
                                                    df['Positivos'], 
                                                    random_state=0,
                                                   stratify=df['Positivos'])
vect = CountVectorizer(min_df=5, ngram_range=(1,2)).fit(X_train)
X_train_vectorized = vect.transform(X_train)
model = LogisticRegression(max_iter=5000)
model.fit(X_train_vectorized, y_train)
from joblib import dump
dump([model,vect], 'model_vect.joblib') 