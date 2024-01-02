import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Projeto 2 - Previsão de Renda",
     page_icon=":$$$:",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')
renda['data_ref'] = pd.to_datetime(renda['data_ref'])


# DATE PICKER
max_data = renda['data_ref'].max()
min_data = renda['data_ref'].min()

data_inicial = st.sidebar.date_input('Data inicial', 
                value = min_data,
                min_value = min_data,
                max_value = max_data)
data_final = st.sidebar.date_input('Data inicial', 
                value = max_data,
                min_value = min_data,
                max_value = max_data)    

st.sidebar.write('Data inicial = ', data_inicial)
st.sidebar.write('Data inicial = ', data_final)

# VARIABLE PICKER
variaveis = renda.drop(columns=['data_ref', 'id_cliente', 'renda', 'Unnamed: 0']).columns
print(variaveis)

variavel = st.sidebar.selectbox(
    'Escolha a variável para análise',
    variaveis
)

renda = renda.query('@data_inicial < data_ref < @data_final')

#PLOTS
fig1, ax1 = plt.subplots(figsize=(24, 8))
# renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
st.write('## Gráficos ao longo do tempo')
sns.lineplot(x='data_ref',y='renda', hue=variavel, data=renda, ax=ax1)
ax1.tick_params(axis='x', rotation=45)
st.pyplot(plt)

st.write('## Histograma')
fig2, ax2 = plt.subplots(figsize=(24, 8))
sns.countplot(x=variavel, data=renda, ax=ax2)
st.pyplot(plt)

st.write('## Gráficos bivariada')
fig, ax = plt.subplots(figsize=(24, 8))
sns.barplot(x=variavel,y='renda',data=renda, ax=ax)
st.pyplot(plt)





