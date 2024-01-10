#!/usr/bin/env python
# coding: utf-8

# ## ANÁLISES ESPACIAIS E CIÊNCIA DE DADOS GEOGRÁFICOS COM PYTHON
# 
# Exercícios referentes ao curso Spatial Analysis and Geospatial Data Science With Python da Udemy. 
# https://here.udemy.com/course/spatial-data-science-with-python/learn/lecture/20169360#overview

# # Difference between concepts
# 
# * Mais de uma coluna é um dataframe ou um geodataframe. E se uma dessas colunas for Geometry (geometria) então é um GeodataFrame, caso contrário é um dataframe
# * Uma coluna pode ser um dataframe ou um geodataframe. E se essa coluna for Geometry, então é uma GeoSeries. 

# In[1]:


import geopandas as gpd
import pandas as pd


# O GeoDataFrame é um dado tabular estruturado que contém GeoSeries.
# 
# A propriedade mais importante do GeoDataFrame é que sempre têm uma coluna GeoSeries que é especial. Essa GeoSeries é referente à Geometry no GeoDataFrame. Quando um método espacial é aplicado ao GeoDataFrame (ou um atributo espacial como "área"), esse comando vai atua na coluna "Geometry'.

# In[3]:


#Ler Countries
shp = r'C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\data\countries.shp'
countries = gpd.read_file(shp)
countries.head(3)


# # DataFrame vs. GeoDataFrame

# In[4]:


# DataFrame
dataFrame = countries[['NAME', 'POP_EST']]
dataFrame.head()


# In[5]:


type(dataFrame)


# In[6]:


# GeoDataFrame
geoDataFrame = countries[['NAME', 'geometry']]
geoDataFrame.head()


# In[7]:


type(geoDataFrame)


# In[8]:


geoDataFrame.plot();


# # Series vs. GeoSeries

# In[11]:


#Series
series = countries['NAME']
series[:5]


# In[12]:


type(series)


# In[14]:


# GeoSeries
geoSeries = countries['geometry']
geoSeries[:5]


# In[16]:


geoSeries.plot()


# In[19]:


#Com GeodataFrames e GeoSeries é possível fazer processamentos espciais usando Geopandas
geoSeries.area


# In[ ]:




