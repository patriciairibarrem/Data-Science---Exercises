#!/usr/bin/env python
# coding: utf-8

# ## ANÁLISES ESPACIAIS E CIÊNCIA DE DADOS GEOGRÁFICOS COM PYTHON
# 
# Exercícios referentes ao curso Spatial Analysis and Geospatial Data Science With Python da Udemy. 
# https://here.udemy.com/course/spatial-data-science-with-python/learn/lecture/20169360#overview

# # Parte II - Introdução ao Geopandas
# 
# Nessa seção serão explorados algumas técnicas para ler, transformar e compreender os sistemas de coordenadas. 

# # 3 - Lendo o conjunto de dados
# "Big datasets" estão em todos os lugares. Isso pode gerar desafios na leitura de todos estes dados de uma só vez. No Geopandas, você pode usar pre-filterinto para carregar dados geoespaciais com Geometry (geometria), Bounding Box (caixa delimitadora) ou Rows (linhas). 
# 
# * Ler conjunto de dados usando geometria
# * Ler conjunto de dados usando filtro de linha

# In[3]:


import geopandas as gpd
import pandas as pd


# In[21]:


#Ler o arquivo Countries (vamos usar a geometria depois)

shp = r'C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\data\countries.shp'
countries = gpd.read_file(shp)
countries.head()


# In[23]:


#Em GeoPandas, a propriedade crs (Sistema de Referência de Coordenadas) de um GeoDataFrame é usada para armazenar e gerenciar as informações de projeção espacial
countries.crs


# In[16]:


countries.plot()


# # Lendo o conjunto de dados usando Geometry

# In[40]:


countries[countries['CONTINENT'] == 'Africa'].head()


# In[41]:


countries[countries['CONTINENT'] == 'Africa'].plot()


# In[42]:


#Lendo Acled Dataset selecionando Africa

africa_acled = gpd.read_file(
    r"C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\data\acled2019.shp",
    mask = countries[countries["CONTINENT"] == "Africa"]
)
africa_acled.plot(markersize=0.5);


# # Lendo o conjunto de dados usando Rows

# In[46]:


acled_subset = gpd.read_file(
    r"C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\data\acled2019.shp",
    rows=200
)
acled_subset.plot();


# In[47]:


acled_subset = gpd.read_file(
    r"C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\data\acled2019.shp",
    rows=slice(200, 500)
)
acled_subset.plot();


# # Lendo o conjunto de dados - Revisão
# 
# * mask --> enquanto está lendo o dado, você pode filtrar por geometry (geometria) usando o parametro mask
# * rows --> você pode usar rows (linhas) para limitar o número de rows enquanto lê os dados

# In[ ]:




