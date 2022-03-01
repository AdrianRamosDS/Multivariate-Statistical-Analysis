# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:04:02 2020

@author: Adrian Ramos Perez
"""

import pandas as pd

DF = pd.read_csv('Andbrain_DataSet-3.csv')

#%% a)	Calcule las medidas de tendencia central (todas las variables) y en base a la descripción emotions sensor data set
# de una interpretación de los resultados obtenidos para una de las variables. 
MedidasMatrix = pd.DataFrame(columns=['disgust','surprise','neutral','anger','sad','happy','fear'])
MedidasMatrix['disgust']= DF['disgust'].mode()
MedidasMatrix['disgust']= DF['disgust'].mean()
MedidasMatrix['disgust']= DF['disgust'].median()

MedidasMatrix.iloc(2,['surprise']) = DF['surprise'].mode()
Anger_mean = DF['surprise'].mean()
Anger_median = DF['surprise'].median()

Anger_mode = DF['neutral'].mode()
Anger_mean = DF['neutral'].mean()
Anger_median = DF['neutral'].median()

Anger_mode = DF['anger'].mode()
Anger_mean = DF['anger'].mean()
Anger_median = DF['anger'].median()

Anger_mode = DF['sad'].mode()
Anger_mean = DF['sad'].mean()
Anger_median = DF['sad'].median()

Anger_mode = DF['happy'].mode()
Anger_mean = DF['happy'].mean()
Anger_median = DF['happy'].median()

Anger_mode = DF['fear'].mode()
Anger_mean = DF['fear'].mean()
Anger_median = DF['fear'].median()

#%% b)	Calcule las medidas de dispersión univariantes. 
# ¿Cómo interpreta los valores  obtendios de la varianza y la desviación estándar?
varianza = DF.var()
desviacion = DF.std()

#%% c)	Calcule las medidas de dispersión bivariantes.
Covarianza = DF.cov()
Correlacion = DF.corr()

#%% d)	¿Qué variables presentan una relación  directa y qué variables presentan relación inversa?
# Directa = directa todas las demás positivas pero no es muy fuerte la relación al no pasar de .6
# Inversa = La sorpresa-enojo, sorpresa-felicidad, enojo-felicidad, enojo-miedo, tristeza-felicidad y miedo -felicidad

#%% e)	¿Qué variables presentan la mayor y  la menor correlación?
# mayor es neutral-disgusto,  correlación no inversa está entre enojo-tristeza

#%% f)	Si dos variables tienen correlación cero, entonces ¿se puede concluir qué son independientes? Justifica tu respuesta.
# No necesariamente significa que no están  relcionadas en cierto parámetro, pero no podemos afirmarlo para otros parámetros.