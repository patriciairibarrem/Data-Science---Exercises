#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install beautifulsoup4')


# In[2]:


#importar bibliotecas
import requests #para realizar requisições HTML
from bs4 import BeautifulSoup
import re # trabalhar com expressão regular


# Website: https://politica.estadao.com.br/eleicoes/2020/candidatos
# Extrair as seguintes informações:
# 
# * Nome do candidato
# * Partido do candidato
# * Estado
# * Cidade
# * Endereço de link do candidato

# In[3]:


#criação de variável e atributo
r = requests.get("https://politica.estadao.com.br/eleicoes/2020/candidatos")


# In[4]:


r.text #conteúdo em html


# In[7]:


#tratar dado com objeto do beautifulsoup, o bs4
soup = BeautifulSoup(r.text, 'html.parser')
type(soup)


# no website, vá para "inspect" com o botão direito.
# essa é a etapa mais trabalhosa para o analista de dados.

# In[11]:


#utilizar o método examina os descendentes de uma tag e recupera todos os descendentes que correspondem aos seus valores?
candidatos = soup.find_all("div", attrs={"class": "col-xs-12 -only"})
type(candidatos)


# In[12]:


#listar os items que estão na lista de candidatos
candidatos[:3] #primeiros elementos da lista


# In[15]:


#extração do nome do candidato utilizando a TAG "img"
nome_candidato = candidatos[1].img["alt"]
nome_candidato2 = candidatos[1].a["title"]
print('Extração do nome do candidato utilizando a TAG "img": ', nome_candidato)
print('Extração do nome do candidato utilizando a TAg "a"): ',nome_candidato2)


# In[16]:


#extraindo o partido do candidato
partido = candidatos[1].span.text
print(partido)


# In[17]:


import re


# In[18]:


print(candidatos[1].a["href"])


# In[19]:


print(re.split('/', candidatos[1].a["href"]))


# In[23]:


print("Estado do candidato:", re.split('/', candidatos[1].a["href"])[6])
print("Cidade do candidato:", re.split('/', candidatos[1].a["href"])[7])


# In[24]:


#atribuir para as variáveis
estado = re.split('/', candidatos[1].a["href"])[6]
cidade = re.split('/', candidatos[1].a["href"])[7]
link = candidatos[1].a["href"]


# In[25]:


print(estado,cidade,link)


# In[27]:


#lista de candidatos para percorrer o código
lista_candidatos = []
for candidato in candidatos:
    dados_candidato =[]
    dados_candidato.append(candidato.img["alt"])
    dados_candidato.append(candidato.span.text)
    dados_candidato.append(re.split('/', candidato.a["href"])[6])
    dados_candidato.append(re.split('/', candidato.a["href"])[7])
    dados_candidato.append(candidato.a["href"])
    lista_candidatos.append(dados_candidato)


# In[33]:


lista_candidatos[:2]


# In[35]:


import pandas as pd


# In[36]:


#criar dataframe
df_candidatos = pd.DataFrame(lista_candidatos, columns=['nome_candidato', 'partido', 'estado', 'cidade', 'link'])


# In[37]:


df_candidatos[:4]


# Explorando e tratando os dados coletados

# In[40]:


df_candidatos['estado'].value_counts() #prova real. verifica no site se os números estão corretos.


# Tratamento de dados

# In[41]:


df_candidatos[:2].cidade.str.replace('-',' ').str.upper()


# In[43]:


df_candidatos[:2]['cidade'].str.upper().str.replace('-',' ').str.replace("SAO", "SÃO")


# In[46]:


df_candidatos['cidade'] = df_candidatos['cidade'].str.upper().str.upper().str.replace('-',' ').str.replace("SAO", "SÃO")
df_candidatos


# In[47]:


df_candidatos.nome_candidato = df_candidatos.nome_candidato.str.upper()
df_candidatos.estado = df_candidatos.estado.str.upper()
df_candidatos[:3]


# Verificando coleta de dados

# In[ ]:




