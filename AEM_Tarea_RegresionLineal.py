# -*- coding: utf-8 -*-
"""
ANÁLISIS ESTADÍSTICO MULTIVARIADO
TAREA Regresión Lineal
@author: Adrián Ramos Pérez
"""
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn import datasets, linear_model

#%% Database import
Dataset = pd.read_csv('farmers_salary_transactions.csv')

#%% Variables
X = 0
Y = 0

#%% Linear Regression
lr = linear_model.LinearRegression()
#lr.fit(X,Y)
lr.predict