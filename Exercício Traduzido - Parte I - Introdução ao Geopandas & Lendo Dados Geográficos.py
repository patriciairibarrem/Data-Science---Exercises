#!/usr/bin/env python
# coding: utf-8

# ## ANÁLISES ESPACIAIS E CIÊNCIA DE DADOS GEOGRÁFICOS COM PYTHON
# 
# Exercícios referentes ao curso Spatial Analysis and Geospatial Data Science With Python da Udemy. 
# https://here.udemy.com/course/spatial-data-science-with-python/learn/lecture/20169360#overview
# 

# # Parte I - Introdução ao Geopandas
# 
# Nessa seção serão abordadas bibliotecas como GeoPandas and Numpy. O Geopandas, segue a mesma estrutura de dados do Pandas e contém GeodataFrame e GeoSeries. Ela pode ser utilizada par analisar e manipular dados, mas também para executar operações geoespaciais como geométricas e projeções, próprias da biblioteca Shapely. 

# # 1 - Lendo Dados Espaciais
# 
# Objetivos:
# * Ler e escrever dados geográficos (shapefile, geopackage, geojson... etc.) em Geopandas

# In[7]:


get_ipython().system('pip install geopandas')


# In[15]:


import geopandas as gpd


# In[28]:


#lendo o dado

#1. Lendo Countries armazenados na minha máquina. Adicionei o r por causa do \ 
shp = r'C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\data\countries.shp'
countries = gpd.read_file(shp)


# In[30]:


#Explore countries data
countries.head()


# In[31]:


#linhas e colunas do arquivo Countries
countries.shape


# Normalmente, nós precisamos visualizar o dado em formato de mapa. Geopandas é construído em cima do Matplotlib e Descartes para visualizar mapas facilmente. Podemos, portanto, usar o metódo GeodataFrame.plot() para isso.

# In[33]:


countries.plot()


# # 2 - Lendo CSV com Pandas e convertendo para GeodataFrame
# 
# Comma-separated values (CSV) é, normalmente, o tipo de arquivo mais utilizado em ciência de dados. Muitos conjuntos de dados, no entanto, possuem componentes geográficos (lat/long) que podem ser facilmente convertidos em geometrias e podem ser utilizados em análises de dados espaciais.
# 
# Objetivos:
# * Ler arquivo .csv e converter em Geopandas GeodataFrame
# * Converter o dado para o formato Geospatial 

# In[34]:


import geopandas as gpd
import pandas as pd


# In[36]:


#lendo arquivo .csv
df = pd.read_csv(r'C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\data\acled2019.csv')
df.head()


# In[37]:


df.shape


# * Usamos points_from_xy() do Geopandas para transformar Longitude e Latitude em lista do Shepefly: Objetos de pontos e seus conjuntos como geometria enquanto cria o GeoDataFrame.

# In[39]:


#convertendo para GeodataFrame
gdf = gpd.GeoDataFrame(
    df, 
    geometry=gpd.points_from_xy(df.longitude, df.latitude)
)
gdf.head()


# In[42]:


gdf.plot(markersize=2);


# O ideal não é ler o arquivo e depois converter os dados. Isso pode gastar muito tempo e recursos da máquina. O melhor é converter o .csv em dado espacial, mas isso também pode levar um tempo dependendo da sua máquina. 

# In[45]:


#escreva o código para shapefile e exporte
gdf.to_file(r"C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\data\acled2019.shp", crs={'init' :'epsg:4326'})


# In[46]:


#escreva o código para geojson e exporte
gdf.to_file(r"C:\Users\iribarre\Downloads\2+-+Introduction+to+Geopandas\data\acled2019-Geojson.geojson", driver='GeoJSON')


# #  REVISÃO
# 
# * ler_arquivo(path/to/file) --> ler dados geográficos e retornar GedataFrame
# * .head() método que retorna as primeiras 5 linhas. Você pode ajustar as linhas usando, por exemplo, .head(8)
# * .shape() retorna o número de linhas e colunas de um dado
# * .plot() cria um mapa com dado geográfico
# * points_from_xy() --> converte latitude & longittude em GeodataFrame
# * to_file() --> escrevendo códigos para dados geoespaciais 
