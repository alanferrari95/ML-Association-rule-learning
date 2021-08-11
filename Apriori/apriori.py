#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:05:55 2019

@author: Alan
"""

#Apriori

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0,20)])
    
    
# Entrenar el algoritmo de Apriori
from apyori import apriori
rules = apriori(transactions, min_support = 0.003 , min_confidence = 0.2,
                min_lift = 3, min_length = 2)
"""
min_support: cantidad de veces que el producto aparece en todo el dataset.
    Por ejemplo, el DS es de una semana, y nosotros queremos un producto que se venda
    3 veces por dia. Entonces hacemos 3*7/7500, que nos da 0.0028, redondeamos en 0.003

min_confidence: en la cantidad de cestas que aparecen esos dos supuestos productos.
    Como le pusimos 0.2, le estamos diciendo que COMO MINIMO nos busque productos
    que aparecen en el 20% de las cestas.

min_lift: 
    
min_lenght:
    

"""
# Visualización de los resultados
results = list(rules)

results[0]
resultados=[]
for k in range (0,154):
    resultados.append(str(results[k]))