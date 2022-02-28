#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Rocío Carrasco
"""
#%% Importar librerias
import pandas as pd
import numpy as np
import researchpy as rp
import statsmodels.api as sm
import scipy.stats as stats
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.stats.multicomp as mc


#%% Cargar base de datos EJEMPLO 1
data= pd.read_csv('/Users/luisluque/Downloads/AEMP2019/Base de datos/PlantGrowth.csv')
rp.summary_cont(data['weight'])
rp.summary_cont(data['weight'].groupby(data['group']))

#%% Boxplot
fig = plt.figure(figsize= (5, 5))
ax = fig.add_subplot(111)

ax.set_title("Box Plot of Weight by Group", fontsize= 20)
ax.set

data1 =[data['weight'][data['group'] == 'Ninguno'],
        data['weight'][data['group'] == 'Fertilizante'],
        data['weight'][data['group'] == 'Riego'],
        data['weight'][data['group'] == 'F y R']]

ax.boxplot(data1, labels= ['Ninguno','Fertilizante','Riego','F y R'],
           showmeans= True)

plt.xlabel("Group")
plt.ylabel("Weight ")

plt.show()

#%% Modelo anova
#Ho:m1=m2=...=mn
#h1: al menos una media es diferente
anova_1=ols('weight~C(group)',data=data).fit()
tabla_anova_1=sm.stats.anova_lm(anova_1,typ=2)
tabla_anova_1
#%%Hipótesis del modelo
#Normalidad Shapiro-wilk
#Ho: Normalidad
#H1: No hay normalidad
stats.shapiro(anova_1.resid)
#%% Homocedasticidad
#Levene test (sin normalidad)
#Ho: Homocedasticidad
#H1: No Homocedasticidad
stats.levene(data['weight'][data['group'] == 'Ninguno'],
        data['weight'][data['group'] == 'Fertilizante'],
        data['weight'][data['group'] == 'Riego'],
        data['weight'][data['group'] == 'F y R'])

#%% Bartlett test (con normalidad)
#Ho: Homocedasticidad
#H1: No Homocedasticidad
#stats.bartlett(data['weight'][data['group'] == 'Ninguno'],
#        data['weight'][data['group'] == 'Fertilizante'],
#        data['weight'][data['group'] == 'Riego'],
#        data['weight'][data['group'] == 'F y R'])

#%% Comparaciones múltiples (Tukey test) Post hoc
comp=mc.MultiComparison(data['weight'], data['group'])
post_hoc_res=comp.tukeyhsd()
print(post_hoc_res.summary())

#%% Cargar base de datos EJEMPLO 2
data_2=pd.read_excel('/Users/luisluque/Downloads/Diet.xlsx')
data_2.info()
rp.summary_cont(data_2['weight6weeks'])
rp.summary_cont(data_2['weight6weeks'].groupby(data_2['Diet']))

#%%Boxplot
fig = plt.figure(figsize= (10, 10))
ax = fig.add_subplot(111)

ax.set_title("Box Plot of Weight6weeks by Diet", fontsize= 20)
ax.set

data2 =[data_2['weight6weeks'][data_2['Diet'] == 'A'],
        data_2['weight6weeks'][data_2['Diet'] == 'B'],
        data_2['weight6weeks'][data_2['Diet'] == 'C']]

ax.boxplot(data2, labels= ['A','B','C'],
           showmeans= True)

plt.xlabel("Diet")
plt.ylabel("Weight6weeks ")

plt.show()


#%% anova statsmodels
#Ho:m1=m2=...=mn
#H1: Al menos una media es diferente
anova_2 = ols('weight6weeks ~ C(Diet)', data=data_2).fit()
tabla_anova_2 = sm.stats.anova_lm(anova_2, typ=2)
tabla_anova_2

#%% Hipótesis del modelo
#Normalidad prueba de Shapiro-Wilk
#Ho:Normalidad
#H1: No normalidad
stats.shapiro(anova_2.resid)

#%%Homocedasticidad Prueba de Bartlett
#Ho:Homocedasticidad
#H1: No Homocedasticidad
stats.bartlett(data_2['weight6weeks'][data_2['Diet'] == 'A'],
             data_2['weight6weeks'][data_2['Diet'] == 'B'],
             data_2['weight6weeks'][data_2['Diet'] == 'C'])

#%% Cargar datos EJEMPLO 3
#create data
data_3 = pd.DataFrame({'water': np.repeat(['daily', 'weekly'], 15),
                   'sun': np.tile(np.repeat(['low', 'med', 'high'], 5), 2),
                   'height': [6, 6, 6, 5, 6, 5, 5, 6, 4, 5,
                              6, 6, 7, 8, 7, 3, 4, 4, 4, 5,
                              4, 4, 4, 4, 4, 5, 6, 6, 7, 8]})

#%% Modelo anova two way
anova_3 = ols('height ~ C(water) + C(sun) + C(water):C(sun)', data=data_3).fit()
tabla_anova_3=sm.stats.anova_lm(anova_3, typ=2)
tabla_anova_3

#%%Comparación múltiple Prueba de Tukey
comp = mc.MultiComparison(data_3['height'],data_3['sun'])
post_hoc_res = comp.tukeyhsd()
print(post_hoc_res.summary())
comp2 = mc.MultiComparison(data_3['height'],data_3['water'])
post_hoc_res2 = comp2.tukeyhsd()
print(post_hoc_res2.summary())
